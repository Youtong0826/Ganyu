import discord , datetime , os
from discord.ext import commands

bot = commands.Bot(
    command_prefix='g!',
    intents = discord.Intents.all()
)

for Filename in os.listdir('src/commands'):
    if Filename.endswith(".py"):
        bot.load_extension(f"commands.{Filename[:-3]}")

def guild_ids():
    guild_ids = []  

    for n in bot.guilds:  
        guild_ids.append(n.id)
        
    return guild_ids

bot.activity = discord.Game(
    name="g!help owo"
)

#@bot.command()
#async def send(ctx,membed:discord.Member = None,message=None):
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

@bot.slash_command(
    name="test",
    description="Test",
    guild_ids = 939145544926912552
)
async def test(ctx):
    embed = discord.Embed(
        title="This is a test command owo"
    )
    await ctx.respond("test")

@bot.command()
async def load(ctx,extension):
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
    await ctx.send(embed = embed)
    print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}]:{ctx.author.name} loaded {extension} Cog in {ctx.author.guild}")

@bot.command()
async def unload(ctx,extension):
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
    await ctx.send(embed = embed)
    print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}]:{ctx.author.name} unloaded {extension} Cog in {ctx.author.guild}")

@bot.command()
async def reload(ctx,extension):
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
    await ctx.send(embed = embed)
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

            await interaction.response.send_message(embed = modal_embed)

        modal.add_item(input_text_title)
        modal.add_item(input_text_description)

        modal.callback = modal_callback

        await interaction.response.send_modal(modal)
    
    view.add_item(modal_button)
    
    modal_button.callback = modal_button_callback

    ctx.send(embed=embed, view = view)

@bot.event
async def on_ready():
    print(">>Bot is online<<")

@bot.event 
async def on_command_error(ctx,error):
    bool1 = False
    bool2 = False

    def on_cmd_error(keywords,error):#尋找回報中是否含有關鍵字
        test = 0
        for n in keywords:
            if n in f'{error}':
                test += 1

        if test == len(keywords):
            return True

        else:
            return False

    def embed_copy(des):#快速嵌入訊息
        embed = discord.Embed(
            title = "指令執行失敗..",
            description = f"原因: {des}",
            color = discord.Colour.random()
        )

        return embed

    if on_cmd_error(keywords=["Missing Permission"],error=error):
        bool1 = True
        if f"{ctx.command}" == "say":
            embed = embed_copy(des="我沒有刪除訊息的權限")

        else:

            embed= embed_copy(des="我沒有權限..")
    if on_cmd_error(keywords=["Member","not found"],error=error):
        bool1 = True
        embed= embed_copy(des="查無此人")

    if on_cmd_error(keywords=['Command','is not found'],error=error):
        bool1 = True
        bool2 = False
        embed= embed_copy(des="沒有這個指令啦!")

    if on_cmd_error(keywords=['Converting to "literal_eval" failed for parameter "a".'],error=error):
        bool1 = True
        embed= embed_copy(des="第一個數字是不是怪怪的hmm")

    if on_cmd_error(keywords=['Converting to "literal_eval" failed for parameter "b".'],error=error):
        bool1 = True
        embed= embed_copy(des="第二個數字是不是怪怪的hmm")

    if on_cmd_error(keywords=["b is a required argument that is missing."],error=error):
        bool1 = True
        embed= embed_copy(des="阿你的第二個數字勒..")

    if on_cmd_error(keywords=['a is a required argument that is missing.'],error=error):
        bool1 = True
        embed= embed_copy(des="你不輸入數字我怎麼算...")

    if on_cmd_error(keywords=['arg is a required argument that is missing.'],error=error):
        bool1 = True
        if f"{ctx.command}" == "say":
            embed= embed_copy(des="沒有可以模仿的話..")

        elif f"{ctx.command}" == "ac":
            embed= embed_copy(des="此為測試功能")

    if on_cmd_error(keywords=['Converting to "int" failed for parameter "nember"'],error=error):
        bool1 = True
        embed= embed_copy(des=f"奇怪..您好像不是輸入一個完整的數字欸")

    if on_cmd_error(keywords=['id is a required argument that is missing.'],error=error):
        bool1 = True
        embed= embed_copy(des=f"缺少用來查找用戶的id")

    if on_cmd_error(keywords=['name is a required argument that is missing.'],error=error):
        bool1 = True
        embed= embed_copy(des=f"缺少用來查找id的用戶名")

    if on_cmd_error(keywords=["description is a required argument that is missing."],error=error):
        bool1 = True
        embed = embed_copy(des="缺少內容")

    if bool1 == False:
        #embed=event.embed_copy(des="待釐清... :(")
        print(error)

    if bool2 == False:
        await ctx.send(embed = embed)

    print(f"""
Time:'{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}'
User:'{ctx.author.name}' 
Guild:{ctx.author.guild}' 
Command:{ctx.command}'
Error:'{error}' 
bool1:'{bool1}' 
bool2:'{bool2}'
""")

@bot.event
async def on_member_join(member : discord.Member):
    if member.guild.id == 719198103227465738:
        chnnel = bot.get_channel(719521057286914129)
        embed = discord.Embed(
            title=f"{member.name} 來到了{member.guild.name}!",
            description=f" {member.mention} 您是第本伺服器第 **{member.guild.member_count}** 個用戶，請先查看 {member.guild.rules_channel.mention} 再進行其他操作喔",
            color=discord.Colour.random(),
            timestamp=datetime.datetime.utcnow()
        )
        embed.set_thumbnail(url=member.avatar)
        embed.set_footer(text="成員加入",icon_url="https://cdn.discordapp.com/avatars/921673886049910795/5f07bb3335678e034600e94bc1515c7f.png?size=1024")

        await chnnel.send(embed=embed)

@bot.event
async def on_reaction_add(reaction : discord.Reaction,user : discord.Member):
    if reaction.message.id == 960762107966656582:
        if reaction.emoji == "👍":
            user.add_roles(roles=960443431291871252)

if __name__ == "__main__":
    with open("token","r") as f:
        bot.run(f.read())