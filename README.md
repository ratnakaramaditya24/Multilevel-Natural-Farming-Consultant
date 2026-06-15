# Multilevel-Natural-Farming-Consultant
# 🌱 KrishiMitra AI - Multilevel Natural Farming Consultant

KrishiMitra AI is a multilingual AI-powered farming assistant designed to support farmers with crop guidance, disease identification, weather-based recommendations, and market insights through an easy-to-use voice-enabled interface.

**KrishiMitra means "Farmer's Friend"** — an AI companion that helps farmers make better agricultural decisions using modern AI technology.


## 🚀 Project Overview

Many farmers face challenges in getting quick and reliable agricultural guidance, especially in regional languages.

KrishiMitra AI solves this problem by providing:

- 🎤 Voice-based farming assistance
- 🌿 AI crop disease detection
- 🌦 Weather-based farming recommendations
- 📈 Crop market intelligence
- 🗣 Multiple Indian language support
- 🌱 Natural and organic farming solutions

The system focuses on accessibility for farmers by enabling interaction through speech and regional languages.


## ✨ Features

### 🎤 1. Voice Enabled AI Farming Assistant

Farmers can interact naturally using voice.

Workflow:

Farmer Speech
      ↓
Speech Recognition
      ↓
Groq Llama AI
      ↓
Farming Advice
      ↓
Text-to-Speech Response

Features:

- Voice input support
- AI-generated farming advice
- Regional language responses
- Audio output for farmers


### 🌿 2. Crop Disease Detection

Farmers can upload crop leaf images.

The AI system:

- Detects possible crop diseases
- Provides confidence score
- Explains symptoms
- Suggests natural treatments
- Gives prevention methods

Focus:
✔ Organic solutions  
✔ Natural farming practices  
✔ Farmer-friendly explanations  


### 🌦 3. Weather Intelligence

Prototype weather module provides:

- Dynamic temperature simulation
- Humidity information
- Crop-specific recommendations
- Irrigation guidance
- Disease risk prediction

The architecture supports integration with real-time weather APIs.


### 📈 4. Market Intelligence

The system provides:

- Crop price insights
- Selling recommendations
- AI-generated market guidance

Helping farmers make better selling decisions.


### 🌐 5. Multilingual Support

Supported Indian languages:

- English
- Hindi
- Telugu
- Tamil
- Kannada
- Malayalam
- Marathi

Farmers can:

✔ Speak in their language  
✔ Receive AI advice in their language  
✔ Listen to responses through audio  


## 🛠️ Tech Stack

### Frontend

- Streamlit

### AI / Machine Learning

- Groq API
- Llama 3.3 70B Versatile Model
- Hugging Face Transformers

### Computer Vision

- Hugging Face Plant Disease Detection Model

### Voice Technology

- Speech Recognition
- Google Text-To-Speech (gTTS)
- Streamlit Mic Recorder

### Other Libraries

- Python
- PyTorch
- Pillow
- Transformers


## 🧠 AI Architecture


                 User / Farmer
                       |
        --------------------------------
        |                              |
   Voice Question                 Crop Image
        |                              |
 Speech Recognition            Vision Model
        |                              |
        -------- Groq Llama AI --------
                       |
              Farming Intelligence
                       |
        --------------------------------
        |                              |
     Text Advice                Voice Response



## 📂 Project Structure

KrishiMitra-AI

│
├── app.py
│
├── requirements.txt
│
├── packages.txt
│
└── README.md


## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/KrishiMitra-AI.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run Streamlit:

```bash
streamlit run app.py
```


## 🔐 Environment Setup

Add your Groq API key in Streamlit secrets:

```toml
GROQ_API_KEY="your_api_key"
```


## 📌 Future Improvements

- Real-time weather API integration
- Live mandi price integration
- Offline farmer assistant support
- More regional languages
- Mobile application deployment


## 🎯 Impact

KrishiMitra AI aims to make agricultural knowledge more accessible by combining:

🌱 Artificial Intelligence  
🎤 Voice Technology  
🌿 Natural Farming Knowledge  
🌎 Regional Language Support  

to empower farmers with instant and intelligent farming assistance.


## 👨‍💻 Developed For

AI Assignment - Connecting Dreams Foundation

Building technology that supports farmers and sustainable agriculture.

