import random
import discord
import datetime
import json
import requests
import tkinter
from discord.ext import commands
from core.classes import Cog_ExtenSion
from ganyu import messages

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
    async def say(self, ctx, *, arg):

        await ctx.message.delete()
        await ctx.send(arg)

        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} ID:{ctx.author.id} 
Guild:{ctx.author.guild} 
Command:{ctx.command}
            """)

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

        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} ID:{ctx.author.id} 
Guild:{ctx.author.guild} 
Command:{ctx.command}
            """)

    @commands.command()
    async def about(self, ctx):
        await ctx.send(random.choice(messages))
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def ping(self, ctx):

        embed = discord.Embed(
            title=f"💫💫💫 Ping: {round(self.bot.latency*1000)} ms",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_footer(
            text=f"{ctx.author.name}",
            icon_url=ctx.author.avatar
        )

        await ctx.send(embed=embed)

        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def getuser(self, ctx, id: int):
        embed = discord.Embed(
            title="成功!",
            description=f"id為 {id} 的用戶是 {self.bot.get_user(id).name} !",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_footer(
            text=f"{ctx.author.name}",
            icon_url=ctx.author.avatar
        )

        await ctx.send(embed=embed)
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def getid(self, ctx, name: discord.Member):

        embed = discord.Embed(
            title="成功!",
            description=f"用戶名為 {name.name} 的id是 {name.id} !",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )

        embed.set_footer(
            text=f"{ctx.author.name}",
            icon_url=ctx.author.avatar
        )

        await ctx.send(embed=embed)

        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

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
                def bug_callbacl(title,description):
                    with open("Error report.txt","a",encoding="utf-8") as f:
                        return f.write(f"\
                            \n[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}]\
                            \n----名稱: {title}\
                            \n----詳細敘述: {description}\
                            \n----提出者: {interaction.user}  id:{interaction.user.id}")
                        
                bug_callbacl(title = modal.children[0].value,description = modal.children[1].value)

                def bug_callbacl(title, description):
                    with open("Error report", "a", encoding="utf-8") as f:
                        return f.write(f"\
[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}]\n\
                        \n#名稱:\n{title}\n\
                        \n#詳細敘述:\n{description}\n\n\
                        提出者:{interaction.user}  id:{interaction.user.id}")

                bug_callbacl(
                    title=modal.children[0].value, description=modal.children[1].value)


                modal_embed = discord.Embed(
                    title=f"感謝 {interaction.user.name} 提出回報!",
                    description=f"以下為 {interaction.user.mention} 的回報內容",
                    color=discord.Colour.random(),
                    timestamp=datetime.datetime.utcnow()
                )
                modal_embed.add_field(
                    name="名稱:",
                    value=f"{modal.children[0].value}",
                    inline=False
                )
                modal_embed.add_field(
                    name="詳細敘述:",
                    value=f"{modal.children[1].value}",
                    inline=False
                )

                modal_embed.set_footer(
                    text="Erro report", icon_url="https://cdn.discordapp.com/avatars/921673886049910795/5f07bb3335678e034600e94bc1515c7f.png?size=1024")

                await interaction.response.send_message(embed=modal_embed)

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


def setup(bot):
    bot.add_cog(Cucmd(bot))
