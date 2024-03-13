# Import necessary modules and types
import discord
from discord.ext import commands


# Define the Sync class which inherits from commands.Cog
class Sync(commands.Cog):
    def __init__(self, bot):
        # Initialize the bot instance
        self.bot = bot

    # Define the sync command
    @commands.command()
    @commands.guild_only()  # Ensure the command is only usable in a guild
    @commands.is_owner()  # Ensure only the owner can use this command
    async def sync(
        self,
        ctx: commands.Context,  # The context in which the command is called
    ) -> None:
        try:
            # Sync commands to the current guild
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
            print(f"Synced to guild: {synced}")
            await ctx.send(f"Synced {len(synced)} commands to the current guild.")
        except discord.HTTPException as e:
            # Handle HTTP exceptions
            await ctx.send(f"An error occurred while syncing: {e}")


# Define the setup function for adding the cog to the bot
async def setup(bot):
    await bot.add_cog(Sync(bot))
