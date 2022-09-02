import  discord , datetime , ast
from discord.ext import commands
from core.classes import CogExtension

class Math(CogExtension):

    @commands.command()
    async def fac(
        self,
        ctx,
        a: ast.literal_eval
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

                fac = []
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

def setup(bot):
    bot.add_cog(Math(bot))