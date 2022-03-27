import random , discord , datetime , ast , json
from discord.ext import commands
from core.classies import Cog_ExtenSion
from ganyu import messages

class Other(Cog_ExtenSion):

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
def setup(bot):
    bot.add_cog(Other(bot))