import discord
import datetime
import random
import requests
import json
from lib.function import SendBGM

async def Avatar(ctx,member,type="slash"):
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

    if type == "command":
        await ctx.send(embed=embed)

    elif type == "slash":
        await ctx.respond(embed=embed)

    SendBGM(ctx)

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

async def Pic(ctx,type="slash"):
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
        label="在Pixiv上查看這張圖片!", 
        url=f"https://pixiv.net/artworks/{imgInfo['url']}", emoji="🖼️"
    )

    main_view.add_item(website_button)
    if type == "command":
        await ctx.send(embed=embed, view=main_view)

    elif type == "slash":
        await ctx.respond(embed=embed,view=main_view)
    
    SendBGM(ctx)
