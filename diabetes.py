import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('diabetes_model.pkl', 'rb'))

st.title("Diabetes Prediction")


preg = st.number_input("Pregnancies")
glucose = st.number_input("Glucose")
bp = st.number_input("Blood Pressure")
skin = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")


if st.button("Predict"):
    result = model.predict([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    st.success("Diabetic" if result[0] == 1 else "Not Diabetic")


