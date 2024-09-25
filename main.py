from api.gcp.googleSheets import GoogleSheets
from machineLearning.svm.predict import predict
from userInterface.pyqt.mainLayout import Ui_Dialog
from PyQt5 import QtCore, QtGui, QtWidgets
import pickle, sys



    # Replace with actual API key and sheet ID
api_key = 'AIzaSyDm_hlrMN3Jnbv3gpqjnp3-AxBL0p0yJnQ'
sheet_id = '1ldRvUorkTKZApqkLkD_NXiJm5DkLKa6A3WO-uNmigPE'

def getLatestVitals():
    # Initialize GoogleSheets
    gs = GoogleSheets(api_key, sheet_id)
    raw_data = gs.fetch_data()

    # Assuming the first row contains headers like ['Day', 'SpO2', 'Temperature', 'Heart Rate', 'Age', 'CMR']
    # Skip the first row (headers) and process the next rows
    if raw_data and len(raw_data) > 1:
        # Process and transform the first data row into numerical values
        data_row = raw_data[1]  # Skip the header row by using the second row (index 1)
        
        # Convert 'TRUE'/'FALSE' to boolean values
        processed_data = [
            int(data_row[0]),  # Day
            float(data_row[1]),  # SpO2
            float(data_row[2]),  # Temperature
            int(data_row[3]),  # Heart Rate
            int(data_row[4]),  # Age
            True if data_row[5].upper() == 'TRUE' else False  # Convert 'TRUE'/'FALSE' to boolean
        ]
        return processed_data
    else:
        print("No valid data found.")
        return None


    
def getModel(path):
    # Load the trained model 
    with open(path, 'rb') as model_file:
        return pickle.load(model_file)

def getPrediction(data: list[list]):
    model = getModel('./machineLearning/svm/model/model.pkl')
    return predict(model=model, data=data)


def getPercentage(min, max, current):
    return (current-min)/(max-min)


# percentage: 0 to 1 
#   -> (outputs red to green based on the percentage)
# fade: 0 to 255 
#   -> (reduces the contrast)
def getGradient(percentage: float, fade: int = 150) -> tuple:
    pct_diff = 1.0 - percentage
    red_color = min(255, pct_diff*2 * 255)
    green_color = min(255, percentage*2 * 255)
    return f"rgba({red_color}, {green_color}, 0, {fade})"


def getUi(data: list, prediction):
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)

    # update all the readings
    Dialog.setWindowTitle("Patient Report")
    ui.label_24.setText("View Details")
    ui.progressBar.setProperty("value", prediction)
    print(getPercentage(0, 100, prediction))
    print(getGradient(getPercentage(0, 100, prediction)))
    ui.progressBar.setStyleSheet("QProgressBar{\n"
                "    background: rgb(227, 227, 227);\n"
                "    border-radius: 10px;\n"
                "    text-align: center\n"
                "}\n"
                "\n"
                "QProgressBar::chunk {\n"
                f"    background-color: {getGradient(getPercentage(0, 100, prediction))};\n"
                "    margin: 1px;\n"
                "    border-radius: 10px;\n"
                "}")
    ui.progressBar_2.setProperty("value", data[1])
    ui.progressBar_4.setProperty("value", data[2])
    ui.progressBar_3.setProperty("value", data[3])
    ui.label_10.setText(f"Day {data[0]}")   # Day
    ui.label_7.setText(f': {data[1]} %')    # SpO2
    ui.label_9.setText(f': {data[2]} `F')   # temperature   
    ui.label_8.setText(f': {data[3]} bpm')  # heart rate
    ui.label_2.setText(f"Age: {data[4]}")   # Age
    ui.label_3.setText(f"CMR: {data[5]}")   # Comor
    ui.label_11.setText(f"Survival Rate: {prediction}%")
    ui.label.setText("Patient name")
    
    
 # Dialog.show()
  
    return app, Dialog
   
if __name__ == "__main__":
    
    readings = getLatestVitals()

    prediction = getPrediction([readings])[0]
    print(f'Survival rate: {prediction}%')

    # get ui
    app, Dialog = getUi(readings, prediction)



    # start ui
    Dialog.show()

    # exit ui
    sys.exit(app.exec_())







