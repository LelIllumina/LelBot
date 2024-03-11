import os
from typing import Optional
from typing_extensions import Literal

import discord
from discord.ext import commands
from discord.ext.commands import Context, Greedy

from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await self.load_extensions()

        activity = discord.Game(name="Lelussy Smash Bros")
        await self.change_presence(status=discord.Status.idle, activity=activity)

        print(f'Logged in as {self.user.name} ({self.user.id})')
        print("Ready!")

    async def load_extensions(self):
    # Load extensions (cogs) from the 'extensions' folder
        for filename in os.listdir('./extensions'):
            if filename.endswith('.py'):
                try:
                    await self.load_extension(f'extensions.{filename[:-3]}')
                except Exception as e:
                    print(f"Failed to load extension {filename[:-3]}: {e}")
                    
bot = MyBot(command_prefix=commands.when_mentioned_or('lel', 'LeL', 'lEl',
                                                      'LEL', 'lel ', 'LeL ',
                                                      'lEl ', 'LEL '),
            intents=intents)

@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(ctx: Context,
               guilds: Greedy[discord.Object],
               spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        try:
            if spec == "~":
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "*":
                ctx.bot.tree.copy_global_to(guild=ctx.guild)
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "^":
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync(guild=ctx.guild)
                synced = []
            else:
                synced = await ctx.bot.tree.sync()
        except discord.HTTPException as e:
            await ctx.send(f"An error occurred while syncing: {e}")
            return

        message = f"Synced {len(synced)} commands "
        if spec is None:
            message += "globally"
        else:
            message += "to the current guild."
        await ctx.send(message)
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
            ret += 1
        except discord.HTTPException:
            pass

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

token = os.getenv('BOT_TOKEN')
bot.run(token)
