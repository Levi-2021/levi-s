import os
import discord
import asyncio
from discord.ext import commands
from dotenv import load_dotenv
import json
from discord.ui import Button, View


load_dotenv()
token = os.getenv('token')


bot = commands.Bot(command_prefix="/", intents=discord.Intents.default())
bot.remove_command("help")


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

helpGuide = json.load(open("help.json"))

def createHelpEmbed(pageNum=0, inline=False):
    pageNum = (pageNum) % len(list(helpGuide))
    pageTitle = list(helpGuide)[pageNum]
    embed = discord.Embed(color=discord.Color.blue(), title=pageTitle)
    for key, val in helpGuide[pageTitle].items():
        embed.add_field(name=bot.command_prefix +
                        key, value=val, inline=inline)
        embed.set_footer(text=f"Page {pageNum+1} of {len(list(helpGuide))}")
    return embed

@bot.tree.command(name="help", description="The help command")
async def help(interaction: discord.Interaction):
    currentPage = 0

    async def next_callback(interaction: discord.Interaction):
        nonlocal currentPage, sent_msg
        currentPage += 1
        await interaction.response.edit_message(embed=createHelpEmbed(pageNum=currentPage), view=myview)

    async def previous_callback(interaction: discord.Interaction):
        nonlocal currentPage, sent_msg
        currentPage -= 1
        await interaction.response.edit_message(embed=createHelpEmbed(pageNum=currentPage), view=myview)

    previousButton = Button(label="<", style=discord.ButtonStyle.blurple)
    nextButton = Button(label=">", style=discord.ButtonStyle.blurple)
    previousButton.callback = previous_callback
    nextButton.callback = next_callback

    myview = View()
    myview.add_item(previousButton)
    myview.add_item(nextButton)

    sent_msg = await interaction.response.send_message(embed=createHelpEmbed(currentPage), view=myview)



async def main():
    async with bot:
        await load()
        await bot.start(token)
asyncio.run(main())

