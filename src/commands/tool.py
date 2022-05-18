import html
import  discord , datetime , requests , json 
from discord.ext import commands
from core.classes import Cog_ExtenSion
from lib.function import translate,wiki_search
from commands.rpg import bot_icon_url

google_translate_icon_url = "https://th.bing.com/th/id/R.93d2c8f15964faae1e75331caf7d8fe0?rik=vl9rlcN9fh1oEw&pid=ImgRaw&r=0"
wikipedia_icon_url = "https://www.bing.com/images/search?view=detailV2&ccid=CLnSyWEa&id=E66C2DFADDB113B154BE0073382FBCEF88E51ACB&thid=OIP.CLnSyWEawnaZ8T3saUMfsgHaHa&mediaurl=https%3a%2f%2f3c1703fe8d.site.internapcdn.net%2fnewman%2fgfx%2fnews%2fhires%2f2017%2f58af0228b8aa8.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.08b9d2c9611ac27699f13dec69431fb2%3frik%3dyxrliO%252b8LzhzAA%26pid%3dImgRaw%26r%3d0&exph=1500&expw=1500&q=wikipedia&simid=607995489110011574&FORM=IRPRST&ck=D48A403BD14BEB6F8CABA45AE032EAD4&selectedIndex=4"

class Tool(Cog_ExtenSion):

    @commands.command()
    async def translate(self,ctx,*,text=None):
        if text != None:
            translate_text = translate(str(text),"zh-TW")
            embed = discord.Embed(
                title="成功! 以下為翻譯結果",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )

            embed.add_field(
                name="原文",
                value=f"```{text}```"
            )
            embed.add_field(
                name="翻譯",
                value=f"```{translate_text}```",
                inline=False
            )

        else:
            embed = discord.Embed(
                title="歡迎使用翻譯小工具!",
                description="此指令可以將各種語言翻譯成中文\n使用方法 g!translate `文字`",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )

        embed.set_thumbnail(url=google_translate_icon_url)
        embed.set_footer(text="translate",icon_url=bot_icon_url)

        await ctx.send(embed = embed)

    @commands.command()
    async def wiki(self,ctx,text=None):
        article = wiki_search(text=text)

        if len(article) >= 6000:
            article = article[0:2390]+"..."

        print(article)
        
        if text != None:
            embed = discord.Embed(
                title=text,
                description=article,
                color=discord.Colour.random())
        
        else:
            embed = discord.Embed(
                title="歡迎使用維基百科!",
                description="使用方法 g!wiki `text`",
                color=discord.Colour.random()
            )

        embed.set_thumbnail(url=wikipedia_icon_url)
        embed.set_footer(text="infomation from wikipedia.org",icon_url=bot_icon_url)        
        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Tool(bot))