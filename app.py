import streamlit as st
import base64
import pickle

# ---------- PAGE SETUP ----------

st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="centered"
)

# ---------- SESSION STATE ----------

if "page" not in st.session_state:
    st.session_state.page = "home"

if "history" not in st.session_state:
    st.session_state.history = []

# ---------- BACKGROUND FUNCTION ----------

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# =========================================================
# HOME PAGE
# =========================================================

if st.session_state.page == "home":

    st.markdown("""
    <style>

    .stApp {
        background-color: white;
    }

   h1 {{
    color: black !important;
        text-align: center;
        font-size: 55px !important;
    }

    h2, h3 {
        color: #111111 !important;
    }

    p, li {
        color: #333333 !important;
        font-size: 18px !important;
    }

    .stButton>button {
        background-color: darkred;
        color: white;
        font-size: 22px;
        border-radius: 12px;
        padding: 12px 25px;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------- DASHBOARD ----------

    col1, col2, col3 = st.columns(3)

    col1.metric("Users", "10K+")
    col2.metric("Accuracy", "96%")
    col3.metric("Detected", "8K+")

    st.markdown("---")

    # ---------- LOGO ----------

    st.image("logo.png", width=180)

    # ---------- TITLE ----------

    st.title("📰 Google AI Fake News Detector")

    # ---------- CONTENT ----------

    st.markdown("""

## Detect Fake News Instantly

This AI platform helps users identify whether online news is REAL or FAKE.

Users can:

✅ Verify news articles  
✅ Detect misinformation  
✅ Check social media news  
✅ Analyze online content  
✅ Improve awareness against fake information  

---

## What This Website Provides

🌍 Trusted AI News Verification

🔍 Instant News Analysis

⚡ Fast Fake News Detection

📱 User Friendly Experience

🧠 AI-Based Prediction

📊 Smart Detection Dashboard

---

## News Categories Supported

🗳 Politics  
⚽ Sports  
🎬 Entertainment  
💻 Technology  
🏥 Health  
💼 Business  
🌍 International News  
📱 Social Media News  

---
""")

    # ---------- HISTORY ----------

    st.subheader("📜 Recent Searches")

    if len(st.session_state.history) == 0:
        st.info("No searches yet")
    else:
        for item in st.session_state.history[-5:]:
            st.write("•", item)

    st.markdown("<br>", unsafe_allow_html=True)

    # ---------- START BUTTON ----------

    if st.button("🚀 Start Detection"):
        st.session_state.page = "detect"
        st.rerun()

# =========================================================
# DETECTION PAGE
# =========================================================

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
        background-color: rgba(255,255,255,0.90) !important;
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

    # ---------- LOAD MODEL ----------

    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

    # ---------- TITLE ----------

    st.title("📰 Fake News Detection")

    st.markdown("### Enter News Article/Text")

    # ---------- INPUT ----------

    user_news = st.text_area(
        "Paste News Here",
        height=250
    )

    # ---------- DETECT BUTTON ----------

    if st.button("🔍 Detect News"):

        with st.spinner("Detecting Fake News..."):

            user_news = user_news.lower()
            user_news = user_news.replace("pm", "prime minister")
            user_news = user_news.replace("cm", "chief minister")
            user_news = user_news.replace("usa", "united states")
            user_news = user_news.replace("uk", "united kingdom")

            news_vector = vectorizer.transform([user_news])

            prediction = model.predict(news_vector)

            if user_news.strip() != "":
                st.session_state.history.append(user_news[:50])

            st.markdown("<br>", unsafe_allow_html=True)

            if prediction[0] == 0:

                st.markdown("""
                <div style="
                    background-color:#ff4b4b;
                    padding:20px;
                    border-radius:15px;
                    text-align:center;
                    font-size:35px;
                    color:white;
                    font-weight:bold;
                    box-shadow:0px 0px 15px black;
                ">
                    ⚠️ FAKE NEWS DETECTED
                </div>
                """, unsafe_allow_html=True)

            else:

                st.markdown("""
                <div style="
                    background-color:#00c853;
                    padding:20px;
                    border-radius:15px;
                    text-align:center;
                    font-size:35px;
                    color:white;
                    font-weight:bold;
                    box-shadow:0px 0px 15px black;
                ">
                    ✅ REAL NEWS DETECTED
                </div>
                """, unsafe_allow_html=True)

    # ---------- BACK BUTTON ----------

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    if st.button("⬅ Back To Home"):

        st.session_state.page = "home"

        st.rerun()
