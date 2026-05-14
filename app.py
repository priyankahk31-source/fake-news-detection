import streamlit as st
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
    </style>
    """

    st.markdown(page_bg, unsafe_allow_html=True)

    st.image("logo.png", width=150)

    model = pickle.load(open("model.pkl", "rb"))
    vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

    st.title("📰 Fake News Detection")

    user_news = st.text_area("Paste News Here", height=200)

    if st.button("Detect News"):

        with st.spinner("Detecting Fake News..."):

            news_vector = vectorizer.transform([user_news])

            prediction = model.predict(news_vector)

            if prediction[0] == 0:
                st.error("⚠️ Fake News")
            else:
                st.success("✅ Real News")
