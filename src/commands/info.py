from os import name
import discord , datetime
from discord.ext import commands
from core.classes import Cog_ExtenSion

"""
g!allinfo
g!serinfo
g!botinfo
g!userinfo
g!update
g!invite
"""


class Info(Cog_ExtenSion):
    @commands.command()
    async def allinfo(self, ctx):
        embed = discord.Embed(
            title="一次查看所有資訊!",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar)

        view_main = discord.ui.View(timeout=None)

        select_main = discord.ui.Select(
            options=[
                discord.SelectOption(
                    label="UserInfo",
                    value="user",
                    description="查看用戶資訊",
                    emoji="📰"
                ),
                discord.SelectOption(
                    label="BotInfo",
                    value="bot",
                    description="查看Ganyu甘雨的資訊",
                    emoji="🤖"
                ),
                discord.SelectOption(
                    label="SerInfo",
                    value="ser",
                    description="查看有關伺服器的資訊",
                    emoji="📘"
                )
            ],
            placeholder="選擇你要查看的資訊"
        )

        async def mainselectcallback(interaction):

            if select_main.values[0] == "bot":
                embed = discord.Embed(
                    title=f"{self.bot.user}",
                    color=0x9c8ff,
                    timestamp=datetime.datetime.utcnow()
                )
                embed.add_field(
                    name="📆 創建時間",
                    value="`2022/1/21(GMT+8:00)`",
                    inline=False
                )
                embed.add_field(
                    name="📜 ID",
                    value=f"`921673886049910795`",
                    inline=False
                )
                embed.add_field(
                    name="🌐 伺服器",
                    value=f'`{len(self.bot.guilds)}`'
                )
                embed.add_field(
                    name="📊 用戶",
                    value=f'`{len(self.bot.users)}`'
                )
                embed.add_field(
                    name="💫 Ping",
                    value=f"`{round(self.bot.latency*1000)} ms`"
                )
                embed.set_footer(
                    text="created by Youtong._.0826",
                    icon_url="https://cdn.discordapp.com/avatars/856041155341975582/a5a57f0acdd5c5fb868c9ad50cf7c319.png?size=256"
                )
                mainbutton1 = discord.ui.Button(
                    style=discord.ButtonStyle.primary,
                    label="Invite Link",
                    emoji="🔗",
                    url="https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=0&scope=bot"
                )
                view = discord.ui.View(timeout=None)
                view.add_item(mainbutton1)
                view.add_item(select_main)

                await interaction.response.edit_message(
                    embed=embed,
                    view=view
                )

            elif select_main.values[0] == "user":
                roles = ""
                roles3 = ""
                roles_count = 0
                member = ctx.author

                if member.nick == None:
                    nick = "無"

                else:
                    nick = member.nick

                if member.bot:
                    dbot = "Yes"

                else:
                    dbot = "No"

                for n in member.roles:

                    if n.name != '@everyone':

                        roles += f"{n.mention} | "
                        roles_count += 1

                        if len(roles) < 1014:

                            roles_count2 = roles_count
                            roles3 = f"{roles}"

                if len(roles) > 1014:
                    roles = f"{roles3}+{roles_count-roles_count2} Roles..."

                embed = discord.Embed(
                    title=f"{member.name} 的個人資訊 ",
                    color=0x9c8fff,
                    timestamp=datetime.datetime.utcnow()
                )

                embed.set_thumbnail(
                    url=member.avatar
                )

                embed.add_field(
                    name="🐬 暱稱",
                    value=f"{nick}"
                )

                embed.add_field(
                    name="🤖 Bot",
                    value=f"{dbot}"
                )

                embed.add_field(
                    name="💳 ID",
                    value=f"`{member.id}`",
                    inline=False
                )

                embed.add_field(
                    name="📆 創建時間",
                    value=f"{member.created_at.strftime('%Y/%m/%d')}"
                )

                embed.add_field(
                    name="📆 加入時間",
                    value=f"{member.joined_at.strftime('%Y/%m/%d')}"
                )

                embed.add_field(
                    name=f"📰 身分組[{roles_count}]:",
                    value=f"\n {roles}", inline=False
                )

                embed.set_footer(
                    text=f"{ctx.author.name}",
                    icon_url=ctx.author.avatar
                )

                view = discord.ui.View(timeout=None)
                view.add_item(select_main)

                await interaction.response.edit_message(embed=embed, view=view)

            elif select_main.values[0] == "ser":
                mbot = 0
                person = 0
                booster = ""
                guild = ctx.author.guild

                for n in guild.members:

                    if n.bot:
                        mbot += 1

                    else:
                        person += 1

                if guild.premium_progress_bar_enabled:
                    bar = "已開啟"

                else:
                    bar = "未開啟"

                for n in guild.premium_subscribers:
                    booster += f"{n}\n"

                if booster == "":
                    booster = "無"

                if guild.rules_channel != None:
                    rules_channel = f"\n{guild.rules_channel.mention}"
                else:
                    rules_channel = "無"

                emojis = []
                animated_emojis = []

                for n in guild.emojis:
                    if n.animated:
                        animated_emojis.append(n)
                    else:
                        emojis.append(n)

                embed = discord.Embed(
                    title=f'{guild}',
                    color=0x9c8fff,
                    timestamp=datetime.datetime.utcnow()
                )               

                embed.add_field(
                    name="📘 __一般__",
                    value=f"創建時間: `{guild.created_at.strftime('%Y/%m/%d')}`\
                        \n 擁有者: `{guild.owner.name}`\
                        \n 個人id: `{guild.owner_id}`",
                    inline=False
                )

                embed.add_field(
                    name="☄️ __加成__",
                    value=f"\
                        次數: `{guild.premium_subscription_count}`\n\
                        等級: `{guild.premium_tier}`\n\
                        進度條: `{bar}`"
                )

                embed.add_field(
                    name="📈 __人數__",
                    value=f"\
                        總人數: {guild.member_count}\n\
                        活人: {person}\n\
                        機器人: {mbot}"
                )

                embed.add_field(
                    name="📊 __頻道數__",
                    value=f"\
                        頻道數: {len(guild.channels)}\n\
                        文字頻道: {len(guild.text_channels)}\n\
                        語音頻道: {len(guild.voice_channels)}"
                )                

                embed.add_field(
                    name="👾 __貼圖__",
                    value=f"\
                        數量: {len(guild.emojis)}\n\
                        靜態貼圖: {len(emojis)} \n\
                        動態貼圖: {len(animated_emojis)}"
                )

                embed.add_field(
                    name="📰 __其他__",
                    value=f"\
                        主要語言: {guild.preferred_locale}\n\
                        規則頻道: {rules_channel}",
                )

                embed.set_thumbnail(url=guild.icon)

                embed.set_footer(
                    text=f"{ctx.author.name}",
                    icon_url=ctx.author.avatar
                )

                if guild.rules_channel == None:
                    rulebutton = discord.ui.Button(
                        style=discord.ButtonStyle.danger,
                        emoji="🔖",
                        label="無法前往規則頻道!"
                    )

                else:
                    rulebutton = discord.ui.Button(
                        style=discord.ButtonStyle.success,
                        emoji="🔖",
                        label="Rules channel",
                        url=f"https://discord.com/channels/{guild.id}/{guild.rules_channel.id}"
                    )

                    view_main.add_item(rulebutton)

                chechboosterbutton = discord.ui.Button(
                    style=discord.ButtonStyle.success,
                    emoji="📖",
                    label="Booster"
                )
                Rolesbutton = discord.ui.Button(
                    style=discord.ButtonStyle.primary,
                    emoji="📋",
                    label="Roles"
                )
                backbutton = discord.ui.Button(
                    style=discord.ButtonStyle.success,
                    emoji="🔙",
                    label="back"
                )

                view = discord.ui.View(timeout=None)
                view_else = discord.ui.View(timeout=None)

                view_else.add_item(backbutton)
                view.add_item(chechboosterbutton)
                view.add_item(Rolesbutton)
                view.add_item(select_main)

                async def checkboostercallback(interaction):
                    await interaction.response.edit_message(
                        embed=discord.Embed(
                            title=f"加成此伺服器的人 ({len(guild.premium_subscribers)})",
                            description=f"{booster}"
                        ),
                        view=view_else
                    )

                async def backcallback(interaction):
                    await interaction.response.edit_message(
                        embed=embed,
                        view=view
                    )

                async def rolescallback(interaction):
                    roles_count = 0
                    roles = ""

                    for n in guild.roles:
                        if n.name != '@everyone':
                            roles += f"{n.mention} | "
                            roles_count += 1

                            if len(roles) < 1014:
                                roles_count2 = roles_count
                                roles3 = f"{roles}"

                    if len(roles) > 1014:
                        roles = f"{roles3}+{roles_count-roles_count2} Roles..."

                    await interaction.response.edit_message(
                        embed=discord.Embed(
                            title=f"身分組[{roles_count}]",
                            description=f"{roles}"
                        ),
                        view=view_else
                    )

                chechboosterbutton.callback = checkboostercallback
                backbutton.callback = backcallback
                Rolesbutton.callback = rolescallback

                await interaction.response.edit_message(
                    embed=embed,
                    view=view
                )

        view_main.add_item(select_main)
        select_main.callback = mainselectcallback

        await ctx.send(embed=embed, view=view_main)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def serinfo(self, ctx):
        can_see = True
        mbot = 0
        person = 0
        booster = ""
        guild = ctx.author.guild

        for n in guild.members:

            if n.bot:
                mbot += 1

            else:
                person += 1

        if guild.premium_progress_bar_enabled:
            bar = "已開啟"

        else:
            bar = "未開啟"

        for n in guild.premium_subscribers:
            booster += f"{n}\n"

        if booster == "":
            booster = "無"

        if guild.rules_channel != None:
            rules_channel = f"\n{guild.rules_channel.mention}"
        else:
            rules_channel = "無"

        emojis = []
        animated_emojis = []

        for n in guild.emojis:
            if n.animated:
                animated_emojis.append(n)
            else:
                emojis.append(n)

        if can_see == True:
            embed_main = discord.Embed(
                title=f'{guild}',
                description=f"伺服器id:`{guild.id}`",
                color=0x9c8fff,
                timestamp=datetime.datetime.utcnow()
            )

            embed_main.add_field(
                name="📘 __概要__",
                value=f"\
                創建時間: `{guild.created_at.strftime('%Y/%m/%d')}`\
                \n 擁有者: `{guild.owner.name}`\
                \n 個人id: `{guild.owner_id}`",
            )

            embed_main.add_field(
                name="☄️ __加成__",
                value=f"\
                次數: {guild.premium_subscription_count}\
                \n等級: {guild.premium_tier}\
                \n進度條: `{bar}`"
            )

            embed_main.add_field(
                name="📈 __人數__",
                value=f"\
                總人數: {guild.member_count}\
                \n活人: {person}\
                \n機器人: {mbot}"
            )

            embed_main.add_field(
                name="📊 __頻道數__",
                value=f"\
                頻道數: {len(guild.channels)}\
                \n文字頻道: {len(guild.text_channels)}\
                \n語音頻道: {len(guild.voice_channels)}")

            

            embed_main.add_field(
                name="👾 __貼圖__",
                value=f"\
                數量: {len(guild.emojis)}\
                \n靜態貼圖: {len(emojis)} \
                \n動態貼圖: {len(animated_emojis)}"
            )

            embed_main.add_field(
                name="📰 __其他__",
                value=f"\
                主要語言: {guild.preferred_locale}\
                \n規則頻道: {rules_channel}",
            )

            embed_main.set_thumbnail(
                url=guild.icon
            )

            embed_main.set_footer(
                text=f"{ctx.author.name}",
                icon_url=ctx.author.avatar
            )

            checkboosterbutton = discord.ui.Button(
                style=discord.ButtonStyle.success,
                emoji="📖",
                label="Booster"
            )

            backbutton = discord.ui.Button(
                style=discord.ButtonStyle.success,
                emoji="🔙",
                label="back"
            )

            rolesbutton = discord.ui.Button(
                style=discord.ButtonStyle.primary,
                emoji="📋",
                label="Roles"
            )

            view_main = discord.ui.View(timeout=None)
            view = discord.ui.View(timeout=None)

            view.add_item(backbutton)
            view_main.add_item(checkboosterbutton)
            view_main.add_item(rolesbutton)

            async def cbbcallback(interaction):

                await interaction.response.edit_message(
                    embed=discord.Embed(
                        title=f"加成此伺服器的人({len(guild.premium_subscribers)})",
                        description=f"{booster}"),
                    view=view
                )

            async def backcallback(interaction):

                await interaction.response.edit_message(
                    embed=embed_main,
                    view=view_main
                )

            async def rolescallback(interaction):
                roles_count = 0
                roles = ""

                for n in guild.roles:
                    if n.name != '@everyone':
                        roles += f"{n.mention} | "
                        roles_count += 1

                        if len(roles) < 1014:
                            roles_count2 = roles_count
                            roles3 = f"{roles}"

                if len(roles) > 1014:
                    roles = f"{roles3}+{roles_count-roles_count2} Roles..."

                await interaction.response.edit_message(
                    embed=discord.Embed(
                        title=f"身分組[{roles_count}]",
                        description=f"{roles}"
                    ),
                    view=view
                )
            checkboosterbutton.callback = cbbcallback
            backbutton.callback = backcallback
            rolesbutton.callback = rolescallback

            await ctx.send(
                embed=embed_main,
                view=view_main
            )

        else:
            embed = discord.Embed(
                title="此功能暫未開啟",
                color=discord.Colour.random()
            )

        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def botinfo(self, ctx):

        can_see = True

        if can_see == True:

            embed = discord.Embed(
                title=f"{self.bot.user}",
                color=0x9c8ff,
                timestamp=datetime.datetime.utcnow()
            )

            embed.add_field(
                name="📆 創建時間",
                value="`2022/1/21(GMT+8:00)`",
                inline=False
            )

            embed.add_field(
                name="📜 ID",
                value=f"`921673886049910795`",
                inline=False
            )

            embed.add_field(
                name="🌐 伺服器",
                value=f'`{len(self.bot.guilds)}`'
            )
            print(len(self.bot.guilds))
            embed.add_field(
                name="📊 用戶",
                value=f'`{len(self.bot.users)}`'
            )

            embed.add_field(
                name="💫 Ping",
                value=f"`{round(self.bot.latency*1000)} ms`"
            )

            embed.set_footer(
                text="created by Youtong._.0826",
                icon_url="https://cdn.discordapp.com/avatars/856041155341975582/a5a57f0acdd5c5fb868c9ad50cf7c319.png?size=256"
            )

            mainbutton1 = discord.ui.Button(
                style=discord.ButtonStyle.primary,
                label="Invite Link",
                emoji="🔗",
                url="https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=380108955712&scope=bot%20applications.commands"
            )

            mian_view = discord.ui.View(timeout=None)
            mian_view.add_item(mainbutton1)

        await ctx.send(embed=embed, view=mian_view)

        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member = None):
        if member != None:
            roles = ""
            roles3 = ""
            roles_count = 0

            if member.nick == None:
                nick = "無"

            else:
                nick = member.nick

            if member.bot:
                dbot = "Yes"

            else:
                dbot = "No"

            for n in member.roles:

                if n.name != '@everyone':

                    roles += f"{n.mention} | "
                    roles_count += 1

                    if len(roles) < 1014:

                        roles_count2 = roles_count
                        roles3 = f"{roles}"

            if len(roles) > 1014:
                roles = f"{roles3}+{roles_count-roles_count2} Roles..."

            roles.strip("|")

            embed_main = discord.Embed(
                title=f"{member.name} 的個人資訊 ",
                color=0x9c8fff,
                timestamp=datetime.datetime.utcnow()
            )

            embed_main.set_thumbnail(
                url=member.avatar
            )

            embed_main.add_field(
                name="🐬 暱稱",
                value=f"{nick}"
            )

            embed_main.add_field(
                name="🤖 Bot",
                value=f"{dbot}"
            )

            embed_main.add_field(
                name="💳 ID",
                value=f"`{member.id}`",
                inline=False
            )

            embed_main.add_field(
                name="📆 創建時間",
                value=f"{member.created_at.strftime('%Y/%m/%d')}"
            )

            embed_main.add_field(
                name="📆 加入時間",
                value=f"{member.joined_at.strftime('%Y/%m/%d')}"
            )

            embed_main.add_field(
                name=f"📰 身分組[{roles_count}]:",
                value=f"\n {roles}", inline=False
            )

            embed_main.set_footer(
                text=f"{ctx.author.name}",
                icon_url=ctx.author.avatar
            )

            main_view = discord.ui.View(timeout=None)

        else:
            user = ctx.author
            roles = ""
            roles2 = ""
            roles_count = 0

            if user.nick == None:
                nick = "無"

            else:
                nick = user.nick

            if user.bot:
                dbot = "Yes"

            else:
                dbot = "No"

            for n in user.roles:
                if n.name != '@everyone':
                    roles += f"{n.mention} | "
                    roles_count += 1

                    if len(roles) < 1014:
                        roles_count2 = roles_count
                        roles2 = f"{roles}"

            if len(roles) > 1014:
                roles = f"{roles2}+{roles_count - roles_count2} Roles"
             
            roles.strip("|")

            roles.strip("|")

            embed_main = discord.Embed(
                title=f"{user.name} 的個人資料",
                color=0x9c8fff, timestamp=datetime.datetime.utcnow()
            )
            embed_main.set_thumbnail(url=user.avatar)
            embed_main.add_field(
                name="🐬 暱稱",
                value=f"{nick}"
            )
            embed_main.add_field(
                name="🤖 Bot",
                value=f"{dbot}"
            )
            embed_main.add_field(
                name="💳 ID",
                value=f"`{user.id}`",
                inline=False
            )
            embed_main.add_field(
                name=f"🗓️ 創建時間",
                value=f"{user.created_at.strftime('%Y/%m/%d')}"
            )
            embed_main.add_field(
                name="🗓️ 加入時間",
                value=f"{user.joined_at.strftime('%Y/%m/%d')}"
            )
            embed_main.add_field(
                name=f"📰 身分組:({roles_count})",
                value=f" {roles}", inline=False
            )
            embed_main.set_footer(
                text=f"{user.name}",
                icon_url=f"{user.avatar}"
            )
            main_view = discord.ui.View(timeout=None)

        await ctx.send(
            embed=embed_main,
            view=main_view
        )

        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def invite(self, ctx):

        link = "[邀請連結 | invite link](https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=380108955712&scope=bot%20applications.commands)"
        server_link = "[點擊這裡!](https://discord.gg/K3kxVAHHF8)"

        embed = discord.Embed(
            title="邀請我至你的伺服器!",
            description=f"{link}",
            color=discord.Colour.random(),
        )

        #embed = discord.Embed(title="🚫此功能暫未開啟",color=discord.Colour.random())
        await ctx.send(embed=embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def invites(self, ctx: discord.ApplicationContext):
        embed = discord.Embed(
            title=f"{ctx.guild.name} 的邀請榜", color=discord.Color.blue())
        context = ""
        invites = await ctx.guild.invites()

        invites.sort(key=lambda k: k.uses, reverse=True)

        numbers = [
            ":one:",
            ":two:",
            ":three:",
            ":four:",
            ":five:",
            ":six:",
            ":seven:",
            ":eight:",
            ":nine:",
            ":keycap_ten:"
        ]
        for n in invites:
            if str(n.inviter)[:-5] == "":
                invites.remove(n)

        for index, invite in enumerate(invites):
            if index == 10:
                break      
            context += f"{numbers[index]} {str(invite.inviter)[:-5]} 邀請 {invite.uses} 人\n\n"

        embed.description = context

        await ctx.channel.send(embed=embed)

    @commands.command()
    async def roleinfo(self,ctx : discord.ApplicationContext,role : discord.Role = None ):
        if role != None:
            role_data = {
                "🗒️ 名字" : role.mention,
                "💳 id" : role.id,
                "📊 人數" : len(role.members),
                "🗓️ 創建時間" : role.created_at.strftime('%Y/%m/%d'),
                "👾 貼圖" : role.unicode_emoji
            }

            embed = discord.Embed(
                title=f'有關 {role.name}身分組的資訊',
                color=role.color,
                timestamp=datetime.datetime.utcnow()
            )

            for n in role_data:
                if n == None:
                    n = "無"
                embed.add_field(name=n,value=role_data[n],inline=False)
  
        else:
            embed = discord.Embed(
                title="g!roleinfo 取得身分組資訊!",
                description="使用方法❓ g!roleinfo `標註身分組/身分組名稱/身分組id`",
                color=discord.Colour.random()
            )

        await ctx.send(embed=embed)
            
def setup(bot):
    bot.add_cog(Info(bot))
