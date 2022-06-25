import discord
import requests
import youtube_dl
from discord.ext import commands
from core.classes import Cog_ExtenSion

class Music(Cog_ExtenSion):

    @commands.command()
    async def join(self,ctx:discord.ApplicationContext):
        user : discord.Member = ctx.author 
        
        if user.voice and user.voice.channel: 
            try:
                await user.voice.channel.connect()
                await ctx.send("成功加入語音!✨")

            except:
                await ctx.send("無法加入語音!❌")

    @commands.command()
    async def leave(self,ctx:discord.ApplicationContext):
        user : discord.Member = ctx.author 
        
        if user.voice and user.voice.channel: 
            try:
                await ctx.voice_client.disconnect()
                await ctx.send("需要的時候再叫我吧 💫")

            except:
                await ctx.send("無法離開此語音! ❌")


def setup(bot):
    bot.add_cog(Music(bot))