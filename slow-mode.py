import discord
from discord.ext import commands
from discord import app_commands


class slow_mode(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="slow-mode", description="Enable or disable slow mode in the channel")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def slow_mode(self, interaction:discord.Interaction):
        try:
            if interaction.channel.slowmode_delay != 0:
                await interaction.channel.edit(slowmode_delay=0)
                await interaction.response.send_message('Disabled slow mode \n\nTo enable this again use "/slow-mode"', ephemeral=True)
                return
            if interaction.channel.slowmode_delay == 0:
                await interaction.channel.edit(slowmode_delay=5)
                await interaction.response.send_message('Enabled slow mode \n\nTo disable this use "/slow-mode"', ephemeral=True)
                return
        except:
            await interaction.response.send_message('Make sure "Manage Channels" is turned on for the bot role.')


async def setup(bot):
    await bot.add_cog(slow_mode(bot))