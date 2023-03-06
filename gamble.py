import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
import random

class gamble(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="gamble", description="Gamble your money")
    async def gamble(self, interaction:discord.Interaction, amount:int):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        cursor.execute(f"SELECT wallet, bank FROM main WhERE user_id = {interaction.user.id}")
        bal = cursor.fetchone()

        try:
            wallet = bal[0]
            bank = bal[1]

        except:
            wallet = bal
            bank = bal
        
        if wallet < amount:
            return await interaction.response.send_message("You don't have enaugh money (brokie)")
        
        user_strikes = random.randint(1, 15)
        bot_strikes = random.randint(5, 15)

        if user_strikes > bot_strikes:
            precentage = random.randint(50, 100)
            amount_won = int(amount*(precentage/100))
            cursor.execute("UPDATE main SET wallet = ? WHERE user_id = ?", (wallet + amount_won, interaction.user.id))
            db.commit()
            embed = discord.Embed(description=f"You Won 💸{amount_won}!", color=discord.Color.green(), timestamp=interaction.created_at)
            embed.set_author(icon_url=interaction.user.display_avatar.url, name=f"{interaction.user.name} New balance")
            embed.add_field(name="Wallet", value=f"`💸{wallet + amount_won}`")
            embed.add_field(name="Bank", value=f"`💸{bank}`")
            embed.add_field(name="Networth", value=f"`💸{wallet + bank + amount_won}`")
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1138/1138038.png")
            await interaction.response.send_message(embed=embed)

        elif user_strikes < bot_strikes:
            precentage = random.randint(0, 80)
            amount_lost = int(amount*(precentage/100))
            cursor.execute("UPDATE main SET wallet = ? WHERE user_id = ?", (wallet - amount_lost, interaction.user.id))
            db.commit()
            embed = discord.Embed(description=f"You Lost 💸{amount_lost}", color=discord.Color.red(), timestamp=interaction.created_at)
            embed.set_author(icon_url=interaction.user.display_avatar.url, name=f"{interaction.user.name} New balance")
            embed.add_field(name="Wallet", value=f"`💸{wallet - amount_lost}`")
            embed.add_field(name="Bank", value=f"`💸{bank}`")
            embed.add_field(name="Networth", value=f"`💸{wallet + bank - amount_lost}`")
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1138/1138038.png")
            await interaction.response.send_message(embed=embed)

        else:
            embed = discord.Embed(description=f"You Tied", color=discord.Color.orange(), timestamp=interaction.created_at)
            embed.set_author(icon_url=interaction.user.display_avatar.url, name=f"{interaction.user.name} New balance")
            embed.add_field(name="Wallet", value=f"`💸{wallet}`")
            embed.add_field(name="Bank", value=f"`💸{bank}`")
            embed.add_field(name="Networth", value=f"`💸{wallet + bank}`")
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1138/1138038.png")
            await interaction.response.send_message(embed=embed)

        cursor.close()
        db.close()


async def setup(bot):
    await bot.add_cog(gamble(bot))