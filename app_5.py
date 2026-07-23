import streamlit as st
import joblib

# Load the saved model and vectorizer
files = joblib.load("NLP_casestudy_files (2).pkl")

model = files["model"]
vectorizer = files["vectorizer"]

st.set_page_config(page_title="Email Spam Detection", page_icon="📧")

st.title("📧 Email Spam Detection")
st.write("Enter an email message below and click **Predict**.")

email = st.text_area("Email Text")

if st.button("Predict"):

    if email.strip() == "":
        st.warning("Please enter an email.")
    else:
        email_vector = vectorizer.transform([email])
        prediction = model.predict(email_vector)[0]

        if prediction == 1:
            st.error("🚫 Spam Email")
        else:
            st.success("✅ Not Spam Email")