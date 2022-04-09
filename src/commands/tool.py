import json
import  discord , datetime , requests
from discord.ext import commands
from core.classes import Cog_ExtenSion
from lib.translate import translate
from commands.rpg import bot_icon_url

google_translate_icon_url = "https://www.bing.com/images/search?view=detailV2&ccid=k9LI8Vlk&id=B47268DA962A9DBE1E3D13681D7E7DC3956B5FBE&thid=OIP.k9LI8Vlk-q4edTMcr32P4AHaHa&mediaurl=https%3a%2f%2fwww.googlewatchblog.de%2fwp-content%2fuploads%2fgoogle-translate-logo-1024x1024.png&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.93d2c8f15964faae1e75331caf7d8fe0%3frik%3dvl9rlcN9fh1oEw%26pid%3dImgRaw%26r%3d0&exph=1024&expw=1024&q=google+translate&simid=608052427486337817&FORM=IRPRST&ck=66C7BB1A428CEFDDAF43B514B70D2DBD&selectedIndex=0"
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
                description="使用方法 g!translate `text`",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )

        embed.set_thumbnail(url=google_translate_icon_url)
        embed.set_footer(text="translate",icon_url=bot_icon_url)        
        await ctx.send(embed = embed)

    @commands.command()
    async def wiki(self,ctx,text=None):
        wiki = "https://zh.wikipedia.org"
        wiki_search_url = f"https://zh.wikipedia.org/w/index.php?search={text}"
        wiki_url = f"https://zh.wikipedia.org/wiki/{text}"
        web = requests.get(wiki_url)
        web.encoding = "UTF-8"
        web_data = json.loads(web.text)
        print(web_data)
        if text != None:
            embed = discord.Embed(
                title=wiki_url,
                description=f"[原文連結]({wiki_url})|[官網]({wiki})",
                color=discord.Colour.random()
            )

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