from core.classes import CogExtension
from discord.ext import commands
import discord

class InteractionEvent(CogExtension):

    @commands.Cog.listener()
    async def on_interaction(self,interaction:discord.Interaction):
        if interaction.is_command():return

        if interaction.custom_id.endswith("ping"):
            roles = interaction.user.guild.roles
            if interaction.custom_id == "PA_ping":
                for role in roles :
                    if role.id == 962261741050413096:
                        if role in interaction.user.roles:
                            await interaction.user.remove_roles(role)
                            await interaction.response.send_message(content=f"已成功移除身分組✅",ephemeral=True)

                        else:
                            await interaction.user.add_roles(role)
                            await interaction.response.send_message(content=f"已成功領取身分組✅",ephemeral=True)

            if interaction.custom_id == "Bu_ping":  
                for role in roles :
                    if role.id == 1009478887140511915:
                        if role in interaction.user.roles:
                            await interaction.user.remove_roles(role)
                            await interaction.response.send_message(content=f"已成功移除身分組✅",ephemeral=True)

                        else:
                            await interaction.user.add_roles(role)
                            await interaction.response.send_message(content=f"已成功領取身分組✅",ephemeral=True)

def setup(bot):
    bot.add_cog(InteractionEvent(bot))
