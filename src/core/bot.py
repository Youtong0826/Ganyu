import os

from typing import (
    Any,
    Union,
)

from discord import (
    Bot, 
    ApplicationContext as Context,
    ActionRow,
    Embed,
    Colour,
    SelectMenu,
    Interaction, 
    ComponentType,
    Button as DiscordButton,
)

from discord.ui import (
    View,
    Button,
    Select
)

from lib.functions import (
    get_now_time,
    must_field_embed
)
from database import Database

class Bot(Bot):
    def __init__(self, description=None, database_path: str = None, *args, **options):
        super().__init__(description, *args, **options)
        self.__database_path = database_path
        
        self.commands_list = {
            "ganyu": must_field_embed(
                Embed(
                    title="Ganyu 指令清單",
                    description="可使用`/report`來提出建議或回報錯誤ㄛ~",
                    color=0xec8fff
                ),
                [
                    ["fun", "查看娛樂指令"],
                    ["info", "查看資訊指令"],   
                    ["manage", "查看管理員指令"],
                    ["tool", "查看小工具指令"],
                    #["music", "查看音樂功能的指令"],
                    ["other", "查看其他指令"],
                ]
            ),
            "fun": must_field_embed(
                Embed(
                    title="Fun 娛樂指令清單",
                    color=Colour.random()
                ),
                [
                    ["dice `數字` ", "讓這個機器人幫你骰骰子"],
                    ["mora","猜拳"],
                    ["luck","幸運值"],
                    ["spank","拍屁屁"]
                ]
            ),
            "info": must_field_embed(
                Embed(
                    title="Info 資訊指令清單",
                    color=Colour.random()
                ),
                [
                    ["allinfo","一次查看所有資訊!"],
                    ["userinfo `user`", "查看使用者在此伺服器的資訊"],
                    ["serinfo", "查看伺服器的資訊"],
                    ["botinfo", "查看機器人的資訊"],
                    ["invite", "獲取邀請連結"],
                    ["invites", "查看本服邀請榜"],
                    ["roleinfo `身分組`","取得身分組資訊"],
                ]
            ),
            "other": must_field_embed(
                Embed(
                    title="Other 其他指令清單",
                    color=Colour.random()
                ),
                [
                    ["ping", "查看機器人延遲"],
                    ["say `文字`", "讓這個機器人模仿你說話"],
                    ["dm `成員` `文字`" , "讓 Ganyu 私訊某人"]
                ]
            ),
            "manage": must_field_embed(
                Embed(
                    title="Mange 管理指令清單",
                    color=Colour.random()
                ),
                [
                    ["ban `成員`", "停權其他用戶"],
                    ["kick `成員`", "踢出其他用戶"],
                    ["clear `數量`", "清理訊息"],
                    ["addrole `成員` `身分組`", "新增身分組至一名用戶" ]
                ]
            ),
            "tool": must_field_embed(
                Embed(
                    title="Tool 實用小工具",
                    color=Colour.random()
                ),
                [
                    ["translate `要翻譯後的語言` `文字`","翻譯"],
                    ["embed `標題` `內容`","傳送Embed訊息"],
                    ["words `句子`","字數轉換"],
                    ["bullshit `主題` `字數`","唬爛產生器" ],
                    ["math","計算機"],
                    ["wiki `關鍵字`","搜索維基百科"]
                ]
            ),
            #"music": mustFieldEmbed(
            #    discord.Embed(
            #        title="Music 音樂功能 v1.0",
            #        color=discord.Colour.random()
            #    ),
            #    [
            #        ["play `連結 or 關鍵字`", "播放音樂"],
            #        ["pause","暫停音樂"],
            #        ["resume","取消暫停音樂"],
            #        ["skip","跳過音樂"],
            #        ["queue","查看播放清單"],
            #        ["clearqueue","清空播放清單"],
            #        ["dc","中斷連線"],
            #        ["np","查看正在播放的音樂資訊"]
            #    ]
            #)
        }
    @property
    def database(self):
        return Database(self.__database_path)
    
    
        
    def get_interaction_value(self, interaction: Interaction):
        return [data.get("components",{})[0].get("value") for data in interaction.data.get("components",{})]
    
    def get_select_value(self, interaction: Interaction, index: int = -1) -> Union[Any, list[Any]]:
        return interaction.data.get("values")[index] if index != -1 else interaction.data.get("values")
    
    def from_component(self, view: View, component: Union[ActionRow, DiscordButton, SelectMenu]):
        kwargs = component.to_dict()
        kwargs.pop('type')
        
        match component.type:
            case ComponentType.button:
                view.add_item(Button(**kwargs))
                
            case ComponentType.select:
                view.add_item(Select(**kwargs))
                
            case ComponentType.role_select:
                view.add_item(Select(select_type=ComponentType.role_select, **kwargs))
                
            case ComponentType.user_select:
                view.add_item(Select(select_type=ComponentType.user_select, **kwargs))
                
            case ComponentType.channel_select:
                view.add_item(Select(select_type=ComponentType.channel_select, **kwargs))
                
            case _:
                for c in component.children:
                    self.from_component(view, c)
                    
    def load_extension(self, folder: str, mode: str = "load", is_notice: bool = True) -> None:

        loading_method = {
            "load": super().load_extension,
            "reload": super().reload_extension,
            "unload": super().unload_extension
        }

        if is_notice:
            print(f"start {mode}ing {folder}")

        for Filename in os.listdir(f'src/{folder}'):
            if Filename.endswith(".py"):
                loading_method[mode](f"{folder}.{Filename[:-3]}")
                if is_notice:
                    print(f'-- {mode}ed "{Filename}"')

        print(f"{mode}ing {folder} end")
        
    def log(self, ctx: Context):
        print(f'[{get_now_time()}] At the guild - {ctx.author.guild}. {ctx.author} used the command - "{ctx.command}"')
        
    async def dev_warn(self, ctx: Context):
        return await ctx.response.send_message('❌ 此為開發者功能!', ephemeral=True)