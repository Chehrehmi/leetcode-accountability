import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from app.models.base import Base

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    problem_number = Column(Integer, nullable=False)
    difficulty = Column(String, nullable=True) # Easy, Medium, Hard
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
