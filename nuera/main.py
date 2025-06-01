import webbrowser
import time
import win32com.client
import os
import speech_recognition as sr
import datetime
from config import api_key
from google.generativeai import configure, GenerativeModel
import random
import re

configure(api_key="AIzaSyAviQ3zuLOhNMnnUnEORHTEJhgXxFt6Rcc")
model = GenerativeModel()

chatStr = ""

# ✅ Save both prompt & response in GeminiAI folder
def log_prompt_and_response(prompt_text, response_text):
    folder_path = "../GeminiAI"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(folder_path, f"prompt_{timestamp}.txt")

    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"Prompt: {prompt_text}\n\nResponse:\n{response_text}")

# ✅ Chat function that saves prompt & response
def chat(query):
    global chatStr
    chatStr = f"Srija: {query}\nNeura: "
    try:
        response = model.generate_content(query)
        response_text = response.text if hasattr(response, 'text') else "I couldn't understand that."
        print(f"Neura: {response_text}")
        say(response_text)
        log_prompt_and_response(query, response_text)
        return response_text
    except Exception as e:
        print(f"Error: {str(e)}")
        return "Error in AI response."

# ✅ AI response generator (e.g., for writing emails)
def ai(prompt):
    text = f"AI response for Prompt: {prompt} \n *********************\n\n"
    try:
        response = model.generate_content(prompt)
        if response and hasattr(response, 'text'):
            print(response.text)
            text += response.text
        log_prompt_and_response(prompt, response.text)
    except Exception as e:
        print(f"Error: {e}")
        say("Error communicating with Gemini AI")

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(text):
    if not text or len(text) == 0:
        return
    clean_text = re.sub(r"[*_]", "", text)
    safe_text = clean_text.replace('"', "'")
    if len(clean_text) > 100:
        speaker.Speak(clean_text)
    else:
        command = f'powershell -Command "& {{Add-Type -AssemblyName System.Speech; ' \
                  f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{safe_text}\')}}"'
        try:
            os.system(command)
        except Exception as e:
            speaker.Speak(clean_text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing....")
            query = r.recognize_google(audio, language="en-in")
            print(f"Srija: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Neura"

if __name__ == '__main__':
    say("Hello, I am Neura AI")
    while True:
        print("Listening.....")
        query = takeCommand()

        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"]]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]} mam...")
                webbrowser.open(site[1])

        if "the time" in query:
            strftime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"the time is {strftime}")
        elif "open camera".lower() in query.lower():
            say("opening camera")
            os.system("start explorer shell:appsfolder\\Microsoft.WindowsCamera_8wekyb3d8bbwe!App")
        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)
        elif "Neura Quit".lower() in query.lower():
            exit()
        elif "reset chat".lower() in query.lower():
            chatStr = ""
        else:
            print("chatting....")
            chat(query)