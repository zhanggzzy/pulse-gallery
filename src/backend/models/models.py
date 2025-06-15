# src/backend/models/models.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()


class Image(Base):
    __tablename__ = 'images'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    filename = Column(String, nullable=False)
    filepath = Column(String, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())


class DisplayRecord(Base):
    __tablename__ = 'display_records'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    image_id = Column(Integer, ForeignKey('images.id'), nullable=False)
    display_time = Column(DateTime(timezone=True), server_default=func.now())
