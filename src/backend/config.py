# src/backend/config.py

import os
import sys
from dotenv import load_dotenv

load_dotenv()

DEBUG_MODE: bool = os.getenv("DEBUG_MODE", "false").lower() == "true"
ENV: str = os.getenv("ENV", "development")
PROJECT_ROOT_DIR: str = os.path.abspath(
    os.getenv("PROJECT_ROOT_DIR", os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
IMAGE_DIR: str = os.getenv("IMAGE_DIR", "data/images")
IMAGE_DIR_ABS: str = os.path.abspath(IMAGE_DIR)
DB_PATH: str = os.getenv("DB_PATH", "data/database.db")
DB_PATH_ABS: str = os.path.abspath(DB_PATH)

if DEBUG_MODE:
    print(f"[DEBUG] Loaded configuration:"
            f"\n    {DEBUG_MODE=},"
            f"\n    {ENV=},"
            f"\n    {PROJECT_ROOT_DIR=}"
            f"\n    {IMAGE_DIR=},"
            f"\n    {IMAGE_DIR_ABS=},"
            f"\n    {DB_PATH=},"
            f"\n    {DB_PATH_ABS=},"
            )


if PROJECT_ROOT_DIR not in sys.path:
    sys.path.append(PROJECT_ROOT_DIR)


def is_prod() -> bool:
    """
    Check if the application is running in production mode.
    """
    return ENV.lower() == "production"