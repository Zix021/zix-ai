import os
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
import openai

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

class Zix:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.recognizer.listen(source)
            try:
                return self.recognizer.recognize_google(audio)
            except:
                return ""

    def ask_gpt(self, question):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message['content']

if __name__ == "__main__":
    zix = Zix()
    zix.speak("Hello, I am Zix. How can I assist you?")
    while True:
        command = zix.listen().lower()
        if "goodbye" in command:
            zix.speak("Goodbye!")
            break
        elif command:
            answer = zix.ask_gpt(command)
            zix.speak(answer)