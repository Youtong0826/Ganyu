from lib.cog import Log
from core import Bot
from dotenv import load_dotenv
import asyncio
import os


load_dotenv()

intents = Intents.all()

intents.message_content = False
intents.presences = False

bot = Bot(
    command_prefix="g!",
    intents=intents,
)

for folder in ["commands","events"]: bot.load_extension(folder) 



@bot.command()
async def sptrole(ctx : Context):
    if ctx.author.id != 856041155341975582: return

    embed = Embed(
        title="索取你要的身分組!",
        color=Colour.nitro_pink()
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
            "detail":"**thinking**",
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
            await asyncio.sleep(10.0)

    while True:
        await run_activity_loop()

if __name__ == "__main__":
    bot.run(os.environ.get("TOKEN"))
    #bot.run()
#OTg3NjY0MTUxNjI1MjAzNzcy.GL-ETm.b9CbYtNdCrxGILBpT2S_lrQ2-HrIzldGjwZLoI
