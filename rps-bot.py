import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View
import random

class rps_bot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="rps-bot", description="Play rock paper scissors agaist a bot")
    async def rps(self, interactions: discord.Interaction):
        async def rps1(interactions: discord.Interaction):
            choices = ["rock", "paper", "scissors",]
            computers_answer = random.choice(choices)

            rock = Button(label="Rock", style=discord.ButtonStyle.green, emoji="🪨")
            paper = Button(
                label="Paper", style=discord.ButtonStyle.green, emoji="🧻")
            scissors = Button(label="Scissors",
                            style=discord.ButtonStyle.green, emoji="✂️")

            view = View()
            view.add_item(rock)
            view.add_item(paper)
            view.add_item(scissors)
            await interactions.response.send_message("Chose between rock, paper or scissors", view=view)

            play_again = Button(label="Play again",
                                style=discord.ButtonStyle.green)
            view = View()
            view.add_item(play_again)

            async def button1_callback(interaction: discord.Interaction):
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
                if interactions.user == interaction.user:

                    if computers_answer == "rock":
                        await interaction.response.send_message(f"The computer chose **ROCK** so {interaction.user.mention} tied.", view=view)
                        await interactions.edit_original_response(view=myview)

                    if computers_answer == "paper":
                        await interaction.response.send_message(f"The computer chose **PAPER** so {interaction.user.mention} lost.", view=view)
                        await interactions.edit_original_response(view=myview)

                    if computers_answer == "scissors":
                        await interaction.response.send_message(f"The computer chose **SCISSORS** so {interaction.user.mention} won!", view=view)
                        await interactions.edit_original_response(view=myview)

                else:
                    await interaction.response.send_message(f"You're not {interactions.user.mention}", ephemeral=True)

            rock.callback = button1_callback

            async def button2_callback(interaction: discord.Interaction):
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
                if interactions.user == interaction.user:

                    if computers_answer == "rock":
                        await interaction.response.send_message(f"The computer chose **ROCK** so {interaction.user.mention} won!", view=view)
                        await interactions.edit_original_response(view=myview)

                    if computers_answer == "paper":
                        await interaction.response.send_message(f"The computer chose **PAPER** so {interaction.user.mention} tied.", view=view)
                        await interactions.edit_original_response(view=myview)

                    if computers_answer == "scissors":
                        await interaction.response.send_message(f"The computer chose **SCISSORS** so {interaction.user.mention} lost.", view=view)
                        await interactions.edit_original_response(view=myview)

                else:
                    await interaction.response.send_message(f"You're not {interactions.user.mention}", ephemeral=True)

            paper.callback = button2_callback

            async def button3_callback(interaction: discord.Interaction):
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
                if interactions.user == interaction.user:

                    if computers_answer == "rock":
                        await interaction.response.send_message(f"The computer chose **ROCK** so {interaction.user.mention} lost.", view=view)
                        await interactions.edit_original_response(view=myview)

                    if computers_answer == "paper":
                        await interaction.response.send_message(f"The computer chose **PAPER** so {interaction.user.mention} won!", view=view)
                        await interactions.edit_original_response(view=myview)

                    if computers_answer == "scissors":
                        await interaction.response.send_message(f"The computer chose **SCISSORS** so {interaction.user.mention} tied.", view=view)
                        await interactions.edit_original_response(view=myview)

                else:
                    await interaction.response.send_message(f"You're not {interactions.user.mention}", ephemeral=True)

            scissors.callback = button3_callback
            play_again.callback = rps1

        choices = ["rock", "paper", "scissors",]
        computers_answer = random.choice(choices)

        rock = Button(label="Rock", style=discord.ButtonStyle.green, emoji="🪨")
        paper = Button(label="Paper", style=discord.ButtonStyle.green, emoji="🧻")
        scissors = Button(label="Scissors",
                        style=discord.ButtonStyle.green, emoji="✂️")

        view = View()
        view.add_item(rock)
        view.add_item(paper)
        view.add_item(scissors)
        await interactions.response.send_message("Chose between rock, paper or scissors", view=view)

        play_again = Button(label="Play again", style=discord.ButtonStyle.green)
        view = View()
        view.add_item(play_again)

        async def button1_callback(interaction: discord.Interaction):
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
            if interactions.user == interaction.user:

                if computers_answer == "rock":
                    await interaction.response.send_message(f"The computer chose **ROCK** so {interaction.user.mention} tied.", view=view)
                    await interactions.edit_original_response(view=myview)

                if computers_answer == "paper":
                    await interaction.response.send_message(f"The computer chose **PAPER** so {interaction.user.mention} lost.", view=view)
                    await interactions.edit_original_response(view=myview)

                if computers_answer == "scissors":
                    await interaction.response.send_message(f"The computer chose **SCISSORS** so {interaction.user.mention} won!", view=view)
                    await interactions.edit_original_response(view=myview)

            else:
                await interaction.response.send_message(f"You're not {interactions.user.mention}", ephemeral=True)

        rock.callback = button1_callback

        async def button2_callback(interaction: discord.Interaction):
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
            if interactions.user == interaction.user:

                if computers_answer == "rock":
                    await interaction.response.send_message(f"The computer chose **ROCK** so {interaction.user.mention} won!", view=view)
                    await interactions.edit_original_response(view=myview)

                if computers_answer == "paper":
                    await interaction.response.send_message(f"The computer chose **PAPER** so {interaction.user.mention} tied.", view=view)
                    await interactions.edit_original_response(view=myview)

                if computers_answer == "scissors":
                    await interaction.response.send_message(f"The computer chose **SCISSORS** so {interaction.user.mention} lost.", view=view)
                    await interactions.edit_original_response(view=myview)

            else:
                await interaction.response.send_message(f"You're not {interactions.user.mention}", ephemeral=True)

        paper.callback = button2_callback

        async def button3_callback(interaction: discord.Interaction):
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
            if interactions.user == interaction.user:

                if computers_answer == "rock":
                    await interaction.response.send_message(f"The computer chose **ROCK** so {interaction.user.mention} lost.", view=view)
                    await interactions.edit_original_response(view=myview)

                if computers_answer == "paper":
                    await interaction.response.send_message(f"The computer chose **PAPER** so {interaction.user.mention} won!", view=view)
                    await interactions.edit_original_response(view=myview)

                if computers_answer == "scissors":
                    await interaction.response.send_message(f"The computer chose **SCISSORS** so {interaction.user.mention} tied.", view=view)
                    await interactions.edit_original_response(view=myview)

            else:
                await interaction.response.send_message(f"You're not {interactions.user.mention}", ephemeral=True)

        scissors.callback = button3_callback
        play_again.callback = rps1

async def setup(bot):
    await bot.add_cog(rps_bot(bot))