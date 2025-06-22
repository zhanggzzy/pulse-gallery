# src/backend/api/image.py

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.backend.models.models import Image
from src.backend.deps.database import get_db
from src.backend.config import DEBUG_MODE, IMAGE_DIR_ABS

import random
import os

router = APIRouter()

@router.get("/random")
def get_random_image(db: Session = Depends(get_db)):
    """
    Get a random image from the database.
    """
    if DEBUG_MODE:
        print("[DEBUG] Fetching a random image from the database.")

    try:
        images = db.query(Image).all()
        if not images:
            return {"message": "No images found."}
        
        image = random.choice(images)

        ret_image = {
            "id": image.id,
            "name": image.filename,
            "path": os.path.join(IMAGE_DIR_ABS, image.filepath),
            "ext": image.filepath.split('.')[-1] if '.' in image.filepath else '',
        }

        if DEBUG_MODE:
            print(f"[DEBUG] fetch random image: {ret_image}")

        return ret_image
    except Exception as e:
        if DEBUG_MODE:
            print(f"[DEBUG] Exception occurred while fetching random image: {e}")
        return {"error": "Failed to fetch random image."}
