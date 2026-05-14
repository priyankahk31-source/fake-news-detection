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

h2, h3 {{
    color: white !important;
}}

p, li {{
    color: white !important;
    font-size: 18px;
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

# ---------- HOME PAGE ----------

st.title("📰 AI Fake News Detection System")

st.markdown("""

## Welcome

Fake news spreads misinformation rapidly through social media and digital platforms.

This AI-powered system helps users identify whether a news article is REAL or FAKE using Machine Learning and NLP.

---

## Categories of News

🗳 Politics  
⚽ Sports  
🎬 Entertainment  
💻 Technology  
🏥 Health  
💼 Business  

---

## Features

✅ AI Detection  
✅ Fast Prediction  
✅ User Friendly Interface  
✅ Machine Learning Based  
✅ NLP Processing  

---

## Technologies Used

🐍 Python  
🤖 Machine Learning  
📚 NLP  
🌐 Streamlit  
🧠 Scikit-learn  

---

## Future Scope

🎤 Voice Input  
🌍 Multi-language Detection  
🔗 News URL Detection  
🧠 BERT & Deep Learning  
📱 Mobile Friendly System

---
""")

# ---------- START BUTTON ----------

start = st.button("🚀 Start Detection")

# ---------- MAIN DETECTOR ----------

if start:

    st.subheader("📝 Enter News Article")

    user_news = st.text_area(
        "Paste News Here",
        height=200
    )

    if st.button("Detect News"):

        with st.spinner("Detecting Fake News..."):

            news_vector = vectorizer.transform([user_news])

            prediction = model.predict(news_vector)

            if prediction[0] == 0:
                st.error("⚠️ Fake News")
            else:
                st.success("✅ Real News")
