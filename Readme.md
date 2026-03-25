

# Business Review Sentiment Analyzer

## Overview

The **Business Review Sentiment Analyzer** is a machine learning project that analyzes customer reviews and predicts whether the sentiment of the review is **positive or negative**.

The goal of this project is to demonstrate how **Natural Language Processing (NLP)** and **Machine Learning** can help businesses quickly understand customer feedback.

---

## Problem Statement

Businesses receive a large number of customer reviews across different platforms.
Manually analyzing each review to understand customer sentiment can be:

* Time-consuming
* Inconsistent
* Difficult to scale

This project provides an automated way to **classify reviews based on sentiment**.

---

## Features

* Accepts customer review text as input
* Cleans and processes the text data
* Uses a trained machine learning model to predict sentiment
* Displays a **sentiment score and prediction**
* Simple and interactive interface built using **Streamlit**

---

## How It Works

1. The user enters a business review.
2. The review text is **preprocessed** (cleaning, tokenization, etc.).
3. The processed text is passed to a **trained sentiment analysis model**.
4. The model generates a **sentiment score**.
5. The score is mapped to either:

   * **Positive**
   * **Negative**

---

## Tech Stack

* **Python**
* **Machine Learning**
* **Natural Language Processing (NLP)**
* **Streamlit** (for UI)

---

## Project Structure

```
business-review-sentiment-analyzer
│
├── app.py                 # Streamlit application
├── model.pkl              # Trained sentiment model
├── requirements.txt       # Project dependencies
└── README.md              # Project documentation
```


🎥 Demo Video:
https://github.com/Allure815/Sentiment-Analyzer/blob/main/Demo-Sentiment%20analyzer.mp4

---

## Application Screenshot

Below is the interface of the sentiment analyzer:

📷 Screenshot:
https://github.com/Allure815/Sentiment-Analyzer/blob/main/Sentiment-ss.png

---

## Use Cases

* Customer feedback analysis
* Brand reputation monitoring
* Product review analysis
* Learning project for **NLP and Machine Learning**

---

## Status

Prototype project created for **learning and demonstration purposes**.
Future improvements may include:

* Multi-class sentiment (Positive / Neutral / Negative)
* Real-time review scraping
* Visualization dashboards
