import random , discord , datetime , ast , json
from discord.ext import commands
from core.classies import Cog_ExtenSion

class Math(Cog_ExtenSion):

    @commands.command()
    async def math(self,ctx):

        embed=discord.Embed(
            title="算數",
            description="ex:g!add 10 20 ex:g!sqrt 20",
            color=discord.Colour.random()
        )
        embed.add_field(
            name='g!add',
            value='加法'
        )
        embed.add_field(
            name='g!remove',
            value='減法'
        )
        embed.add_field(
            name='g!mupy',
            value='乘法'
        )
        embed.add_field(
            name='g!dvsn',
            value='除法'
        )
        embed.add_field(
            name='g!sqrt',
            value='平方根'
        )
        embed.add_field(
            name='g!square',
            value='平方'
        )
        embed.add_field(
            name='g!fac',
            value='列出該數的因數(正負因數不列入考量)',
            inline=False
        )
        embed.set_footer(
            text=f"{ctx.author.name}",
            icon_url=ctx.author.avatar
        )

        await ctx.send(embed=embed)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}""")

    @commands.command()
    async def add(
        self,
        ctx,
        a : ast.literal_eval,
        b : ast.literal_eval
    ):
        embed = discord.Embed(
            title=" 執行成功!",
            description=f"{a} + {b}的結果為: {a+b}",
            color=discord.Colour.random()
        )
        await ctx.send(embed=embed)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}""")

    @commands.command()
    async def remove(
        self,
        ctx,a : ast.literal_eval,
        b : ast.literal_eval
    ):
        embed = discord.Embed(
            title=" 執行成功!",
            description=f"{a} - {b}的結果為: {a-b}",
            color=discord.Colour.random()
        )

        await ctx.send(embed=embed)
        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

    @commands.command()
    async def mupy(
        self,
        ctx,
        a : ast.literal_eval,
        b : ast.literal_eval
    ):
        embed = discord.Embed(
            title=" 執行成功!",
            description=f"{a} × {b}的結果為: {a*b}",
            color=discord.Colour.random()
        )

        await ctx.send(embed=embed)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

    @commands.command()
    async def dvsn(
        self,
        ctx,
        a : ast.literal_eval,
        b : ast.literal_eval
    ):
        embed = discord.Embed(
            title=" 執行成功!",
            description=f"{a} ÷ {b}的結果為: {a/b}",
            color=discord.Colour.random()
        )

        await ctx.send(embed=embed)
        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

    @commands.command()
    async def sqrt(
        self,
        ctx,
        a : ast.literal_eval
    ):
        if "-" in f'{a}':

            embed = discord.Embed(
                title=" 錯誤",
                description=f"負數沒有平方根!",
                color=discord.Colour.random()
            )

        else:

            embed = discord.Embed(
                title="Math執行成功!",
                description=f"{a} 開根號的結果為: {a**0.5}",
                color=discord.Colour.random()
            )

        await ctx.send(embed=embed)

        print(
            f"""Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

    @commands.command()
    async def square(
        self,
        ctx,
        a : ast.literal_eval
    ):
        embed = discord.Embed(
            title=" 執行成功!",
            description=f"{a}的平方結果為: {a*a}",
            color=discord.Colour.random()
        )

        await ctx.send(embed=embed)

        print(
            f"""Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

    @commands.command()
    async def fac(
        self,
        ctx,
        a : ast.literal_eval
    ):
        if len(f"{a}") > 6:

            embed = discord.Embed(
                title=" 錯誤",
                description=f"{a}太長了 該數不能超過6位數!",
                color=discord.Colour.random())

        else:

            if '-' in f'{a}':

                    embed = discord.Embed(
                        title="無法執行..",
                        description=f"原因:正負因數不列入考量..",
                        color=discord.Colour.random())
            else:

                fac=[]
                time = 0

                for i in range(1, a+1): 
                    time += 1

                    if a % i == 0:
                        fac.append(i) 
                        continue

                    else:
                        pass

                if len(fac) == 0:
                    embed = discord.Embed(
                        title=" 錯誤",
                        description=f"{a}沒有因數!",
                        color=discord.Colour.random())

                else:
                    embed = discord.Embed(
                        title=" 執行成功!",
                        description=f"{a}擁有的因數: {fac}",
                        color=discord.Colour.random())

        await ctx.send(embed=embed)

        print(
            f"""Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

def setup(bot):
    bot.add_cog(Math(bot))