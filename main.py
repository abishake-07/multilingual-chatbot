import speech_recognition as sr 
import logging 
import os 
from gtts import gTTS
import google.generativeai as genai 
import streamlit as st 
from dotenv import load_dotenv


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


def text_to_speech(text): 
    """
    Saving the derived text from the model into a audio file
    """
    ttx = gTTS(text=text,lang='en')
    ttx.save("output.mp3")


def configure():
    load_dotenv()


def gemini_model(user_input):
    """
    Configuring the Gemini API credentials 
    """
    genai.configure(api_key=os.getenv('gemini_key'))
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_input)
    results = response.text
    return results








def main():
    '''  
I want to create the following functions:
 1. takeCommand(): This function will take voice input from the microphone.
 2. textToSpeech(): This function will convert the text result into an audio file.
 3. AImodel(): This function will retrieve the Gemini credentials for use in AI tasks.
 4. main(): This will consist of the Streamlit application, integrating all the components.
'''

    configure()

    st.title("Multilingual Chatbot 🤖")

    if st.button("Ask Away!"):
        with st.spinner("Listening...."):
            text = takeCommand()
            response= gemini_model(text)
            text_to_speech(response)
            st.success(f"Response: {response}")
            



    #query = takeCommand()
   # print(query)

main()