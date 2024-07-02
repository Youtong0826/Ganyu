import random
import discord
import datetime

from discord import (
    ApplicationContext as Context,
    Colour,
    Embed,
    EmbedField,
    EmbedFooter,
    Member,
    option,
    slash_command
)

from discord.ui import (
    View,
    Button,
)

from lib.cog import CogExtension
from lib.functions import (
    get_pixiv_images, 
    get_now_time
)

class SlashCucmd(CogExtension):

    @slash_command(description="讓機器人模仿你說的話!")
    async def say(self, ctx: Context, *, msg: str):
        self.bot.log(ctx)
        await ctx.response.send_message("已成功發送訊息!", ephemeral=True)
        await ctx.send(msg, allowed_mentions=discord.AllowedMentions.none())

    @slash_command(description="查看頭像")
    async def avatar(self, ctx: Context, *, member: discord.Member = None):
        self.bot.log(ctx)
        await ctx.respond(embed=Embed(
            color=Colour.random(),
            timestamp=get_now_time(),
            image=member.avatar if member else ctx.author.avatar,
            footer=EmbedFooter("/avatar | Ganyu", self.bot.icon_url)
        ))

    @slash_command(description="查看機器人延遲!")
    async def ping(self, ctx: Context):
        self.bot.log(ctx)

        await ctx.respond(embed=Embed(
            title=f"Ping: {round(self.bot.latency*1000)} ms 💫 ",
            color=discord.Colour.random(),
        ))
    
    @slash_command(description="查看有關甘雨的圖片")
    async def pic(self, ctx: Context):
        img = random.choice(get_pixiv_images("ganyu"))

        await ctx.respond(
            embed=Embed(
                title=img["title"],
                description=f'繪師：{img["user"]}',
                color=Colour.nitro_pink(),
                timestamp=get_now_time(),
                image='https://pixiv.cat/'+img["url"]+'.jpg',
                footer=EmbedFooter(
                    "Pixiv.net", 
                    "https://www.bing.com/th?id=ODL.d9cafa2b269e74dcb05b3314a76d721f&w=100&h=100&c=12&pcl=faf9f7&o=6&dpr=1.25&pid=13.1"
                )
            ), 
            view=View(
                Button(
                    label="在Pixiv上查看這張圖片!", 
                    url=f"https://pixiv.net/artworks/{img['url']}", 
                    emoji="🖼️"
                ),
                timeout=None
            )
        )

    @slash_command(descripton="創建一個嵌入訊息")
    @option("title", str, description="標題", required=False)
    @option("title", str, description="敘述", required=False)
    async def embed(self, ctx: Context, title: str, *, description: str = None):
        self.bot.log(ctx)
        if not title:
            await ctx.respond(embed=Embed(
                title="使用g!embed來傳送Embed訊息",
                description="用法 g!embed `標題(空格須加上"")` `內文`"
            ))
            
        await ctx.respond(embed=Embed(
            title=title,
            description=description,
            color=discord.Colour.random()
        ))

    @slash_command(descripton="給點小建議或是回報錯誤")
    async def report(self, ctx: Context):
        await ctx.respond(
            embed=Embed(
                title="錯誤回報",
                description="可用來回報錯誤 或是有什麼話想對開發者說都可以使用此功能喔<3",
                color=discord.Colour.random()
            ), 
            view=View(
                Button(
                    style=discord.ButtonStyle.success,
                    label="開啟回報表單!",
                    custom_id="open_report_button"
                ),
                timeout=None
            ))
        
        
    @slash_command()
    async def sptrole(self, ctx : Context):
        if ctx.author.id != 856041155341975582: return await self.bot.dev_warn()

        await self.bot.get_channel(962264203324948500).send(
            embed=Embed(
                title="索取你要的身分組!",
                color=Colour.nitro_pink()
            ), 
            view=View(
                Button(
                    style=discord.ButtonStyle.success,
                    label="公告Ping",
                    custom_id="PA_ping"
                ),
                Button(
                    style=discord.ButtonStyle.primary,
                    label="機器人更新ping",
                    custom_id="Bu_ping"
                ),
                timeout=None
        ))

def setup(bot):
    bot.add_cog(SlashCucmd(bot))