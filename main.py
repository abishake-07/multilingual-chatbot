import speech_recognition as sr 
import logging 
import os 
from gtts import gTTS
import google.generativeai as genai 
import streamlit as st 


# Making a logger file to understand the different instances ( functions ) executed 
LOG_DIR  = "logs_dir"
LOG_FILE_NAME = "system.log"

os.makedirs(LOG_DIR,exist_ok=True)

log_path = os.path.join(LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(
    filename=log_path,
    format="[%(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

'''  
I want to create the following functions:
 1. takeCommand(): This function will take voice input from the microphone.
 2. textToSpeech(): This function will convert the text result into an audio file.
 3. AImodel(): This function will retrieve the Gemini credentials for use in AI tasks.
 4. main(): This will consist of the Streamlit application, integrating all the components.
'''


def takeCommand():
    """
    This function takes a voice command & recognizes your saying based on your accent

    Returns:
        text as query
    """
    recog  = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening to your query....')
        recog.pause_threshold=1
        audio = recog.listen(source)

    try: 
        print('Recognizing...')
        query = recog.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e: 
        logging.info(e)
        print('Please try again!')
        return "None"
    return query


