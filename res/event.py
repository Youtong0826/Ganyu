#import discord
#import datetime 
#import random
#from discord.ext import commands
#from lib.function import translate
#from core.classes import Cog_ExtenSion
#
#class Event(Cog_ExtenSion):
#    
#    @commands.Cog.listener()
#    async def on_ready(self):
#        print(">>Bot is online<<")
#        print(f"-- Watching {len(self.bot.guilds)} guilds & {len(self.bot.users)} users ")
#    
#        def guild_ids():
#            guild_ids = []
#
#            for n in self.bot.guilds:
#                guild_ids.append(n.id)
#
#            return guild_ids
#
#        activity = discord.Activity(type=discord.ActivityType.watching,name = f"g!help | {len(self.bot.guilds)} 個伺服器")
#
#        await self.bot.change_presence(status = discord.Status.streaming, activity = activity)
#
#    @commands.Cog.listener()
#    async def on_message(self,message : discord.Message):
#        if message.author == self.bot.user : return
#
#        else:
#
#            if self.bot.user in message.mentions:
#                response = random.choice(["hi","早安","找我嗎?"])
#                await message.channel.send(response)
#
#            elif ".." in message.content:
#                dots = random.choice(["...","..",".........."])
#                await message.channel.send(dots)
#
#            elif "HI" in message.content.upper():
#                await message.channel.send("hi")
#
#            elif "🤔" in message.content:
#                await message.channel.send("🤔")
#
#            elif "🛐" in message.content:
#                await message.send("🛐")
#
#            elif "👀" in message.content:
#                await message.send("👀")
#
#        await self.bot.process_commands(message)
#
#    @commands.Cog.listener()
#    async def on_command_error(self,ctx : discord.ApplicationContext, error):
#        chiness = translate(str(error), "zh-TW")
#        if chiness.endswith("。"):
#            chiness = chiness[:-1]
#
#        embed = discord.Embed(title="錯誤",description="以下為回報內容",color=discord.Color.red())
#
#        embed.add_field(name="原始內容",value=f"```{error}```",inline=False)
#
#        embed.add_field(name="翻譯後",value=f"```{chiness}```",inline=False)
#
#        embed.add_field(
#            name="應對措施",
#            value="如果Bot發生錯誤或是使用指令沒回應的話 極有可能是Bot本身的問題 如遇到此情況可使用 `g!report` 來回報給作者們 當然也可能是使用者的問題w",
#            inline=False
#        )
#
#        print(f"[{datetime.datetime.now(tz=datetime.timezone(datetime.timedelta(hours=8))).strftime('%Y/%m/%d %H:%M:%S')}] {ctx.author.name} use {ctx.command} in {ctx.author.guild} return a error:{error}")
#
#        await ctx.send(embed=embed)
#
#    @commands.Cog.listener()
#    async def on_member_join(self,member: discord.Member):
#        def join_message():
#            embed = discord.Embed(
#                title=f"{member.name} 來到了{member.guild.name}!",
#                description=f" {member.mention} 您是第本伺服器第 **{member.guild.member_count}** 個用戶，請先查看 {member.guild.rules_channel.mention} 再進行其他操作喔",
#                color=discord.Colour.random(),
#                timestamp=datetime.datetime.utcnow()
#            )
#            if member.avatar == None:
#                thunbnail = member.default_avatar
#
#            else:
#                thunbnail = member.avatar
#
#            embed.set_thumbnail(url=thunbnail)
#            embed.set_footer(
#                text="成員加入", icon_url="https://cdn.discordapp.com/avatars/921673886049910795/5f07bb3335678e034600e94bc1515c7f.png?size=1024")
#            return embed
#
#        if member.guild.id == 719198103227465738:
#            chnnel = self.bot.get_channel(719521057286914129)
#            await chnnel.send(embed=join_message())
#
#        elif member.guild.id == 956614306345123923:
#            chnnel = self.get_channel(957157665526673419)
#            await chnnel.send(embed=join_message())
#
#def setup(bot):
#    bot.add_cog(Event(bot))