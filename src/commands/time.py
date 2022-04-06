import discord
import datetime
from discord.ext import commands
from core.classes import Cog_ExtenSion

<<<<<<< HEAD
class Time(Cog_ExtenSion):    
=======

class Time(Cog_ExtenSion):
>>>>>>> 4a26b9d9f551679ba7316a4fba2ecd69fb1f9a22

    @commands.command()
    async def time(self, ctx, key=None):

        if key == None:
            embed = discord.Embed(title="世界時間 world time",
                                  color=discord.Colour.random())
            embed.add_field(
                name="台北 Taipei ",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="北京 Beijing ",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="夏威夷 Hawaii ",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-10))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="安克拉治 Anchorage ",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-9))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="溫哥華 vancouver ",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-8))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="鳳凰城 Phoenix",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-7))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="墨西哥城 Moxico City",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-6))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="紐約 New York",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-5))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="卡拉卡斯 Caracas",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-4))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="聖保羅 Sao Paulo",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=-3))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="倫敦 London",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=0))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="柏林 Berlin",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=1))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="開羅 Cairo",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=2))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="莫斯科 Moscow", value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=3))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="杜拜 Dubai",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=4))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="新德里 New Delhi",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=5.5))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="仰光 Yangon",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=6.5))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="曼谷 Bangkok",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=7))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="東京 Tokyo",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=9))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="雪梨 Sydney",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=10))).strftime('%Y-%m-%d %H:%M:%S')}"
            )
            embed.add_field(
                name="威靈頓 Wellington",
                value=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=12))).strftime('%Y-%m-%d %H:%M:%S')}"
            )

        elif f"{key}" == "taiwan" or "TW" or "tw" or "Tw":
            embed = discord.Embed(
                title="台北時間",
                description=f"{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}"
            )

        await ctx.send(embed=embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")


def setup(bot):
    bot.add_cog(Time(bot))
