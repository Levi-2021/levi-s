import discord
from discord.ext import commands
from discord import app_commands
import requests

class iss(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="iss", description="Get information about iss (International Space Station)")
    async def iss(self, interaction: discord.Interaction):
        url = "https://api.wheretheiss.at/v1/satellites/25544"

        response = requests.get(url).json()

        latitude = response['latitude']
        longitude = response['longitude']
        altitude = response['altitude']
        velocity = response['velocity']
        visibility = response['visibility']
        footprint = response['footprint']
        timestamp = response['timestamp']
        daynum = response['daynum']
        solar_lat = response['solar_lat']
        solar_lon = response['solar_lon']
        units = response['units']

        embed = discord.Embed(
            title="🚀International Space Station (iss)🚀", color=discord.Color.blue())
        embed.add_field(name="Coordinates:",
                        value=f"{latitude}, {longitude}", inline=True)
        embed.add_field(name="Altitude:", value=f"{altitude} {units}", inline=True)
        embed.add_field(name="Velocity:",
                        value=f"{velocity} {units} per hour", inline=True)
        embed.add_field(name="Visibility:", value=f"{visibility}", inline=True)
        embed.add_field(name="Footprint:", value=f"{footprint}", inline=True)
        embed.add_field(name="Timestamp:", value=f"{timestamp}", inline=True)
        embed.add_field(name="Day Number:", value=f"{daynum}", inline=True)
        embed.add_field(name="Solar_lat:", value=f"{solar_lat}", inline=True)
        embed.add_field(name="Solar_lon:", value=f"{solar_lon}", inline=True)
        embed.set_image(
            url="https://www.nasa.gov/sites/default/files/thumbnails/image/iss056e201046large.jpg")

        await interaction.response.send_message(embed=embed)

async def setup(bot):
    await bot.add_cog(iss(bot))