import pandas as pd
import pickle
from sklearn.svm import SVC

def predict(model: SVC, data: list):
    # Convert the input data to a DataFrame
    prediction_data = pd.DataFrame(data, columns=['Number Of Days', 'Oxygen', 'Temperature', 'Heart Rate', 'Age', 'Comorbidities'])

    # Predict the probabilities
    probability = model.predict_proba(prediction_data)

    # Generate the survival rates
    survival_rates = [round(i[1]*100) for i in probability]
    return survival_rates


if __name__ == "__main__":
    
    # Load the trained model 
    with open('./machineLearning/svm/model/model.pkl', 'rb') as model_file:
        svm_model = pickle.load(model_file)

    testData = [15, 94, 99, 120, 35, True]
    prob = predict(svm_model, [testData])
    print(f'Probability: {prob}')
    
