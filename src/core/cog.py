from discord.ext import commands
from core import Bot

class CogExtension(commands.Cog):
    def __init__(self, bot: Bot):
        self.bot: Bot = bot