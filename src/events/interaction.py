from discord import (
    Cog,
    Colour,
    Embed,
    EmbedField,
    Interaction
)
import random

from lib.cog import CogExtension
from lib.role import choose_role

class InteractionEvent(CogExtension):
    @Cog.listener()
    async def on_interaction(self,interaction:Interaction):
        if interaction.is_command(): return

        custom_id = interaction.custom_id
        if custom_id.endswith("ping"):
            if interaction.custom_id == "PA_ping":
                await choose_role(interaction.user, 962261741050413096)

            if interaction.custom_id == "Bu_ping":  
                await choose_role(interaction.user, 1009478887140511915)
                
            return await interaction.response.send_message(content=f"已成功變更身分組✅",ephemeral=True)
    
        if custom_id == "rpc_punch":
            result = random.choice([
                ["你輸了..", "下次再來吧!"],
                ["平手!", "勢均力敵呢!"],
                ["你贏了!!", "幹得不錯嘛!"]    
            ])

            await interaction.response.edit_message(embed=Embed(
                title = result[0],
                description = result[1],
                color = Colour.random()
            ))
        

def setup(bot):
    bot.add_cog(InteractionEvent(bot))
