from urllib import parse
import youtube_dl
import requests
import html
import json
import re

def translate(text, to_language="auto", text_language="auto"):
    GOOGLE_TRANSLATE_URL = 'http://translate.google.com/m?q=%s&tl=%s&sl=%s'
    text = parse.quote(text)
    url = GOOGLE_TRANSLATE_URL % (text,to_language, text_language)

    response = requests.get(url)
    
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    result = re.findall(expr, response.text)

    return "" if (len(result) == 0) else html.unescape(result[0])

def get_pixiv_images(key: str) -> list[dict[str, str]]:
    
    datas = [
        json.loads(requests.get(f"https://www.pixiv.net/ajax/search/artworks/{key}?word={key}&order=date_d&mode=all&p={str(i)}&s_mode=s_tag_full&type=all&lang=zh_tw").text)["body"]["illustManga"]["data"] 
        for i in range(1, 4)
    ]
    
    images = [{
        "title": d["title"],
        "user": d["userName"],
        "url": str(d["id"])
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
