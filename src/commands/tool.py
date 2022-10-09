from lib.function import bullshit, translate, wiki_search, calculator, GetVideoInfo ,SendBGM
from core.classes import CogExtension
from lib.bot_config import bot_icon_url
from discord.ext import commands
from command_lib import tool
import discord

wikipedia_icon_url = "https://www.bing.com/images/search?view=detailV2&ccid=CLnSyWEa&id=E66C2DFADDB113B154BE0073382FBCEF88E51ACB&thid=OIP.CLnSyWEawnaZ8T3saUMfsgHaHa&mediaurl=https%3a%2f%2f3c1703fe8d.site.internapcdn.net%2fnewman%2fgfx%2fnews%2fhires%2f2017%2f58af0228b8aa8.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.08b9d2c9611ac27699f13dec69431fb2%3frik%3dyxrliO%252b8LzhzAA%26pid%3dImgRaw%26r%3d0&exph=1500&expw=1500&q=wikipedia&simid=607995489110011574&FORM=IRPRST&ck=D48A403BD14BEB6F8CABA45AE032EAD4&selectedIndex=4"
translate_to = ["南非語","阿拉伯語","阿賽拜疆語","比利時語","保加利亞語",""]

class Tool(CogExtension):

    @commands.command()
    async def translate(self,ctx,language : discord.Option(str,"選擇要翻譯成的語言",choices=["繁中","英語","日語","簡中","印尼語"]),*,text=None):
        await tool.translate(ctx,language,text)

    @commands.command()
    async def wiki(self,ctx,keywords=None):
        await tool.wikiInfo(ctx,keywords,self.bot)

    @commands.command()
    async def words(self,ctx,*,text=None):
        await tool.words(ctx,text)
    
    @commands.command()
    async def bullshit(self,ctx,topic:str = None,minlen:int = None):
        await tool.bullshit(ctx,topic,minlen)

    @commands.command()
    async def math(self,ctx,formula=None):
        await tool.math(ctx,formula)

    @commands.command()
    async def ytinfo(self,ctx : discord.ApplicationContext,url = None):
        vdata = GetVideoInfo(url)

        embed = discord.Embed(
            title="TEST",
        )

        for n in vdata:
            print(n)
            embed.add_field(name=n ,value=vdata[n],inline=True)

        await ctx.send(embed=embed)

    @commands.command()
    async def genshin(self,ctx,uid=None,server=None):
        await tool.genshininfo(ctx,uid,server)

def setup(bot):
    bot.add_cog(Tool(bot))