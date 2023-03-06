import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
import random

class daily(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="daily", description="Earn between 💸10,000 and 💸15,000 every day")
    @app_commands.checks.cooldown(1, 86400)
    async def daily(self, interaction:discord.Interaction):

        member = interaction.user
        earnings = random.randint(10000, 15000)
        # earnings = random.randint(1000000000, 1000000001)
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

    @daily.error
    async def on_daily_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):

            Error = round(error.retry_after)

            if Error > 3600:
                Error = round(Error/3600)
                if Error == 1:
                    embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                    embed.add_field(name=f"You can collect money again in {Error} hour", value="")
                    await interaction.response.send_message(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                    embed.add_field(name=f"You can collect money again in {Error} hours", value="")
                    await interaction.response.send_message(embed=embed)
                    return

            if Error > 60:
                Error = round(Error/60)

                if Error == 1:
                    embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                    embed.add_field(name=f"You can collect money again in {Error} minute", value="")
                    await interaction.response.send_message(embed=embed)
                    return
                
                else:
                    
                    embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                    embed.add_field(name=f"You can collect money again in {Error} minutes", value="")
                    await interaction.response.send_message(embed=embed)
                    return

            if Error < 60:
                embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                embed.add_field(name=f"You can collect money again in {Error} seconds", value="")
                await interaction.response.send_message(embed=embed)
                return


async def setup(bot):
    await bot.add_cog(daily(bot))
    

