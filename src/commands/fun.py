import random
import discord
import datetime
from discord.ext import commands
from core.classes import Cog_ExtenSion

"""
fun command list
g!dice
g!rpg
"""

class Fun(Cog_ExtenSion):

    @commands.command()
    async def dice(self, ctx, number: int = None):
        if number != None:
            if int(number) > 6 or int(number) < 1:
                embed = discord.Embed(
                    title="...... >:(",
                    description=f"叫你選1~6 你選{number}幹嘛啦!",
                    color=discord.Colour.random()
                )
                await ctx.send(embed=embed)
            else:
                dice = [1, 2, 3, 4, 5, 6]
                end = random.choice(dice)
                if end == number:
                    embed = discord.Embed(
                        title="成功!",
                        description=f"恭喜你成功骰到了{number}!",
                        color=discord.Colour.random()
                    )
                else:
                    embed = discord.Embed(
                        title="很遺憾..",
                        description=f"您骰到了{end}..",
                        color=discord.Colour.random()
                    )
        else:
            embed = discord.Embed(
                title="選擇你要猜的號碼!",
                description="輸入 g!dice 1~6",
                color=discord.Colour.random()
            )

        await ctx.send(embed=embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def rainbow(self,ctx):
        embed = discord.Embed()

        embed.set_image("https://cdn.discordapp.com/attachments/616315208251605005/616319462349602816/Tw.gif")

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Fun(bot))
