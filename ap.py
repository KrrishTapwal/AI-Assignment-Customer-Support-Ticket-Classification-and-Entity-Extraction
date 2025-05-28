import streamlit as st

# Dummy prediction functions for illustration
def predict_issue_type(text):
    # Replace with your actual model prediction code
    return "Installation Issue"

def predict_urgency_level(text):
    # Replace with your actual model prediction code
    return "High"

st.title("🚀 Customer Support Ticket Classifier")

st.markdown("""
Welcome! Enter your customer support ticket below, and get predictions for:

- **Issue Type** (e.g., Installation Issue, Billing, Technical, etc.)
- **Urgency Level** (Low, Medium, High)

This app uses traditional NLP and ML techniques for classification.
""")

ticket_text = st.text_area("Type your support query here:")

if st.button("Predict"):
    if ticket_text.strip() == "":
        st.warning("Please enter a support query to classify.")
    else:
        issue = predict_issue_type(ticket_text)
        urgency = predict_urgency_level(ticket_text)
        st.success(f"**Predicted Issue Type:** {issue}")
        st.success(f"**Predicted Urgency Level:** {urgency}")

