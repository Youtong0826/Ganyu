import discord
import datetime
from discord.ext import commands
from core.classes import Cog_ExtenSion


def mustFieldEmbed(embed: discord.Embed, fields: list) -> discord.Embed:
    for i in fields:
        embed.add_field(name=i[0], value=i[1])
    return embed


# 定義指令的help
ganyuCommands = {
    "ganyu": mustFieldEmbed(
        discord.Embed(
            title="Ganyu 指令清單",
            description="可使用`g!report`來回報錯誤",
            color=0xec8fff
        ),
        [
            ["g!fun", "查看娛樂的指令清單"],
            ["g!info", "查看資訊的指令清單"],
            ["g!cucmd", "查看常用的指令"],
            ["g!manage", "查看管理員指令"],
            ["g!owner", "開發者專屬"],
        ]
    ),
    "fun": mustFieldEmbed(
        discord.Embed(
            title="Fun 娛樂指令清單",
            color=discord.Colour.random()
        ),
        [
            ["g!dice `int` ", "讓這個機器人幫你骰骰子"],
            ["g!rpg", "RPG系統(製作中)"],
        ]
    ),
    "info": mustFieldEmbed(
        discord.Embed(
            title="Info 資訊指令清單",
            color=discord.Colour.random()
        ),
        [
            ["g!allinfo", "一次性查看所有資訊"],
            ["g!userinfo", "查看使用者在此伺服器的資訊"],
            ["g!serinfo", "查看伺服器的資訊"],
            ["g!botinfo", "查看機器人的資訊"],
            ["g!time", "查看各國時間"],
            ["g!invite", "獲取邀請連結"],
            ["g!invites", "查看本服邀請榜"],
        ]
    ),
    "cmd": mustFieldEmbed(
        discord.Embed(
            title="Cucmd 常用指令清單",
            color=discord.Colour.random()
        ),
        [
            ["g!about ", "關於甘雨"],
            ["g!ping", "查看機器人延遲"],
            ["g!say `text`", "讓這個機器人模仿你說話"],
            ["g!getid `user`", "透過用戶取得id"],
            ["g!getuser `id`", "透過id取得用戶"],
            ["g!embed `title` `description`", "傳送一則嵌入訊息\n(如有空格需加"")"],
            ["g!embedtitle `title`", "傳送一則嵌入訊息\n(如有空格需加"")"]
        ]
    ),
    "manage": mustFieldEmbed(
        discord.Embed(
            title="Mange 管理指令清單",
            color=discord.Colour.random()
        ),
        [
            ["g!ban `user`", "停權其他用戶"],
            ["g!kick `user`", "踢出其他用戶"]
        ]
    ),
    "owner": mustFieldEmbed(
        discord.Embed(
            title="Owner 開發者專屬指令",
            color=discord.Colour.random()
        ),
        [
            ["g!load `name`", "載入Cog"],
            ["g!reload `name`", "重新載入Cog"],
            ["g!unload `name`", "移除Cog"],
        ]
    ),
}


class Help(Cog_ExtenSion):

    @commands.command(name="help", description="查看指令清單")
    async def help(self, ctx):
        main_select = discord.ui.Select(
            placeholder="選擇要查看的指令清單",
            options=[
                discord.SelectOption(
                    label=" Ganyu help ",
                    value="ganyu",
                    description="查看指令清單",
                    emoji="🤖"
                ), discord.SelectOption(
                    label=" Fun ",
                    value="fun",
                    description="查看 Fun 指令清單",
                    emoji="🎉"
                ), discord.SelectOption(
                    label=" Info ",
                    value="info",
                    description="查看 Info 指令清單",
                    emoji="📘"
                ), discord.SelectOption(
                    label=" Cucmd ",
                    value="cmd",
                    description="查看Cucmd 指令清單",
                    emoji="📰"
                ), discord.SelectOption(
                    label=" Manage ",
                    value="manage",
                    description="查看 Manage 指令清單",
                    emoji="⚙️"
                ), discord.SelectOption(
                    label=" Owner ",
                    value="owner",
                    description="開發者專屬",
                    emoji="🔒"
                )
            ]
        )

        main_view = discord.ui.View(timeout=None)
        main_view.add_item(main_select)

        async def main_select_callback(interaction):

            await interaction.response.edit_message(
                embed=ganyuCommands[main_select.values[0]],
                view=main_view
            )

        main_select.callback = main_select_callback

        await ctx.send(
            embed=ganyuCommands["ganyu"],
            view=main_view
        )

        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def fun(self, ctx):
        await ctx.send(embed=ganyuCommands["fun"])
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def info(self, ctx):
        await ctx.send(embed=ganyuCommands["info"])
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def cucmd(self, ctx):
        await ctx.send(embed=ganyuCommands["cmd"])
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def manage(self, ctx):
        await ctx.send(embed=ganyuCommands["manage"])
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")

    @commands.command()
    async def owner(self, ctx):
        await ctx.send(embed=ganyuCommands["owner"])
        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author} use the {ctx.command} in {ctx.author.guild}")


def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))