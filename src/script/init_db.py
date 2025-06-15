# src/script/init_db.py

import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from src.backend.models.models import Base


load_dotenv()
db_path = os.getenv("DB_PATH")

if not db_path:
    raise ValueError("DB_PATH environment variable is not set.")

db_url = f"sqlite:///{db_path}"
print(f"Connecting to database at {db_url}")

engine = create_engine(db_url)
Base.metadata.create_all(engine)
print("Database initialized successfully.")