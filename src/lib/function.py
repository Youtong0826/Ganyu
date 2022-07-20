from bs4 import BeautifulSoup
from urllib import parse
import youtube_dl
import requests
import datetime
import discord
import html
import json
import re

def translate(text, to_language="auto", text_language="auto"):
    GOOGLE_TRANSLATE_URL = 'http://translate.google.cn/m?q=%s&tl=%s&sl=%s'
    text = parse.quote(text)
    url = GOOGLE_TRANSLATE_URL % (text,to_language,text_language)
    response = requests.get(url)
    data = response.text
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    result = re.findall(expr, data)
    if (len(result) == 0):
        return ""
    return html.unescape(result[0])

def mustFieldEmbed(embed: discord.Embed, fields: list) -> discord.Embed:
    for i in fields:
        embed.add_field(name=i[0], value=i[1])
    return embed

def wiki_search(text):
    url = f"https://zh.wikipedia.org/wiki/{text}"
    web = requests.get(url=url)

    soup = BeautifulSoup(web.text,"html.parser")
    articles = soup.select("div.mw-parser-output")
    
    art = ""

    for n in articles:
        art += n.text


    art = art[:200] + " ... go [wikipedia](https://zh.wikipedia.org) to check more info!"

    return art

def bluffshit(topic,minlen):
    url = "https://api.howtobullshit.me/bullshit"

    data = {
        "Topic":str(topic),
        "MinLen":int(minlen)
    }

    response = requests.post(url=url,json=data)

    return      \
        response\
        .text   \
        .replace("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","")\
        .replace("<br>","")

def calculator(LatexExpression):
    url = "https://mathsolver.microsoft.com/cameraexp/api/v1/solvesimplelatex"

    data = {
        "LatexExpression": str(LatexExpression).replace("÷","/").replace("×","*"), 
        "clientInfo": {
            "platform": 
            "web"
            }
        }

    response = requests.post(url=url,json=data)
    return json.loads(response.text).get("solution")

def GetVideoInfo(youtube_url):
    
    data = {}

    with youtube_dl.YoutubeDL() as ydl:

        original_data = ydl.extract_info(str(youtube_url), download=False)
        
        data["id"] = original_data.get("id")
        data["title"] = original_data.get("title")
        data["thumbnail"] = original_data.get("thumbnail")
        data["uploader"] = original_data.get("uploader")
        data["duration"] = original_data.get("duration") #時長(秒)
        data["view_count"] = original_data.get("view_count") 
        data["comment_count"] = original_data.get("comment_count")
        data["like_count"] = original_data.get("like_count")
        data["dislike_count"] = original_data.get("dislike_count")
        data["average_rating"] = original_data.get("average_rating") #平均分數
        data["description"] = original_data.get("description") #描述
        data["tags"] = original_data.get("tags") #標籤
        data["url"] = original_data.get("webpage_url") #連結
        data["upload_date"] = original_data.get("upload_date") 
        
    return data

def SendBGM(ctx):
    time = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime("%Y/%m/%d %H:%M:%S")
    print(f'[{time}] {ctx.author} use the "{ctx.command}" command in {ctx.author.guild}')

def ErrorBGM(ctx,error):
    time = datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime("%Y/%m/%d %H:%M:%S")
    print(f'[{time}] {ctx.author.name} use the "{ctx.command}" command in {ctx.author.guild} return a error:{error}')