import asyncio
from lib.function import SendBGM
from discord.ext import commands
import discord
import os

intents = discord.Intents.all()

intents.message_content = False
intents.presences = False

bot = commands.Bot(
    command_prefix="g!",
    intents=intents
)

bot.remove_command("help")

def load_extension(folder:str,mode:str="load",is_notice:bool=True):

    loading_method = {
        "load":bot.load_extension,
        "reload":bot.reload_extension,
        "unload":bot.unload_extension
    }

    if is_notice:print(f"Start {mode} {folder}")

    for Filename in os.listdir(f'src/{folder}'):

        if Filename.endswith(".py"):
            loading_method[mode](f"{folder}.{Filename[:-3]}")
            if is_notice:print(f'-- {mode}ed "{Filename}"')

for folder in ["commands","slash_commands","events"]: load_extension(folder) 

@bot.command()
async def load(ctx:discord.ApplicationContext, folder, extension=None):
    if ctx.author.id not in [611118369474740244, 856041155341975582]: return

    if not extension:load_extension(folder)

    bot.load_extension(f"{folder}.{extension}")
    embed = discord.Embed(
        title=f"Loaded - {folder}.{extension} - Cog",
        color=0x5cff8d
    )

    await ctx.send(embed=embed)
    SendBGM(ctx)

@bot.command()
async def unload(ctx, folder, extension=None):
    if ctx.author.id not in [611118369474740244, 856041155341975582]: return

    if not extension:load_extension(folder,"unload")
    
    bot.unload_extension(f"{folder}.{extension}")
    embed = discord.Embed(
        title=f"Unloaded - {folder}.{extension} - Cog",
        color=0x5cff8d
    )
    await ctx.send(embed=embed)
    SendBGM(ctx)

@bot.command()
async def reload(ctx, folder, extension=None):
    if ctx.author.id not in [611118369474740244, 856041155341975582]: return

    if not extension:load_extension(folder,"reload")
    
    bot.reload_extension(f"{folder}.{extension}")
    embed = discord.Embed(
        title=f"Reloaded - {folder}.{extension} - Cog",
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

        names = [
            f"/help | {len(bot.guilds)} 個伺服器",
            f"/help | {len(bot.users)} 個用戶",
            f"/help | ping {round(bot.latency * 1000)} ms",
            f"/help | no message intent sad :("
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
            "detail":"**thinking**",
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

        for i in range(len(names)):
            activity = discord.Activity(name=names[i] ,**ACTIVITY_OPTION)
            await bot.change_presence(activity=activity,status=discord.Status.idle)

    while True:
        await run_activity_loop()

if __name__ == "__main__":
    bot.run(os.environ.get("TOKEN"))
    #bot.run()
    #"OTg3NjY0MTUxNjI1MjAzNzcy.
    #GWUpNq.maxR8kDBX7oR6eUYsK3zWrh
    #NJrSqKajn9ZVra4"
