import datetime
import discord
import requests
import youtube_dl
import asyncio
from lib.bot_config import bot_icon_url
from discord.ext import commands
from core.classes import Cog_ExtenSion

songs_queue = {}
voice_clients = {}

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

        else:
            await ctx.send("找不到語音頻道 請您加入一個吧 😭")

    @commands.command()
    async def leave(self,ctx:discord.ApplicationContext):
        user : discord.Member = ctx.author 
        
        if user.voice and user.voice.channel: 
            try:
                await ctx.voice_client.disconnect()
                await ctx.send("需要的時候再叫我吧 💫")

            except:
                await ctx.send("無法離開此語音! ❌")

        else:
            await ctx.send("你得加入我在的頻道我才能離開喔!")

    @commands.command()
    async def play(self,ctx:discord.ApplicationContext,url):
        user : discord.Member = ctx.author

        try :
            voice_client = await user.voice.channel.connect()
            voice_clients[user.guild.id] = voice_client

            ytdl_option = { "format" : "bestaudio/best" }
            ffmpeg_option = {"options" : "-vn"}

            ytdl = youtube_dl.YoutubeDL(ytdl_option)

            loop = asyncio.get_event_loop()

            data = await loop.run_in_executor(None,lambda:ytdl.extract_info(url,download=False))
            song = data.get("url")

            songs_queue[user.guild.id] = [].append(data.get("id"))

            player = discord.FFmpegPCMAudio(song,**ffmpeg_option,executable="C:\\ffmpeg\\bin\\ffmpeg.exe")
            voice_client.play(player)

            embed = discord.Embed(
                title = data.get("title"),
                description = data.get("description"),
                color = discord.Colour.blue(),
                timestamp = datetime.datetime.utcnow()
            )

            udt = data.get("upload_date")
            udt = udt[:-4] + "/" + udt[4:6] + "/" + udt[6:8] 

            tags = ""

            for n in data.get('tags'):
                tags += "#" + str(n).replace("'","") + " "

            fields = {
                "🎵 片長": f"{int(data.get('duration')//60)}:{int(data.get('duration')%60)}",
                "📅 上傳時間" : udt,
                "👀 觀看人數" : data.get("view_count"),
                "👍 喜歡": data.get("like_count"),
                "📌 標籤" : tags
            }
            for n in fields:
                embed.add_field(name=n,value=fields[n],inline=False)
            embed.set_thumbnail(url=data.get('thumbnail'))
            embed.set_footer(text="Ganyu Music",icon_url=bot_icon_url)
            await ctx.send(embed=embed)

        except:
            await ctx.send("無法連線到您的語音頻道! ❌")

            
    @commands.command()
    async def pause(self,ctx:discord.ApplicationContext):
        try:
            voice_clients[ctx.author.guild.id].pause()

            await ctx.send("已暫停音樂! ▶️")

        except:
            ctx.send("發生錯誤! ❌")

    @commands.command()
    async def resume(self,ctx:discord.ApplicationContext):
        try:
            voice_clients[ctx.author.guild.id].resume()

            await ctx.send("已撥放音樂! ⏸️")

        except:
            ctx.send("發生錯誤! ❌")

    @commands.command()
    async def stop(self,ctx:discord.ApplicationContext):
        try:
            voice_clients[ctx.author.guild.id].stop()
            await voice_clients[ctx.author.guild.id].disconnect()

        except:
            ctx.send("發生錯誤! ❌")

def setup(bot):
    bot.add_cog(Music(bot))