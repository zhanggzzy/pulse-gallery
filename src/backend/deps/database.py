# src/backend/deps/database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.backend.config import DB_PATH_ABS, DEBUG_MODE


db_url = f"sqlite:///{DB_PATH_ABS}"

engine = create_engine(db_url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    """
    Dependency to get a database session.
    """

    if DEBUG_MODE:
        print(f"[DEBUG] Creating new database session with URL: {db_url}")

    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        if DEBUG_MODE:
            print(f"[DEBUG] Exception occurred while using database session: {e}")
        db.rollback()
        raise
    finally:
        db.close()