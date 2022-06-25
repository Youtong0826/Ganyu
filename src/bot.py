import discord
import datetime 
import os
from discord.ext import commands

bot = commands.Bot(
    command_prefix='g!',
    intents=discord.Intents.all()
)

for Filename in os.listdir('src/commands'):
    if Filename.endswith(".py"):
        bot.load_extension(f"commands.{Filename[:-3]}")

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


if __name__ == "__main__":
        bot.run("OTg3NjY0MTUxNjI1MjAzNzcy.G3fUvi.csW7ExjgLaXcc_0AKK59mUsA_DJdk5CgthNbR0")