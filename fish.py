import sqlite3
import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
import random

class fish(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="fish", description="Fish for fishes")
    async def hunt(self, interaction:discord.Interaction):
        animal_list = [None,"🐟 Normal Fish", "🐠 Tropical Fish", " 🍥 Fish Cake", "🐡 Blowfish"]
                
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        cursor.execute(f"SELECT * FROM fish WHERE user_id = {interaction.user.id}")
        animals = cursor.fetchone()

        cursor.execute(f"SELECT rod FROM tools WHERE user_id = {interaction.user.id}")
        rod = cursor.fetchone()

        amount = random.randint(1,10)
        hunt = random.choice(animal_list)

        if rod[0] > 0:
            if hunt == animal_list[1]:
                cursor.execute("UPDATE fish SET normal_fish = ? WHERE user_id = ?", (animals[1] + amount, interaction.user.id))
            if hunt == animal_list[2]:
                cursor.execute("UPDATE fish SET tropical_fish = ? WHERE user_id = ?", (animals[2] + amount, interaction.user.id))
            if hunt == animal_list[3]:
                cursor.execute("UPDATE fish SET fish_cake = ? WHERE user_id = ?", (animals[3] + amount, interaction.user.id))
            if hunt == animal_list[4]:
                cursor.execute("UPDATE fish SET blowfish = ? WHERE user_id = ?", (animals[4] + amount, interaction.user.id))
            if hunt == animal_list[0]:
                cursor.execute("UPDATE tools SET rod = ? WHERE user_id = ?", (rod[0] - 1, interaction.user.id))
                embed = discord.Embed(title="You got nothing :(", color=discord.Color.red())
                await interaction.response.send_message(embed=embed)
                return
            
            cursor.execute(f"UPDATE tools SET rod = ? WHERE user_id = ?", (rod[0] - 1, interaction.user.id))
            embed = discord.Embed(title=f"You got x{amount} {hunt}", color=discord.Color.green())
            await interaction.response.send_message(embed=embed)

        else:

            await interaction.response.send_message("You don't have any rods, you can buy them in the store")

        db.commit()
        cursor.close()
        db.close()


async def setup(bot):
    await bot.add_cog(fish(bot))