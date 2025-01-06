import speech_recognition as sr
from os import path
from pydub import AudioSegment


# conveting MP3 Adudio file to WAV format
# sound = AudioSegment.from_mp3("test.mp3")
# sound.export("transcript.wav", format = "wav")

# Transcribing the Audio file to text
AUDIO_FILE = "test.wav"
transcript = ""

audioSource = sr.Recognizer()
with sr.AudioFile(AUDIO_FILE) as source:
    audio = audioSource.record(source)
    try:
        transcript = audioSource.recognize_google(audio)
        print("Text: ", transcript)
    except Exception as e:
        print("Error: ", str(e))

with open("transcript.txt", "w") as export_file:
    export_file.write("Transcript: ")
    export_file.write(transcript)
