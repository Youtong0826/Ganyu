from enum import Enum
from dataclasses import dataclass

from discord import (
    ApplicationContext as Context,
    ButtonStyle,
    Colour,
    Embed,
    EmbedField,
    EmbedFooter,
    Member,
    Role,
    TextChannel,
    option,
    slash_command
)

from discord.ui import (
    View,
    Button,
)

from lib.cog import CogExtension
from lib.functions import get_now_time

class ManageType(Enum):
    kick = 1
    ban = 2
    unban = 3
    mute = 4

@dataclass    
class Management:
    name: str
    ch_name: str
    ch_original: str
    permissions_name: str
    permissions: bool
    

class SlashManage(CogExtension):
    
    async def manage(self, ctx: Context, user: Member, member: Member, type: ManageType, title: str, reason: str ="無"):
        match type:
            case ManageType.kick:
                data = Management(
                    "kick",
                    "踢出",
                    "`踢出成員`",
                    "`kick_member`",
                    user.guild_permissions.kick_members
                )
                
            case ManageType.ban:
                data = Management(
                    "ban",
                    "停權",
                    "`對成員停權`"
                    "`ban_member`",
                    user.guild_permissions.ban_members
                )
                
            case ManageType.unban:
                data = Management(
                    "unban",
                    "解除停權`",
                    "`解除停權`",
                    "`ban_member`",
                    user.guild_permissions.ban_members
                )
                
            case ManageType.mute:
                data = Management(
                    "kick",
                    "禁言",
                    "`禁言成員`",
                    "`mute_members`",
                    user.guild_permissions.mute_members
                )
                
            case _:
                data = Management(
                    "kick",
                    "踢出",
                    "`踢出成員`",
                    "`kick_member`",
                    False
                )

        if not data.permissions:
            return await ctx.respond(embed=Embed(
                title="你沒有權限!",
                description=f"缺少權限 {data.permissions_name} {data.ch_original}",
                color=0xff2e2e,
                timestamp=get_now_time(),
                footer=EmbedFooter(f"/{data.name}", self.bot.icon_url)
            ))
            
        match type:
            case ManageType.kick:
                await member.kick(reason=reason)
                
            case ManageType.ban:
                await member.ban(reason=reason)
                
            case ManageType.unban:
                await member.unban(reason=reason)
                
            case ManageType.mute:
                await member.timeout(reason=reason)
            

        await ctx.respond(embed=Embed(
            title=f"{member.name} {title}",
            description=f"{member.mention} 已被 {user.mention} 使用 {data.name} 指令{data.ch_name}了",
            color=0xff2e2e,
            timestamp=get_now_time(),
            footer=EmbedFooter(f"/{data.name}", self.bot.icon_url),
            fields=[
                EmbedField("Reason", f"```{reason}```")
            ]
        ))

    @slash_command(description="踢出成員")
    @option("member", Member, description="選擇成員", required=False)
    async def kick(self, ctx: Context, member: Member, *, required=False):
        self.bot.log(ctx)
        if not member:
            return await ctx.respond(embed=Embed(
                title="/kick 踢除成員",
                description="用法 /kick `提及/id/名字` `原因(可空)`"
            ))
            

        await self.manage(
            ctx=ctx,
            user=ctx.author,
            member=member,
            type="kick",
            title="從這個伺服器消失了!",
            reason=reason,
        )
            
    @slash_command(description="停權成員")
    @option("member", Member, description="選擇成員", required=False)
    async def ban(self, ctx: Context, member: Member, *, required=False):
        self.bot.log(ctx)
        if not member:
            return await ctx.respond(embed=Embed(
                title="/ban 停權成員",
                description="用法 /ban `提及/id/名字` `原因(可空)`"
            ))
            
        await self.manage(
            ctx=ctx,
            user=ctx.author,
            member=member,
            type="ban",
            title="被停權了",
            reason=reason,
        )
        
    @slash_command(description="解除停權")
    @option("member", Member, description="選擇成員", required=False)
    async def unban(self, ctx: Context, member: Member, *, required=False):
        self.bot.log(ctx)
        if not member:
            return await ctx.respond(embed=Embed(
                title="/unban 對成員解除停權",
                description="用法 /unban `提及/id/名字` `原因(可空)`"
            ))

        await self.manage(
            ctx=ctx,
            user=ctx.author,
            member=member,
            type="unban",
            title="已解除停權",
            reason=reason,
        )
        
    @slash_command(description="新增身分組至另一名成員!")
    @option("member", Member, description="選擇成員", required=False)
    @option("role", Member, description="選擇身分組", required=False)
    async def addrole(self, ctx: Context, member: Member, role: Role):
        self.bot.log(ctx)
        if not role or not member:
            return await ctx.respond(embed=Embed(
                title="使用 /addrole 對成員新增身分組!",
                color=Colour.random(),
                fields=[
                    EmbedField(
                        "使用方法", 
                        "/addrole `提及成員/成員名稱/id` `身分組名稱/id`"
                    ),
                    EmbedField(
                        "特殊情況",
                        '如果是 `身分組` 或 `成員` 含有空格的話 請在兩邊加上 `"` 範例: `/addrole "You Tong0826" "管理 管理員"`'
                    )
                ],
                footer=EmbedFooter("/addrole | Ganyu", self.bot.icon_url)
            ))

        if not ctx.author.guild_permissions.manage_roles:
            await ctx.respond(embed=Embed(
                title="你沒有權限!",
                description=f"缺少權限 `mange_roles` `管理身分組`",
                color=0xff2e2e,
            ))
        await member.add_roles(role)
        await ctx.respond(embed=Embed(
            title="已成功新增身分組!",
            color=0xff2e2e,
            timestamp=get_now_time(),
            footer=EmbedFooter("/addrole | Ganyu", self.bot.icon_url)
        ))

    @slash_command(description="清理訊息")
    @option("limit", int, description="數量", required=False)
    async def clear(self, ctx: Context, limit: int):
        self.bot.log(ctx)
        
        if not limit:
            return await ctx.respond(embed=Embed(
                title="/clear 清理訊息",
                description="用法: clear `數量`",
                color=0xff2e2e,
                timestamp=get_now_time(),
                footer=EmbedFooter("/clear | Ganyu", self.bot.icon_url)
            ))
            
        if not ctx.author.guild_permissions.manage_messages:
            return await ctx.respond(embed=Embed(
                title="你沒有權限!",
                description="缺少權限 `manage_message` `管理訊息`",
                color=0xff2e2e,
                timestamp=get_now_time(),
                footer=EmbedFooter("/clear | Ganyu", self.bot.icon_url)
            ))
            
  
        if limit <= 0:
            return await ctx.response.send_message(f"`無法清理 {limit} 則訊息`", ephemeral=True);
        
        if limit >= 25:
            return await ctx.respond(
                f"請問您確定要刪除**{limit}**則訊息嗎?", 
                view=View(
                    Button(
                        style=ButtonStyle.success,
                        label="確定",
                        custom_id=f"clear_yes_{limit}"
                    ),
                    Button(
                        style=ButtonStyle.danger,
                        label="取消",
                        custom_id=f"clear_no_{limit}"
                    )
                )
            )


        deleted = await ctx.channel.purge(limit=limit)
        msg = await ctx.respond(embed=Embed(
            title="已刪除訊息!",
            description=f"成功刪除了**{len(deleted)}**則訊息",
            color=0xff2e2e,
            timestamp=get_now_time(),
        ))

        if deleted:
            await msg.delete_original_message(delay=5.0)

def setup(bot):
    bot.add_cog(SlashManage(bot))
