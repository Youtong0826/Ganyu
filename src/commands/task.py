import discord
from discord.ext import tasks
from core.classes import Cog_ExtenSion

class Task(Cog_ExtenSion):
    @tasks.loop(seconds=10)
    async def looping(self):

        #bot_activitys = [
        #    discord.Activity(type = discord.ActivityType.listening,name = "g!help"),
        #    discord.Activity(type=discord.ActivityType.watching,name = f"{len(bot.guilds)} 個伺服器"),
        #    discord.Activity(type=discord.ActivityType.watching,name = f"{len(bot.users)} 個用戶"),
        #    discord.Activity(type=discord.ActivityType.playing,name = f"{len(bot.commands)} 條指令")
        #]
    #
        #activity = random.choice(bot_activitys)
        print("44")

        channel = self.bot.get_channel(957161962733723678)
        await channel.send("qq")

        #await bot.change_presence(status = discord.Status.streaming, activity = activity)

def setup(bot):
    bot.add_cog(Task(bot))