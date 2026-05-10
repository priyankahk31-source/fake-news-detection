import streamlit as st
import base64
import pickle

# ---------- BACKGROUND IMAGE ----------

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_base64("background.jpg")

# ---------- PAGE DESIGN ----------

page_bg = f"""
<style>

.stApp {{
    background-image: url("data:image/jpg;base64,{img}");
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

textarea {{
    background-color: rgba(255,255,255,0.85) !important;
    color: black !important;
    font-size: 18px !important;
}}

h1 {{
    color: white !important;
    text-align: center;
    font-size: 55px !important;
    text-shadow: 2px 2px 5px black;
}}

.stButton>button {{
    background-color: darkred;
    color: white;
    font-size: 20px;
    border-radius: 12px;
    padding: 10px 20px;
}}

</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

# ---------- LOGO ----------

st.image("logo.png", width=150)

# ---------- LOAD SAVED MODEL ----------

model = pickle.load(open("model.pkl", "rb"))

vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# ---------- TITLE ----------

st.title("📰 Fake News Detection")

# ---------- USER INPUT ----------

user_news = st.text_area(
    "Enter News Here",
    height=200
)

# ---------- DETECT BUTTON ----------

if st.button("Detect"):

    with st.spinner("Detecting Fake News..."):

        news_vector = vectorizer.transform([user_news])

        prediction = model.predict(news_vector)

        if prediction[0] == 0:
            st.error("⚠️ Fake News")
        else:
            st.success("✅ Real News")
