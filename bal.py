import discord
from discord.ext import commands
from discord import app_commands
import sqlite3

class balance(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="balance", description="Check someones balance")
    async def bal(self, interaction:discord.Interaction, member:discord.Member = None):
        if member is None:
            member = interaction.user

        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        cursor.execute(f"SELECT wallet, bank FROM main WHERE user_id = {member.id}")
        bal = cursor.fetchone()
        try:
            wallet = bal[0]
            bank = bal[1]

        except:
            wallet = 0 
            bank = 0

        embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
        embed.set_author(icon_url=member.display_avatar.url, name=f"{member.name} Bank account")
        embed.add_field(name="Wallet", value=f"`💸{wallet}`")
        embed.add_field(name="Bank", value=f"`💸{bank}`")
        embed.add_field(name="Networth", value=f"`💸{wallet + bank}`")
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1138/1138038.png")
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(balance(bot))