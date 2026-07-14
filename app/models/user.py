import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app.models.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    discord_id = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, nullable=False)
    joined_at = Column(DateTime, default=datetime.datetime.utcnow)
