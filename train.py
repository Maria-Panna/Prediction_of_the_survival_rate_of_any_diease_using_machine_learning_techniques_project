import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pickle

# Step 1: Load and preprocess data
data = pd.read_csv("./machineLearning/dataGeneration/data.csv")
data.drop(columns=['Patient Number'], axis=1, inplace=True)

label_encoder = LabelEncoder()
data['Comorbidities'] = label_encoder.fit_transform(data['Comorbidities'])
data['Status Of Patient'] = label_encoder.fit_transform(data['Status Of Patient'])

#  'Status Of Patient' is the target variable
X = data.drop(columns=['Status Of Patient'])
y = data['Status Of Patient']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Train the SVM model
svm_model = SVC(kernel='linear', probability=True, random_state=42)
svm_model.fit(X_train, y_train)

# Step 3: Evaluate the model
y_pred = svm_model.predict(X_test)

print('classification_report:')
print(classification_report(y_test, y_pred))

print('\nconfusion_matrix:')
print(confusion_matrix(y_test, y_pred))

accuracy = accuracy_score(y_test, y_pred)
print(f'\nAccuracy: {accuracy:.2f}')

# Step 4: Save the trained model 
with open('./machineLearning/svm/model/model.pkl', 'wb') as model_file:
    pickle.dump(svm_model, model_file)


print("Trained Model saved successfully.")
