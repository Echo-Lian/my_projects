from gtts import gTTS
import os

text = []
file_path = "/Users/echolian/Library/CloudStorage/OneDrive-UniversityofHelsinki/GitHub/github_repo/my_projects/TTS_reader/extract_text/example.txt"
folder_name = "/Users/echolian/Library/CloudStorage/OneDrive-UniversityofHelsinki/GitHub/github_repo/my_projects/TTS_reader/gTTS/mp3"

# open text file
with open(file_path, "r", encoding="utf-8") as file:
    text = file.read()

# Optionally limit length (gTTS can fail on extremely long text)
max_chars = 4000
chunks = [text[i:i+max_chars] for i in range(0, len(text), max_chars)]

# Convert each chunk to speech
for i, chunk in enumerate(chunks, 1):
    tts = gTTS(chunk, lang='en')
    filename = f"mp3/output_{i}.mp3"
    tts.save(filename)
    os.system(f"afplay {filename}")  # macOS built-in player