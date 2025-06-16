# src/backend/api/image.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.backend.models.models import Image
from src.backend.deps.database import get_db

import random
import os

router = APIRouter()

@router.get("/random")
def get_random_image(db: Session = Depends(get_db)):
    """
    Get a random image from the database.
    """
    images = db.query(Image).all()
    if not images:
        return {"message": "No images found."}
    
    image = random.choice(images)

    return {
        "id": image.id,
        "name": image.filename,
        "path": os.path.join(os.getenv("IMAGE_DIR", ""), image.filepath)
    }
