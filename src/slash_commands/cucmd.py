import random
import discord
import datetime
import json
import requests
from core.classes import Cog_ExtenSion
from lib.function import SendBGM

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

class SlashCucmd(Cog_ExtenSion):

    @discord.application_command(description="讓機器人模仿你說的話!")
    async def say(self, ctx : discord.ApplicationContext, *, msg : discord.Option(str,"訊息")):
        if "@everyone" in msg:
            await ctx.respond(f"{ctx.author.mention} 請勿提及everyone!! :x:")
        
        else:
            await ctx.respond(msg)

        SendBGM(ctx)

    @discord.application_command(description="查看頭像")
    async def avatar(self, ctx, *, member: discord.Option(discord.Member,"選擇成員") = None):
        user = ctx.author
        if member != None:
            embed = discord.Embed(
                title=f" ",
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

        await ctx.respond(embed=embed)

        SendBGM(ctx)

    @discord.application_command(description="查看機器人延遲!")
    async def ping(self, ctx):

        embed = discord.Embed(
            title=f"Ping: {round(self.bot.latency*1000)} ms 💫 ",
            color=discord.Colour.random(),
        )

        await ctx.respond(embed=embed)

        SendBGM(ctx)
    
    @discord.application_command(description="查看有關甘雨的圖片")
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
        embed.set_footer(text="Pixiv.net", icon_url=pixiv_image_url)

        main_view = discord.ui.View(timeout=None)
        website_button = discord.ui.Button(
            label="在Pixiv上查看這張圖片!", url=f"https://pixiv.net/artworks/{imgInfo['url']}", emoji="🖼️")

        main_view.add_item(website_button)

        await ctx.respond(embed=embed, view=main_view)
        SendBGM(ctx)

    @discord.application_command(descripton="創建一個嵌入訊息")
    async def embed(self, ctx, title:discord.Option(str,"標題"), *, description: discord.Option(str,"敘述") =None):
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


        await ctx.respond(embed=embed)
        SendBGM(ctx)

    @discord.application_command(descripton="給點小建議或是回報錯誤")
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
                    text=f"{user} 提出回報",
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

        await ctx.respond(embed=embed, view=view)

    @discord.application_command(descripton="私訊他人")
    async def dm(self,ctx,member:discord.Option(discord.Member,"成員")=None ,*, message :discord.Option(str,"要發送的訊息") = None):
        await member.send(content=message)
        embed = discord.Embed(title="已成功傳送私訊!")

        await ctx.respond(embed=embed)
        SendBGM(ctx)

def setup(bot):
    bot.add_cog(SlashCucmd(bot))