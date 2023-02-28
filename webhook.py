import discord
from discord.ext import commands
from discord import app_commands
from discord_webhook import DiscordWebhook


class webhook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="webhook", description="Make a webhook with your avatar, name and custom message")
    async def webhook(self, interaction: discord.Interaction, message: str):
        webhook = await interaction.channel.create_webhook(name=interaction.user.name, avatar=await interaction.user.avatar.read(), reason=f"Requested by {interaction.user}")
        await interaction.response.send_message(f"Succesfully made a webhook with the name **{interaction.user.name}**", ephemeral=True)
        webhook1 = DiscordWebhook(
            url=f'{webhook.url}', content=f"{message}")
        webhook1.execute()
        await webhook.delete()


    @app_commands.command(name="create-webhook", description="Make a webhook with a custom avatar, name and message")
    async def create_webhook(self, interaction: discord.Interaction, name: str, message: str, avatar: discord.Member):
        webhook = await interaction.channel.create_webhook(name=name, avatar=await avatar.avatar.read(), reason=f"Requested by {interaction.user}")
        embed = discord.Embed(title="Succesfully made a webhook", colour=discord.Color.blue(
        ), timestamp=interaction.created_at)
        embed.add_field(name="Name:", value=f"\"{name}\"")
        embed.add_field(name="Message:", value=f"\"{message}\"")
        embed.add_field(name="Avatar:", value="")
        embed.set_thumbnail(url=avatar.avatar.url)

        await interaction.response.send_message(embed=embed, ephemeral=True)
        print(interaction.user)
        webhook1 = DiscordWebhook(
            url=f'{webhook.url}', content=f"{message}")
        webhook1.execute()
        await webhook.delete()
        
async def setup(bot):
    await bot.add_cog(webhook(bot))