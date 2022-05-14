import discord
import datetime 
import os
from discord.ext import commands , tasks
from lib.function import translate
import random

bot = commands.Bot(
    command_prefix='g!',
    intents=discord.Intents.all()
)

for Filename in os.listdir('src/commands'):
    if Filename.endswith(".py"):
        bot.load_extension(f"commands.{Filename[:-3]}")

# @bot.command()
# async def send(ctx,membed:discord.Member = None,message=None):
#    link = "[點擊這裡!](https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=380108955712&scope=bot%20applications.commands)"
#    embed = discord.Embed(
#        title="來自 Ganyu 甘雨 官方的重要公告!",
#        description=f"由於開發者的疏失，導致目前在您伺服器內的{bot.user.mention}需要被重新邀請否則對日後的更新會有__重大影響__\n\n此為新的邀請連結 > {link}\n\n造成您的不便請見諒 也請各位迅速邀請 以便於日後的更新",
#        color=discord.Colour.random()
#    )
#    sended = []
#    for n in bot.guilds:
#        if n.owner not in sended:
#            sended.append(n.owner)
#            await n.owner.send(embed=embed)


#@bot.slash_command(
#    name="test",
#    description="Test",
#    guild_ids=guild_ids())
#async def test(ctx):
#    embed = discord.Embed(
#        title="This is a test command owo"
#    )
#    await ctx.respond("test")


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
    print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}]:{ctx.author.name} loaded {extension} Cog in {ctx.author.guild}")


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
    print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}]:{ctx.author.name} unloaded {extension} Cog in {ctx.author.guild}")


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
    print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}]:{ctx.author.name} reloaded {extension} Cog in {ctx.author.guild}")


@bot.command()
async def modal(ctx):

    embed = discord.Embed(
        title="Modal",
        description="modal test"
    )

    view = discord.ui.View()

    modal_button = discord.ui.Button(
        label="open modal"
    )

    async def modal_button_callback(interaction):

        modal = discord.ui.Modal(title="測試表單")

        input_text_title = discord.ui.InputText(
            style=discord.InputTextStyle.short,
            label="title",
            placeholder="input your title"
        )

        input_text_description = discord.ui.InputText(
            style=discord.InputTextStyle.long,
            label="description",
            placeholder="input your discription"
        )

        async def modal_callback(interaction):

            modal_embed = discord.Embed(
                title=f"{modal.children[0].value}",
                description=f"{modal.children[1].value}"
            )

            await interaction.response.send_message(embed=modal_embed)

        modal.add_item(input_text_title)
        modal.add_item(input_text_description)

        modal.callback = modal_callback

        await interaction.response.send_modal(modal)

    view.add_item(modal_button)

    modal_button.callback = modal_button_callback

    ctx.send(embed=embed, view=view)


@bot.event
async def on_ready():
    print(">>Bot is online<<")
    print(f"-- Watching {len(bot.guilds)} guilds & {len(bot.users)} users ")
 
    def guild_ids():
        guild_ids = []

        for n in bot.guilds:
            guild_ids.append(n.id)
        
        return guild_ids

    activity = discord.Activity(type=discord.ActivityType.watching,name = f"{len(bot.guilds)} 個伺服器")

    await bot.change_presence(status = discord.Status.streaming, activity = activity)

@bot.event
async def on_command_error(ctx, error):
    chiness = translate(str(error), "zh-TW")
    if chiness.endswith("。"):
        chiness = chiness[:-1]
    
    embed = discord.Embed(title="錯誤",description="以下為回報內容",color=discord.Color.red())

    embed.add_field(name="原始內容",value=f"```{error}```",inline=False)

    embed.add_field(name="翻譯後",value=f"```{chiness}```",inline=False)

    embed.add_field(
        name="應對措施",
        value="如果Bot發生錯誤或是使用指令沒回應的話 極有可能是Bot本身的問題 如遇到此情況可使用 `g!report` 來回報給作者們 當然也可能是使用者的問題w",
        inline=False
    )
    print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {error} in {ctx.author.guild}")
    
    await ctx.send(embed=embed)


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


@bot.event
async def on_reaction_add(reaction: discord.Reaction, user: discord.Member):
    if reaction.message.id == 960762107966656582:
        if reaction.emoji == "👍":
            user.add_roles(roles=960443431291871252)

#@tasks.loop(seconds=10)
#async def looping():
#
#    bot_activitys = [
#        discord.Activity(type = discord.ActivityType.listening,name = "g!help"),
#        discord.Activity(type=discord.ActivityType.watching,name = f"{len(bot.guilds)} 個伺服器"),
#        discord.Activity(type=discord.ActivityType.watching,name = f"{len(bot.users)} 個用戶"),
#        discord.Activity(type=discord.ActivityType.playing,name = f"{len(bot.commands)} 條指令")
#    ]
#    
#    activity = random.choice(bot_activitys)
#
#    await bot.change_presence(status = discord.Status.streaming, activity = activity)
#
#looping(bot).start()

if __name__ == "__main__":
        bot.run("OTIxNjczODg2MDQ5OTEwNzk1.Yb2Vsg.qnZ86wXlT1dQdJzYoDrKUVQlhZU")

