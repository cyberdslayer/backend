from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.transcribe_route import router as transcribe_router
from routes.synthesize_route import router as synthesize_router
import os
from dotenv import load_dotenv

app = FastAPI()

load_dotenv()

frontend_url = os.getenv("FRONTEND_URL")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[frontend_url],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Register routes
app.include_router(transcribe_router, prefix="/api/transcribe")
app.include_router(synthesize_router, prefix="/api/synthesize")
