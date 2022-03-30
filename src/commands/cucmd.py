import random , discord , datetime , json , requests
from discord.ext import commands
from core.classies import Cog_ExtenSion
from ganyu import messages

imageIdList = []
for i in range(3):
    url = f"https://www.pixiv.net/ajax/search/artworks/%E7%94%98%E9%9B%A8?word=%E7%94%98%E9%9B%A8&order=date_d&mode=all&p={str(i+1)}&s_mode=s_tag_full&type=all&lang=zh_tw"
    root = requests.get(url)
    rootData = json.loads(root.text)
    imageData = rootData["body"]["illustManga"]["data"]
    for i in imageData:
        imageInfo = {
            "title":i["title"],
            "user":i["userName"] #指作者
        }
        if i["pageCount"] > 1:
            imageInfo["url"] = f'{str(i["id"])}-1'
        else:
            imageInfo["url"] = f'{str(i["id"])}'
        imageIdList.append(imageInfo)

class Cucmd(Cog_ExtenSion):

    @commands.command()
    async def say(self,ctx ,*, arg):

        await ctx.message.delete()
        await ctx.send(arg)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)

    @commands.command()
    async def avatar(self,ctx,*,member:discord.Member):

        embed = discord.Embed(
            title = f"這是 {member.name} 的頭貼",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        embed.set_image(url=member.avatar)

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(embed = embed)

        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} ID:{ctx.author.id} 
Guild:{ctx.author.guild} 
Command:{ctx.command}
            """)

    @commands.command()
    async def about(self,ctx):

        await ctx.send(random.choice(messages))

        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} 
ID:{ctx.author.id} 
Guild:{ctx.author.guild} 
Command:{ctx.command}
            """)

    @commands.command()
    async def ping(self,ctx):

        embed=discord.Embed(
            title=f"💫💫💫 Ping: {round(self.bot.latency*1000)} ms",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_footer(
            text=f"{ctx.author.name}",
            icon_url=ctx.author.avatar
        )

        await ctx.send(embed=embed)

        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} 
ID:{ctx.author.id} 
Guild:{ctx.author.guild} 
Command:{ctx.command}
            """)

    @commands.command()
    async def getuser(self,ctx,id:int):
        embed = discord.Embed(
            title = "成功!",
            description = f"id為 {id} 的用戶是 {self.bot.get_user(id).name} !",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(embed = embed)

    @commands.command()
    async def getid(self,ctx,name:discord.Member):

        embed = discord.Embed(
            title = "成功!",
            description = f"用戶名為 {name.name} 的id是 {name.id} !",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(embed = embed)

        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} 
ID:{ctx.author.id} 
Guild:{ctx.author.guild} Command:{ctx.command}
            """)

    @commands.command()
    async def pic(self,ctx):
        imgInfo = random.choice(imageIdList)

        imgURL = 'https://pixiv.cat/'+imgInfo["url"]+'.jpg'

        embed = discord.Embed(
            title = imgInfo["title"],
            description = f'繪師：{imgInfo["user"]}',
            color = discord.Colour.nitro_pink(),
        )

        embed.set_image(url=imgURL)

        await ctx.send(embed=embed)
    
    @commands.command()
    async def embed(self,ctx,title,description):

        embed = discord.Embed(
            title = title,
            description= description,
            color = discord.Colour.random()
        )

        await ctx.send(embed = embed)

    @commands.command()
    async def embedtitle(self,ctx , title):

        embed = discord.Embed(
            title = title,
            color = discord.Colour.random()
        )

        await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Cucmd(bot))