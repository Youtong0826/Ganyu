import random , discord , datetime , ast , json
from discord.ext import commands
from core.classies import Cog_ExtenSion

"""
fun command list
g!say
g!avatar
g!dice
g!math
g!rpg
"""

class Fun(Cog_ExtenSion):
    
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

        await ctx.send(embed = embed)#_url_as(format=None, static_format='webp', size=1024))

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}
            """)

    @commands.command()
    async def dice(self,ctx,nember:int):
        if int(nember) > 6 or int(nember) < 1:
            embed = discord.Embed(
                title = "...... >:(",
                description = f"叫你選1~6 你選{nember}幹嘛啦!",
                color=discord.Colour.random()
            )
            await ctx.send(embed = embed)
        else:
            dice = [1,2,3,4,5,6]
            end = random.choice(dice)
            if end == nember:
                embed = discord.Embed(
                    title = "成功!",
                    description = f"恭喜你成功骰到了{nember}!",
                    color = discord.Colour.random()
                )
            else:
                embed = discord.Embed(
                    title = "很遺憾..",
                    description = f"您骰到了{end}..",
                    color = discord.Colour.random()
                )
            await ctx.send(embed = embed)

def setup(bot):
    bot.add_cog(Fun(bot))
