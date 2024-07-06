import os

from typing import (
    Any,
    Union,
)

from discord import (
    ApplicationContext as Context,
    ActionRow,
    Bot,
    ButtonStyle,
    Button as DiscordButton,
    Colour,
    ComponentType,
    Embed,
    EmbedField,
    EmbedFooter,
    EmbedMedia,
    Guild,
    Interaction,
    Member,
    User, 
    SelectMenu,
)

from discord.ui import (
    View,
    Button,
    Select
)

from lib.embed import must_field_embed
from lib.timing import get_now_time
from database import Database

class Bot(Bot):
    def __init__(self, description=None, database_path: str = None, *args, **options):
        super().__init__(description, *args, **options)
        self.__database_path = database_path
        
        self.commands_list = {
            "ganyu": must_field_embed(
                Embed(
                    title="Ganyu 指令清單",
                    description="可使用 `/report` 來提出建議或回報錯誤ㄛ~",
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
                    ["/dice", "骰骰子"],
                    ["/rps","剪刀石頭布"],
                    ["/luck","幸運值"],
                    ["/spank","拍屁屁"]
                ]
            ),
            "info": must_field_embed(
                Embed(
                    title="Info 資訊指令清單",
                    color=Colour.random()
                ),
                [
                    ["/allinfo","一次查看所有資訊!"],
                    ["/userinfo `用戶`", "查看使用者在此伺服器的資訊"],
                    ["/serinfo", "查看伺服器的資訊"],
                    ["/botinfo", "查看機器人的資訊"],
                    ["/invite", "獲取邀請連結"],
                    ["/invites", "查看本服邀請榜"],
                    ["/roleinfo `身分組`","取得身分組資訊"],
                ]
            ),
            "other": must_field_embed(
                Embed(
                    title="Other 其他指令清單",
                    color=Colour.random()
                ),
                [
                    ["/ping", "查看機器人延遲"],
                    ["/say `文字`", "讓這個機器人模仿你說話"],
                ]
            ),
            "manage": must_field_embed(
                Embed(
                    title="Mange 管理指令清單",
                    color=Colour.random()
                ),
                [
                    ["/ban `成員`", "停權其他用戶"],
                    ["/kick `成員`", "踢出其他用戶"],
                    ["/clear `數量`", "清理訊息"],
                    ["/addrole `成員` `身分組`", "新增身分組至一名用戶" ]
                ]
            ),
            "tool": must_field_embed(
                Embed(
                    title="Tool 實用小工具",
                    color=Colour.random()
                ),
                [
                    ["/translate `語言` `文字`","翻譯"],
                    ["/embed `標題` `內容`","傳送Embed訊息"],
                    ["/words `句子`","字數轉換"],
                    ["/bullshit `主題` `字數`","唬爛產生器" ],
                    ["/math `算式`","計算機"],
                    ["/wiki `關鍵字`","搜索維基百科"]
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
        
        self.icon_url = "https://cdn.discordapp.com/avatars/921673886049910795/5f07bb3335678e034600e94bc1515c7f.png?size=256"
        self.id = 921673886049910795
    
    @property
    def database(self):
        return Database(self.__database_path)
      
    @property
    def mention(self) -> str:
        return f"<@{self.id}>"
      
    def get_bot_data(self, original: View = None) -> dict[str, Embed | View]:            
        if not original: original = View()
        return {
            "embed": Embed(
                title=f"{self.user}",
                color=0x9c8ff,
                timestamp=get_now_time(),
                fields=[
                    EmbedField(**i) for i in [
                        {"name": "📆 創建時間", "value": "`2022/1/21(GMT+8:00)`", "inline": False},
                        {"name": "📜 ID", "value": "`921673886049910795`", "inline": False},
                        {"name": "🌐 伺服器", "value": f"`{len(self.guilds)}`", "inline": True},
                        {"name": "📊 用戶", "value": f"`{len(self.users)}`","inline": True},
                        {"name": "💫 Ping", "value": f"`{round(self.latency * 1000)} ms`", "inline": True}
                    ]       
                ],
                footer=EmbedFooter("made by Ganyu-Bot-Devs", self.icon_url)
            ), 
            "view": self.merge_view(View(
                Button(
                    style=ButtonStyle.primary,
                    label="Invite me!",
                    emoji="🔗",
                    url="https://ptb.discord.com/api/oauth2/authorize?client_id=921673886049910795&permissions=380108955712&scope=bot%20applications.commands"
                ),
                Button(
                    label="Support Server",
                    emoji="❓",
                    url="https://discord.gg/AVCWGuuUex"
                ),
                timeout=None
            ), original) 
        }
        
    def get_user_data(self, user: Union[Member, User], original: View = None) -> dict[str, Embed | View]:
        count = 0
        roles = list(filter(lambda x: x.name != "@everyone", user.roles))
        while sum(map(lambda x: len(x.mention)+3, roles)) >= 1014:
            count += 1
            roles.pop()
            
        roles = "無" if not roles else ' | '.join(map(lambda x: x.mention, roles))
        
        if count: roles += f" +{count} Roles..."
        
        if not original: original = View()
        
        return {
            "embed": Embed(
                title=f"{user.name} 的個人資訊 ",
                color=0x9c8ff,
                timestamp=get_now_time(),
                fields=[
                    EmbedField(**i) for i in [
                        {"name": "🐬 暱稱", "value": f"`{user.nick if user.nick else "無"}`"},
                        {"name": "🤖 Bot", "value": f"`{"yes" if user.bot else "no"}`"},
                        {"name": "💳 ID", "value": f"`{user.id}`"},
                        {"name": "📆 創建時間", "value": f"`{user.created_at.strftime('%Y/%m/%d')}`"},
                        {"name": "📆 加入時間", "value": f"`{user.joined_at.strftime('%Y/%m/%d')}`"},
                        {"name": f"📰 身分組[{len(user.roles)-1}]:", "value": roles}
                    ]       
                ],
                footer=EmbedFooter("userinfo | 用戶資訊", self.icon_url)
            ), 
            "view": original
        }
    
    def get_guild_data(self, guild: Guild, original: View = None): 
        if not original: original = View()
        return {
            "embed": Embed(
                title=guild.name,
                color=0x9c8fff,
                timestamp=get_now_time(),
                thumbnail=EmbedMedia(guild.icon.url) ,
                footer=EmbedFooter("serverinfo | 伺服器資訊", self.icon_url),
                fields=[
                    EmbedField(**i) for i in [
                        {"name": "🚹 __服主__", "value": f"`{guild.owner.mention}`"},
                        {"name": "💳 __ID__", "value": f"`{guild.id}`"},
                        {"name": "🗓️ __創建時間__", "value": f"`{guild.created_at.strftime('%Y/%m/%d')}`"},
                        {"name": "📈 __人數__", "value": f"`{guild.member_count}`"},
                        {"name": "📊 __頻道數__" , "value": f"`{len(guild.channels)}`"},
                        {"name": "👾 __表情符號__", "value": f"`{len(guild.emojis)}`"},
                        {"name": "📌 __身分組__", "value": f"`{len(guild.roles)}`"},
                    ]
                ]
            ),
            "view": self.merge_view(View(
                Button(
                    style=ButtonStyle.primary,
                    emoji="📘",
                    label="更多資訊!",
                    custom_id="serverinfo_moreinfo"
                ),      
                Button(
                    style=ButtonStyle.success,
                    emoji="📖",
                    label="加成者",
                    custom_id="serverinfo_booster"
                ),
                Button(
                    style=ButtonStyle.primary,
                    emoji="📋",
                    label="身分組",
                    custom_id="serverinfo_roles"
                )
            ), original)
        }
    
    def get_interaction_value(self, interaction: Interaction):
        return [data.get("components",{})[0].get("value") for data in interaction.data.get("components",{})]
    
    def get_select_value(self, interaction: Interaction, index: int = -1) -> Union[Any, list[Any]]:
        return interaction.data.get("values")[index] if index != -1 else interaction.data.get("values")
    
    def from_component(self, component: Union[ActionRow, DiscordButton, SelectMenu], custom_id: str = None, view: View = None) -> View:      
        if not view:
            view = View(timeout=None)
            
        if custom_id:
            try:
                component = list(filter(lambda x: x.custom_id == custom_id, component.children))[0]
                
            except:
                return None
        
        match component.type:
            case ComponentType.button:
                view.add_item(Button.from_component(component))
                
            case ComponentType.select:
                view.add_item(Select.from_component(component))
                
            case ComponentType.role_select:
                view.add_item(Select.from_component(component))
                
            case ComponentType.user_select:
                view.add_item(Select.from_component(component))
                
            case ComponentType.channel_select:
                view.add_item(Select.from_component(component))
                
            case _:
                for c in component.children:
                    self.from_component(view, c)
                    
        return view
             
    def merge_view(self, *views: View) -> View:
        childrens = []
        for i in views:
            childrens += i.children
            
        return View(*childrens)        
           
    def _load_extension(self, folder: str = None, extension: str = None, is_notice: bool = True) -> None:
        if extension:
            return self.load_extension(f"{folder}.{extension}")
        
        if is_notice:
            print(f"start loading {folder}")
            
        for Filename in os.listdir(f'src/{folder}'):
            if Filename.endswith(".py"):
                self.load_extension(f"{folder}.{Filename[:-3]}")
                if is_notice:
                    print(f'-- loaded "{Filename}"')

        print(f"loading {folder} end")
        
    def _unload_extension(self, folder: str = None, extension: str = None, is_notice: bool = True) -> None:
        if extension:
            return self.unload_extension(f"{folder}.{extension}")
        
        if is_notice:
            print(f"start unloading {folder}")
            
        for Filename in os.listdir(f'src/{folder}'):
            if Filename.endswith(".py"):
                self.unload_extension(f"{folder}.{Filename[:-3]}")
                if is_notice:
                    print(f'-- unloaded "{Filename}"')

        print(f"unloading {folder} end")
        
    def _reload_extension(self, folder: str = None, extension: str = None, is_notice: bool = True) -> None:
        if extension:
            return self.reload_extension(f"{folder}.{extension}")
        
        if is_notice:
            print(f"start reloading {folder}")
            
        for Filename in os.listdir(f'src/{folder}'):
            if Filename.endswith(".py"):
                self.reload_extension(f"{folder}.{Filename[:-3]}")
                if is_notice:
                    print(f'-- reloaded "{Filename}"')

        print(f"reloading {folder} end")  
    
    def log(self, ctx: Context):
        print(f'[{get_now_time().strftime("%Y/%m/%d %H:%M:%S")}] At the guild - {ctx.author.guild}. {ctx.author} used the command - "{ctx.command}"')
        
    def error(self, ctx: Context, error: Exception):
        print(f'[{get_now_time().strftime("%Y/%m/%d %H:%M:%S")}] At the guild - {ctx.author.guild}. When {ctx.author} used the command - "{ctx.command}", return a error:{error}')
    
    async def dev_warn(self, ctx: Context):
        return await ctx.response.send_message('❌ 此為開發者功能!', ephemeral=True)