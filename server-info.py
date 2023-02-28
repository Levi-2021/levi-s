import discord
from discord.ext import commands
from discord import app_commands


class server_info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="server-info", description="Shows the info about the server")
    async def serverinfo(self, interaction: discord.Interaction):
        roles = [role for role in interaction.guild.roles]
        guild = interaction.guild
        total = len(interaction.guild.text_channels) + \
                len(interaction.guild.voice_channels)
            
        try:
            embed = discord.Embed(timestamp=interaction.created_at,
                                colour=discord.Color.blue())
            embed.set_thumbnail(url=interaction.guild.icon.url)
            embed.set_author(name=f"Server Info - {interaction.guild.name}")
            embed.add_field(name=f"Roles", value=f"{len(roles)}", inline=True)
            embed.add_field(name="Server name", value=f"{guild.name}", inline=True)
            embed.add_field(name="Voice channels", value=len(
                interaction.guild.voice_channels), inline=True)
            embed.add_field(name="Server created", value=interaction.guild.created_at.strftime(
                "%a,%#d %B %Y, %I:%M %p UTC"), inline=True)
            embed.add_field(name="Text channels", value=len(
                interaction.guild.text_channels), inline=True)
            embed.add_field(name="Member count",
                            value=f"{guild.member_count}", inline=True)
            embed.add_field(name="Categorys", value=len(
                interaction.guild.categories), inline=True)
            embed.add_field(name="Total channels", value=(total), inline=True)

            await interaction.response.send_message(embed=embed)
            return

        except:
            embed = discord.Embed(timestamp=interaction.created_at,
                                colour=discord.Color.blue())
            embed.set_author(name=f"Server Info - {interaction.guild.name}")
            embed.add_field(name=f"Roles", value=f"{len(roles)}", inline=True)
            embed.add_field(name="Server name", value=f"{guild.name}", inline=True)
            embed.add_field(name="Voice channels", value=len(
                interaction.guild.voice_channels), inline=True)
            embed.add_field(name="Server created", value=interaction.guild.created_at.strftime(
                "%a,%#d %B %Y, %I:%M %p UTC"), inline=True)
            embed.add_field(name="Text channels", value=len(
                interaction.guild.text_channels), inline=True)
            embed.add_field(name="Member count",
                            value=f"{guild.member_count}", inline=True)
            embed.add_field(name="Categorys", value=len(
                interaction.guild.categories), inline=True)
            embed.add_field(name="Total channels", value=(total), inline=True)

            await interaction.response.send_message(embed=embed)
            return


async def setup(bot):
    await bot.add_cog(server_info(bot))