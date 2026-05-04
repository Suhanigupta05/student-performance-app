import streamlit as st
import joblib

# load trained model
model = joblib.load("model.pkl")

st.title("student Performance Predictor")
st.write("Predict marks based on study hours and attendance")

# inputss
study_hours=st.slider("Study Hours",0,24,5)
attendance=st.slider("Attendance (%)",0,100,75)

# prediction
if st.button("Predicts Marks"):
    prediction=model.predict([[study_hours,attendance]])
    st.success(f"Predicts Marks: {prediction[0]:.2f}")
               



