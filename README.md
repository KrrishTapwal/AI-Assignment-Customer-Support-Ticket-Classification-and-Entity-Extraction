# AI-Assignment-Customer-Support-Ticket-Classification-and-Entity-Extraction

.

Project: Ticket Classification and Entity Extraction
Overview
This project builds a machine learning pipeline to classify customer support tickets by issue type and urgency level, and extract key entities like product names, dates, and complaint keywords from ticket text.

Requirements
Python 3.7+

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
(Ensure requirements.txt includes: pandas, numpy, scikit-learn, nltk, matplotlib, seaborn, gradio, streamlit, joblib)

How to Run
1. Jupyter Notebook
Open and run ticket_classification.ipynb

Steps include:

Data loading and preprocessing

Feature engineering (TF-IDF, ticket length, sentiment)

Model training for issue type and urgency classifiers

Entity extraction (products, dates, complaint keywords)

Evaluation using classification reports and confusion matrices

Saving trained models and vectorizers

2. Gradio App
Run Gradio interface for interactive predictions:

bash
Copy
Edit
python gradio_app.py
Features:

Single ticket text input or batch processing

Displays predicted issue type, urgency, and extracted entities

3. Streamlit App
Run Streamlit app for advanced UI and visualizations:

bash
Copy
Edit
streamlit run streamlit_app.py
Features:

Supports single and batch ticket inputs

Visualizes ticket distributions and model performance metrics

Shows feature importance and confusion matrices

Bonus Features Implemented
Ticket distribution plots by issue type and urgency

Feature importance visualization from Random Forest model

Confusion matrices and classification reports for detailed evaluation

Batch processing support in both Gradio and Streamlit apps for multiple ticket inputs

Notes and Limitations
Models trained on the provided dataset may have varying performance on new/unseen data.

Entity extraction uses rule-based methods; some entities may be missed or incorrectly identified.

Sentiment feature is basic; could be improved with advanced NLP methods.

Further tuning and model experimentation recommended for production use.
