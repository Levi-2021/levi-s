import discord
from discord.ext import commands
from discord import app_commands


class role_info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @app_commands.command(name="role-info", description="Information about the role")
    async def role_info(self, interaction: discord.Interaction, role: discord.Role):
        color = role.color
        if role.hoist == True:
            hoist = "Yes"
        if role.hoist == False:
            hoist = "No"
        if role.managed == True:
            managed = "Yes"
        if role.managed == False:
            managed = "No"
        if role.mentionable == True:
            mentionable = "Yes"
        if role.mentionable == False:
            mentionable = "No"

        embed = discord.Embed(
            title=f"{role}", color=color, timestamp=interaction.created_at)
        embed.add_field(name="ID:", value=role.id, inline=True)
        embed.add_field(name="Hoisted?", value=hoist, inline=True)
        embed.add_field(name="Position:", value=role.position, inline=True)
        embed.add_field(name="Color:", value=role.color, inline=True)
        embed.add_field(name="Mention:", value=f"`<@&{role.id}>`", inline=True)
        embed.add_field(name="Managed?", value=managed, inline=True)
        embed.add_field(name="Mentionable?", value=mentionable, inline=True)

        await interaction.response.send_message(embed=embed)
        return
    
async def setup(bot):
    await bot.add_cog(role_info(bot))