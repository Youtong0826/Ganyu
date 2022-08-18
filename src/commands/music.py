from dataclasses import dataclass
from lib.bot_config import bot_icon_url
from core.classes import Cog_ExtenSion
from lib.function import GetVideoInfo
from youtube_dl import YoutubeDL
from discord.ext import commands
import datetime
import discord

class Music(Cog_ExtenSion):
    def __init__(self, bot):
        super().__init__(bot)
        
        self.is_playing = False
        self.is_paused = False

        # 2d array containing [song, channel]
        self.music_queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

        self.FFMPEG_OPTIONS = {
            'executable':'res/assets/ffmpeg/bin/ffmpeg.exe',
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }

        self.vc = None
     
    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: 
                data = ydl.extract_info("ytsearch:%s" % item, download=False)
                info = data['entries'][0]
                url = info['webpage_url']
                
            except Exception: 
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title'],'url':url}

    def play_next(self):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']

            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())
        else:
            self.is_playing = False
    
    async def play_music(self, ctx):
        if len(self.music_queue) > 0:
            self.is_playing = True

            m_url = self.music_queue[0][0]['source']
            
            if self.vc == None or not self.vc.is_connected():
                self.vc = await self.music_queue[0][1].connect()
                
                if self.vc == None:
                    await ctx.send("無法連線至語音頻道")
                    return
            else:
                await self.vc.move_to(self.music_queue[0][1])
            
            self.music_queue.pop(0)

            self.vc.play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next())

        else:
            self.is_playing = False

    def music_embed(self,url:str) -> discord.Embed:
        data = GetVideoInfo(url)
        description = data['description']

        embed = discord.Embed(
            title=data['title'],
            description=description[:50] + f' ... [查看更多]({url})',
            color=discord.Colour.nitro_pink(),
            timestamp=datetime.datetime.utcnow()
        )

        udt = data.get("upload_date")
        udt = udt[:-4] + "/" + udt[4:6] + "/" + udt[6:8]

        tags = ""
        tag_limit = 0

        for n in data.get('tags'):
            if tag_limit < 5:
                tag_limit += 1
                tags += "#" + str(n).replace("'","") + " "

        fields = {
            "👀 觀看人數" : data.get("view_count"),
            "👍 喜歡": data.get("like_count"),
            "🎵 片長": f"{int(data.get('duration')//60)}:{int(data.get('duration')%60)}",
            "📅 上傳時間" : udt,
            "👤 上傳者": data["uploader"],
            "📌 標籤" : tags
        }

        for n in fields:
            embed.add_field(
                name=n,
                value=fields[n],
                inline=True
            )

        embed.set_image(url=data["thumbnail"])
        embed.set_footer(text="Ganyu Music",icon_url=bot_icon_url)
        
        return embed

    @commands.command(name="play", aliases=["p","playing"])
    async def play(self, ctx, *args):
        query = " ".join(args)
        
        if ctx.author.voice is None:
            
            await ctx.send("請先連線至語音頻道!")
            
        elif self.is_paused:
            self.vc.resume()

        else:
            voice_channel = ctx.author.voice.channel
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("無法取得歌曲資訊 請嘗試其他關鍵字")
            else:
                await ctx.send("已新增歌曲至播放清單!")
                self.music_queue.append([song, voice_channel])

                embed = self.music_embed(song['url'])
                
                if self.is_playing == False:
                    await self.play_music(ctx)
                    await ctx.send(embed=embed)

    @commands.command(name="pause")
    async def pause(self, ctx, *args):
        if self.is_playing:
            self.is_playing = False
            self.is_paused = True
            self.vc.pause()
            await ctx.send("已暫停音樂")

        elif self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.vc.resume()
            await ctx.send("已播放音樂")

    @commands.command(name = "resume", aliases=["r"])
    async def resume(self, ctx, *args):
        if self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.vc.resume()
            await ctx.send("已播放音樂")

    @commands.command(name="skip", aliases=["s"])
    async def skip(self, ctx):
        if self.vc != None and self.vc:
            self.vc.stop()
            await ctx.send("已跳過歌曲")
            
            await self.play_music(ctx)


    @commands.command(name="queue", aliases=["q"])
    async def queue(self, ctx):
        retval = ""
        for i in range(len(self.music_queue)):
            # display a max of 5 songs in the current queue
            if (i > 4): break
            retval += self.music_queue[i][0]['title'] + "\n"
            print(self.music_queue[i][0]['title'])

        if retval != "":
            await ctx.send(retval)
        else:
            await ctx.send("播放清單內沒有歌曲")

    @commands.command(name="clearqueue", aliases=["c", "bin"])
    async def clearqueue(self, ctx):
        if self.vc != None and self.is_playing:
            self.vc.stop()

        self.music_queue = []
        await ctx.send("已清空播放清單內的所有歌曲")

    @commands.command(name="leave", aliases=["disconnect", "l", "d"])
    async def dc(self, ctx):
        self.is_playing = False
        self.is_paused = False
        await self.vc.disconnect()
        await ctx.send("需要的時候再叫我吧~")

def setup(bot):
    bot.add_cog(Music(bot))