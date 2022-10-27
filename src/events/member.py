from lib.classes import CogExtension
from discord.ext import commands
import datetime
import discord
import random

class MemberEvent(CogExtension):
    @commands.Cog.listener()
    async def on_member_join(self,member: discord.Member):
        def join_message():
            coming = random.choice(["來到了","降落在了","轉生到了","穿越到了"])

            embed = discord.Embed(
                title=f"{member.name} {coming} {member.guild.name}!",
                description=f"歡迎! {member.mention} 您是第本伺服器第 **{member.guild.member_count}** 個用戶，請先查看 {member.guild.rules_channel.mention} 再進行其他操作喔",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )

            if member.avatar == None:
                thumbnail = member.default_avatar

            else:
                thumbnail = member.avatar

            embed.set_thumbnail(url=thumbnail)

            embed.set_footer(
                text="成員加入", icon_url="https://cdn.discordapp.com/avatars/921673886049910795/5f07bb3335678e034600e94bc1515c7f.png?size=1024"
            )

            return embed

        if member.guild.id == 719198103227465738:
            channel = self.bot.get_channel(719521057286914129)
            await channel.send(embed=join_message())

        elif member.guild.id == 956614306345123923:
            channel = self.bot.get_channel(957157665526673419)
            for role in member.guild.roles:
                if role.id == 962261737602703391:await member.add_roles(role)
                 
            await channel.send(embed=join_message())

def setup(bot):
    bot.add_cog(MemberEvent(bot))