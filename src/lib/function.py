import re
import html
from urllib import parse
import requests
import discord
from bs4 import BeautifulSoup

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
    articles = soup.select("div.mw-parser-output p")
    
    art = ""

    for n in articles:
        art+=n.text

    art = art.split()[0]

    return art