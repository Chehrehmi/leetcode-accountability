import datetime
from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepository
from app.repositories.submission_repo import SubmissionRepository
from app.repositories.streak_repo import StreakRepository

class SubmissionService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)
        self.submission_repo = SubmissionRepository(db)
        self.streak_repo = StreakRepository(db)

    def log_submission(self, discord_id: str, problem_number: int, difficulty: str = None):
        user = self.user_repo.get_user_by_discord_id(discord_id)
        if not user:
            return False, "You are not registered yet! Please use `/register` first."

        # Log the submission
        self.submission_repo.create_submission(user.id, problem_number, difficulty)

        # Update streak
        streak = self.streak_repo.get_streak(user.id)
        today = datetime.datetime.utcnow().date()
        
        if streak.last_submission == today:
            return True, f"Submission for problem {problem_number} logged! (You already completed your daily goal today)."

        new_current = streak.current
        new_longest = streak.longest

        if streak.last_submission == today - datetime.timedelta(days=1):
            # Continued streak
            new_current += 1
        else:
            # Broken or first streak
            new_current = 1

        if new_current > new_longest:
            new_longest = new_current

        self.streak_repo.update_streak(streak, new_current, new_longest, today)

        return True, f"Great job! Problem {problem_number} logged. Your current streak is now **{new_current}** days!"
