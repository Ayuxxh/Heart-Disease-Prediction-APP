import streamlit as st
import pickle
import numpy as np


model = pickle.load(open("heart_model.pkl", "rb"))

st.title("Heart Disease Prediction App")
st.write("Enter patient data to predict the risk of heart disease")

# Input fields

name = st.text_input('Patient Name')
age = st.number_input("Age", min_value=1, max_value=120, value=45)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3, 4])
trestbps = st.number_input("Resting Blood Pressure", value=120)
chol = st.number_input("Cholesterol", value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
restecg = st.selectbox("Resting ECG", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", value=150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak (ST depression)", value=1.0)
slope = st.selectbox("ST Slope", [0, 1, 2])

sex = 1 if sex == "Male" else 0
inputs = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope]])

if st.button("Predict"):
    result = model.predict(inputs)[0]
    if result == 1:
        st.error(f" {name} is likely to have heart disease, Needs immidiate attention!")
    else:
        st.success(f" {name} is Unlikely to have heart disease")