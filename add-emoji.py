import discord
from discord.ext import commands
from discord import app_commands
from io import BytesIO
import aiohttp

class add_emoji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @app_commands.command(name="add-emoji", description="Adds an emoji to the server")
    @app_commands.describe(url="Link of image that you want as emoji")
    @app_commands.describe(name="Name of the emoji")
    @app_commands.checks.has_permissions(manage_emojis_and_stickers=True)
    async def add_emoji(self, interaction: discord.Interaction, url: str, name: str):
        guild = interaction.guild
        async with aiohttp.ClientSession() as ses:
            async with ses.get(url) as r:
                try:
                    imgOrGif = BytesIO(await r.read())
                    bValue = imgOrGif.getvalue()
                    if r.status in range(200, 299):
                        emoji = await guild.create_custom_emoji(image=bValue, name=name)
                        embed = discord.Embed(
                            title="Succefully added an emoji!", color=discord.Color.blue())
                        embed.add_field(name="", value=f"Emoji name: **{name}**")
                        embed.set_thumbnail(url=url)
                        await interaction.response.send_message(embed=embed)
                        await ses.close()
                    else:
                        await interaction.response.send_message(f"This did not work | {r.status}")
                except:
                    await interaction.response.send_message("The file is too thicc")

async def setup(bot):
    await bot.add_cog(add_emoji(bot))