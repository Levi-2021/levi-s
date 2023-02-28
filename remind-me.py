import discord
from discord.ext import commands
from discord import app_commands
import enum
from asyncio import sleep 


class choices(enum.Enum):
    seconds = 1
    minutes = 2
    hours = 3
    days = 4


class remind_me(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="remind-me", description="Reminder")
    async def remind_me(self, interaction: discord.Interaction, message: str, unit: choices, time: int):
        if unit == unit.seconds:
            if time >= 120:
                embed = discord.Embed(color=discord.Color.blue(),
                                    timestamp=interaction.created_at)
                embed.add_field(
                    name=f"", value=f"**I will remind you in {time} seconds!**\n\nMessage: {message}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                await sleep(time)
                embed = discord.Embed(
                    title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                embed.add_field(name="Reminder:", value=f"{message}")
                await interaction.user.send(embed=embed)
                return

            else:
                await interaction.response.send_message("Time must be 120 seconds or more", ephemeral=True)
                return

        if unit == unit.minutes:
            if time >= 2:
                embed = discord.Embed(color=discord.Color.blue(),
                                    timestamp=interaction.created_at)
                embed.add_field(
                    name=f"", value=f"**I will remind you in {time} minutes!**\n\nMessage: {message}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                await sleep(time * 60)
                embed = discord.Embed(
                    title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                embed.add_field(name="Reminder:", value=f"{message}")
                await interaction.user.send(embed=embed)
                return

            else:
                await interaction.response.send_message("Time must be 2 minutes or more", ephemeral=True)
                return

        if unit == unit.hours:
            if time >= 2:
                embed = discord.Embed(color=discord.Color.blue(),
                                    timestamp=interaction.created_at)
                embed.add_field(
                    name=f"", value=f"**I will remind you in {time} hours!**\n\nMessage: {message}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                await sleep(time * 3600)
                embed = discord.Embed(
                    title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                embed.add_field(name="Reminder:", value=f"{message}")
                await interaction.user.send(embed=embed)
                return

            if time == 1:
                embed = discord.Embed(color=discord.Color.blue(),
                                    timestamp=interaction.created_at)
                embed.add_field(
                    name=f"", value=f"**I will remind you in 1 hour!**\n\nMessage: {message}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                await sleep(time * 3600)
                embed = discord.Embed(
                    title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                embed.add_field(name="Reminder:", value=f"{message}")
                await interaction.user.send(embed=embed)
                return

            else:
                await interaction.response.send_message("Time must be 1 hour or more", ephemeral=True)
                return

        if unit == unit.days:
            if time >= 2:
                embed = discord.Embed(color=discord.Color.blue(),
                                    timestamp=interaction.created_at)
                embed.add_field(
                    name=f"", value=f"**I will remind you in {time} days!**\n\nMessage: {message}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                await sleep(time * 3600)
                embed = discord.Embed(
                    title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                embed.add_field(name="Reminder:", value=f"{message}")
                await interaction.user.send(embed=embed)
                return

            if time == 1:
                embed = discord.Embed(color=discord.Color.blue(),
                                    timestamp=interaction.created_at)
                embed.add_field(
                    name=f"", value=f"**I will remind you in 1 day!**\n\nMessage: {message}")
                await interaction.response.send_message(embed=embed, ephemeral=True)
                await sleep(time * 86400)
                embed = discord.Embed(
                    title="", color=discord.Color.blue(), timestamp=interaction.created_at)
                embed.add_field(name="Reminder:", value=f"{message}")
                await interaction.user.send(embed=embed)
                return

            else:
                await interaction.response.send_message("Time must be 1 hour or more", ephemeral=True)
                return

            
async def setup(bot):
    await bot.add_cog(remind_me(bot))

