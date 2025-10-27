This project aims to build some TTS (Text to Speech) Reader application from easiest to highest-quality, which includes concrete commands and small code examples, and point out trade-offs for example CPU vs GPU, offline vs cloud and licenses etc.

Level:
1. Super simple, offline, low-effort: `pyttsx3` (local, built-in voices)

2. Free + good quality, easy server: `gTTS` (Google TTS wrapper) or coqui/tts CLI (open-source)

3. High-quality neural TTS: VITS / Tacotron2 + HiFi-GAN, Tortoise TTS, or Coqui TTS models — best with GPU

4. Turn it into a reader app: add a GUI (PySimpleGUI / Tkinter) or a small web UI (Flask / Streamlit) + caching