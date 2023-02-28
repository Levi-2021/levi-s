import discord
from discord.ext import commands
from discord import app_commands
import numpy

class check_perms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @app_commands.command(name="check-role-perms", description="Check which permissions the role has")
    async def role_perms(self, interaction: discord.Interaction, role: discord.Role):
        perm_list = [perm[0] for perm in role.permissions if perm[1]]
        np_list = numpy.array(perm_list)
        color = role.color

        embed = discord.Embed(title=role.name, color=color,
                            timestamp=interaction.created_at)
        embed.add_field(name="Role has permissions to:",
                        value=np_list, inline=True)

        await interaction.response.send_message(embed=embed)


    @app_commands.command(name="check-user-perms", description="Check which permissions the user has")
    async def user_perms(self, interaction: discord.Interaction, member: discord.Member):
        perm_list = [perm[0] for perm in member.guild_permissions if perm[1]]
        np_list = numpy.array(perm_list)

        embed = discord.Embed(
            title=member.name, color=discord.Color.blue(), timestamp=interaction.created_at)
        embed.add_field(name="Member has permissions to:",
                        value=np_list, inline=True)

        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(check_perms(bot))