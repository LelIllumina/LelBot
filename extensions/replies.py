# Import necessary modules
import random
import re
from discord.ext import commands


class CumCog(commands.Cog):
    # Initialize the Cog with the bot instance
    def __init__(self, bot):
        # Store the bot instance for later use
        self.bot = bot
        # Define a list of responses that the bot can use
        self.responses = [
            "Tf you want",
            "nigga stfu",
            "go fuck yourself",
            "bro cant even write commands",
            "dumbahh mf",
            "stop being retarded",
            "seek help fag",
            "learn to type",
            "stop it",
            "so fucking stupid",
            "i give you the retard award",
            "Throughout heaven and earth, i alone dont gaf",
            "You are hereby invited to go fuck yourself",
            "shove a rock up your ass",
            "say my name again and youll need diapers the rest of your life",
            "may your l's be many and lel's few",
        ]
        # Define a list of emotes that the bot can use
        self.cum = [
            "<:WatameCum:1082767151850586224>",
            "<:AmeliaNut:1169328287152078950>",
            "<:Kronut:1170834004371578961>",
            "<:GuraCum:1170834245913153567>",
            "<:PekoCum:1170834266230374460>",
        ]

    # Listener for on_message event
    # This function is called whenever a message is sent in a channel the bot has access to.
    @commands.Cog.listener("on_message")
    async def on_cum(self, message):
        # Ignore messages from the bot itself
        if message.author == self.bot.user:
            return

        # Convert the message content to lowercase for case-insensitive matching
        msg = message.content.lower()

        # Check if the message contains the word 'cum'
        if "cum" in msg:
            # Choose a random emote from the list
            emote = random.choice(self.cum)
            # Send the chosen emote to the channel
            await message.channel.send(emote)

        # Check if the message contains the word 'cunny'
        elif "cunny" in msg:
            # Send a specific emote to the channel
            await message.channel.send("<:KaguyaSob:1102331479066935316>")

        # Process commands in the message
        await self.bot.process_commands(message)

    # Listener for on_message event
    # This function is called whenever a message is sent in a channel the bot has access to.
    @commands.Cog.listener("on_message")
    async def on_lel(self, message):
        # Ignore messages from the bot itself
        if message.author == self.bot.user:
            return

        # Check if the message contains the word 'lel'
        if re.search(r"\blel\b", message.content.lower().strip()):
            # Choose a random response from the list
            response = random.choice(self.responses)
            # Send the chosen response to the channel
            await message.channel.send(response)

        # Process commands in the message
        await self.bot.process_commands(message)


# Setup function for the Cog
# This function is called when the Cog is loaded.
async def setup(bot):
    # Add the Cog to the bot
    await bot.add_cog(CumCog(bot))
