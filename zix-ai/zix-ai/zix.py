import os
import speech_recognition as sr
import pyttsx3
from dotenv import load_dotenv
from openai import OpenAI  # New import style

load_dotenv()

class Zix:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # New client initialization

    # ... (keep existing speak/listen methods)

    def ask_gpt(self, question):
        response = self.client.chat.completions.create(  # Updated method chain
            model="gpt-4",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message.content  # Updated response access

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