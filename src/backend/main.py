# src/backend/main.py

from fastapi import FastAPI
from src.backend.api import image
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.routing import APIRoute
from src.backend.config import DEBUG_MODE, IMAGE_DIR_ABS, is_prod



# Initialize FastAPI application
app = FastAPI(title="Pulse Gallery API", version="0.0.1")

if is_prod():
    app.mount("/images", StaticFiles(directory="data/images"), name="images")
    app.mount("/", StaticFiles(directory="static", html=True), name="frontend")
else:
    app.mount("/images", StaticFiles(directory=IMAGE_DIR_ABS), name="images")

app.include_router(image.router, prefix="/api/image")

if DEBUG_MODE:
    print("[DEBUG] === Registered Routes ===")
    for route in app.routes:
        if isinstance(route, APIRoute):
            print(f"[DEBUG] [route] path: {route.path} - methods: {route.methods}")
        else:
            print(f"[DEBUG] [mount] path: {route.path} - type: {type(route)}")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
