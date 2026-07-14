import discord
from discord.ext import commands

class LeetCodeBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Load the accountability cog
        await self.load_extension("app.commands.accountability")
        
        # Sync slash commands to Discord
        await self.tree.sync()
        print("Slash commands synced successfully!")

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

bot = LeetCodeBot()
