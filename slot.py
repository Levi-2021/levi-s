import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
import random

class slot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="slot", description="Slot your money")
    async def slot(self, interaction:discord.Interaction, amount:int):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT wallet, bank FROM main WhERE user_id = {interaction.user.id}")
        bal = cursor.fetchone()

        try:
            wallet = bal[0]

        except:
            wallet = 0 

        if wallet < amount:
            return await interaction.response.send_message("You don't have enaugh money in your wallet")
        
        times_factors = random.randint(1, 5)
        earing = int(amount*times_factors)

        final = []
        for i in range(3):
            a = random.choice(["🍉", "💎", "💰"])
            final.append(a)
        if final[0] == final[1] or final[0] == final[2] or final[2] == final[0]:
            cursor.execute("UPDATE main SET wallet = ? WHERE user_id = ?", (wallet + earing, interaction.user.id))
            db.commit()
            embed = discord.Embed(title=f"Slot Machine", color=discord.Color.green(), timestamp=interaction.created_at)
            embed.add_field(name=f"You Won 💸{earing}", value=f"{final}")
            embed.add_field(name="----------------------------------", value=f"**Multiplier** X {times_factors}", inline=False)
            embed.add_field(name="----------------------------------", value=f"**New Balance** 💸{wallet + earing} ", inline=False)
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1055/1055823.png")
            await interaction.response.send_message(embed=embed)

        else:
            cursor.execute("UPDATE main SET wallet = ? WHERE user_id = ?", (wallet - earing, interaction.user.id))
            db.commit()
            embed = discord.Embed(title=f"Slot Machine", color=discord.Color.red(), timestamp=interaction.created_at)
            embed.add_field(name=f"You Lost 💸{earing}", value=f"{final}")
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1055/1055823.png")
            await interaction.response.send_message(embed=embed)

            cursor.close()
            db.close()


async def setup(bot):
    await bot.add_cog(slot(bot))