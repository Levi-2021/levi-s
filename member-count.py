import discord
from discord.ext import commands
from discord import app_commands


class member_count(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="member-count", description="Shows the membercount of the server")
    async def member_count(self, interaction: discord.Interaction):
        membercount = interaction.guild.member_count

        embed = discord.Embed(title=f'{membercount} members in "{interaction.guild.name}"',
                            colour=discord.Color.blue())
        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(member_count(bot))