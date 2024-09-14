# 🎙️ Multilingual Voice Chatbot 🤖

This project implements a **multilingual voice-controlled chatbot** using **Python**, **Google Text-to-Speech (gTTS)**, and **Streamlit**. It can **listen** to your voice commands, **recognize** them, **generate a response** using the **Gemini AI API**, and **speak** the response back to you. It's perfect for hands-free interactions in multiple languages!

---

## 🚀 Features
- **Voice Command Input**: Interact using your voice; the chatbot listens and understands.
- **Multilingual Support**: Recognizes voice commands in multiple accents.
- **AI-Powered Responses**: Get intelligent responses using the **Gemini AI** API.
- **Speech Output**: Chatbot speaks its response, creating a conversational experience.

---

## 🛠️ How it Works

1. **Take Voice Input**:  
   - The function `takeCommand()` listens for voice input via your microphone.
   - It recognizes the speech using **Google's Speech Recognition API** and returns it as text.

2. **Generate AI Response**:  
   - The `gemini_model()` function retrieves credentials from your environment and uses the **Gemini AI** API to generate responses based on the input text.

3. **Convert Text to Speech**:  
   - Once the response is generated, `text_to_speech()` converts the text response into an audio file using **gTTS** and saves it as `output.mp3`.

4. **Streamlit Application**:  
   - The `main()` function integrates the entire application into a **Streamlit** interface, making it easy to interact with the chatbot via a web interface.
   - Press the **"Ask Away!"** button, and the chatbot will listen, respond, and speak!

---

## 🛑 Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.x**  
- **requirements.txt**: `pip install streamlit`  
- **dotenv** for environment variable handling:  
  `pip install python-dotenv`

- Make your Gemini API key! 

---

## 🔧 Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/multilingual-voice-chatbot.git
   cd multilingual-voice-chatbot
