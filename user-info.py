import discord
from discord.ext import commands
from discord import app_commands


class user_info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="user-info", description="Shows the info about the member")
    async def userinfo(self, interaction: discord.Interaction, member: discord.Member = None):
        if member == None:
            member = interaction.user
        roles = [role for role in member.roles]

        roles = len(roles) - 1

        if member.bot == True:
            bot = "Yes"
        if member.bot == False:
            bot = "No"

        embed = discord.Embed(colour=discord.Color.blue(),
                            timestamp=interaction.created_at)
        embed.set_author(name=f"Member Info - {member}")
        embed.set_thumbnail(url=member.display_avatar.url)
        embed.add_field(name="ID:", value=member.id, inline=True)
        embed.add_field(name="Created at:", value=member.created_at.strftime(
            "%a,%#d %B %Y, %I:%M %p UTC"), inline=True)
        embed.add_field(name="Joined at:", value=member.joined_at.strftime(
            "%a,%#d %B %Y, %I:%M %p UTC"), inline=True)
        embed.add_field(name="Roles:", value=f"{roles}", inline=True)
        embed.add_field(name="Nickname?", value=member.nick, inline=True)
        embed.add_field(name="Bot?", value=bot, inline=True)
        
        await interaction.response.send_message(embed=embed)
            
async def setup(bot):
    await bot.add_cog(user_info(bot))