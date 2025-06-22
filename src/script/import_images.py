# src/script/import_images.py

import os

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from src.backend.models.models import Image, Base
from src.backend.config import IMAGE_DIR, IMAGE_DIR_ABS, DB_PATH, DB_PATH_ABS

if not IMAGE_DIR or not DB_PATH:
    raise ValueError("IMAGE_DIR and DB_PATH environment variables must be set.")


def find_all_images(image_dir):
    """Recursively find all image files in the given directory."""
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp'}

    for root, _, files in os.walk(image_dir):
        print(f"[LOG] Scanning directory: {root}")
        for file in files:
            if os.path.splitext(file)[1].lower() in image_extensions:
                # add relative path from IMAGE_DIR_ABS to the file
                relative_path = os.path.relpath(os.path.join(root, file), IMAGE_DIR_ABS)
                print(f"[LOG] Image file found: {relative_path}")
                yield relative_path


def import_images():
    """Import images from the specified directory into the database."""
    session = SessionLocal()
    count_new = 0
    count_existing = 0

    for filepath in find_all_images(IMAGE_DIR_ABS):
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
    print(f"[LOG] Importing images from directory: {IMAGE_DIR_ABS}")

    db_url = f"sqlite:///{DB_PATH_ABS}"
    print(f"[LOG] Using database URL: {db_url}")

    engine = create_engine(db_url, echo=False)
    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(bind=engine)

    import_images()
