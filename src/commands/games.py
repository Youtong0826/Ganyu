import random , discord 
from discord.ext import commands
from core.classes import Cog_ExtenSion

"""
game commands list
g!number - 猜數字遊戲
"""

GameData = []

def checkUserGame(member:discord.member):
    for i in GameData:
        if i.player == member:
            return True
        else:
            return False

def getUserGame(member:discord.member):
    for i in GameData:
        if i.player == member:
            return i
        else:
            return None

class numberGame():
    def __init__(self,player):
        self.player = player
        self.number = random.randint(1,100)
        
    async def start(self,ctx):
        await ctx.send(
            discord.Embed(
                title = "猜數字",
                description = f"遊戲開始，請從1~100中猜數字吧",
            )
        )

    async def checkNumber(self,ctx,number):
        await ctx.send(
            discord.Embed(
                title = "猜數字",
                description = f"遊戲開始，請從1~100中猜數字吧",
            )
        )


class Games(Cog_ExtenSion):
    @commands.command()
    async def game(self,ctx):
        check = checkUserGame(ctx.author)
        if not check:
            GameData.append(numberGame(ctx.author))
            game = getUserGame(ctx.author)
            game.start(ctx)

def setup(bot):
    bot.add_cog(Games(bot))
