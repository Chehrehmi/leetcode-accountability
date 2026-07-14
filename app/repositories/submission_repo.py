from typing import List
from sqlalchemy.orm import Session
from app.models.submission import Submission

class SubmissionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_submission(self, user_id: int, problem_number: int, difficulty: str = None) -> Submission:
        submission = Submission(user_id=user_id, problem_number=problem_number, difficulty=difficulty)
        self.db.add(submission)
        self.db.commit()
        self.db.refresh(submission)
        return submission

    def get_submissions_by_user(self, user_id: int) -> List[Submission]:
        return self.db.query(Submission).filter(Submission.user_id == user_id).all()
