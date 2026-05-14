import streamlit as st
import base64
import pickle

# ---------- PAGE SETUP ----------

st.set_page_config(
    page_title="Fake News Detection",
    page_icon="📰",
    layout="centered"
)

# ---------- PAGE SWITCH ----------

if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------- BACKGROUND FUNCTION ----------

def get_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# =========================================================
# HOME PAGE
# =========================================================

if st.session_state.page == "home":

    # WHITE HOME PAGE DESIGN

    st.markdown("""
    <style>

    .stApp {
        background-color: white;
    }

    h1 {
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

    st.title("📰 AI Fake News Detection System")

    st.markdown("""
    ## Welcome

    Fake news has become one of the biggest challenges in the digital world.

    Social media platforms spread information rapidly, making it difficult to identify whether news is REAL or FAKE.

    This AI-powered Fake News Detection System uses:

    - Machine Learning
    - Natural Language Processing (NLP)
    - Text Analysis

    to classify news articles accurately.

    ---

    ## Why Fake News Detection is Important

    ✅ Prevents misinformation  
    ✅ Creates awareness  
    ✅ Helps people identify trusted news  
    ✅ Reduces online rumors  
    ✅ Supports responsible journalism  

    ---

    ## Categories of News

    🗳 Politics  
    ⚽ Sports  
    🎬 Entertainment  
    💻 Technology  
    🏥 Health  
    💼 Business  
    🌍 International News  
    📱 Social Media News  

    ---

    ## Main Features

    ✅ AI-Based Prediction  
    ✅ Real vs Fake Classification  
    ✅ Fast Detection System  
    ✅ NLP Text Processing  
    ✅ Interactive User Interface  
    ✅ Easy To Use  

    ---

    ## Technologies Used

    🐍 Python  
    🤖 Machine Learning  
    📚 NLP  
    🌐 Streamlit  
    🧠 Scikit-learn  

    ---

    ## Future Scope

    🎤 Voice Input Detection  
    🌍 Multi-language Support  
    🔗 News URL Detection  
    🧠 Deep Learning Integration  
    📱 Better Mobile Support  
    ☁️ Cloud Database Support  

    ---
    """)

    st.markdown("<br>", unsafe_allow_html=True)

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

    # LOGO

    st.image("logo.png", width=150)

    # LOAD MODEL

    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

    # TITLE

    st.title("📰 Fake News Detection")

    st.markdown("### Enter News Article/Text")

    # TEXT AREA

    user_news = st.text_area(
        "Paste News Here",
        height=250
    )

    # DETECT BUTTON

    if st.button("🔍 Detect News"):

        with st.spinner("Detecting Fake News..."):

            news_vector = vectorizer.transform([user_news])

            prediction = model.predict(news_vector)

            st.markdown("<br>", unsafe_allow_html=True)

            if prediction[0] == 0:
                st.error("⚠️ This News is FAKE")
            else:
                st.success("✅ This News is REAL")

    # BACK BUTTON AT BOTTOM

    st.markdown("<br><br><br>", unsafe_allow_html=True)

    if st.button("⬅ Back To Home"):

        st.session_state.page = "home"

        st.rerun()
