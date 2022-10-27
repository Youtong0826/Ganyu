from lib.classes import CogExtension
from discord.ext import commands
import discord
import random

class MessageEvent(CogExtension):

    @commands.Cog.listener()
    async def on_message(self, message:discord.Message):
        if message.author == self.bot.user or message.author.bot : return

        else:
            if self.bot.user in message.mentions:
                response = random.choice(["hi","早安","找我嗎?","幹嘛ping我@@",".w."])
                await message.channel.send(response)

def setup(bot):
    bot.add_cog(MessageEvent(bot))
