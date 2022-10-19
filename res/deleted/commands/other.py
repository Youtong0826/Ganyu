import random
import discord
import datetime
from command_lib import other
from discord.ext import commands
from core.classes import CogExtension
from lib.function import SendBGM

class Cucmd(CogExtension):

    @commands.command()
    async def send(self,ctx,member :discord.Member = None):
        link = "[點擊這裡!](https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=380108955712&scope=bot%20applications.commands)"
        embed = discord.Embed(
            title="非常抱歉打擾您 以下是來自甘雨緊急公告",
            description=f"簡單來說機器人又爆了 將造成機器人下線一陣子 為此我們深感抱歉 我們正在尋找能夠替代的營運商 希望能早點恢復吧Qwq",
            color=discord.Colour.random()
        )
        if member != None:
            await member.send(embed=embed)
        
        else:
            sended = []
            for n in self.bot.guilds:
                if n.owner not in sended:
                    sended.append(n.owner)
                    await n.owner.send(embed=embed)

    @commands.command()
    async def say(self, ctx : discord.ApplicationContext, *, arg):
        if "@everyone" in arg:
            await ctx.send(f"{ctx.author.mention} 請勿提及everyone!! :x:")
        
        else:
            
            try:
                await ctx.message.delete()

            except:
                pass

            await ctx.send(arg)

        SendBGM(ctx)

    @commands.command()
    async def avatar(self, ctx, *, member: discord.Member = None):
        await other.avatar(ctx,member)

    @commands.command()
    async def about(self, ctx):
        SendBGM(ctx)

    @commands.command()
    async def ping(self, ctx):

        embed = discord.Embed(
            title=f"Ping: {round(self.bot.latency*1000)} ms 💫 ",
            color=discord.Colour.random(),
        )

        await ctx.send(embed=embed)

        SendBGM(ctx)

    @commands.command()
    async def getroleid(self,ctx,role: discord.Role):
        embed = discord.Embed(
            title=f"成功",
            description=f"{role.mention} 的id為 {role.id}",
            color=discord.discord.Colour.random()
        )

        await ctx.send(embed=embed)
    
    @commands.command()
    async def pic(self, ctx):
        await other.Pic(ctx,"command")

    @commands.command()
    async def embed(self, ctx, title, *, description=None):
        if title != None:
            if description == None:
                description = ""

            embed = discord.Embed(
                title=title,
                description=description,
                color=discord.Colour.random()
            )
        
        else:
            embed = discord.Embed(
                title="使用g!embed來傳送Embed訊息",
                description="用法 g!embed `標題(空格須加上"")` `內文`"
            )


        await ctx.send(embed=embed)
        SendBGM(ctx)

    @commands.command()
    async def report(self, ctx):
        view = discord.ui.View(timeout=None)

        report_button = discord.ui.Button(
            style=discord.ButtonStyle.success,
            label="開啟回報表單!"
        )

        view.add_item(report_button)

        async def report_button_callback(interaction):
            modal = discord.ui.Modal(
                title="機器人Bug回報表單"
            )

            input_text_title = discord.ui.InputText(
                style=discord.InputTextStyle.short,
                label="名稱",
                placeholder="此次回報的名稱"
            )

            input_text_description = discord.ui.InputText(
                style=discord.InputTextStyle.long,
                label="詳細敘述",
                placeholder="此次回報的敘述",
                max_length=1024
            )

            async def Moadl_callback(interaction):

                title = modal.children[0].value
                description = modal.children[1].value
                user = interaction.user

                #def bug_callback(title,description,modal,user):
                #    with open("Error report.txt","a",encoding="utf-8") as f:
                #        return f.write(f"\
                #            \n[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}]\
                #            \n----名稱: {title}\
                #            \n----詳細敘述: {description}\
                #            \n----提出者: {interaction.user}  id:{interaction.user.id}")
#
                report_embed = discord.Embed(
                    title=title,
                    description=description,
                    timestamp=datetime.datetime.utcnow(),
                    color=discord.Colour.random()
                )

                report_embed.set_footer(
                    text=f"來自 {user} 的回報",
                    icon_url=user.avatar
                )

                channel = self.bot.get_channel(966010451643215912)

                await channel.send(embed=report_embed)

                dm_embed = discord.Embed(
                    title=f"感謝您提出回報!!",
                    description=f"以下為您的回報內容",
                    color=discord.Colour.random(),
                    timestamp=datetime.datetime.utcnow()
                )
                dm_embed.add_field(
                    name="回報名稱:",
                    value=f"{title}",
                    inline=False
                )
                dm_embed.add_field(
                    name="詳細敘述:",
                    value=f"{description}",
                    inline=False
                )

                dm_embed.set_footer(
                    text="Error report", 
                    icon_url="https://cdn.discordapp.com/avatars/921673886049910795/5f07bb3335678e034600e94bc1515c7f.png?size=1024"
                    )
                
                await user.send(embed=dm_embed)

                await interaction.response.send_message(content=f"✅ 已成功提出回報，詳細內容請查看私訊",ephemeral=True)

                print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the error report in {ctx.author.guild}")

            modal.callback = Moadl_callback

            modal.add_item(input_text_title)
            modal.add_item(input_text_description)

            await interaction.response.send_modal(modal)

        report_button.callback = report_button_callback

        embed = discord.Embed(
            title="錯誤回報",
            description="可用來回報錯誤 或是有什麼話想對開發者說都可以使用此功能喔<3",
            color=discord.Colour.random()
        )

        await ctx.send(embed=embed, view=view)

    @commands.command()
    async def vote(self,ctx,topic:discord.Option(str,"投票的主題",name="主題"),options:discord.Option(str,"要投票的選項",name="選項")):
        view = discord.ui.View()
        description = ""

        for option in options.split():
            view.add_item(discord.ui.Button(
                style=discord.ButtonStyle.primary,
                label=option,
                custom_id=f"{ctx.author.guild.id}_vote_{option}_0"
            ))

            description += f"**{option}** - 0 (0%)\n"

        embed = discord.Embed(
            title=topic,
            description=description,
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )

        async def vote_button_response(interaction:discord.Interaction):
            id = interaction.custom_id
            votes = int(id[id.index("_",3):]) + 1

            interaction.custom_id = id.replace(id[id.index("_",3):],votes)

            embed:discord.Embed = interaction.message.embeds[0]
            embed.description = embed.description.replace()

            interaction.response.edit_message()

    @commands.command()
    async def getguild(self,ctx):
        guilds = ""
        bot : commands.Bot = self.bot 

        for guild in bot.guilds:
            if guild.member_count >= 50:
                guilds += f"[**{guild.name}** 擁有者:**{guild.owner.name}** **{len(guild.members)}**人]\n"

        embed = discord.Embed(
            title="所在的伺服器(多人)",
            description=guilds
        )

        await ctx.send(embed=embed)

    @commands.command()
    async def dm(self,ctx,member:discord.Member=None ,*, message = None):
        await member.send(content=message)
        embed = discord.Embed(title="已成功傳送私訊!")

        await ctx.send(embed=embed)
        SendBGM(ctx)

def setup(bot):
    bot.add_cog(Cucmd(bot))