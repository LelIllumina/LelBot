# Import necessary modules
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Set up bot intents to specify which events the bot will receive
intents = discord.Intents.default()
intents.message_content = True

# Define the LelBot class, which inherits from commands.Bot
class LelBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        # Call the parent class constructor with the provided arguments
        super().__init__(*args, **kwargs)

    # Define an asynchronous method to load extensions
    async def load_extensions(self):
        # Iterate over all files in the 'extensions' directory
        for filename in os.listdir("./extensions"):
            # Check if the file is a Python file
            if filename.endswith(".py"):
                try:
                    # Attempt to load the extension
                    await self.load_extension(f"extensions.{filename[:-3]}")
                    # Print a success message
                    print(f"Successfully loaded extension: {filename[:-3]}")
                except Exception as e:
                    # Print an error message if the extension fails to load
                    print(f"Failed to load extension {filename[:-3]}: {e}")

    # Define an asynchronous method that runs when the bot is ready
    async def on_ready(self):
        # Print the bot's username and ID
        print(f"Logged in as {self.user.name} ({self.user.id})")
        print("Ready!")
        # Load extensions when the bot is ready
        await self.load_extensions()

        # Set the bot's activity to playing "Lelussy Smash Bros"
        activity = discord.Game(name="Lelussy Smash Bros")
        await self.change_presence(status=discord.Status.idle, activity=activity)


# Initialize the bot with command prefixes and intents
bot = LelBot(
    command_prefix=commands.when_mentioned_or(
        "lel", "LeL", "lEl", "LEL", "lel ", "LeL ", "lEl ", "LEL "
    ),
    intents=intents,
)

# Run the bot with the token from environment variables
token = os.getenv("BOT_TOKEN")
bot.run(token)
