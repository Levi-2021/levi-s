import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
import random

class work(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="work", description="Earn between 💸750 and 💸1,250 every 10 minutes")
    @app_commands.checks.cooldown(1, 600)
    async def work(self, interaction:discord.Interaction):

        member = interaction.user

        earnings = random.randint(750, 1250)

        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        cursor.execute(f"SELECT wallet, bank FROM main WhERE user_id = {member.id}")
        bal = cursor.fetchone()

        try:
            wallet = bal[0]
            bank = bal[1]

        except:
            wallet = 0 
            bank = 0

        sql = ("UPDATE main SET wallet = ? WHERE user_id = ?")
        val = (wallet + int(earnings), member.id)
        cursor.execute(sql, val)

        earned = wallet + int(earnings)
        embed = discord.Embed(description=f"You earned 💸{earnings}", color=discord.Color.blue(), timestamp=interaction.created_at)
        embed.set_author(icon_url=interaction.user.display_avatar.url, name=f"{interaction.user.name} New balance")
        embed.add_field(name="Wallet", value=f"`💸{earned}`")
        embed.add_field(name="Bank", value=f"`💸{bank}`")
        embed.add_field(name="Networth", value=f"`💸{earned + bank}`")
        embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1138/1138038.png")
        await interaction.response.send_message(embed=embed)

        db.commit()
        cursor.close()
        db.close()

    @work.error
    async def on_work_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):

            Error = round(error.retry_after)

            if Error > 60:
                Error = round(Error/60)
                if Error == 1:
                    embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                    embed.add_field(name=f"You can work again in {Error} minute", value="")
                    await interaction.response.send_message(embed=embed)
                    return
                
                else:
                    
                    embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                    embed.add_field(name=f"You can work again in {Error} minutes", value="")
                    await interaction.response.send_message(embed=embed)
                    return

            if Error < 60:
                embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                embed.add_field(name=f"You can work again in {Error} seconds", value="")
                await interaction.response.send_message(embed=embed)
                return


async def setup(bot):
    await bot.add_cog(work(bot))
    

