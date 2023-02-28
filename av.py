import discord
from discord.ext import commands
from discord import app_commands


class av(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @app_commands.command(name="av", description="Shows the avatar of the user")
    async def av(self, interaction: discord.Interaction, user: discord.Member = None):
        if user == None:
            user = interaction.user

        embed = discord.Embed(color=discord.Color.blue(
        ), title=f"{user}", timestamp=interaction.created_at,)
        embed.set_image(url=user.display_avatar.url)
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(av(bot))