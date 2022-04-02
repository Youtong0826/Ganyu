from site import venv
import discord , datetime
from discord.ext import commands
from core.classes import Cog_ExtenSion

class Help(Cog_ExtenSion):

    @commands.command()
    async def help(self,ctx):

        embed = discord.Embed(
            title="Ganyu 指令清單",
            description="可使用`g!report`來回報錯誤",
            color = 0xec8fff,
            timestamp = datetime.datetime.utcnow()
        )

        embed.add_field(
            name = 'g!fun',
            value = '查看娛樂的指令清單',
        )

        embed.add_field(
            name = 'g!info',
            value = '查看資訊的指令清單',
        )

        embed.add_field(
            name = 'g!cucmd',
            value = '查看常用的指令',
        )

        embed.add_field(
            name = 'g!mange',
            value = '查看管理員指令',
        )

        embed.add_field(
            name = 'g!owner',
            value = '開發者專屬',
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        main_select = discord.ui.Select(
            placeholder="選擇要查看的指令清單",
            options=[
                discord.SelectOption(
                    label=" Ganyu help ",
                    value="ganyu",
                    description="查看指令清單",
                    emoji="🤖"
                ),discord.SelectOption(
                    label=" Fun ",
                    value="fun",
                    description="查看 Fun 指令清單",
                    emoji="🎉"
                ),discord.SelectOption(
                    label=" Info ",
                    value="info",
                    description="查看 Info 指令清單",
                    emoji="📘"
                ),discord.SelectOption(
                    label=" Cucmd ",
                    value="cmd",
                    description="查看Cucmd 指令清單",
                    emoji="📰"
                ),discord.SelectOption(
                    label=" Mange ",
                    value="mange",
                    description="查看 Mange 指令清單",
                    emoji="⚙️"
                ),discord.SelectOption(
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
            if main_select.values[0] == "ganyu":
                embed = discord.Embed(
                    title="Ganyu 指令清單",
                    description="可使用g!report來開啟回報表單",
                    color = 0xec8fff,
                    timestamp = datetime.datetime.utcnow()
                )   

                embed.add_field(
                    name = 'g!fun',
                    value = '查看娛樂的指令清單',
                )

                embed.add_field(
                    name = 'g!info',
                    value = '查看資訊的指令清單',
                )

                embed.add_field(
                    name = 'g!cucmd',
                    value = '查看常用的指令',
                )

                embed.add_field(
                    name = 'g!mange',
                    value = '查看管理員指令',
                )

                embed.add_field(
                    name = 'g!owner',
                    value = '開發者專屬',
                )

                embed.set_footer(
                    text = f"{ctx.author.name}",
                    icon_url = ctx.author.avatar
                )

            elif main_select.values[0] == "fun":
                embed = discord.Embed(
                    title = "fun 指令清單",
                    color = discord.Colour.random(),
                    timestamp = datetime.datetime.utcnow()
                )

                embed.add_field(
                    name = "g!dice `int`",
                    value = "讓這個機器人幫你骰骰子"
                )

                embed.add_field(
                    name = "g!rpg",
                    value = "RPG系統(製作中)"
                )

                embed.set_footer(
                    text = f"{ctx.author.name}",
                    icon_url = ctx.author.avatar
                )

            elif main_select.values[0] == "info":
                embed = discord.Embed(
                    title = "info 指令清單",
                    color = discord.Colour.random(),
                    timestamp = datetime.datetime.utcnow()
                )
                embed.add_field(
                    name="g!allinfo",
                    value="一次性查看所有資訊"
                )
                embed.add_field(
                    name = "g!userinfo",
                    value = "查看使用者在此伺服器的資訊"
                )       
                embed.add_field(
                    name = "g!serinfo `user`",
                    value = "查看伺服器的資訊"
                )       
                embed.add_field(
                    name = "g!botinfo",
                    value = "查看機器人的資訊"
                )       
                embed.add_field(
                    name = "g!time",
                    value = "查看各國時間"
                )       
                embed.add_field(
                    name="g!invite",
                    value="獲取邀請連結"
                )       
                embed.set_footer(
                    text = f"{ctx.author.name}",
                    icon_url = ctx.author.avatar
                )

            elif main_select.values[0] == "cmd":
                embed = discord.Embed(
                    title = "cucmd 指令清單",
                    color = discord.Colour.random(),
                    timestamp = datetime.datetime.utcnow()
                )

                embed.add_field(
                    name = "g!about",
                    value = "關於甘雨"
                )

                embed.add_field(
                    name = "g!ping",
                    value = "查看機器人延遲"
                )

                embed.add_field(
                    name = "g!say `text`",
                    value = "讓這個機器人模仿你說話"
                )

                embed.add_field(
                    name = "g!getid `user`",
                    value =" 透過用戶取得用戶id"
                )

                embed.add_field(
                    name = "g!getuser `id`",
                    value = "透過id取的用戶"
                )

                embed.add_field(
                    name="g!embed `title` `description`",
                    value='傳送一則嵌入訊息\n(如有空格需加"")'
                )

                embed.add_field(
                    name="g!embedtitle `title`",
                    value="傳送只有標題的嵌入訊息(同上)"
                )

                embed.set_footer(
                    text = f"{ctx.author.name}",
                    icon_url = ctx.author.avatar
                )
            elif main_select.values[0] == "mange":
                embed = discord.Embed(
                    title="Mange 管理指令清單",
                    color=discord.Colour.random(),
                    timestamp=datetime.datetime.now()
                )
                embed.add_field(
                    name="g!ban `user`",
                    value="停權其他用戶"
                )
                embed.add_field(
                    name="g!kick `user`",
                    value="踢出其他用戶"
                )
                embed.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar)
            elif main_select.values[0] == "owner":
                embed = discord.Embed(
                    title="開發者專屬",
                    color=discord.Colour.random(),
                    timestamp=datetime.datetime.now()
                )
                embed.add_field(
                    name="g!load `name`",
                    value="載入Cog"
                )
                embed.add_field(
                    name="g!reloag `name`",
                    value="重新載入Cog"
                )
                embed.add_field(
                    name="g!unloag `name`",
                    value="移除Cog"
                )
                embed.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar)


            await interaction.response.edit_message(
                embed = embed,
                view = main_view
            )

        main_select.callback = main_select_callback

        await ctx.send(
            embed = embed,
            view = main_view
        )

        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}
User:{ctx.author} 
ID:{ctx.author.id} 
Guild:{ctx.author.guild} 
Command:{ctx.command}
            """)

    @commands.command()
    async def fun(self,ctx):

        embed = discord.Embed(
            title = "Fun 娛樂指令清單",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )
        embed.add_field(
            name = "g!dice `int` ",
            value = "讓這個機器人幫你骰骰子"
        )

        embed.add_field(
            name = "g!rpg",
            value = "RPG系統(製作中)"
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(
            embed = embed
        )

        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} 
ID:{ctx.author.id} 
Guild:{ctx.author.guild} 
Command:{ctx.command}
            """)

    @commands.command()
    async def info(self,ctx):

        embed = discord.Embed(
            title = "Info 資訊指令清單",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        embed.add_field(
            name = "g!allinfo",
            value = "一次性查看所有資訊!"
        )

        embed.add_field(
            name = "g!userinfo `user`",
            value = "查看使用者在此伺服器的資訊"
        )

        embed.add_field(
            name = "g!serinfo",
            value = "查看伺服器的資訊"
        )

        embed.add_field(
            name = "g!botinfo",
            value = "查看機器人的資訊"
        )

        embed.add_field(
            name = "g!time",
            value = "查看各國時間"
        )

        embed.add_field(
            name = "g!invite",
            value = "獲取邀請連結"
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(embed=embed)

        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} 
ID:{ctx.author.id} 
Guild:{ctx.author.guild} 
Command:{ctx.command}
            """)
        
    @commands.command()
    async def cucmd(self,ctx):

        embed = discord.Embed(
            title = "Cucmd 常用指令清單",
            color = discord.Colour.random(),
            timestamp = datetime.datetime.utcnow()
        )

        embed.add_field(
            name = "g!about",
            value = "關於甘雨"
        )

        embed.add_field(
            name = "g!ping",
            value = "查看機器人延遲"
        )

        embed.add_field(
            name = "g!say `text`",
            value = "讓機器人模仿你說話"
        )

        embed.add_field(
            name = "g!getid `user`",
            value = "透過用戶取得用戶id"
        )

        embed.add_field(
            name = "g!getuser `id`",
            value = "透過id取得用戶"
        )

        embed.add_field(
            name="g!embed `title` `descripion`",
            value='傳送一則嵌入訊息\n(如有空格請加上"")'
        )

        embed.add_field(
            name="g!embedtitle `title`",
            value="傳送只有標題的嵌入訊息(同上)"
        )

        embed.set_footer(
            text = f"{ctx.author.name}",
            icon_url = ctx.author.avatar
        )

        await ctx.send(embed=embed)

        print(
            f"""
Time:{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')} 
User:{ctx.author} 
ID:{ctx.author.id} 
Guild:{ctx.author.guild} 
Command:{ctx.command}
            """)

    @commands.command()
    async def mange(self,ctx):
        embed = discord.Embed(
            title="Mange 管理指令清單",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.now()
        )
        embed.add_field(
            name="g!ban `user`",
            value="停權其他用戶"
        )
        embed.add_field(
            name="g!kick `user`",
            value="踢出其他用戶"
        )
        embed.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar)

        await ctx.send(embed=embed)

    @commands.command()
    async def owner(self,ctx):
        embed = discord.Embed(
            title="開發者專屬",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.now()
        )
        embed.add_field(
            name="g!load `name`",
            value="載入Cog"
        )
        embed.add_field(
            name="g!reloag `name`",
            value="重新載入Cog"
        )
        embed.add_field(
            name="g!unloag `name`",
            value="移除Cog"
        )
        embed.set_footer(text=ctx.author.name,icon_url=ctx.author.avatar)

        await ctx.send(embed=embed)

def setup(bot):
    bot.remove_command("help")
    bot.add_cog(Help(bot))