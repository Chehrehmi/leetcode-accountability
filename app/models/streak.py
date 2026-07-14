from sqlalchemy import Column, Integer, Date, ForeignKey
from app.models.base import Base

class Streak(Base):
    __tablename__ = "streaks"

    # We use user_id as primary key here since it's a 1:1 relation to user
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    current = Column(Integer, default=0)
    longest = Column(Integer, default=0)
    last_submission = Column(Date, nullable=True)
