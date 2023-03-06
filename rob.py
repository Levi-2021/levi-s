import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
import random

class rob(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="rob", description="Rob a member for their money")
    @app_commands.checks.cooldown(1, 86400)
    @app_commands.describe(member="Member you want to rob")
    async def rob(self, interaction:discord.Interaction, member:discord.Member):
        if member == interaction.user.bot:
            await interaction.response.send_message("You you can't rob a bot :(")
            return
        
        if member.id == interaction.user.id:
            await interaction.response.send_message("You're gonna rob yourself?")
            return
        
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        cursor.execute(f"SELECT wallet FROM main WhERE user_id = {member.id}")
        bal = cursor.fetchone()
        memberwallet = bal[0]

        cursor.execute(f"SELECT * FROM tools WHERE user_id = {member.id}")
        tools = cursor.fetchone()
        anti_rob_token = tools[4]

        if memberwallet == 0:
            await interaction.response.send_message(f"{member.mention} doesn't have any money in his wallet!")
            cursor.close()
            db.close()
            return
        
        if anti_rob_token != 0:
            embed = discord.Embed(title="", color=discord.Color.red(), timestamp=interaction.created_at)
            embed.add_field(name="", value=f"{interaction.user.mention} tried to rob {member.mention} but he used an anti rob token!")
            await interaction.response.send_message(embed=embed)
            cursor.execute("UPDATE tools SET anti_rob_token = ? WHERE user_id = ?", (anti_rob_token - 1, member.id))
            db.commit()
            cursor.close()
            db.close()
            return

        cursor.execute(f"SELECT wallet, bank FROM main WHERE user_id = {interaction.user.id}")
        bal = cursor.fetchone()

        userwallet = bal[0]
        userbank = bal[1]

        randint = random.randint(1,10)

        if randint > 1:
            precentage = random.randint(50, 80)
            amount = round(memberwallet*(precentage/100))
            cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (userbank + amount, interaction.user.id))
            cursor.execute("UPDATE main SET wallet = ? WHERE user_id = ?", (memberwallet - amount, member.id))
            db.commit()
            embed = discord.Embed(description=f"You robbed {member.display_name} for 💸{amount}!",color=discord.Color.green(), timestamp=interaction.created_at)
            embed.set_author(icon_url=interaction.user.display_avatar.url, name=f"{interaction.user.name} Bank account")
            embed.add_field(name="Wallet", value=f"`💸{userwallet}`")
            embed.add_field(name="Bank", value=f"`💸{userbank + amount}`")
            embed.add_field(name="Networth", value=f"`💸{userwallet + userbank + amount}`")
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1138/1138038.png")
            await interaction.response.send_message(embed=embed)
            
            
        if randint == 1:
            amount = random.randint(2000, 3000)
            cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (userbank - amount, interaction.user.id))
            db.commit()
            embed = discord.Embed(title=f"You've been fined 💸{amount} for robbing {member.display_name}!", color=discord.Color.red(), timestamp=interaction.created_at)
            embed.add_field(name="Wallet", value=f"`💸{userwallet}`")
            embed.add_field(name="Bank", value=f"`💸{userbank - amount}`")
            embed.add_field(name="Networth", value=f"`💸{userwallet + userbank - amount}`")
            embed.set_thumbnail(url="https://cdn-icons-png.flaticon.com/512/1138/1138038.png")
            await interaction.response.send_message(embed=embed)

        cursor.close()
        db.close()
            
    @rob.error
    async def on_rob_error(self, interaction: discord.Interaction, error: app_commands.AppCommandError):
        if isinstance(error, app_commands.CommandOnCooldown):

            Error = round(error.retry_after)

            if Error > 3600:
                Error = round(Error/3600)
                if Error == 1:
                    embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                    embed.add_field(name=f"You can rob again in {Error} hour", value="")
                    await interaction.response.send_message(embed=embed)
                    return
                else:
                    embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                    embed.add_field(name=f"You can rob again in {Error} hours", value="")
                    await interaction.response.send_message(embed=embed)
                    return

            if Error > 60:
                Error = round(Error/60)

                if Error == 1:
                    embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                    embed.add_field(name=f"You can rob again in {Error} minute", value="")
                    await interaction.response.send_message(embed=embed)
                    return
                
                else:
                    
                    embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                    embed.add_field(name=f"You can rob again in {Error} minutes", value="")
                    await interaction.response.send_message(embed=embed)
                    return

            if Error < 60:
                embed = discord.Embed(title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                embed.add_field(name=f"You can rob again in {Error} seconds", value="")
                await interaction.response.send_message(embed=embed)
                return

async def setup(bot):
    await bot.add_cog(rob(bot))