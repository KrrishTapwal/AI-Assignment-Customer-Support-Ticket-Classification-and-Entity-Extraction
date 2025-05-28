import streamlit as st
import joblib
import numpy as np

# Load model and vectorizer
model = joblib.load('random_forest_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("Customer Support Ticket Classifier")
st.write("Enter your support query below and get the predicted category.")

# Input text box
user_input = st.text_area("Type your query here:")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text to classify.")
    else:
        # Transform input using vectorizer
        input_vect = vectorizer.transform([user_input])
        
        # Predict category
        prediction = model.predict(input_vect)[0]
        
        # Show prediction
        st.success(f"Predicted Category: **{prediction}**")

