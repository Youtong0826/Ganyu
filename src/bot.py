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

@bot.event
async def on_ready():
    print(">>Bot is online<<")
    print(f"-- Watching {len(bot.guilds)} guilds & {len(bot.users)} users ")

    activity = discord.Activity(type=discord.ActivityType.watching,name = f"g!help | {len(bot.guilds)} 個伺服器")
    await bot.change_presence(status = discord.Status.streaming, activity = activity)

@bot.event
async def on_message(message : discord.Message):
    if message.author == bot.user or message.author.bot : return

    else:
        if bot.user in message.mentions:
            response = random.choice(["hi","早安","找我嗎?","幹嘛ping我@@"])
            await message.channel.send(response)

    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx : discord.ApplicationContext, error):
    chiness = translate(str(error), "zh-TW")

    if chiness.endswith("。"):
        chiness = chiness[:-1]

    embed = discord.Embed(title="錯誤",description="以下為回報內容",color=discord.Color.red())

    embed.add_field(name="原始內容",value=f"```{error}```",inline=False)

    embed.add_field(name="翻譯後",value=f"```{chiness}```",inline=False)

    embed.add_field(
        name="應對措施",
        value="如果Bot或是指令發生錯誤的話可使用 `g!report` 來回報給作者們!\n或是給個建議也可以喔! 我們非常需要您的建議!",
        inline=False
    )

    ErrorBGM(ctx,error)
    await ctx.send(embed=embed)

#@bot.event
#async def on_application_command_error(ctx : discord.ApplicationContext, error):
#    chiness = translate(str(error), "zh-TW")
#
#    if chiness.endswith("。"):
#        chiness = chiness[:-1]
#
#    embed = discord.Embed(title="錯誤",description="以下為回報內容",color=discord.Color.red())
#
#    embed.add_field(name="原始內容",value=f"```{error}```",inline=False)
#
#    embed.add_field(name="翻譯後",value=f"```{chiness}```",inline=False)
#
#    embed.add_field(
#        name="應對措施",
#        value="如果Bot或是指令發生錯誤的話可使用 `g!report` 來回報給作者們!\n或是給個建議也可以喔! 我們非常需要您的建議!",
#        inline=False
#    )
#
#    ErrorBGM(ctx,error)
#    await ctx.respond(embed=embed)

@bot.event
async def on_member_join(member: discord.Member):
    def join_message():

        embed = discord.Embed(
            title=f"{member.name} 來到了{member.guild.name}!",
            description=f" {member.mention} 您是第本伺服器第 **{member.guild.member_count}** 個用戶，請先查看 {member.guild.rules_channel.mention} 再進行其他操作喔",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )

        if member.avatar == None:
            thunbnail = member.default_avatar

        else:
            thunbnail = member.avatar

        embed.set_thumbnail(url=thunbnail)

        embed.set_footer(
            text="成員加入", icon_url="https://cdn.discordapp.com/avatars/921673886049910795/5f07bb3335678e034600e94bc1515c7f.png?size=1024")

        return embed

    if member.guild.id == 719198103227465738:
        chnnel = bot.get_channel(719521057286914129)
        await chnnel.send(embed=join_message())

    elif member.guild.id == 956614306345123923:
        chnnel = bot.get_channel(957157665526673419)
        await chnnel.send(embed=join_message())

if __name__ == "__main__":
        bot.run("OTIxNjczODg2MDQ5OTEwNzk1.GK9jYd.csgia_s2BWgYMCEPNrHGxHzcRcWOI6Duph7WiE")