# Import necessary modules
import re
import random
import discord
from discord.ext import commands

# Functions
# This section is for defining utility functions that will be used in the Cog.


def add_character_after_syllables(text, character):
    # Split the text into words
    words = text.split()
    result = []

    # Process each word
    for word in words:
        # Split the word into syllables
        syllables = re.split(r"(?<=[aeiouAEIOU])", word)

        # Filter out empty strings and add the character after each syllable
        edited_word = character.join(filter(None, syllables))

        # Add 'h' after each vowel with 50% probability
        if character in "aeiouAEIOU" and random.random() < 0.5:
            edited_word += "h"

        result.append(edited_word)

    # Join the words back together
    return " ".join(result)


# Commands
# This section is for defining commands that the bot can execute.


class SlashCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Command: cum
    # Description: A command to send a specific emote.
    @commands.hybrid_command(name="cum", description="cum")
    async def cum_command(self, ctx):
        await ctx.send("<:WatameCum:1082767151850586224>")

    # Command: iamthecum
    # Description: A command to send a specific message.
    @commands.hybrid_command(name="iamthecum", description="Of my Cum")
    async def cum_bone(self, ctx):
        await ctx.send(open("files/i_am_the_cum.txt").read())

    # Command: cleanup
    # Description: A command to send a specific message.
    @commands.hybrid_command(
        name="cleanup", description="cleanup on aisle... my unferwear"
    )
    async def clean_up(self, ctx):
        await ctx.send(
            "https://cdn.discordapp.com/attachments/1100521070706032741/1170839074676932688/RDT_20231105_1916061462893037909646913.gif?ex=655a7fdc&is=65480adc&hm=d42815228f0b1db79d07a8f1d71d5318690cc9d89f92867bbbac330ad2778e0e&"
        )

    # Command: kys
    # Description: A command to send a specific message.
    @commands.hybrid_command(name="kys", description="kys : Kill Yourself")
    async def kys(self, ctx):
        await ctx.send(open("files/kill_yourself.txt").read())

    # Command: lelreaction
    # Description: A command to send a specific image.
    @commands.hybrid_command(name="lelreaction", description="Live lel reaction")
    async def lel(self, ctx):
        with open("files/meme.png", "rb") as f:
            picture = discord.File(f)
            await ctx.send(file=picture)

    # Command: moan
    # Description: A command to send a modified message.
    @commands.hybrid_command(name="moan", description="uohh~")
    async def moan(self, ctx, *, moan_text=None):
        if moan_text is None:
            username = ctx.author.name
        else:
            username = moan_text

        moan = add_character_after_syllables(username, "h") + "~"
        await ctx.send(moan)


# Setup function for the Cog
# This function is called when the Cog is loaded.
async def setup(bot):
    await bot.add_cog(SlashCommands(bot))
