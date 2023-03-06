import discord
from discord.ext import commands
from discord import app_commands
import sqlite3

class withdraw(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="withdraw", description="Withdraw your money")
    async def withdraw(self, interaction:discord.Interaction, amount:int):

        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM main WhERE user_id = {interaction.user.id}")
        data = cursor.fetchone()

        try:
            wallet = data[1]
            bank  = data[2]
        except:
            await interaction.response.send_message("There was an error")
        
        if amount == "all":
            amount = bank

        if bank < amount:
            return await interaction.response.send_message("You do not have that much money")
        
        else:
            cursor.execute("UPDATE main SET wallet = ? WHERE user_id = ?", (wallet + amount, interaction.user.id))
            cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank - amount, interaction.user.id))
        

            embed = discord.Embed(description=f"Successfully withdraw 💸{amount}", color=discord.Color.blue(), timestamp=interaction.created_at)
            embed.set_author(icon_url=interaction.user.display_avatar.url, name=f"{interaction.user.name} Bank account")
            embed.add_field(name="Wallet", value=f"`💸{wallet + amount}`")
            embed.add_field(name="Bank", value=f"`💸{bank - amount}`")
            embed.add_field(name="Networth", value=f"`💸{wallet + bank}`")
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1138/1138038.png")

            await interaction.response.send_message(embed=embed)

        db.commit()
        cursor.close()
        db.close()


async def setup(bot):
    await bot.add_cog(withdraw(bot))