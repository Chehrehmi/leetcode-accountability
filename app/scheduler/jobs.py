import os
import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from app.services.leaderboard_service import LeaderboardService
from app.database.session import SessionLocal

scheduler = AsyncIOScheduler()

async def morning_reminder(bot):
    print("Running morning reminder...")

async def night_reminder(bot):
    print("Running night reminder...")

async def weekly_leaderboard(bot):
    print("Running weekly leaderboard...")

def setup_scheduler(bot):
    # Morning reminder at 9 AM
    scheduler.add_job(morning_reminder, CronTrigger(hour=9, minute=0), args=[bot])
    
    # Night reminder at reminder hour from .env (e.g. 21)
    reminder_hour = int(os.getenv("REMINDER_HOUR", "21"))
    scheduler.add_job(night_reminder, CronTrigger(hour=reminder_hour, minute=0), args=[bot])
    
    # Sunday leaderboard at 10 AM
    scheduler.add_job(weekly_leaderboard, CronTrigger(day_of_week='sun', hour=10, minute=0), args=[bot])
    
    scheduler.start()
