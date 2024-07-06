from core import CogExtension

from discord import (
    ApplicationContext as Context,
    Embed,
    option,
    slash_command
)

def extension_autocomplete(ctx: Context):
    return {
        "commands": [
            "fun",
            "help",
            "info",
            "manage",
            "other",
            "tool",
        ],
        "events": [
            "error",
            "interaction",
            "member",
            "message",
        ],
        "cogs": [
          "cog"  
        ]
    }[ctx.options["folder"]]

class SlashCog(CogExtension):
    @slash_command()
    @option("folder", str, choices=["commands", "events", "cogs"])
    @option("extension", str, autocomplete=extension_autocomplete, required=None)
    async def load(self, ctx: Context, folder: str, extension: str = None):
        self.bot.log(ctx)
        if ctx.author.id not in [611118369474740244, 856041155341975582]: 
            return await self.bot.dev_warn()

        if extension:
            return self.bot._load_extension(folder)

        self.bot._load_extension(folder, extension)
        
        await ctx.response.send_message(embed=Embed(
            title=f"Loaded - {folder}.{extension} - Cog",
            color=0x5cff8d
        ), ephemeral=True)
        
        self.bot.log(ctx)
        
    @slash_command()
    @option("folder", str, choices=["commands", "events", "cogs"])
    @option("extension", str, autocomplete=extension_autocomplete, required=None)
    async def unload(self, ctx: Context, folder: str, extension: str = None):
        self.bot.log(ctx)
        if ctx.author.id not in [611118369474740244, 856041155341975582]: 
            return await self.bot.dev_warn()

        if not extension:
           return self.bot._unload_extension(folder)

        self.bot._unload_extension(folder, extension)
        
        await ctx.response.send_message(embed=Embed(
            title=f"Unloaded - {folder}.{extension} - Cog",
            color=0x5cff8d
        ), ephemeral=True)
        
        self.bot.log()

    @slash_command()
    @option("folder", str, choices=["commands", "events", "cogs"])
    @option("extension", str, autocomplete=extension_autocomplete, required=None)
    async def reload(self, ctx: Context, folder: str, extension: str = None):
        self.bot.log(ctx)
        if ctx.author.id not in [611118369474740244, 856041155341975582]: 
            return await self.bot.dev_warn()

        if not extension:
            return self.bot._reload_extension(folder)

        self.bot._reload_extension(folder, extension)
        
        await ctx.response.send_message(embed=Embed(
            title=f"Reloaded - {folder}.{extension} - Cog",
            color=0x5cff8d
        ), ephemeral=True)

def setup(bot):
    bot.add_cog(SlashCog(bot))