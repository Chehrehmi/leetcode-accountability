import datetime
from sqlalchemy.orm import Session
from app.models.streak import Streak

class StreakRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_streak(self, user_id: int) -> Streak | None:
        return self.db.query(Streak).filter(Streak.user_id == user_id).first()

    def create_streak(self, user_id: int) -> Streak:
        streak = Streak(user_id=user_id, current=0, longest=0, last_submission=None)
        self.db.add(streak)
        self.db.commit()
        self.db.refresh(streak)
        return streak

    def update_streak(self, streak: Streak, current: int, longest: int, last_submission: datetime.date) -> Streak:
        streak.current = current
        streak.longest = longest
        streak.last_submission = last_submission
        self.db.commit()
        self.db.refresh(streak)
        return streak
