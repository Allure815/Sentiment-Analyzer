import streamlit as st
from model import preprocess_text, model

st.title("AI Business Review Sentiment Analyzer")

review = st.text_area("Enter a business review:")

if st.button("Analyze Sentiment"):
    if review.strip() == "":
        st.warning("Please enter a review.")
    else:
        processed = preprocess_text(review)
        prediction = model.predict(processed)[0][0]

        if prediction > 0.5:
            st.success("Sentiment: Positive 🙂")
        else:
            st.error("Sentiment: Negative 🙁")


#User types review
#↓
#preprocess_text()
#↓
#model.predict()
#↓
#number (0–1)
#↓
#Positive or Negative
#↓
#Shown on screen
