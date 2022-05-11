import discord
from discord.ext import tasks
from core.classes import Cog_ExtenSion

class Task(Cog_ExtenSion):
    @tasks.loop(seconds=10)
    async def looping(self):
        channel = self.bot.get_channel(957161962733723678)
        await channel.send("qq")
        #bot_activitys = [
        #    discord.Activity(type = discord.ActivityType.listening,name = "g!help"),
        #    discord.Activity(type=discord.ActivityType.watching,name = f"{len(bot.guilds)} 個伺服器"),
        #    discord.Activity(type=discord.ActivityType.watching,name = f"{len(bot.users)} 個用戶"),
        #    discord.Activity(type=discord.ActivityType.playing,name = f"{len(bot.commands)} 條指令")
        #]
    
        #activity = random.choice(bot_activitys)
        #await bot.change_presence(status = discord.Status.streaming, activity = activity)

    looping.start()

def setup(bot):
    bot.add_cog(Task(bot))