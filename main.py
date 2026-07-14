import os
import asyncio
from dotenv import load_dotenv
from app.bot.client import bot
from app.database.init_db import init_db
from app.scheduler.jobs import setup_scheduler

load_dotenv()

async def main():
    # Initialize the database (creates tables if they don't exist)
    init_db()
    
    token = os.getenv("DISCORD_TOKEN")
    if not token or token == "your_bot_token_here":
        print("ERROR: Please set your DISCORD_TOKEN in the .env file")
        return

    # Start the scheduler
    setup_scheduler(bot)

    # Start the bot
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
