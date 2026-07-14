import discord
from discord.ext import commands
from discord import app_commands
from app.services.user_service import UserService
from app.services.submission_service import SubmissionService
from app.services.leaderboard_service import LeaderboardService
from app.database.session import SessionLocal

class AccountabilityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="register", description="Register for the LeetCode accountability platform")
    async def register(self, interaction: discord.Interaction):
        db = SessionLocal()
        try:
            service = UserService(db)
            success, message = service.register_user(str(interaction.user.id), interaction.user.display_name)
            await interaction.response.send_message(message, ephemeral=not success)
        finally:
            db.close()

    @app_commands.command(name="done", description="Log your daily LeetCode submission")
    @app_commands.describe(problem_number="The LeetCode problem number you solved")
    async def done(self, interaction: discord.Interaction, problem_number: int):
        db = SessionLocal()
        try:
            service = SubmissionService(db)
            success, message = service.log_submission(str(interaction.user.id), problem_number)
            await interaction.response.send_message(message)
        finally:
            db.close()

    @app_commands.command(name="leaderboard", description="View the current streak leaderboard")
    async def leaderboard(self, interaction: discord.Interaction):
        db = SessionLocal()
        try:
            service = LeaderboardService(db)
            leaderboard_msg = service.get_top_streaks()
            await interaction.response.send_message(leaderboard_msg)
        finally:
            db.close()

    @app_commands.command(name="stats", description="View your current stats and streak")
    async def stats(self, interaction: discord.Interaction):
        from app.repositories.streak_repo import StreakRepository
        from app.repositories.user_repo import UserRepository
        
        db = SessionLocal()
        try:
            user_repo = UserRepository(db)
            user = user_repo.get_user_by_discord_id(str(interaction.user.id))
            if not user:
                await interaction.response.send_message("You are not registered! Use `/register` first.", ephemeral=True)
                return
                
            streak_repo = StreakRepository(db)
            streak = streak_repo.get_streak(user.id)
            
            stats_msg = f"📊 **Stats for {user.username}**\n"
            stats_msg += f"🔥 Current Streak: {streak.current} days\n"
            stats_msg += f"🏆 Longest Streak: {streak.longest} days\n"
            if streak.last_submission:
                stats_msg += f"📅 Last Submission: {streak.last_submission}"
            
            await interaction.response.send_message(stats_msg)
        finally:
            db.close()

    @app_commands.command(name="help", description="Show available commands")
    async def help_cmd(self, interaction: discord.Interaction):
        help_msg = (
            "**🤖 LeetCode Accountability Bot**\n\n"
            "`/register` - Join the accountability tracker\n"
            "`/done <problem_number>` - Log your daily problem\n"
            "`/stats` - Check your current streak and stats\n"
            "`/leaderboard` - View the server leaderboard\n"
        )
        await interaction.response.send_message(help_msg, ephemeral=True)

async def setup(bot):
    await bot.add_cog(AccountabilityCog(bot))
