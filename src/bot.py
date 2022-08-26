import asyncio
from lib.function import translate, SendBGM, ErrorBGM
from discord.ext import commands
import discord , datetime
import random
import os

intents = discord.Intents.all()

intents.message_content = False
intents.presences = False

bot = commands.Bot(
    command_prefix='g!',
    intents= intents
)

bot.remove_command("help")

print('Start load commands file')
for Filename in os.listdir('src/commands'):
    if Filename.endswith(".py"):
        bot.load_extension(f"commands.{Filename[:-3]}")
        print(f'-- loaded "{Filename[:-3]}" file')

print('Start load slash_commands file')
for Filename in os.listdir('src/slash_commands'):
    if Filename.endswith(".py"):
        bot.load_extension(f"slash_commands.{Filename[:-3]}")
        print(f'-- loaded "{Filename[:-3]}" file')

@bot.command()
async def load(ctx, extension):
    if ctx.author.id == 611118369474740244 or 856041155341975582:
        bot.load_extension(f"commands.{extension}")
        embed = discord.Embed(
            title=f"Loaded - {extension} - Cog",
            color=0x5cff8d
        )
    else:
        embed = discord.Embed(
            title="此為開發者專屬功能",
            color=0x5cff8d
        )
    await ctx.send(embed=embed)
    SendBGM(ctx)

@bot.command()
async def unload(ctx, extension):
    if ctx.author.id == 611118369474740244 or 856041155341975582:
        bot.unload_extension(f"commands.{extension}")
        embed = discord.Embed(
            title=f"Unloaded - {extension} - Cog",
            color=0x5cff8d
        )
    else:
        embed = discord.Embed(
            title="此為開發者專屬功能",
            color=0x5cff8d
        )
    await ctx.send(embed=embed)
    SendBGM(ctx)

@bot.command()
async def reload(ctx, extension):
    if ctx.author.id == 611118369474740244 or 856041155341975582:
        bot.reload_extension(f"commands.{extension}")
        embed = discord.Embed(
            title=f"Reloaded - {extension} - Cog",
            color=0x5cff8d
        )

    else:
        embed = discord.Embed(
            title="此為開發者專屬功能",
            color=0x5cff8d
        )
    await ctx.send(embed=embed)
    SendBGM(ctx)

@bot.command()
async def sptrole(ctx : discord.ApplicationContext):
    if ctx.author.id != 856041155341975582: return

    embed = discord.Embed(
        title="索取你要的身分組!",
        color=discord.Colour.nitro_pink()
    )

    pa_button = discord.ui.Button(
        style=discord.ButtonStyle.success,
        label="公告Ping",
        custom_id="PA_ping"
    )

    bu_button = discord.ui.Button(
        style=discord.ButtonStyle.primary,
        label="機器人更新ping",
        custom_id="Bu_ping"
    )

    view = discord.ui.View(timeout=None)
    view.add_item(pa_button)
    view.add_item(bu_button)

    await bot.get_channel(962264203324948500).send(embed=embed,view=view)

@bot.event
async def on_ready():
    print(">>Bot is online<<")
    print(f"-- Watching {len(bot.guilds)} guilds & {len(bot.users)} users ")

    async def run_activity_loop():

        watching = discord.ActivityType.watching

        names = [
            f"/help | {len(bot.guilds)} 個伺服器",
            f"/help | {len(bot.users)} 個用戶",
            f"/help | ping {round(bot.latency * 1000)} ms"
        ]

        ACTIVITY_OPTION = {
            "application_id": 921673886049910795,
            "status" : discord.Status.streaming,
            "url" : "https://discord.gg/AVCWGuuUex",
            "type" : discord.ActivityType.watching,
            "timestamp" : {
                "start":1000,
                "end":2000
            },
            "state":"正在觀看",
            "detail":"**使用我的用戶們<3**",
            "assets" :{
                "large_image":"largetest",
                "large_text":"largetest",
                "small_image" :"smalltest",
                "small_text" : "smalltest"
            },
            "button" :{
                "label" : "Support",
                "url" : "https://discord.gg/AVCWGuuUex "
            }
        }

        STREANING_OPTION = {
            "platfrom": "Discord",
            "game" : "/help",
            "url" : "https://discord.gg/AVCWGuuUex",
            "detail":"**使用我的用戶們<3**",
            "assets" :{
                "large_image":"largetest",
                "large_text":"largetest",
                "small_image" :"smalltest",
                "small_text" : "smalltest"
            },
        }

        activity = discord.Activity(name=names[0],**ACTIVITY_OPTION)
        await bot.change_presence(status = discord.Status.streaming, activity = activity)
        await asyncio.sleep(5)

        activity = discord.Activity(name=names[1],**ACTIVITY_OPTION)
        await bot.change_presence(status = discord.Status.streaming, activity = activity)
        await asyncio.sleep(5)

        activity = discord.Activity(name=names[2],**ACTIVITY_OPTION)
        await bot.change_presence(status = discord.Status.streaming, activity = activity)
        await asyncio.sleep(5)

    while True:
        await run_activity_loop()

