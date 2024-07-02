from discord.ext import commands
import datetime
import discord

from core import Bot

class CogExtension(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot