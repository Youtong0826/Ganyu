import discord , datetime
from discord.ext import commands
from core.classes import Cog_ExtenSion
from lib.bot_config import bot_icon_url
from lib.function import SendBGM
from commands.info import ServerDict,BotDict,UserDict

class SlashInfo(Cog_ExtenSion):

    @discord.application_command(description="查看所有的資訊!")
    async def allinfo(self, ctx):
        embed = discord.Embed(
            title="一次查看所有資訊!",
            color=discord.Colour.random(),
        )

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

        async def mainselectcallback(interaction : discord.Interaction):

            if select_main.values[0] == "bot":
                info = BotDict(self.bot)
                embed = info["Embed"]
                view = info["View"]

            elif select_main.values[0] == "user":
                info = UserDict(ctx.author)
                embed = info["Embed"]
                view = info["View"]

            elif select_main.values[0] == "ser":
                info = ServerDict(ctx.author.guild)
                embed = info["Embed"]
                view = info["View"]

            view.add_item(select_main)

            await interaction.response.edit_message(embed=embed,view=view)

        view_main.add_item(select_main)
        select_main.callback = mainselectcallback

        await ctx.respond(embed=embed, view=view_main)
        SendBGM(ctx)

    @discord.application_command(description="查看伺服器資訊!")
    async def serinfo(self, ctx):

        Setting = ServerDict(guild=ctx.author.guild)

        await ctx.send_response(
            embed=Setting["Embed"],
            view=Setting["View"]
        )
        
        SendBGM(ctx)

    @discord.application_command(description="查看機器人資訊!")
    async def botinfo(self, ctx):
        Setting = BotDict(bot=self.bot)

        await ctx.send_response(embed=Setting["Embed"],view=Setting["View"])

        SendBGM(ctx)

    @discord.application_command(description="查看用戶資訊!")
    async def userinfo(self, ctx, member: discord.Member = None):
        if member != None:
            info = UserDict(member)

        else:
            info = UserDict(ctx.author)

        await ctx.send_response(embed=info["Embed"],view=info["View"])

        SendBGM(ctx)

    @discord.application_command(description="邀請機器人")
    async def invite(self, ctx):

        link = "[邀請連結 | invite link](https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=294695021638&scope=bot%20applications.commands)"
        server_link = "[點擊這裡!](https://discord.gg/K3kxVAHHF8)"

        embed = discord.Embed(
            title="邀請我至你的伺服器!",
            description=f"{link}\n(若無法邀請可能是伺服器已滿 需等待驗證)",
            color=discord.Colour.random(),
        )

        #embed = discord.Embed(title="🚫此功能暫未開啟",color=discord.Colour.random())
        await ctx.respond(embed=embed)
        SendBGM(ctx)

    @discord.application_command(description="查看邀請排行榜!")
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

        await ctx.respond(embed=embed)
        SendBGM(ctx)

    @discord.application_command(description="查看身分組資訊!")
    async def roleinfo(self,ctx : discord.ApplicationContext,*,role : discord.Option(discord.Role,"選擇身分組") = None ):

        if role != None:
            role_data = {
                "🗒️ 名字" : role.mention,
                "💳 id" : role.id,
                "📊 人數" : len(role.members),
                "🗓️ 創建時間" : role.created_at.strftime('%Y/%m/%d'),
                "👾 貼圖" : role.unicode_emoji
            }

            embed = discord.Embed(
                title=f'有關 {role.name} 身分組的資訊',
                color=role.color,
                timestamp=datetime.datetime.utcnow()
            )

            view = discord.ui.View(timeout=None)
            backview = discord.ui.View(timeout=None)

            checkbutton = discord.ui.Button(
                style=discord.ButtonStyle.success,
                label="擁有者",
                emoji="📊"
            )
            backbutton = discord.ui.Button(
                style=discord.ButtonStyle.primary,
                label="回去",
                emoji="🔙"
            )

            async def checkbuttoncallback(interaction:discord.Interaction):
                role_members = ""
                role_members_count = 0
                for n in role.members:
                    role_members_count += 1
                    role_members += f"{n.name}\n"
                    if len(role_members) >= 1014:
                        role_members += f"+{len(role.members) - role_members_count}人.."
                        break

                checkembed = discord.Embed(
                    title=f"擁有此身分組的人",
                    description=role_members,
                    color=discord.Colour.random()
                )

                await interaction.response.edit_message(embed=checkembed,view=backview)

            async def backbuttoncallback(interaction:discord.Interaction):
                await interaction.response.edit_message(embed=embed,view=view)
            
            for n in role_data:
                if n == None:
                    n = "無"
                embed.add_field(name=n,value=role_data[n],inline=False)

            checkbutton.callback = checkbuttoncallback
            backbutton.callback = backbuttoncallback

            view.add_item(checkbutton)
            backview.add_item(backbutton)
  
        else:
            view = discord.ui.View()
            embed = discord.Embed(
                title="使用 g!roleinfo 取得身分組資訊!",
                description="使用方法❓ g!roleinfo `標註身分組/身分組名稱/身分組id`",
                color=discord.Colour.random()
            )

        embed.set_footer(
            text="rolenfo | 身分組資訊",
            icon_url=bot_icon_url
        )
        await ctx.send_response(embed=embed,view=view)
        SendBGM(ctx)

def setup(bot):
    bot.add_cog(SlashInfo(bot))