import discord
from discord.ext import commands
from discord import app_commands


class purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @app_commands.command(name="purge", description="Purge up to 200 messages at a time (Administrator required)")
    @app_commands.describe(amount="Mount of messages (max 200), administrator required")
    @app_commands.checks.has_permissions(administrator=True)
    async def purge(self, interaction: discord.Interaction, amount: int):
        if amount >= 201:
            await interaction.response.send_message("Make sure the amount is set to **200 or less**", ephemeral=True)
            return
        if amount <= 0:
            await interaction.response.send_message("Make sure the amount is set to **1 or above**", ephemeral=True)
            return
        if amount == 1:
            embed = discord.Embed(title="", colour=discord.Color.blue(
            ), timestamp=interaction.created_at)
            embed.add_field(name=f"", value="Succesfully deleted **1 message**")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            await interaction.channel.purge(limit=1)
            return
        if amount <= 200:
            embed = discord.Embed(title="", colour=discord.Color.blue(
            ), timestamp=interaction.created_at)
            embed.add_field(
                name=f"", value=f"Succesfully deleted **{amount} messages**")
            await interaction.response.send_message(embed=embed, ephemeral=True)
            await interaction.channel.purge(limit=amount)
            return

async def setup(bot):
    await bot.add_cog(purge(bot))