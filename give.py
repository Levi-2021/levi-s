import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
import random

class give(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="give", description="Give someone your money")
    @app_commands.describe(member="Member you want to give money")
    async def give(self, interaction:discord.Interaction, member:discord.Member, amount:int):

        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        cursor.execute(f"SELECT bank FROM main WhERE user_id = {member.id}")
        bal = cursor.fetchone()

        memberbank = bal[0]

        cursor.execute(f"SELECT wallet, bank FROM main WHERE user_id = {interaction.user.id}")
        bal = cursor.fetchone()

        userwallet = bal[0]
        userbank = bal[1]

        if userwallet < amount:
            await interaction.response.send_message(f"{interaction.user.mention} you don't have that much money in your wallet")
            cursor.close()
            db.close()
            return

        cursor.execute("UPDATE main SET wallet = ? WHERE user_id = ?", (userwallet - amount, interaction.user.id))
        cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (memberbank + amount, member.id))
        
        embed = discord.Embed(description=f"Succfully gave 💸{amount} to {member.display_name}!",color=discord.Color.blue(), timestamp=interaction.created_at)
        embed.set_author(icon_url=interaction.user.display_avatar.url, name=f"{interaction.user.name} New balance")
        embed.add_field(name="Wallet", value=f"`💸{userwallet - amount}`")
        embed.add_field(name="Bank", value=f"`💸{userbank}`")
        embed.add_field(name="Networth", value=f"`💸{userwallet + userbank - amount}`")
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1138/1138038.png")
        await interaction.response.send_message(embed=embed)
        db.commit()
        cursor.close()
        db.close()

async def setup(bot):
    await bot.add_cog(give(bot))