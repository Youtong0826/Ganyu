from hashlib import md5
from bs4 import BeautifulSoup
from urllib import parse
import youtube_dl
import requests
import datetime
import discord
import random
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

def bullshit(topic,minlen):
    url = "https://api.howtobullshit.me/bullshit"

    data = {
        "Topic":str(topic),
        "MinLen":int(minlen)
    }

    response = requests.post(url=url,json=data)

    return                                                              \
        response                                                        \
        .text                                                           \
        .replace("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;","") \
        .replace("<br>","")

def calculator(LatexExpression):
    url = "https://mathsolver.microsoft.com/cameraexp/api/v1/solvesimplelatex"

    data = {
        "LatexExpression": str(LatexExpression).replace("÷","/").replace("×","*"), 
        "clientInfo": {
            "platform": "web"
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

API_SALT = "xV8v4Qu54lUKrEYFZkJhB8cuOh9Asafs"

def createRandomString(length):
    seed = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for i in range(length):
        result += random.choice(seed)
    return result

def createDS(url, body = ""):
    query = ""
    urlPart = url.split("?")

    if len(urlPart) == 2:
        parameters = urlPart[1].split("&")
        query = "&".join(parameters)

    time = round(int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds()))
    random = createRandomString(6)
    check = md5((f"salt={API_SALT}&t={time}&r={random}&b={body}&q={query}").encode()).hexdigest()

    return f"{time},{random},{check}"

def getGenshininfo(uid,server):
    api_url = f"https://bbs-api-os.hoyolab.com/game_record/genshin/api/index?server={server}&role_id={uid}"

    ds = createDS(url=api_url)

    headers = {
        'Accept' : 'application/json, text/plain, */*',
        'Cookie':'mi18nLang=zh-tw; _MHYUUID=a232123c-a206-4e2e-8444-78daad7b6fa8; _ga=GA1.2.1589446192.1658999142; _gid=GA1.2.1101735951.1658999142; DEVICEFP_SEED_ID=22552ecb28f51ea7; DEVICEFP_SEED_TIME=1658999142283; DEVICEFP=38d7ea61168fb; ltoken=gJvcl9aTHeUhZ3gmjN0or58WuawHgyl21a0fR6PY; ltuid=67987181; cookie_token=K8pGqVFq4j61DbYyMVkVDKEKpHkB0pFSVoNkDDy6; account_id=67987181; _gat=1; _gat_gtag_UA_115635327_39=1',
        "DS" : ds,
        "Host": "bbs-api-os.hoyolab.com",
        "Origin": "https://act.hoyolab.com",
        "x-rpc-app_version": "2.11.1",
        "x-rpc-client_type": "5",
        "x-rpc-language" : "zh-tw"
    }

    #cookies = {
    #    "ltoken" : "gJvcl9aTHeUhZ3gmjN0or58WuawHgyl21a0fR6PY",
    #    "ltuid" : "67987181"
    #}

    result = requests.get(api_url,headers=headers)

    data = json.loads(result.text)["data"]

    return data
