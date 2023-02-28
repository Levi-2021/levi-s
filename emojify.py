import discord
from discord.ext import commands
from discord import app_commands


class emojify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="emojify", description="Emojifys your custom message")
    async def emojify(self, interaction:discord.Interaction, content:str):

        emojis = []
        for s in content.lower():
            if s.isdecimal():
                num2emo = {'0':'zero','1':'one','2':'two','3':'three','4':'four','5':'five','6':'six','7':'seven','8':'eight','9':'nine','!':'exclamation','?':'question','!?':'interrobang'}
                emojis.append(f':{num2emo.get(s)}:')
            elif s.isalpha():
                emojis.append(f':regional_indicator_{s}:')
            else:
                emojis.append(s)
        await interaction.response.send_message (''.join(emojis))

async def setup(bot):
    await bot.add_cog(emojify(bot))