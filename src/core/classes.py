from discord.ext import commands

class CogExtension(commands.Cog):
    def __init__(self, bot):
        self.bot : commands.Bot = bot
