from hashlib import md5
from urllib import parse
import youtube_dl
import wikipedia
import requests

import random
import html
import json
import re

from datetime import (
    datetime, 
    timedelta, 
    timezone
)

from discord import (
    Embed
)

def translate(text, to_language="auto", text_language="auto"):
    GOOGLE_TRANSLATE_URL = 'http://translate.google.com/m?q=%s&tl=%s&sl=%s'
    text = parse.quote(text)
    url = GOOGLE_TRANSLATE_URL % (text,to_language, text_language)

    response = requests.get(url)
    
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    result = re.findall(expr, response.text)

    return "" if (len(result) == 0) else html.unescape(result[0])

def must_field_embed(embed: Embed, fields: list) -> Embed:
    for i in fields:
        embed.add_field(name=i[0], value=i[1])
        
    return embed

def wiki_search(*keywords:str,lang:str = "zh"):
    if keywords == None: return None
    wikipedia.set_lang(lang)
    
    return wikipedia.search(keywords)

def wiki_info(title:str=None,sentences:int=1,lang:str="zh"):
    if title == None : return None
    wikipedia.set_lang(lang)
    
    try: return wikipedia.summary(title,sentences)
    except: return None

def get_pixiv_images(key: str) -> list[dict[str, str]]:
    
    datas = [
        json.loads(requests.get(f"https://www.pixiv.net/ajax/search/artworks/{key}?word={key}&order=date_d&mode=all&p={str(i)}&s_mode=s_tag_full&type=all&lang=zh_tw").text)["body"]["illustManga"]["data"] 
        for i in range(1, 4)
    ]
    
    images = [{
        "title": d["title"],
        "user": d["userName"],
        "url": str(d["id"]) + '-1' if d["pageCount"] > 1 else ' '
    } for data in datas for d in data]
    
    return images   

def bullshit(topic, minlen: int):
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

def get_youtube_video(url:str):
    
    data = {}

    with youtube_dl.YoutubeDL() as ydl:

        original_data = ydl.extract_info(str(url), download=False)

        keys = ["id","title","thumbnail","uploader","duration","view_count","comment_count","like_count",
            "dislike_count","average_rating","description","tags","webpage_url","upload_date"]

        for k in keys:
            data[k] = original_data.get(k)
        
    return data

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

def get_now_time(hours: int = 8) -> datetime:
    return datetime.now(timezone(timedelta(hours=hours)))

if __name__ == "__main__":
    print(get_pixiv_images("ganyu"))