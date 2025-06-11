import streamlit as st
import joblib
import numpy as np

#load the saved regression model
model = joblib.load("regression_model.joblib")

#streamlit app UI
st.title("Job package prediction_model.joblib")
st.write("Enter your CGPA to predict the expected job package: ")

#User input for CGPA
cgpa = st.number_input("CGPA" , min_value=0.0 ,max_value=10.0 ,step=0.1)

#predict button
if st.button("predict package"):
    #prepare input data for model
    input_data = np.array([[cgpa]])

    #predict the package
    prediction = model.predict(input_data)
    predicted_value =float(prediction[0])  #convert Numpy value to Float

    #show the result
    st.success(f"Predicted Package : ₹{predicted_value:,.2f} LPA")