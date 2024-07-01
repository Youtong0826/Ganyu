from lib.cog import CogExtension

from discord import (
    ApplicationContext as Context,
    Embed,
    slash_command
)

class SlashCogs(CogExtension):
    @slash_command()
    async def load(self, ctx: Context, folder: str, extension=None):
        self.bot.log(ctx)
        if ctx.author.id not in [611118369474740244, 856041155341975582]: 
            return await self.bot.dev_warn()

        if not extension:
            self.bot.load_extension(folder)

        self.bot.load_extension(f"{folder}.{extension}")
        
        await ctx.send(embed=Embed(
            title=f"Loaded - {folder}.{extension} - Cog",
            color=0x5cff8d
        ))
        
        self.bot.log(ctx)
        
    @slash_command()
    async def unload(self, ctx: Context, folder: str, extension=None):
        self.bot.log(ctx)
        if ctx.author.id not in [611118369474740244, 856041155341975582]: 
            return await self.bot.dev_warn()

        if not extension:
           self.bot.load_extension(folder, "unload")

        self.bot.unload_extension(f"{folder}.{extension}")
        
        await ctx.send(embed=Embed(
            title=f"Unloaded - {folder}.{extension} - Cog",
            color=0x5cff8d
        ))
        
        self.bot.log()

    @slash_command()
    async def reload(self, ctx: Context, folder: str, extension=None):
        self.bot.log(ctx)
        if ctx.author.id not in [611118369474740244, 856041155341975582]: 
            return await self.bot.dev_warn()

        if not extension:
            self.bot.load_extension(folder, "reload")

        self.bot.reload_extension(f"{folder}.{extension}")
        
        await ctx.send(embed=Embed(
            title=f"Reloaded - {folder}.{extension} - Cog",
            color=0x5cff8d
        ))

def setup(bot):
    bot.add_cog(SlashCogs(bot))