@bot.event
async def on_interaction(interaction:discord.Interaction):
    if interaction.is_command():
        await bot.process_application_commands(interaction) 
        return

    if interaction.custom_id[3:7] == "ping":
        roles = interaction.user.guild.roles
        if interaction.custom_id == "PA_ping":
            for role in roles :
                if role.id == 962261741050413096:
                    if role in interaction.user.roles:
                        await interaction.user.remove_roles(role)
                        await interaction.response.send_message(content=f"已成功移除身分組✅",ephemeral=True)
                    else:
                        await interaction.user.add_roles(role)
                        await interaction.response.send_message(content=f"已成功領取身分組✅",ephemeral=True)
        if interaction.custom_id == "Bu_ping":  
        
            for role in roles :
                if role.id == 1009478887140511915:
                    if role in interaction.user.roles:
                        await interaction.user.remove_roles(role)
                        await interaction.response.send_message(content=f"已成功移除身分組✅",ephemeral=True)
                    else:
                        await interaction.user.add_roles(role)
                        await interaction.response.send_message(content=f"已成功領取身分組✅",ephemeral=True)

@bot.event
async def on_message(message : discord.Message):
    if message.author == bot.user or message.author.bot : return

    else:
        if bot.user in message.mentions:
            response = random.choice(["hi","早安","找我嗎?","幹嘛ping我@@",".w."])
            await message.channel.send(response)

    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx : discord.ApplicationContext, error):
    zhCN = translate(str(error), "zh-TW")

    if zhCN.endswith("。"):
        zhCN = zhCN[:-1]

    embed = discord.Embed(title="錯誤",description="以下為回報內容",color=discord.Color.red())

    embed.add_field(name="原始內容",value=f"```{error}```",inline=False)

    embed.add_field(name="翻譯後",value=f"```{zhCN}```",inline=False)

    embed.add_field(
        name="應對措施",
        value="如果Bot或是指令發生錯誤的話可使用 `g!report` 來回報給作者們!\n或是給個建議也可以喔! 我們非常需要您的建議!",
        inline=False
    )

    ErrorBGM(ctx,error)
    await ctx.send(embed=embed)

@bot.event
async def on_member_join(member: discord.Member):
    def join_message():

        embed = discord.Embed(
            title=f"{member.name} 降落在了 {member.guild.name}!",
            description=f"歡迎! {member.mention} 您是第本伺服器第 **{member.guild.member_count}** 個用戶，請先查看 {member.guild.rules_channel.mention} 再進行其他操作喔",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )

        if member.avatar == None:
            thumbnail = member.default_avatar

        else:
            thumbnail = member.avatar

        embed.set_thumbnail(url=thumbnail)

        embed.set_footer(
            text="成員加入", icon_url="https://cdn.discordapp.com/avatars/921673886049910795/5f07bb3335678e034600e94bc1515c7f.png?size=1024"
        )

        return embed

    if member.guild.id == 719198103227465738:
        channel = bot.get_channel(719521057286914129)
        await channel.send(embed=join_message())

    elif member.guild.id == 956614306345123923:
        channel = bot.get_channel(957157665526673419)
        await channel.send(embed=join_message())

if __name__ == "__main__":
    bot.run(os.environ.get("TOKEN"))
    
    #
    #
    #