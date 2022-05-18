from random import random
import discord
import datetime
from discord.ext import commands
from core.classes import Cog_ExtenSion

async def mange_member(ctx,user:discord.Member, member:discord.Member, type, title, reason=None):

    pms = {}

    if type == "kick":
        pms["per"] = "`kick_member`"
        pms["ch_name"] = "` 踢出成員 `"
        pms["name"] = "kick"
        pms["ch_v"] = "踢出" 

        haved_pms = user.guild_permissions.kick_members

    elif type == "ban":
        pms["per"] = "`ban_member`"
        pms["ch_name"] = "` 對成員停權 `"
        pms["name"] = "ban"
        pms["ch_v"] = "停權"

        haved_pms = user.guild_permissions.ban_members

    elif type == "unban":
        pms["per"] = "`ban_member`"
        pms["ch_name"] = "` 解除停權 `"
        pms["name"] = "unban"
        pms["ch_v"] = "解除停權"

        haved_pms = user.guild_permissions.ban_members

    elif type == "mute":
        pms["per"] = "`mute_members`"
        pms["ch_name"] = "`禁言成員`"
        pms["name"] = "mute"
        pms["ch_v"] = "禁言"

        haved_pms = user.guild_permissions.mute_members

    if haved_pms:
        embed = discord.Embed(
            title=f"{member.name} {title}",
            description=f"{member.mention} 已被 {user.mention} 使用 {pms['name']} 指令{pms['ch_v']}了",
            color=0xff2e2e,
            timestamp=datetime.datetime.utcnow()
        )

        if reason == None:
            reason = "無"

            embed.add_field(
                name="Reason", value=f"```{reason}```"
            )
            
            if type == "kick":                
                await member.kick(reason=reason)

            elif type == "ban":
                await member.ban(reason=reason)

            elif type == "unban":
                await member.unban(reason=reason)

            elif type == "mute":
                mute_role = await member.guild.create_role(
                    reason=reason,
                    name="Muted",
                    permissions=discord.Permissions.general,
                    color=discord.Colour.dark_gray,
                )

                await member.add_roles(roles=mute_role,reason=reason)

    else:
        embed = discord.Embed(
            title="你沒有權限!",
            description=f"缺少權限 {pms['per']} {pms['ch_name']}",
            color=0xff2e2e,
            timestamp=datetime.datetime.utcnow()
        )
        
        
    embed.set_footer(text=f"{user.name}", icon_url=user.avatar)

    await ctx.send(embed = embed)
    print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")


class Mange(Cog_ExtenSion):

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await mange_member(
            ctx=ctx,
            user=ctx.author,
            member=member,
            type="kick",
            title="從這個伺服器消失了!",
            reason=reason
        )

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):

        await mange_member(
            ctx=ctx,
            user=ctx.author,
            member=member,
            type="ban",
            title="從這個伺服器消失了!",
            reason=reason
        )

    @commands.command()
    async def unban(self, ctx, member: discord.Member, *, reason=None):
        await mange_member(
            ctx=ctx,
            user=ctx.author,
            member=member,
            type="unban",
            title="解封了!",
            reason=reason
        )

    @commands.command()
    async def mute(self,ctx,member:discord.Member,*,reason=None):
        await mange_member(
            ctx=ctx,
            user=ctx.author,
            member=member,
            type="mute",
            title="禁言",
            reason=reason
        )

    @commands.command()
    async def delete(self,ctx:discord.ApplicationContext,count : int = None):
        channel : discord.TextChannel = ctx.channel

        if count != None:
            for n in range(count):
                print("s")
                await channel.delete_messages(channel.last_message)
            
            embed = discord.Embed(
                title=f"已成功刪除 {count} 個訊息",
                color=discord.Colour.random()
            )

        else:
            embed = discord.Embed(
                title="歡迎使用g!delete來刪除訊息!",
                description="使用方法g!delete `數量`",
                color=discord.Colour.random()
            )

        await ctx.send(embed=embed)

    @commands.command()
    async def joinmsg(self, ctx, key = "on"):
        await ctx.send(ctx.author.guild.system_channel.name)

    @commands.command()
    async def addrole(self,ctx,role : discord.Role=None,member : discord.Member=None):
        user : discord.Member = ctx.author
        if role and member != None:
            if user.guild_permissions.manage_roles:
                await member.add_roles(role)

                embed = discord.Embed(
                    title="已成功新增身分組!",
                    color=discord.Colour.random()
                )

            else:
                embed = discord.Embed(
                title="你沒有權限!",
                description=f"缺少權限 `mange_roles` `管理身分組`",
                color=0xff2e2e,
            )
                

        else:
            embed = discord.Embed(
                    title="使用g!addrole來替成員新增身分組!",
                    color=discord.Colour.random()
                )
            
            embed.add_field(name="使用方法",value="g!addrole `提及成員/成員名稱/id` `身分組名稱/id`",inline=False)

            embed.add_field(name="特殊情況",value='如果是 `身分組名稱/id` 或 `提及成員/成員名稱/id` 含有空格的話 請在兩邊加上 `"` 範例: `g!addrole "You Tong0826 "管理 管理員""`')

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Mange(bot))
