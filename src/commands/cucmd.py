from optparse import Option
import random
import discord
import datetime
import json
import requests
from discord.ext import commands
from core.classes import Cog_ExtenSion
from lib.bot_config import messages
from lib.bot_config import bot_icon_url

imageIdList = []
for i in range(3):
    url = f"https://www.pixiv.net/ajax/search/artworks/%E7%94%98%E9%9B%A8?word=%E7%94%98%E9%9B%A8&order=date_d&mode=all&p={str(i+1)}&s_mode=s_tag_full&type=all&lang=zh_tw"
    root = requests.get(url)
    rootData = json.loads(root.text)
    imageData = rootData["body"]["illustManga"]["data"]
    for i in imageData:
        imageInfo = {
            "title": i["title"],
            "user": i["userName"]  # 指作者
        }
        if i["pageCount"] > 1:
            imageInfo["url"] = f'{str(i["id"])}-1'
        else:
            imageInfo["url"] = f'{str(i["id"])}'
        imageIdList.append(imageInfo)


class Cucmd(Cog_ExtenSion):

    @commands.command()
    async def send(self,ctx,member :discord.Member =None):
        link = "[點擊這裡!](https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=380108955712&scope=bot%20applications.commands)"
        embed = discord.Embed(
            title="非常抱歉打擾您 以下是來自甘雨緊急公告",
            description=f"目前運行機器人的網站(heroku)出了點問題 將造成機器人下線(具體原因不明) 深感棒抱歉 當然對這方面有經驗&修復方法的人歡迎也私訊作者(YouTong._.0826#9250)",
            color=discord.Colour.random()
        )
        #sended = []
        #for n in self.bot.guilds:
        #    if n.owner not in sended:
        #        sended.append(n.owner)
        #        await n.owner.send(embed=embed)

        await member.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, arg):
        await ctx.message.delete()
        await ctx.send(arg)

        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def avatar(self, ctx, *, member: discord.Member = None):
        user = ctx.author
        if member != None:
            embed = discord.Embed(
                title=f"這是 {member.name} 的頭貼",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )

            embed.set_image(url=member.avatar)

            embed.set_footer(
                text=f"{ctx.author.name}",
                icon_url=ctx.author.avatar
            )

        else:
            embed = discord.Embed(
                title=f"這是 {user.name} 的頭貼",
                color=discord.Colour.random(),
                timestamp=datetime.datetime.utcnow()
            )

            embed.set_image(url=user.avatar)

            embed.set_footer(
                text=f"{user.name}",
                icon_url=user.avatar
            )

        await ctx.send(embed=embed)

        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def about(self, ctx):
        await ctx.send(random.choice(messages))
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def ping(self, ctx):

        embed = discord.Embed(
            title=f"Ping: {round(self.bot.latency*1000)} ms 💫💫💫 ",
            color=discord.Colour.random(),
        )

        await ctx.send(embed=embed)

        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

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
        imgInfo = random.choice(imageIdList)

        imgURL = 'https://pixiv.cat/'+imgInfo["url"]+'.jpg'

        embed = discord.Embed(
            title=imgInfo["title"],
            description=f'繪師：{imgInfo["user"]}',
            color=discord.Colour.nitro_pink(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_image(url=imgURL)

        pixiv_image_url = "https://www.bing.com/th?id=ODL.d9cafa2b269e74dcb05b3314a76d721f&w=100&h=100&c=12&pcl=faf9f7&o=6&dpr=1.25&pid=13.1"
        embed.set_footer(text="from Pixiv.net", icon_url=pixiv_image_url)

        main_view = discord.ui.View(timeout=None)
        website_button = discord.ui.Button(
            label="在Pixiv上查看這張圖片!", url=f"https://pixiv.net/artworks/{imgInfo['url']}", emoji="🖼️")

        main_view.add_item(website_button)

        await ctx.send(embed=embed, view=main_view)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def embed(self, ctx, title, *, description=None):

        if description == None:
            description = ""

        embed = discord.Embed(
            title=title,
            description=description,
            color=discord.Colour.random()
        )

        await ctx.send(embed=embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

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
                    text=f"{user.name} 提出回報",
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
    async def vote(self,ctx,topic=None,quantity:int=None):

        if topic and quantity != None:
            MainEmbed = discord.Embed(
                title="請點擊以下按鈕來設置選項內容!",
                color=discord.Colour.random(),
            )

            MainView = discord.ui.View(timeout=None)

            SettingButton = discord.ui.Button(
                style=discord.ButtonStyle.success,
                label="設置投票內容",
                emoji="📊"
            )

            async def SettingButtonCallback(interaction:discord.Interaction):
                SettingModal = discord.ui.Modal(title="投票設置")

                async def SettingModalCallback(interaction:discord.Interaction):
                    options = ""
                    ModalView = discord.ui.View(timeout=None)

                    for n in(0,quantity*2):
                        if n % 2 == 0:
                            options +=f"{n/2+1}.{SettingModal.children[n].value} ▬▬ 0%\n\n"

                    ModalEmbed = discord.Embed(
                        title=f"{interaction.user.name} 已發起投票",
                        description=f"主題 ▬▬ **{topic}** 選項:\n{options}",
                        color=discord.Colour.random(),
                        timestamp=datetime.datetime.utcnow()
                    )

                    async def OptionButtonCallback(interaction:discord.Interaction):

                        if interaction.custom_id == 0:
                            print()


                    for n in range(0,quantity*2):
                        if n % 2 == 0:

                            OptionButton = discord.ui.Button(
                                    style=discord.ButtonStyle.gray,
                                    label=SettingModal.children[n].value,
                                    emoji=SettingModal.children[n+1].value,
                                    custom_id=n
                                )

                            ModalView.add_item(OptionButton)

                    await interaction.response.edit_message(embed=ModalEmbed,view=ModalView)

                for n in range(1,quantity+1):
                    option = discord.ui.InputText(
                            style=discord.InputTextStyle.short,
                            label=f"選項{n}",
                            placeholder=f"填入選項{n}的名稱",
                            max_length=18,
                            custom_id=str(n+10)
                        )

                    SettingModal.add_item(option)

                    emoji = discord.ui.InputText(
                            style=discord.InputTextStyle.short,
                            label=f"選項{n}的表情符號",
                            placeholder=f"填入選項{n}的表情符號",
                            max_length=1,
                            custom_id=str(n+20)
                        )

                    SettingModal.add_item(emoji)
                
                SettingModal.callback = SettingModalCallback

                await interaction.response.send_modal(SettingModal)
                
            SettingButton.callback = SettingButtonCallback
            MainView.add_item(SettingButton)
        
        else:

            MainEmbed = discord.Embed(
                title="歡迎使用投票功能",
                description="使用方法: g!vote `主題` `幾個選項`",
                color=discord.Colour.random(),
            )

            MainView = discord.ui.View(timeout=None)
        
        await ctx.send(embed=MainEmbed,view=MainView)

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

def setup(bot):
    bot.add_cog(Cucmd(bot))
    
