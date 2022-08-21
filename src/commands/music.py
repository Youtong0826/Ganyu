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

        self.voice_clients = {}

        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

        self.FFMPEG_OPTIONS = {
            'executable':'res/assets/ffmpeg/bin/ffmpeg.exe',
            'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
            'options': '-vn'
        }

    def setup_status(self,id:discord.Guild.id):
        if id not in self.voice_clients.keys():

            default = {
                "is_playing" : False,
                "is_paused" : False,
                "music_queue" : [],
                "vc" : None
            }

            self.voice_clients[id] = default
    
    def get_status(self,id:discord.Guild.id):
        return self.voice_clients[id]

    def search_yt(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try: 
                data = ydl.extract_info("ytsearch:%s" % item, download=False)
                info = data['entries'][0]
                url = info['webpage_url']
                
            except Exception: 
                return False

        return {'source': info['formats'][0]['url'], 'title': info['title'],'url':url}

    def play_next(self,id:discord.Guild.id):
        self.setup_status(id)
        vc_status = self.get_status(id)

        if len( vc_status["music_queue"]) > 0:

            vc_status["is_playing"] = True

            m_url = vc_status["music_queue"][0][0]['source']

            vc_status["music_queue"].pop(0)

            vc_status["vc"].play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next(id))
            
        else:
            vc_status["is_playing"] = False
    
    async def play_music(self, ctx, id:discord.Guild.id):
        self.setup_status(id)
        vc_status = self.get_status(id)

        if len(vc_status["music_queue"]) > 0:
            vc_status["is_playing"] = True

            m_url = vc_status["music_queue"][0][0]['source']
            
            if vc_status["vc"] == None or not vc_status["vc"].is_connected():
                vc_status["vc"] = await vc_status["music_queue"][0][1].connect()
                
                if vc_status["vc"] == None:
                    await ctx.send("無法連線至語音頻道")
                    return
            else:
                await vc_status["vc"].move_to(vc_status["music_queue"][0][1])

            vc_status["vc"].play(discord.FFmpegPCMAudio(m_url, **self.FFMPEG_OPTIONS), after=lambda e: self.play_next(id))

        else:
            vc_status["is_playing"] = False

    def music_embed(self,url:str, id:discord.Guild.id, ctx) -> dict:
        data = GetVideoInfo(url)
        description = data['description']

        embed = discord.Embed(
            title=f"正在播放 {data['title']}",
            description=description[:50] + f' ...[查看更多]({url})',
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

        duration_min = str(data.get('duration')//60)
        duration_sec = str(data.get('duration')%60)

        if int(duration_min) < 10:
            duration_min = "0" + duration_min 

        if int(duration_sec) < 10:
            duration_sec = "0" + duration_sec

        fields = {
            "👀 觀看次數" : data.get("view_count"),
            "👍 喜歡": data.get("like_count"),
            "🎵 片長": f"{duration_min}:{duration_sec}",
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

        control_button = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            label="暫停/播放",
            custom_id="control",
            emoji="⏯️",
            row=0
        )

        skip_button = discord.ui.Button(
            style=discord.ButtonStyle.primary,
            custom_id="skip",
            label="下一首",
            emoji="⏩",
            row=0
        )

        queue_button = discord.ui.Button(
            style=discord.ButtonStyle.success,
            custom_id="queue",
            label="查看播放清單",
            emoji="📃",
            row=0
        )

        dc_button = discord.ui.Button(
            style=discord.ButtonStyle.danger,
            custom_id="dc",
            label="中斷連結",
            emoji="👋",
            row=1
        )

        buttons = [control_button,skip_button,queue_button,dc_button]

        async def button_callback(interaction:discord.Interaction):
            self.setup_status(id)
            vc_status = self.get_status(id)
            if interaction.custom_id == "control":
                if vc_status["is_playing"]:
                    vc_status["is_playing"] = False
                    vc_status["is_paused"] = True
                    vc_status["vc"].pause()

                    await interaction.response.send_message("已暫停音樂!",ephemeral=True)

                else:
                    vc_status["is_playing"] = True
                    vc_status["is_paused"] = False
                    vc_status["vc"].resume()

                    await interaction.response.send_message("已播放音樂!",ephemeral=True)

            elif interaction.custom_id == "skip":
                await self.skip(ctx)

            elif interaction.custom_id == "queue":
                await self.queue(ctx)

            elif interaction.custom_id == "dc":
                await self.dc(ctx)
        
        view = discord.ui.View(timeout=None)

        for btn in buttons:
            view.add_item(btn)
            btn.callback = button_callback        

        return {"embed":embed,"view":view}

    def queue_embed(self,id:discord.Guild.id):
        self.setup_status(id)
        queue = self.get_status(id)["music_queue"]
        description = "正在播放 - "

        if len(queue) <= 1:
            description += f"**{queue[n][0]['title']}**"

        for n in range(len(queue)):
            if n > 10:break
            description += queue[n][0]["title"] + f"\n{n+1}. "

        embed = discord.Embed(
            title="播放清單",
            description=description,
            color = discord.Colour.nitro_pink(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_footer(text="Ganyu Music",icon_url=bot_icon_url)

        if description == "正在播放 - ":
            return False
        
        else:
            return embed

    @commands.command(name="play", aliases=["p","playing"])
    async def play(self, ctx, *args):
        query = " ".join(args)
        self.setup_status(ctx.author.guild.id)
        vc_status = self.get_status(ctx.author.guild.id)
        
        if ctx.author.voice is None:
            
            await ctx.send("請先連線至語音頻道!")
            
        elif vc_status["is_paused"]:
             vc_status["vc"].resume()

        else:
            voice_channel = ctx.author.voice.channel
            song = self.search_yt(query)
            if type(song) == type(True):
                await ctx.send("無法取得歌曲資訊 請嘗試其他關鍵字")
            else:
                await ctx.send("已新增歌曲至播放清單!")
                vc_status["music_queue"].append([song, voice_channel])

                msg = self.music_embed(song['url'],ctx.author.guild.id,ctx)

                embed = msg["embed"]
                view = msg["view"]
                
                if  vc_status["is_playing"] == False:
                    await self.play_music(ctx,ctx.author.guild.id)
                    await ctx.send(embed=embed, view=view)

    @commands.command(name="pause")
    async def pause(self, ctx, *args):
        self.setup_status(ctx.author.guild.id)
        vc_status = self.get_status(ctx.author.guild.id)
        if vc_status["is_playing"]:
            vc_status["is_playing"] = False
            vc_status["is_paused"] = True
            vc_status["vc"].pause()
            await ctx.send("已暫停音樂!")

        elif vc_status["is_paused"]:
            vc_status["is_paused"] = False
            vc_status["is_playing"] = True
            vc_status["vc"].resume()
            await ctx.send("已播放音樂!")

    @commands.command(name = "resume", aliases=["r"])
    async def resume(self, ctx, *args):
        self.setup_status(ctx.author.guild.id)
        vc_status = self.get_status(ctx.author.guild.id)
        if  vc_status["is_playing"]:
            vc_status["is_paused"] = False
            vc_status["is_playing"] = True
            vc_status["vc"].pause()
            await ctx.send("已播放音樂!")

    @commands.command(name="skip", aliases=["s"])
    async def skip(self, ctx):
        self.setup_status(ctx.author.guild.id)
        vc_status = self.get_status(ctx.author.guild.id)

        if vc_status["vc"] != None and vc_status["vc"]:
            vc_status["vc"].stop()

            await ctx.send("已跳過歌曲!")
            
            await self.play_music(ctx,ctx.author.guild.id)

            await ctx.send("下一首播放的是...")

            msg = self.music_embed(vc_status["music_queue"][0][0]["url"],ctx.author.guild.id,ctx)

            embed = msg["embed"]
            view = msg["view"]

            await ctx.send(embed=embed, view=view)


    @commands.command(name="queue", aliases=["q"])
    async def queue(self, ctx):
        embed = self.queue_embed(ctx.author.guild.id)

        if isinstance(embed,bool):
            await ctx.send("播放清單內沒有歌曲")
        else:
            await ctx.send(embed=embed)

    @commands.command(name="clearqueue", aliases=["c", "bin"])
    async def clearqueue(self, ctx):
        self.setup_status(ctx.author.guild.id)
        vc_status = self.get_status(ctx.author.guild.id)
        if vc_status["vc"] != None and vc_status["is_playing"]:
            vc_status["vc"].stop()

        vc_status["music_queue"] = []
        await ctx.send("已清空播放清單內的所有歌曲")

    @commands.command(name="leave", aliases=["disconnect", "l", "d"])
    async def dc(self, ctx):
        self.setup_status(ctx.author.guild.id)
        vc_status = self.get_status(ctx.author.guild.id)

        vc_status["is_playing"] = False
        vc_status["is_paused"] = False

        await vc_status["vc"].disconnect()
        await ctx.send("需要的時候再叫我吧~")

    @commands.command(aliases = ["now"])
    async def np(self,ctx):
        self.setup_status(ctx.author.guild.id)
        vc_status = self.get_status(ctx.author.guild.id)

        url = vc_status["music_queue"][0][0]["url"]

        msg = self.music_embed(url,ctx.author.guild.id,ctx)

        embed = msg["embed"]
        view = msg["view"]

        await ctx.send(embed=embed, view=view)

def setup(bot):
    bot.add_cog(Music(bot))