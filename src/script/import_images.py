# src/script/import_images.py

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.backend.models.models import Image, Base
from dotenv import load_dotenv

load_dotenv()

image_dir = os.getenv("IMAGE_DIR")
db_path = os.getenv("DB_PATH")

if not image_dir or not db_path:
    raise ValueError("IMAGE_DIR and DB_PATH environment variables must be set.")

db_url = f"sqlite:///{db_path}"
engine = create_engine(db_url, echo=False)
SessionLocal = sessionmaker(bind=engine)



def find_all_images(image_dir):
    """Recursively find all image files in the given directory."""
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}

    for root, _, files in os.walk(image_dir):
        for file in files:
            if os.path.splitext(file)[1].lower() in image_extensions:
                yield os.path.join(root, file)


def import_images():
    """Import images from the specified directory into the database."""
    session = SessionLocal()
    count_new = 0
    count_existing = 0

    for filepath in find_all_images(image_dir):
        filepath = os.path.abspath(filepath)
        filename = os.path.basename(filepath)

        exists = session.query(Image).filter_by(filepath=filepath).first()

        if exists:
            count_existing += 1
            print(f"Image already exists: {filename}")
            continue

        img = Image(filename=filename, filepath=filepath)
        session.add(img)
        count_new += 1
        print(f"Imported image: {filename}")

    session.commit()
    session.close()
    print(f"Import complete: {count_new} new images, {count_existing} existing images.")


if __name__ == "__main__":
    import_images()
