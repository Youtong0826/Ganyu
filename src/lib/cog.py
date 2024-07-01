from discord.ext import commands
import datetime
import discord

class CogExtension(commands.Cog):
    def __init__(self, bot):
        self.bot : commands.Bot = bot

class Log:
    def __init__(self, ctx:discord.ApplicationContext) -> None:
        self.ctx = ctx

    def output(self):
        time = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime("%Y/%m/%d %H:%M:%S")
        print(f'[{time}] At the guild - {self.ctx.author.guild}. {self.ctx.author} used the command - "{self.ctx.command}"')

    def error_output(self, error):
        time = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime("%Y/%m/%d %H:%M:%S")
        print(f'[{time}] At the guild - {self.ctx.author.guild}. When {self.ctx.author} used the command - "{self.ctx.command}", return a error:{error}')