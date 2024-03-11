import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up bot intents
intents = discord.Intents.default()
intents.message_content = True

class LelBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def load_extensions(self):
        # Load all extensions from the 'extensions' folder
        for filename in os.listdir('./extensions'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'extensions.{filename[:-3]}')
                    print(f"Successfully loaded extension: {filename[:-3]}") # Print debug info
                except Exception as e:
                    print(f"Failed to load extension {filename[:-3]}: {e}")
        
    async def on_ready(self):
        print(f'Logged in as {self.user.name} ({self.user.id})')
        print("Ready!")
        # Load extensions when the bot is ready
        await self.load_extensions()
        
    # Set bot's activity
        activity = discord.Game(name="Lelussy Smash Bros")
        await self.change_presence(status=discord.Status.idle, activity=activity)

# Initialize bot with command prefixes and intents
bot = LelBot(command_prefix=commands.when_mentioned_or('lel', 'LeL', 'lEl', 'LEL', 'lel ', 'LeL ', 'lEl ', 'LEL '),
            intents=intents)

# Run the bot with the token from environment variables
token = os.getenv('BOT_TOKEN')
bot.run(token)
