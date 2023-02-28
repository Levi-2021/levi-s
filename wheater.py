import discord
from discord.ext import commands
from discord import app_commands
import requests

class wheater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="wheater", description="Shows the wheater in your region")
    @app_commands.describe(location='Specify your location (e.g. "Washington")')
    async def weather(self, interaction: discord.Interaction, location: str):
        try:
            url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&key=APBGDHBQR7RVFY8RZMZTHGA7Q&contentType=json"
            response = requests.get(url).json()

            Latitude = response['latitude']
            Longitude = response['longitude']
            Resolved_Address = response['resolvedAddress']
            days = response['days']
            Date_time = days[0]['datetime']
            temp = days[0]['temp']
            feelslike = days[0]['feelslike']
            humidity = days[0]['humidity']
            Wind_Speed = days[0]['windspeed']
            visibility = days[0]['visibility']
            uvindex = days[0]['uvindex']
            sunrise = days[0]['sunrise']
            description = days[0]['description']
            Precipitation = days[0]['precip']
            precipitation_probability = days[0]['precipprob']
            precipitation_cover = days[0]['precipcover']
            preciptype = days[0]['preciptype'][0]
            snowdepth = days[0]['snowdepth']
            snow = days[0]['snow']
            sunset = days[0]['sunset']
            conditions = days[0]['conditions']

            embed = discord.Embed(
                title=f"Wheater in {Resolved_Address}", color=discord.Color.blue())
            embed.add_field(name="Coordinates:",
                            value=f"{Latitude}, {Longitude}", inline=True)
            embed.add_field(name="Description:", value=description, inline=True)
            embed.add_field(name="Temperature:", value=temp, inline=True)

            embed.add_field(name="Feels like:", value=feelslike, inline=True)
            embed.add_field(name="Wind Speed:", value=Wind_Speed, inline=True)
            embed.add_field(name="Conditions:", value=conditions, inline=True)

            embed.add_field(name="Visibility:", value=visibility, inline=True)
            embed.add_field(name="UV Index:", value=uvindex, inline=True)
            embed.add_field(name="Precipitation:", value=Precipitation, inline=True)

            embed.add_field(name="Precipitation Type:", value=preciptype, inline=True)
            embed.add_field(name="Precipitation Probability:",
                            value=precipitation_probability, inline=True)
            embed.add_field(name="Precipitation Cover:",
                            value=precipitation_cover, inline=True)

            embed.add_field(name="Humidity:", value=humidity, inline=True)
            embed.add_field(name="Sun Rise:", value=sunrise, inline=True)
            embed.add_field(name="Sun Set:", value=sunset, inline=True)

            if snow != 0.0:
                embed.add_field(name="Snow:", value=snow, inline=True)
                embed.add_field(name="Snow Depth:", value=snowdepth, inline=True)
            else:
                embed.add_field(name="Snow:", value="None", inline=True)

            if preciptype == "rain":
                embed.set_image(
                    url="https://www.ramen-vandenbroucke.com/images/articles/image/39/condensatie-aan-je-ramen-hier-volgen-enkele-tips-v1.jpg")
            elif preciptype == "snow":
                embed.set_image(
                    url="https://pension-robinhood.nl/wp-content/uploads/2016/11/image1-002-wpcf_940x450.jpg")

            embed.set_footer(text=f"Date: {Date_time}")

            await interaction.response.send_message(embed=embed)
        except:
            await interaction.response.send_message(f'I can find any data of "{location}". Make sure you spelled it correct')
async def setup(bot):
    await bot.add_cog(wheater(bot))
