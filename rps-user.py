import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View
import enum
class choices(enum.Enum):
    Rock = 1
    Paper = 2
    Scissor = 3

class rps_user(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="rps-user", description="Play rock paper scissors agaist a real person")
    @app_commands.describe(member="Member you want to play against")
    @app_commands.describe(your_choice="Describe your choice (rock paper or scissor)")
    async def rps_user(self, interaction: discord.Interaction, member: discord.Member, your_choice: choices):
        if member.id == interaction.user.id:
            await interaction.response.send_message("You can't play against yourself :(")
            return

        rock = Button(label="Rock", style=discord.ButtonStyle.green, emoji="🪨")
        paper = Button(label="Paper", style=discord.ButtonStyle.green, emoji="🧻")
        scissors = Button(label="Scissors",
                        style=discord.ButtonStyle.green, emoji="✂️")

        view = View(timeout=120)
        view.add_item(rock)
        view.add_item(paper)
        view.add_item(scissors)
        await interaction.response.send_message(f"{member.mention}, **{interaction.user.display_name}** invited you to play Rock Paper Scissors \n\nYou have 2 minutes to pick Rock, Paper or Scissors or this game will end", view=view)

        async def rock_callback(interactions: discord.Interaction):
            rock1 = Button(
                label="Rock", style=discord.ButtonStyle.green, emoji="🪨")
            paper1 = Button(
                label="Paper", style=discord.ButtonStyle.green, emoji="🧻")
            scissors1 = Button(
                label="Scissors", style=discord.ButtonStyle.green, emoji="✂️")

            myview = View()
            rock1.disabled = True
            paper1.disabled = True
            scissors1.disabled = True

            myview.add_item(rock1)
            myview.add_item(paper1)
            myview.add_item(scissors1)

            if interactions.user.id == member.id:
                if your_choice == choices.Rock:
                    embed = discord.Embed(title=f"You tied!",
                                        colour=discord.Color.blue())
                    embed.add_field(
                        name=f"", value=f"**{interaction.user.display_name}** chose 🪨 \n\n**{member.display_name}** chose 🪨")
                    await interactions.response.send_message(embed=embed)
                    await interaction.edit_original_response(view=myview)
                    return

                if your_choice == choices.Paper:
                    embed = discord.Embed(
                        title=f"{member.display_name} won!", colour=discord.Color.blue())
                    embed.add_field(
                        name=f"", value=f"**{interaction.user.display_name}** chose 🧻 \n\n**{member.display_name}** chose 🪨")
                    await interactions.response.send_message(embed=embed)
                    await interaction.edit_original_response(view=myview)
                    return

                if your_choice == choices.Scissor:
                    embed = discord.Embed(
                        title=f"{member.display_name} won!", colour=discord.Color.blue())
                    embed.add_field(
                        name=f"", value=f"**{interaction.user.display_name}** chose ✂️ \n\n**{member.display_name}** chose 🪨")
                    await interactions.response.send_message(embed=embed)
                    await interaction.edit_original_response(view=myview)
                    return

            if interaction.user.id != member.id:
                interaction.response.send_message(
                    f"You're not {member.mention}?", ephemeral=True)

        rock.callback = rock_callback

        async def paper_callback(interactions: discord.Interaction):
            rock1 = Button(
                label="Rock", style=discord.ButtonStyle.green, emoji="🪨")
            paper1 = Button(
                label="Paper", style=discord.ButtonStyle.green, emoji="🧻")
            scissors1 = Button(
                label="Scissors", style=discord.ButtonStyle.green, emoji="✂️")

            myview = View()
            rock1.disabled = True
            paper1.disabled = True
            scissors1.disabled = True

            myview.add_item(rock1)
            myview.add_item(paper1)
            myview.add_item(scissors1)

            if interactions.user.id == member.id:
                if your_choice == choices.Rock:
                    embed = discord.Embed(
                        title=f"{member.display_name} won!", colour=discord.Color.blue())
                    embed.add_field(
                        name=f"", value=f"**{interaction.user.display_name}** chose 🪨 \n\n**{member.display_name}** chose 🧻")
                    await interactions.response.send_message(embed=embed)
                    await interaction.edit_original_response(view=myview)
                    return

                if your_choice == choices.Paper:
                    embed = discord.Embed(title=f"You tied!",
                                        colour=discord.Color.blue())
                    embed.add_field(
                        name=f"", value=f"**{interaction.user.display_name}** chose 🧻 \n\n**{member.display_name}** chose 🧻")
                    await interactions.response.send_message(embed=embed)
                    await interaction.edit_original_response(view=myview)
                    return

                if your_choice == choices.Scissor:
                    embed = discord.Embed(
                        title=f"{interaction.user.display_name} won!", colour=discord.Color.blue())
                    embed.add_field(
                        name=f"", value=f"**{interaction.user.display_name}** chose ✂️ \n\n**{member.display_name}** chose 🧻")
                    await interactions.response.send_message(embed=embed)
                    await interaction.edit_original_response(view=myview)
                    return

            if interaction.user.id != member.id:
                interaction.response.send_message(
                    f"You're not {member.mention}?", ephemeral=True)

        paper.callback = paper_callback

        async def scissors_callback(interactions: discord.Interaction):
            rock1 = Button(
                label="Rock", style=discord.ButtonStyle.green, emoji="🪨")
            paper1 = Button(
                label="Paper", style=discord.ButtonStyle.green, emoji="🧻")
            scissors1 = Button(
                label="Scissors", style=discord.ButtonStyle.green, emoji="✂️")

            myview = View()
            rock1.disabled = True
            paper1.disabled = True
            scissors1.disabled = True

            myview.add_item(rock1)
            myview.add_item(paper1)
            myview.add_item(scissors1)
            if interactions.user.id == member.id:
                if your_choice == choices.Rock:
                    embed = discord.Embed(
                        title=f"{interaction.user.display_name} won!", colour=discord.Color.blue())
                    embed.add_field(
                        name=f"", value=f"**{interaction.user.display_name}** chose 🪨 \n\n**{member.display_name}** chose ✂️")
                    await interactions.response.send_message(embed=embed)
                    await interaction.edit_original_response(view=myview)
                    return

                if your_choice == choices.Paper:
                    embed = discord.Embed(
                        title=f"{member.display_name} won!", colour=discord.Color.blue())
                    embed.add_field(
                        name=f"", value=f"**{interaction.user.display_name}** chose 🧻 \n\n**{member.display_name}** chose ✂️")
                    await interactions.response.send_message(embed=embed)
                    await interaction.edit_original_response(view=myview)
                    return

                if your_choice == choices.Scissor:
                    embed = discord.Embed(title=f"You tied!",
                                        colour=discord.Color.blue())
                    embed.add_field(
                        name=f"", value=f"**{interaction.user.display_name}** chose ✂️ \n\n**{member.display_name}** chose ✂️")
                    await interactions.response.send_message(embed=embed)
                    await interaction.edit_original_response(view=myview)
                    return

            if interaction.user.id != member.id:
                interaction.response.send_message(
                    f"You're not {member.mention}?", ephemeral=True)

        scissors.callback = scissors_callback

async def setup(bot):
    await bot.add_cog(rps_user(bot))