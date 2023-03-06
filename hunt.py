import sqlite3
import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
import random

class hunt(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="hunt", description="Hunt for animals")
    async def hunt(self, interaction:discord.Interaction):
        animal_list = [None,"🦊 Fox", "🐺 Wolf", "🐱 Cat", "🦝 Raccoon", "🐯 Tiger", "🦁 Lion", "🐆 Leopard","🦌 Deer", "🦓 Zebra", "🦄 Unicorn"]
                
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        cursor.execute(f"SELECT * FROM animals WHERE user_id = {interaction.user.id}")
        animals = cursor.fetchone()

        cursor.execute(f"SELECT pistol FROM tools WHERE user_id = {interaction.user.id}")
        pistol = cursor.fetchone()

        amount = random.randint(1,10)
        hunt = random.choice(animal_list)

        if pistol[0] > 0:
            if hunt == animal_list[1]:
                cursor.execute("UPDATE animals SET fox = ? WHERE user_id = ?", (animals[1] + amount, interaction.user.id))
            if hunt == animal_list[2]:
                cursor.execute("UPDATE animals SET wolf = ? WHERE user_id = ?", (animals[2] + amount, interaction.user.id))
            if hunt == animal_list[3]:
                cursor.execute("UPDATE animals SET cat = ? WHERE user_id = ?", (animals[3] + amount, interaction.user.id))
            if hunt == animal_list[4]:
                cursor.execute("UPDATE animals SET raccoon = ? WHERE user_id = ?", (animals[4] + amount, interaction.user.id))
            if hunt == animal_list[5]:
                cursor.execute("UPDATE animals SET tiger = ? WHERE user_id = ?", (animals[5] + amount, interaction.user.id))
            if hunt == animal_list[6]:
                cursor.execute("UPDATE animals SET Lion = ? WHERE user_id = ?", (animals[6] + amount, interaction.user.id))
            if hunt == animal_list[7]:
                cursor.execute("UPDATE animals SET leopard = ? WHERE user_id = ?", (animals[7] + amount, interaction.user.id))
            if hunt == animal_list[8]:
                cursor.execute("UPDATE animals SET deer = ? WHERE user_id = ?", (animals[8] + amount, interaction.user.id))
            if hunt == animal_list[9]:
                cursor.execute("UPDATE animals SET zebra = ? WHERE user_id = ?", (animals[9] + amount, interaction.user.id))
            if hunt == animal_list[10]:
                cursor.execute("UPDATE animals SET unicorn = ? WHERE user_id = ?", (animals[10] + amount, interaction.user.id))
            if hunt == animal_list[0]:
                cursor.execute("UPDATE tools SET pistol ? WHERE user_id = ?", (pistol[0] - 1, interaction.user.id))
                embed = discord.Embed(title="You got nothing :(", color=discord.Color.red())
                await interaction.response.send_message(embed=embed)
                return
            
            cursor.execute(f"UPDATE tools SET pistol = ? WHERE user_id = ?", (pistol[0] - 1, interaction.user.id))
            embed = discord.Embed(title=f"You got x{amount} {hunt}", color=discord.Color.green())
            await interaction.response.send_message(embed=embed)

        else:

            await interaction.response.send_message("You don't have any pistols, you can buy them in the store")

        db.commit()
        cursor.close()
        db.close()


async def setup(bot):
    await bot.add_cog(hunt(bot))