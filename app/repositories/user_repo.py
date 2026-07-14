from sqlalchemy.orm import Session
from app.models.user import User

class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_discord_id(self, discord_id: str) -> User | None:
        return self.db.query(User).filter(User.discord_id == discord_id).first()

    def create_user(self, discord_id: str, username: str) -> User:
        user = User(discord_id=discord_id, username=username)
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user
