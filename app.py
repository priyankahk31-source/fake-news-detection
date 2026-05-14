import streamlit as st
import base64
import pickle

# ---------- PAGE SWITCH ----------

if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- BACKGROUND ----------

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# ---------- HOME PAGE ----------

if st.session_state.page == "home":

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
🔗 URL Detection  
🧠 Deep Learning  
📱 Mobile Friendly  

""")

    if st.button("🚀 Start Detection"):
        st.session_state.page = "detect"
        st.rerun()

# ---------- DETECTOR PAGE ----------

elif st.session_state.page == "detect":

    img = get_base64("background.jpg")

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

    st.image("logo.png", width=150)

    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

    st.title("📰 Fake News Detection")
    st.markdown("<br><br>", unsafe_allow_html=True)

    if st.button("⬅ Back to Home"):

    st.session_state.page = "home"

    st.rerun()
    user_news = st.text_area("Paste News Here", height=200)

    if st.button("Detect News"):

        with st.spinner("Detecting Fake News..."):

            news_vector = vectorizer.transform([user_news])

            prediction = model.predict(news_vector)

            if prediction[0] == 0:
                st.error("⚠️ Fake News")
            else:
                st.success("✅ Real News")
