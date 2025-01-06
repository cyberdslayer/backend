from fastapi import APIRouter, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from fastapi import FastAPI


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

router = APIRouter()

@app.get("/")
async def root():
    return {"message" : "Hello World"}

import shutil
from pathlib import Path


# Path to save uploaded files temporarily
UPLOAD_DIR = Path("uploaded_files")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

class TranscriptionResponse(BaseModel):
    text: str

@app.post("/api/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Accept an audio file, save it, and return a hardcoded transcription.
    """
    try:
        # Ensure the file is an audio file
        if not file.content_type.startswith("audio/"):
            raise HTTPException(status_code=400, detail="Unsupported file type.")

        # Save the uploaded file to the temporary directory
        file_path = UPLOAD_DIR / file.filename
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Return a hardcoded response (replace this with actual transcription logic if needed)
        return {"text": "This is a sample transcription for the uploaded audio file."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")
    finally:
        # Clean up: Remove the uploaded file (optional)
        if file_path.exists():
            file_path.unlink()
