from sqlalchemy.orm import Session
from app.repositories.user_repo import UserRepository
from app.repositories.streak_repo import StreakRepository

class UserService:
    def __init__(self, db: Session):
        self.user_repo = UserRepository(db)
        self.streak_repo = StreakRepository(db)

    def register_user(self, discord_id: str, username: str):
        existing_user = self.user_repo.get_user_by_discord_id(discord_id)
        if existing_user:
            return False, "You are already registered!"
        
        # Create user
        new_user = self.user_repo.create_user(discord_id, username)
        # Initialize streak
        self.streak_repo.create_streak(new_user.id)
        
        return True, f"Welcome {username}! You are now registered. Use `/done` to log your daily LeetCode."
