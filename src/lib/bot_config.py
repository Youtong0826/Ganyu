from lib.function import mustFieldEmbed
import discord

builder = "youtong._.0826#9250"
update = "無"
bot_icon_url = "https://cdn.discordapp.com/avatars/921673886049910795/5f07bb3335678e034600e94bc1515c7f.png?size=1024"
ganyuCommands = {
    "ganyu": mustFieldEmbed(
        discord.Embed(
            title="Ganyu 指令清單",
            description="可使用`/report`來提出建議或回報錯誤ㄛ~",
            color=0xec8fff
        ),
        [
            ["fun", "查看娛樂指令"],
            ["info", "查看資訊指令"],   
            ["manage", "查看管理員指令"],
            ["tool", "查看小工具指令"],
            #["music", "查看音樂功能的指令"],
            ["other", "查看其他指令"],
        ]
    ),
    "fun": mustFieldEmbed(
        discord.Embed(
            title="Fun 娛樂指令清單",
            color=discord.Colour.random()
        ),
        [
            ["dice `數字` ", "讓這個機器人幫你骰骰子"],
            ["mora","猜拳"],
            ["luck","幸運值"],
            ["spank","拍屁屁"]
        ]
    ),
    "info": mustFieldEmbed(
        discord.Embed(
            title="Info 資訊指令清單",
            color=discord.Colour.random()
        ),
        [
            ["allinfo","一次查看所有資訊!"],
            ["userinfo `user`", "查看使用者在此伺服器的資訊"],
            ["serinfo", "查看伺服器的資訊"],
            ["botinfo", "查看機器人的資訊"],
            ["invite", "獲取邀請連結"],
            ["invites", "查看本服邀請榜"],
            ["roleinfo `身分組`","取得身分組資訊"],
        ]
    ),
    "other": mustFieldEmbed(
        discord.Embed(
            title="Other 其他指令清單",
            color=discord.Colour.random()
        ),
        [
            ["ping", "查看機器人延遲"],
            ["say `文字`", "讓這個機器人模仿你說話"],
            ["dm `成員` `文字`" , "讓 Ganyu 私訊某人"]
        ]
    ),
    "manage": mustFieldEmbed(
        discord.Embed(
            title="Mange 管理指令清單",
            color=discord.Colour.random()
        ),
        [
            ["ban `成員`", "停權其他用戶"],
            ["kick `成員`", "踢出其他用戶"],
            ["clear `數量`", "清理訊息"],
            ["addrole `成員` `身分組`", "新增身分組至一名用戶" ]
        ]
    ),
    "tool": mustFieldEmbed(
        discord.Embed(
            title="Tool 實用小工具",
            color=discord.Colour.random()
        ),
        [
            ["translate `要翻譯後的語言` `文字`","翻譯"],
            ["embed `標題` `內容`","傳送Embed訊息"],
            ["words `句子`","字數轉換"],
            ["bullshit `主題` `字數`","唬爛產生器" ],
            ["math","計算機"],
            ["wiki `關鍵字`","搜索維基百科"]
        ]
    ),
    #"music": mustFieldEmbed(
    #    discord.Embed(
    #        title="Music 音樂功能 v1.0",
    #        color=discord.Colour.random()
    #    ),
    #    [
    #        ["play `連結 or 關鍵字`", "播放音樂"],
    #        ["pause","暫停音樂"],
    #        ["resume","取消暫停音樂"],
    #        ["skip","跳過音樂"],
    #        ["queue","查看播放清單"],
    #        ["clearqueue","清空播放清單"],
    #        ["dc","中斷連線"],
    #        ["np","查看正在播放的音樂資訊"]
    #    ]
    #)
}