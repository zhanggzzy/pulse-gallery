# src/backend/main.py

from fastapi import FastAPI
from src.backend.api import image
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from dotenv import load_dotenv
import os


load_dotenv()
image_dir = os.getenv("IMAGE_DIR")

app = FastAPI(title="Pulse Gallery API", version="0.0.1")

app.mount("/images", StaticFiles(directory=image_dir), name="images")
app.include_router(image.router, prefix="/api/image")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
