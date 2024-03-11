import random
import re
from discord.ext import commands

#Functions & Variables


class CumCog(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.responses = [
        "Tf you want", "nigga stfu", "go fuck yourself",
        "bro cant even write commands", "dumbahh mf", "stop being retarded",
        "seek help fag", "learn to type", "stop it", "so fucking stupid",
        "i give you the retard award",
      "Throughout heaven and earth, i alone dont gaf",
      "You are hereby invited to go fuck yourself", "shove a rock up your ass",
      "say my name again and youll need diapers the rest of your life", "may your l's be many and lel's few"
    ]
    
    self.cum = [
      "<:WatameCum:1082767151850586224>",
      "<:AmeliaNut:1169328287152078950>",
      "<:Kronut:1170834004371578961>",
      "<:GuraCum:1170834245913153567>",
      "<:PekoCum:1170834266230374460>"
    ]

  @commands.Cog.listener("on_message")
  async def on_cum(self, message):
    if message.author == self.bot.user:
      return

    msg = message.content.lower()

    if 'cum' in msg:
      emote = random.choice(self.cum)
      await message.channel.send(emote)

      await self.bot.process_commands(message)
    elif 'cunny' in msg:
      await message.channel.send("<:KaguyaSob:1102331479066935316>")

  @commands.Cog.listener("on_message")
  async def on_lel(self, message):
    if message.author == self.bot.user:
      return

    if re.search(r'\blel\b', message.content.lower().strip()):
      response = random.choice(self.responses)
      await message.channel.send(response)

    await self.bot.process_commands(message)

async def setup(bot):
  await bot.add_cog(CumCog(bot))
