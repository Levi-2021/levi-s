import discord
from discord.ext import commands
from discord import app_commands


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="ping", description="Shows the latency of the bot")
    async def ping(self, interaction: discord.Interaction):
        latency = round(self.bot.latency * 1000, 1)
        embed = discord.Embed(title="", color=discord.Color.blue(),
                            timestamp=interaction.created_at)
        embed.add_field(name="Pong! 🏓", value=f"`{latency} ms`", inline=True)

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(ping(bot))