import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


df = pd.read_csv('diabetes.csv')

X = df.drop('Outcome', axis = 1)
y = df['Outcome']



X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


model = RandomForestClassifier(X_train, y_train)

with open('diabetes_model.pkl', 'wb') as f:
    pickle.dumb(model, f)

print("✅ Model trained and saved as diabetes_model.pkl")