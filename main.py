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


### 