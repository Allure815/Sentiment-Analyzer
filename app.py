import streamlit as st
from model import preprocess_text, model

st.title("🧠 AI Business Review Sentiment Analyzer")

review = st.text_area("Enter a business review:")

if st.button("Analyze Sentiment"):

    # ✅ 4️⃣ Input Validation
    if review.strip() == "":
        st.warning("⚠️ Please enter a valid review.")
    
    else:
        # ✅ 5️⃣ Loading Spinner
        with st.spinner("Analyzing..."):
            processed = preprocess_text(review)
            prediction = model.predict(processed)[0][0]

        # ✅ 1️⃣ Confidence Score
        confidence = prediction if prediction > 0.5 else (1 - prediction)

        # Convert to percentage
        confidence_percent = confidence * 100

        # ✅ 2️⃣ Emoji Output
        if prediction > 0.5:
            sentiment = "Positive"
            emoji = "😊"
            st.success(f"{emoji} {sentiment} ({confidence_percent:.2f}% confidence)")
        else:
            sentiment = "Negative"
            emoji = "😡"
            st.error(f"{emoji} {sentiment} ({confidence_percent:.2f}% confidence)")


# ✅ 7️⃣ Model Info Section
st.markdown("---")
st.subheader("Model Info")

st.write("Model: LSTM (TensorFlow/Keras)")
st.write("Dataset: Custom 6-sentence dataset (demo)")
st.write("Accuracy: Not reliable (toy dataset)")