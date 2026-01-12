# model.py
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
import numpy as np

# 6-sentence dataset
texts = [
    "this product is good",
    "amazing service and support",
    "very bad experience",
    "worst product ever",
    "i love this",
    "i hate this"
]
labels = [1, 1, 0, 0, 1, 0]  # 1=positive, 0=negative

# Tokenizer
tokenizer = Tokenizer(num_words=5000, oov_token="<OOV>")
tokenizer.fit_on_texts(texts)
max_len = 10

# Prepare sequences
X = pad_sequences(tokenizer.texts_to_sequences(texts), maxlen=max_len)
y = np.array(labels)

# LSTM model
model = Sequential([
    Embedding(input_dim=5000, output_dim=16, input_length=max_len),
    LSTM(16),
    Dense(1, activation="sigmoid")
])

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
model.fit(X, y, epochs=200, verbose=0)

# Preprocess function
def preprocess_text(text):
    return pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=max_len)
