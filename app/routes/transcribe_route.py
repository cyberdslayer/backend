from fastapi import APIRouter, File, UploadFile, HTTPException
from pathlib import Path
import shutil
import wave
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

# Initialize router
router = APIRouter()

# Path to save uploaded files temporarily
UPLOAD_DIR = Path("uploaded_files")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

@router.post("")
async def transcribe_audio(file: UploadFile = File(...)):
    file_path = UPLOAD_DIR / file.filename

    try:
        # Validate file type
        if not file.content_type.startswith("audio/"):
            raise HTTPException(status_code=400, detail="Unsupported file type.")
        
        # Save file to disk
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Convert audio to WAV if it's not already in that format
        audio = AudioSegment.from_file(file_path)  # pydub can handle various formats (mp3, wav, etc.)
        wav_path = UPLOAD_DIR / (file.filename.rsplit(".", 1)[0] + ".wav")
        audio.export(wav_path, format="wav")  # Export the file as WAV
        
        # Open the WAV file using wave
        with wave.open(str(wav_path), "rb") as audio_file:
            # Ensure the file is in PCM format
            if audio_file.getnchannels() not in [1, 2] or audio_file.getsampwidth() not in [1, 2, 4]:
                raise HTTPException(status_code=400, detail="Invalid audio format.")
        
        # Transcribe using SpeechRecognition
        recognizer = sr.Recognizer()
        with sr.AudioFile(str(wav_path)) as source:
            audio_data = recognizer.record(source)
            transcription = recognizer.recognize_google(audio_data)

        return {"text": transcription}

    except sr.UnknownValueError:
        raise HTTPException(status_code=400, detail="Speech could not be recognized.")
    except sr.RequestError as e:
        raise HTTPException(status_code=500, detail=f"Speech recognition service error: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    finally:
        # Clean up the uploaded and converted files
        if file_path.exists():
            file_path.unlink()
        if wav_path.exists():
            wav_path.unlink()
