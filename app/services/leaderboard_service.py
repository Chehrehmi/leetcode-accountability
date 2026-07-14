from sqlalchemy.orm import Session
from app.models.user import User
from app.models.streak import Streak

class LeaderboardService:
    def __init__(self, db: Session):
        self.db = db

    def get_top_streaks(self, limit: int = 10):
        # Join users and streaks, order by current streak descending
        results = (
            self.db.query(User, Streak)
            .join(Streak, User.id == Streak.user_id)
            .order_by(Streak.current.desc())
            .limit(limit)
            .all()
        )
        
        if not results:
            return "No active users yet!"
            
        leaderboard_str = "**🏆 Current Streak Leaderboard 🏆**\n\n"
        for idx, (user, streak) in enumerate(results, 1):
            leaderboard_str += f"{idx}. **{user.username}** - {streak.current} days (Best: {streak.longest})\n"
            
        return leaderboard_str
