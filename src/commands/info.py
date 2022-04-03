import discord , datetime
from discord.ext import commands
from core.classes import Cog_ExtenSion
from ganyu import update
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
    async def allinfo(self,ctx):
        embed = discord.Embed(
            title="一次查看所有資訊!",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar)

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
                embed=discord.Embed(
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
                    embed = embed,
                    view = view
                )

            elif select_main.values[0] == "user":
                roles = ""
                roles3 = ""
                roles_count = 0
                member = ctx.author

                if member.nick == None:
                    nick = "無"

                else:
                    nick=member.nick

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
                    title = f"{member.name} 的個人資訊 ",
                    color = 0x9c8fff,
                    timestamp = datetime.datetime.utcnow()
                )

                embed.set_thumbnail(
                    url = member.avatar
                )

                embed.add_field(
                    name = "🐬 暱稱",
                    value = f"{nick}"
                )

                embed.add_field(
                    name = "🤖 Bot",
                    value = f"{dbot}"
                )

                embed.add_field(
                    name = "💳 ID",
                    value = f"`{member.id}`",
                    inline = False
                ) 

                embed.add_field(
                    name = "📆 創建時間",
                    value = f"{member.created_at.strftime('%Y/%m/%d')}"
                )

                embed.add_field(
                    name = "📆 加入時間",
                    value = f"{member.joined_at.strftime('%Y/%m/%d')}"
                ) 

                embed.add_field(
                    name = f"📰 身分組[{roles_count}]:",
                    value = f"\n {roles}",inline=False
                )

                embed.set_footer(
                    text = f"{ctx.author.name}",
                    icon_url = ctx.author.avatar
                )

                view = discord.ui.View(timeout=None)
                view.add_item(select_main)

                await interaction.response.edit_message(embed=embed,view = view)

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

                embed = discord.Embed(
                    title=f'{guild}',
                    color=0x9c8fff,
                    timestamp=datetime.datetime.utcnow()
                )

                embed.add_field(
                    name="__:blue_book: 資訊__",
                    value=f"\
                    **創建者:** \n`{guild.owner}`\
                    \n**創建者ID:** `\n{guild.owner_id}`\
                    \n**創建時間:** \n`{guild.created_at.strftime('%Y/%m/%d')}`\
                    \n**伺服器ID:** \n`{guild.id}`"
                )
                embed.add_field(
                    name="__:bar_chart: 統計__",
                    value=f"\
                    **總成員數:** `{guild.member_count}`\
                    \n**活人:** `{person}`\
                    \n**機器人:** `{mbot}`\
                    \n**頻道數:** `{len(guild.channels)}`\
                    \n**身分組數:** `{len(guild.roles)}`\
                    \n**表情符號數:** `{len(guild.emojis)}`"
                )
                embed.add_field(
                    name="__:newspaper: 其他__",
                    value=f"\
                    **加成次數:** `{guild.premium_subscription_count}`\
                    \n**群組等級:** `{guild.premium_tier}`\
                    \n**加成進度條:** `{bar}`\
                    \n**主要語言:** `{guild.preferred_locale}`\
                    \n**規則頻道:** `#{guild.rules_channel}`"
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
                        embed = discord.Embed(
                        title=f"加成此伺服器的人 ({len(guild.premium_subscribers)})",
                        description=f"{booster}"
                        ),
                    view = view_else
                    )

                async def backcallback(interaction):   
                    await interaction.response.edit_message(
                        embed = embed,
                        view = view
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
                        embed = discord.Embed(
                            title=f"身分組[{roles_count}]",
                            description=f"{roles}"
                        ),
                        view = view_else
                        )

                chechboosterbutton.callback = checkboostercallback
                backbutton.callback = backcallback
                Rolesbutton.callback = rolescallback

                await interaction.response.edit_message(
                    embed=embed,
                    view = view
                )

        view_main.add_item(select_main)
        select_main.callback = mainselectcallback

        await ctx.send(embed = embed , view = view_main)

    @commands.command()
    async def serinfo(self,ctx):
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

        if can_see == True:
            embed_main = discord.Embed(
                title = f'{guild}',
                color = 0x9c8fff,
                timestamp = datetime.datetime.utcnow()
            )

            embed_main.add_field(
                name = "__:blue_book: 資訊__",
                value = f"\
                    **創建者:** \n`{guild.owner}`\
                    \n**創建者ID:** `\n{guild.owner_id}`\
                    \n**創建時間:** \n`{guild.created_at.strftime('%Y/%m/%d')}`\
                    \n**伺服器ID:** \n`{guild.id}`"
            )

            embed_main.add_field(
                name = "__:bar_chart: 統計__",
                value = f"\
                    **總成員數:** `{guild.member_count}`\
                    \n**活人:** `{person}`\
                    \n**機器人:** `{mbot}`\
                    \n**頻道數:** `{len(guild.channels)}`\
                    \n**身分組數:** `{len(guild.roles)}`\
                    \n**表情符號數:** `{len(guild.emojis)}`"     
            )

            embed_main.add_field(
                name = "__:newspaper: 其他__",
                value = f"\
                    **加成次數:** `{guild.premium_subscription_count}`\
                    \n**群組等級:** `{guild.premium_tier}`\
                    \n**加成進度條:** `{bar}`\
                    \n**主要語言:** `{guild.preferred_locale}`\
                    \n**規則頻道:** `#{guild.rules_channel}`",inline=True)

            embed_main.set_thumbnail(
                url = guild.icon
            )
    
            embed_main.set_footer(
                text = f"{ctx.author.name}",
                icon_url = ctx.author.avatar
            )

            if guild.rules_channel == None:
                linkbutton = discord.ui.Button(
                    style = discord.ButtonStyle.danger,
                    emoji = "🔖",
                    label = "無法前往規則頻道!"
                )
    
            else:
                linkbutton = discord.ui.Button(
                    style = discord.ButtonStyle.success,
                    emoji = "🔖",label="Rules chnnel",
                    url = f"https://discord.com/channels/{guild.id}/{guild.rules_channel.id}"
                )

                view_main.add_item(linkbutton)

            checkboosterbutton = discord.ui.Button(
                style = discord.ButtonStyle.success,
                emoji = "📖",
                label = "Booster"
            )              

            backbutton = discord.ui.Button(
                style = discord.ButtonStyle.success,
                emoji = "🔙",
                label = "back"
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
                    embed = discord.Embed(
                        title = f"加成此伺服器的人({len(guild.premium_subscribers)})",
                        description = f"{booster}"),
                        view = view
                )
            
            async def backcallback(interaction):

                await interaction.response.edit_message(
                    embed = embed_main,
                    view = view_main
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
                        embed = discord.Embed(
                        title=f"身分組[{roles_count}]",
                        description=f"{roles}"
                        ),
                    view = view
                    )
            checkboosterbutton.callback = cbbcallback
            backbutton.callback = backcallback
            rolesbutton.callback = rolescallback

            await ctx.send(
                embed = embed_main,
                view = view_main
            )

        else:
            embed = discord.Embed(
                title = "此功能暫未開啟",
                color = discord.Colour.random()
            )

        print(f"""\
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} \
ID:{ctx.author.id}\
Guild:{ctx.author.guild} \
Command:{ctx.command}"""
)


    @commands.command()
    async def botinfo(self,ctx):

        can_see = True

        if can_see == True:

            embed = discord.Embed(
                title = f"{self.bot.user}",
                color = 0x9c8ff,
                timestamp = datetime.datetime.utcnow()
            )

            embed.add_field(
                name = "📆 創建時間",
                value = "`2022/1/21(GMT+8:00)`",
                inline = False
            )

            embed.add_field(
                name = "📜 ID",
                value = f"`921673886049910795`",
                inline = False
            )

            embed.add_field(
                name = "🌐 伺服器",
                value = f'`{len(self.bot.guilds)}`'
            )

            embed.add_field(
                name = "📊 用戶",
                value = f'`{len(self.bot.users)}`'
            )

            embed.add_field(
                name = "💫 Ping",
                value = f"`{round(self.bot.latency*1000)} ms`"
            )

            embed.set_footer(
                text = "created by Youtong._.0826",
                icon_url = "https://cdn.discordapp.com/avatars/856041155341975582/a5a57f0acdd5c5fb868c9ad50cf7c319.png?size=256"
            )

            mainbutton1 = discord.ui.Button(
                style = discord.ButtonStyle.primary,
                label = "Invite Link",
                emoji = "🔗",
                url = "https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=0&scope=bot"
            ) 

            mian_view = discord.ui.View(timeout=None)
            mian_view.add_item(mainbutton1)

        await ctx.send(embed=embed,view=mian_view)

        print(
            f"""
            Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
            User:{ctx.author} 
            ID:{ctx.author.id} 
            Guild:{ctx.author.guild} 
            Command:{ctx.command}"""
        )

    @commands.command()
    async def userinfo(self,ctx,member:discord.Member):

        roles = ""
        roles3 = ""
        roles_count = 0

        if member.nick == None:
            nick = "無"

        else:
            nick=member.nick

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

        embed_main = discord.Embed(
            title = f"{member.name} 的個人資訊 ",
            color = 0x9c8fff,
            timestamp = datetime.datetime.utcnow()
        )

        embed_main.set_thumbnail(
            url = member.avatar
        )

        embed_main.add_field(
            name = "🐬 暱稱",
            value = f"{nick}"
        )

        embed_main.add_field(
            name = "🤖 Bot",
            value = f"{dbot}"
        )

        embed_main.add_field(
            name = "💳 ID",
            value = f"`{member.id}`",
            inline = False
        ) 

        embed_main.add_field(
            name = "📆 創建時間",
            value = f"{member.created_at.strftime('%Y/%m/%d')}"
        )

        embed_main.add_field(
            name = "📆 加入時間",
            value = f"{member.joined_at.strftime('%Y/%m/%d')}"
        ) 

        embed_main.add_field(
            name = f"📰 身分組[{roles_count}]:",
            value = f"\n {roles}",inline=False
        )

        embed_main.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        main_view = discord.ui.View(timeout=None)

        await ctx.send(
            embed = embed_main,
            view = main_view
        ) 

        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} 
ID:{ctx.author.id} 
Guild:{ctx.author.guild} 
Command:{ctx.command}"""
        )

    @commands.command()
    async def invite(ctx):

        link = "https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=8192&scope=bot"

        embed = discord.Embed(
            title = "邀請我至你的伺服器!",
            color = discord.Colour.random(),
            url = link
        )

        #embed = discord.Embed(title="🚫此功能暫未開啟",color=discord.Colour.random())
        await ctx.send(embed = embed)
        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} 
ID:{ctx.author.id} 
Guild:{ctx.author.guild} 
Command:{ctx.command}"""
        )
        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} ID:{ctx.author.id} 
Guild:{ctx.author.guild} 
Command:{ctx.command}"""
        )

def setup(bot):
    bot.add_cog(Info(bot))