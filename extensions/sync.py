from typing import Optional
from typing_extensions import Literal

import discord
from discord.ext import commands
from discord.ext.commands import Context, Greedy

class Sync(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    @commands.guild_only()
    @commands.is_owner()
    async def sync(ctx: Context,
                guilds: Greedy[discord.Object],
                spec: Optional[Literal["~", "*", "^"]] = None) -> None:
        if not guilds:
            try:
                if spec == "~":
                    synced = await ctx.bot.tree.sync(guild=ctx.guild)
                    print(f"Synced to guild: {synced}")
                elif spec == "*":
                    ctx.bot.tree.copy_global_to(guild=ctx.guild)
                    synced = await ctx.bot.tree.sync(guild=ctx.guild)
                    print(f"Synced globally to guild: {synced}")
                elif spec == "^":
                    ctx.bot.tree.clear_commands(guild=ctx.guild)
                    await ctx.bot.tree.sync(guild=ctx.guild)
                    synced = []
                    print("Commands cleared and synced.")
                else:
                    synced = await ctx.bot.tree.sync()
                    print(f"Synced globally: {synced}")
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
                print(f"Failed to sync to guild: {guild}")
                pass

        await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

async def setup(bot):
    await bot.add_cog(Sync(bot))
