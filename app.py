import streamlit as st

from groq import Groq

import streamlit as st

from groq import Groq

from PIL import Image

from transformers import pipeline

from gtts import gTTS

from streamlit_mic_recorder import speech_to_text

import random

import tempfile


# ======================
# CONFIG
# ======================

client = Groq(
    api_key=st.secrets["GROQ_API_KEY"]
)

st.set_page_config(
    page_title="KrishiMitra AI",
    page_icon="🌱",
    layout="wide"
)

st.markdown(
"""

<style>


.stApp {

background:
linear-gradient(
120deg,
#f0fff4,
#ffffff
);

}


h1 {

color:#1b5e20;

font-size:45px;

}


.stButton button {

background-color:#2e7d32;

color:white;

border-radius:20px;

padding:10px 25px;

font-weight:bold;

}


.stTabs [data-baseweb="tab"] {

font-size:18px;

font-weight:600;

}


[data-testid="stSidebar"] {

background-color:#e8f5e9;

}


</style>


""",

unsafe_allow_html=True

)



# ======================
# Languages
# ======================


languages={

"English":{
    "tts":"en",
    "speech":"en-IN"
},

"Hindi":{
    "tts":"hi",
    "speech":"hi-IN"
},

"Telugu":{
    "tts":"te",
    "speech":"te-IN"
},

"Tamil":{
    "tts":"ta",
    "speech":"ta-IN"
},

"Kannada":{
    "tts":"kn",
    "speech":"kn-IN"
},

"Malayalam":{
    "tts":"ml",
    "speech":"ml-IN"
},

"Marathi":{
    "tts":"mr",
    "speech":"mr-IN"
}

}



# ======================
# AI Chat
# ======================


def krishi_ai(question,language):


    prompt=f"""

    You are KrishiMitra AI.

    Reply only in {language}.

    Help farmers using natural farming.

    Question:

    {question}

    """


    response=client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
            "role":"user",
            "content":prompt
            }
        ]

    )


    return response.choices[0].message.content



# ======================
# Text To Speech
# ======================


def speak(text,language):


    tts=gTTS(

        text=text,

        lang=languages[language]["tts"]

    )


    file=tempfile.NamedTemporaryFile(

        delete=False,

        suffix=".mp3"

    )


    tts.save(
        file.name
    )


    return file.name


# ======================
# Image Model
# ======================


@st.cache_resource

def load_model():


    return pipeline(

        "image-classification",

        model=
        "Diginsa/Plant-Disease-Detection-Project"

    )



classifier=load_model()



def detect_disease(image,language):


    result=classifier(
        image
    )[0]


    disease=result["label"]

    confidence=round(
        result["score"]*100,
        2
    )


    advice=krishi_ai(

        f"""

        Disease detected:
        {disease}

        Confidence:
        {confidence}

        Suggest organic treatment.

        """,

        language

    )


    return disease,confidence,advice




# ======================
# Weather
# ======================


def weather_advice(
    city,
    crop,
    language
):


    temp=random.randint(
        22,
        42
    )


    humidity=random.randint(
        40,
        90
    )


    price=random.randint(
        1000,
        9000
    )


    prompt=f"""

    City:{city}

    Crop:{crop}

    Temperature:{temp}

    Humidity:{humidity}

    Market price ₹{price}

    Give farming advice.

    """


    return krishi_ai(
        prompt,
        language
    )



# ======================
# UI
# ======================


st.markdown(
"""

# 🌱 KrishiMitra AI

### 🎤 Multilingual Natural Farming Voice Assistant

Helping farmers with AI-powered crop guidance

---

""",
unsafe_allow_html=True
)


st.sidebar.image(
"https://cdn-icons-png.flaticon.com/512/628/628283.png",
width=100
)


st.sidebar.title(
"🌾 Settings"
)


language=st.sidebar.selectbox(

"🌐 Choose Farmer Language",

list(languages.keys())

)


st.sidebar.info(

"""
Features:

🎤 Voice Assistant

🌿 Disease Detection

🌦 Weather Insights

📈 Market Advisory
"""

)



tab1,tab2,tab3=st.tabs(

[
"💬 Farming Assistant",

"🌿 Disease Detection",

"🌦 Weather & Market"

]

)



# CHAT

with tab1:


    st.subheader(
        "🎤 Talk with KrishiMitra AI"
    )


    if "question" not in st.session_state:

        st.session_state.question=""


    voice_question = speech_to_text(


        language=
        languages[language]["speech"],


        start_prompt=
        "🎤 Start Speaking",


        stop_prompt=
        "🛑 Stop Recording",


        just_once=True


    )


    if voice_question:


        st.session_state.question = voice_question



    typed_question = st.text_input(

        "Or type your farming question",

        value=st.session_state.question

    )


    if typed_question:


        st.session_state.question = typed_question



    if st.session_state.question:


        st.info(

            "👨‍🌾 Farmer asked: "
            +
            st.session_state.question

        )



    if st.button(
        "🌱 Get Advice"
    ):


        if st.session_state.question:


            with st.spinner(

                "🌱 KrishiMitra is thinking..."

            ):


                ans = krishi_ai(

                    st.session_state.question,

                    language

                )


            st.success(
                "🌱 KrishiMitra Advice"
            )


            st.write(ans)



            st.audio(

                speak(

                    ans,

                    language

                )

            )


        else:


            st.warning(

                "Please speak or type a question first"

            )

# IMAGE

# ======================
# DISEASE DETECTION TAB
# ======================


with tab2:


    st.subheader(
        "🌿 AI Crop Disease Doctor"
    )


    st.write(
        """
        Upload a crop leaf image and KrishiMitra AI will:

        🔍 Detect possible crop disease  
        📊 Show confidence level  
        🌱 Suggest natural organic treatment  
        🛡 Give prevention methods
        """
    )


    uploaded = st.file_uploader(

        "📷 Upload crop leaf image",

        type=[
            "jpg",
            "jpeg",
            "png"
        ]

    )


    if uploaded:


        img = Image.open(
            uploaded
        )


        col1, col2 = st.columns(2)


        with col1:


            st.image(

                img,

                caption="Uploaded Crop Image",

                use_container_width=True

            )


        with col2:


            with st.spinner(
                "🌱 Analyzing crop health..."
            ):


                disease, conf, advice = detect_disease(

                    img,

                    language

                )


            st.success(
                "🌿 Detection Complete"
            )


            st.metric(

                "Detected Disease",

                disease

            )


            st.metric(

                "Confidence",

                f"{conf}%"

            )


        st.divider()


        st.subheader(
            "🌱 Organic Treatment Advice"
        )


        st.write(
            advice
        )


        st.audio(

            speak(
                advice,
                language
            )

        )


# WEATHER

with tab3:


    city=st.text_input(
        "Enter city/village"
    )


    crop=st.text_input(
        "Enter crop"
    )


    if st.button(
        "Analyze"
    ):


        result=weather_advice(
            city,
            crop,
            language
        )


        st.write(result)


        st.audio(
            speak(
                result,
                language
            )
        )