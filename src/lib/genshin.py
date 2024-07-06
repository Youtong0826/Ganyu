from hashlib import md5
import random
import datetime
import requests
import json

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