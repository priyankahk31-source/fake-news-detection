import streamlit as st
import pandas as pd
import base64

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# BACKGROUND IMAGE
def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_base64("background.png")

page_bg = f"""
<style>
.stApp {{
    background-image: url("data:image/png;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

textarea {{
    background-color: rgba(255,255,255,0.85) !important;
    color: black !important;
}}

h1 {{
    color: white !important;
    text-align: center;
    font-size: 55px !important;
}}

.stButton>button {{
    background-color: darkred;
    color: white;
    font-size: 20px;
    border-radius: 12px;
}}
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# LOAD DATA
fake = pd.read_csv("Fake.csv")
true = pd.read_csv("True.csv")

fake["label"] = 0
true["label"] = 1

data = pd.concat([fake, true])

data["content"] = data["title"] + " " + data["text"]

X = data["content"]
y = data["label"]

vectorizer = TfidfVectorizer(stop_words='english')

X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

model = LogisticRegression()

model.fit(X_train, y_train)

st.title("Fake News Detection")

user_news = st.text_area("Enter News Here")

if st.button("Detect"):

    news_vector = vectorizer.transform([user_news])

    prediction = model.predict(news_vector)

    if prediction[0] == 0:
        st.error("Fake News")
    else:
        st.success("Real News")
