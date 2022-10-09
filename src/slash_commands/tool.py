from lib.function import translate, SendBGM, bullshit, calculator
from lib.bot_config import bot_icon_url 
from core.classes import CogExtension
from command_lib import tool
import discord

class SlashTool(CogExtension):
    @discord.message_command(name="translate")
    async def tr(self,ctx,text:discord.Message):
        await tool.translate(ctx,text=text.content)

    @discord.application_command(description="翻譯功能")
    async def translate(self,ctx,language : discord.Option(str,"選擇要翻譯成的語言",choices=["繁中","簡中","英語","日語","印尼語"]),*,text=None):
        await tool.translate(ctx,language=language,text=text)

    @discord.application_command(description="字數轉換器")
    async def words(self,ctx: discord.ApplicationContext,*,text : discord.Option(str,"輸入您要轉換的句子")):
        await tool.words(ctx,text)

    @discord.application_command(description="唬爛產生器")
    async def bullshit(self,ctx:discord.ApplicationContext,topic:discord.Option(str,"主題")=None,minlen:discord.Option(int,"字數(上限1000)")=None):
        await tool.bullshit(ctx,topic,minlen)

    @discord.application_command(description="計算機")
    async def math(self,ctx:discord.ApplicationContext,formula:discord.Option(str,"算式")=None):
        await tool.math(ctx,formula)

    @discord.application_command(description="搜索維基百科")
    async def wiki(self,ctx,keywords:discord.Option(str,"搜索關鍵字")):
        await tool.wikiInfo(ctx,keywords,self.bot)

def setup(bot):
    bot.add_cog(SlashTool(bot))