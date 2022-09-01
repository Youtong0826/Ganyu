import asyncio
import discord
import datetime
from lib.function import SendBGM

async def mange_member(ctx,user:discord.Member, member:discord.Member, type, title, reason=None,CmdType="slash"):

    pms = {}

    if type == "kick":
        pms["per"] = "`kick_member`"
        pms["ch_name"] = "`踢出成員`"
        pms["name"] = "kick"
        pms["ch_v"] = "踢出" 

        haved_pms = user.guild_permissions.kick_members

    elif type == "ban":
        pms["per"] = "`ban_member`"
        pms["ch_name"] = "`對成員停權`"
        pms["name"] = "ban"
        pms["ch_v"] = "停權"

        haved_pms = user.guild_permissions.ban_members

    elif type == "unban":
        pms["per"] = "`ban_member`"
        pms["ch_name"] = "`解除停權`"
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

        if CmdType == "command":
            await ctx.send(embed = embed)

        elif CmdType == "slash":
            await ctx.respond(embed = embed)
        
        if type == "kick": 
            print("y")     
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
        
        if CmdType == "command":
            await ctx.send(embed = embed)

        elif CmdType == "slash":
            await ctx.respond(embed = embed)
        
    embed.set_footer(text=f"{user.name}", icon_url=user.avatar)
    
    SendBGM(ctx)

async def Addrole(ctx,member,role,type="slash"):
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
        
        embed.add_field(name="使用方法",value="/addrole `提及成員/成員名稱/id` `身分組名稱/id`",inline=False)

        embed.add_field(
            name="特殊情況",
            value='如果是 `身分組名稱/id` 或 `提及成員/成員名稱/id` 含有空格的話 請在兩邊加上 `"` 範例: `/addrole "You Tong0826 "管理 管理員""`'
        )

    if type == "command":
        await ctx.send(embed=embed)

    elif type == "slash":
        await ctx.respond(embed=embed)

async def Clean(ctx:discord.ApplicationContext,limit:int,type="slash"):
    
    if limit != None:

        if ctx.author.guild_permissions.manage_messages:
            if limit <= 0:await ctx.response.send_message("無法清理小於或等於0則訊息",ephemeral=True)

            def is_excessive(msg):
                return limit < 30

            deleted = await ctx.channel.purge(limit=limit,check=is_excessive)

            embed = discord.Embed(
                title="已刪除訊息!",
                description=f"成功刪除了**{len(deleted)}**則訊息",
                color=discord.Colour.green(),
                timestamp= datetime.datetime.utcnow()
            )

            if limit >= 30:

                yes_button = discord.ui.Button(
                    style=discord.ButtonStyle.success,
                    label="確定",
                    custom_id="yes"
                )

                no_button = discord.ui.Button(
                    style=discord.ButtonStyle.danger,
                    label="取消",
                    custom_id="no"
                )

                async def button_response(interaction:discord.Interaction):
                    if interaction.user == ctx.author:
                        if interaction.custom_id == "yes":
                            await interaction.channel.purge(limit=limit)
                            await interaction.response.send_message(embed=embed)
                            await interaction.delete_original_message(delay=5.0)

                        elif interaction.custom_id == "no":
                            await interaction.message.delete()
                            await interaction.response.send_message("已取消刪除")
                            await interaction.delete_original_message(delay=5.0)

                    else:await interaction.response.send_message("只有指令使用者才能進行操作",ephemeral=True)

                yes_button.callback = button_response
                no_button.callback = button_response
                view = discord.ui.View(yes_button,no_button)

                await ctx.respond(f"請問您確定要刪除**{limit}**則訊息嗎?",view=view)
                return

        else:

            embed = discord.Embed(
                title="你沒有權限!",
                description="缺少權限 `manage_message` `管理訊息`",
                color=discord.Colour.red(),
                timestamp=datetime.datetime.utcnow()
            )

        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar)

    else:
        embed = discord.Embed(
            title="使用clear來清理訊息",
            description="用法: clear `數量`"
        )

    if type == "command":
        msg = await ctx.send(embed=embed)

    elif type == "slash":
        irt = await ctx.respond(embed=embed)

    if deleted :
        await asyncio.sleep(5)
        try:await irt.delete_original_message()
        except:await msg.delete()

        await ctx.respond(embed=embed)
