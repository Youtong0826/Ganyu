import discord , datetime
from discord.ext import commands
from core.classies import Cog_ExtenSion

class Mange(Cog_ExtenSion):

    @commands.command()
    async def ban(self, ctx , member : discord.Member ,*, reason=None):

        if ctx.author.guild_permissions.ban_members:

            embed = discord.Embed(
                title=f"{member.name} 從這個伺服器消失了!",
                description=f"{member.mention} 遭到 {ctx.author.mention} 使用 ban 指令停權了",
                color = 0xff2e2e
            )
            await member.ban(reason = reason)
            await ctx.send( embed = embed )   
        else:
            embed = discord.Embed(
                title="你沒有權限!",
                description=f"缺少權限 ban_members \"對成員停權\"",
                color = 0xff2e2e
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

def setup(bot):
    bot.add_cog(Mange(bot))