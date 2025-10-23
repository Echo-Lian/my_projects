import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate', 150)     # words per minute
engine.setProperty('volume', 0.9)   # 0.0 to 1.0

text = "Hello! This is my TTS reader. I want to creat a tts reader for free once for all!"
engine.say(text)
engine.runAndWait()
