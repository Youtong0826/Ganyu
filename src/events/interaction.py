import random

from discord import (
    ButtonStyle,
    Cog,
    Colour,
    ComponentType,
    Embed,
    EmbedField,
    EmbedFooter,
    Interaction
)

from discord.ui import (
    View,
    Button,
)

from lib.cog import CogExtension
from lib.role import choose_role
from lib.functions import get_now_time

class InteractionEvent(CogExtension):
    @Cog.listener()
    async def on_interaction(self,interaction:Interaction):
        if interaction.is_command(): return

        user = interaction.user
        guild = interaction.guild
        custom_id = interaction.custom_id
        components = interaction.message.components
        original = list(filter(lambda x: x.type == ComponentType.string_select, components))
        original = original[0] if original else View()
        if custom_id.endswith("ping"):
            if interaction.custom_id == "PA_ping":
                await choose_role(user, 962261741050413096)

            if interaction.custom_id == "Bu_ping":  
                await choose_role(user, 1009478887140511915)
                
            return await interaction.response.send_message(content=f"已成功變更身分組✅",ephemeral=True)
    
        if custom_id == "rpc_punch":
            result = random.choice([
                ["你輸了..", "下次再來吧!"],
                ["平手!", "勢均力敵呢!"],
                ["你贏了!!", "幹得不錯嘛!"]    
            ])

            return await interaction.response.edit_message(embed=Embed(
                title = result[0],
                description = result[1],
                color = Colour.random()
            ))
            
        if custom_id == "help_select":
            return await interaction.response.edit_message(embed=self.bot.commands_list[self.bot.get_select_value(interaction, 0)])
        
        if custom_id == "allinfo_select":
            match self.bot.get_select_value(interaction, 0):
                case "bot":
                    return await interaction.response.edit_message(**self.bot.get_bot_data(original))
                
                case "user":
                    return await interaction.response.edit_message(**self.bot.get_user_data(user, original))
                    
                case "server":
                    ...
            
        if custom_id == "userinfo_moreinfo":
            return await interaction.response.edit_message(
                embed=Embed(
                    title=f"{user.name} 的個人資訊 ",
                    color=0x9c8ff,
                    timestamp=get_now_time(),
                    thumbnail=interaction.user.avatar,
                    fields=[
                        EmbedField(**i) for i in {
                            {"name": "🖥️ 驗證", "value": f"`{"未驗證" if user.pending else "已驗證"}`"},
                            {"name": "🔱 加成的時間", "value": f"`{user.premium_since if user.premium_since else "尚未加成"}`"},
                            {"name": "⚜️ 徽章數", "value": f"`{len(user.public_flags.all())}`"},
                        }
                    ]
                ),
                view=self.bot.merge_view(View(
                    Button(
                        style = ButtonStyle.primary,
                        label="back",
                        emoji= "🔙",
                        custom_id="userinfo_back"
                    )
                ), original)
            )
        
        if custom_id == "userinfo_back":
            return await interaction.response.edit_message(**self.bot.get_user_data(interaction.user, original))
        
        if custom_id == "serverinfo_moreinfo":
            robot = len(list(filter(lambda x: x.bot, guild.members)))
            return await interaction.response.edit_message(
                embed=Embed(
                    title=guild,
                    color=Colour.random(),
                    thumbnail=guild.icon,
                    footer=EmbedFooter("serverinfo | 伺服器資訊", self.bot.icon_url),
                    fields=[
                        EmbedField(**i) for i in {
                            {"name": "⚜️ __加成次數__", "value": guild.premium_subscription_count},
                            {"name": "🔱 __加成等級__", "value": guild.premium_tier},
                            {"name": "📈 __活人__", "value": guild.member_count-robot},
                            {"name": "📊 __機器人__", "value": robot},
                            {"name": "🐷 __表情符號(靜態)__", "value": len(list(filter(lambda x: x.animated, guild.emojis)))},
                            {"name": "🐸 __表情符號(動態)__", "value": len(list(filter(lambda x: not x.animated, guild.emojis)))},
                        }
                    ]
                ), 
                view=self.bot.merge_view(View(
                    Button(
                        style=ButtonStyle.success,
                        emoji="🔙",
                        label="back",
                        custom_id="serverinfo_back"
                    ),
                    timeout=None  
                ), original)
            )
            
        if custom_id == "serverinfo_booster":
            return await interaction.response.edit_message(
                embed=Embed(
                    title=f"加成者們 [{len(guild.premium_subscribers)}]",
                    description='\n'.join(guild.premium_subscribers) if guild.premium_subscribers else "無",
                    color=Colour.random(),
                    thumbnail=guild.icon,
                    footer=EmbedFooter("serverinfo | 伺服器資訊", self.bot.icon_url),
                ), 
                view=self.bot.merge_view(View(
                    Button(
                        style=ButtonStyle.success,
                        emoji="🔙",
                        label="back",
                        custom_id="serverinfo_back"
                    ),
                    timeout=None 
                ), original)
            )
            
        if custom_id == "serverinfo_roles":
            count = 0
            roles = list(filter(lambda x: x.name != "@everyone", guild.roles))
            while sum(map(lambda x: len(x.mention)+3, roles)) >= 1014:
                count += 1
                roles.pop()

            roles = "無" if not roles else ' | '.join(map(lambda x: x.mention, roles))
            if count: roles += f" +{count} Roles..."
            
            return await interaction.response.edit_message(
                embed=Embed(
                    title=f"身分組 [{len(guild.roles)-1}]",
                    description=roles,
                    color=Colour.random(),
                    thumbnail=guild.icon,
                    footer=EmbedFooter("serverinfo | 伺服器資訊", self.bot.icon_url),
                ), 
                view=self.bot.merge_view(View(
                    Button(
                        style=ButtonStyle.success,
                        emoji="🔙",
                        label="back",
                        custom_id="serverinfo_back"
                    ),
                    timeout=None 
                ), original)
            )
            
        if custom_id == "serverinfo_back":
            return await interaction.response.edit_message(**self.bot.get_guild_data(interaction.user, original))
        
        if custom_id.startswith("roleinfo_owner"):
            role = list(filter(lambda x: x.id == int(custom_id.split('_')[2]), guild.roles))[0]
            count = 0
            while sum(map(lambda x: len(x.mention)+3, role.members)) >= 1010:
                count += 1
                role.members.pop()
                
            members = "無" if not role.members else ' | '.join(map(lambda x: x.mention, role.members))
            if count: members += f" +{count} Members..."

            return await interaction.response.edit_message(
                embed=Embed(
                    title=f"擁有此身分組的人",
                    description=members,
                    color=Colour.random()
                ), 
                view=View(
                    Button(
                        style=ButtonStyle.primary,
                        label="回去",
                        emoji="🔙",
                        custom_id=f"roleinfo_back_{role.id}"
                    ),
                    timeout=None
                )
            )  
            
        if custom_id.startswith("roleinfo_back"):
            role = list(filter(lambda x: x.id == int(custom_id.split('_')[2]), guild.roles))[0]
            return await interaction.response.edit_message(
                embed=Embed(
                    title=f'有關 {role.name} 身分組的資訊',
                    color=role.color,
                    timestamp=get_now_time(),
                    fields=[
                        EmbedField(**i) for i in {
                            {"name": "🗒️ 名字", "value": role.mention},
                            {"name": "💳 id", "value": role.id},
                            {"name": "📊 人數", "value": len(role.members)},
                            {"name": "🗓️ 創建時間", "value": role.created_at.strftime('%Y/%m/%d')},
                            {"name": "👾 貼圖", "value": role.unicode_emoji if role.unicode_emoji else None},
                        }
                    ]
                ),
                view=View(
                    Button(
                        style=ButtonStyle.success,
                        label="擁有者",
                        emoji="📊",
                        custom_id=f"roleinfo_owner_{role.id}"
                    ),
                    timeout=None
                )
            )
        
def setup(bot):
    bot.add_cog(InteractionEvent(bot))
