from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from gtts import gTTS
import io
from pydantic import BaseModel

router = APIRouter()


class SynthesizeRequest(BaseModel):
    text: str

@router.post("")
async def synthesize(request: SynthesizeRequest):
    if not request.text:
        raise HTTPException(status_code=400, detail="Text parameter is required")

    tts = gTTS(request.text)
    audio_file = io.BytesIO()
    tts.write_to_fp(audio_file)
    audio_file.seek(0)

    return StreamingResponse(audio_file, media_type="audio/mp3", headers={"Content-Disposition": "attachment; filename=synthesized_audio.mp3"})
