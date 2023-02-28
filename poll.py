import discord
from discord.ext import commands
from discord import app_commands

class poll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="poll", description="Poll with max 10 choices")
    @app_commands.describe(choice1="choice 1 (required)")
    @app_commands.describe(choice2="choice 2 (required)")
    @app_commands.describe(choice3='choice 3 (optional)')
    @app_commands.describe(choice4='choice 4 (optional)')
    @app_commands.describe(choice5='choice 5 (optional)')
    @app_commands.describe(choice6='choice 6 (optional)')
    @app_commands.describe(choice7='choice 7 (optional)')
    @app_commands.describe(choice8='choice 8 (optional)')
    @app_commands.describe(choice9='choice 9 (optional)')
    @app_commands.describe(choice10='choice 10 (optional)')
    async def poll(self, interaction: discord.Interaction, question: str, choice1: str, choice2: str, choice3: str = None, choice4: str = None, choice5: str = None, choice6: str = None, choice7: str = None, choice8: str = None, choice9: str = None, choice10: str = None
                ):
        if choice3 == None:
            embed = discord.Embed(title=f"{question}", colour=discord.Color.blue(
            ), timestamp=interaction.created_at)
            embed.add_field(
                name=f" :one: {choice1} \n\n:two: {choice2}", value="")
            embed.set_footer(
                text=f"Requested by {interaction.user}")
            msg = await interaction.channel.send(embed=embed)
            await interaction.response.send_message("Succesfully made a poll with 2 choices", ephemeral=True)
            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            return

        if choice4 == None:
            embed = discord.Embed(title=f"{question}", colour=discord.Color.blue(
            ), timestamp=interaction.created_at)
            embed.add_field(
                name=f" :one: {choice1} \n\n:two: {choice2} \n\n:three: {choice3}", value="")
            embed.set_footer(
                text=f"Requested by {interaction.user}")
            msg = await interaction.channel.send(embed=embed)
            await interaction.response.send_message("Succesfully made a poll with 3 choices", ephemeral=True)
            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            await msg.add_reaction("3️⃣")
            return

        if choice5 == None:
            embed = discord.Embed(title=f"{question}", colour=discord.Color.blue(
            ), timestamp=interaction.created_at)
            embed.add_field(
                name=f" :one: {choice1} \n\n:two: {choice2} \n\n:three: {choice3} \n\n:four: {choice4}", value="")
            embed.set_footer(
                text=f"Requested by {interaction.user}")
            msg = await interaction.channel.send(embed=embed)
            await interaction.response.send_message("Succesfully made a poll with 4 choices", ephemeral=True)
            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            await msg.add_reaction("3️⃣")
            await msg.add_reaction("4️⃣")
            return

        if choice6 == None:
            embed = discord.Embed(title=f"{question}", colour=discord.Color.blue(
            ), timestamp=interaction.created_at)
            embed.add_field(
                name=f" :one: {choice1} \n\n:two: {choice2} \n\n:three: {choice3} \n\n:four: {choice4} \n\n:five: {choice5}", value="")
            embed.set_footer(
                text=f"Requested by {interaction.user}")
            msg = await interaction.channel.send(embed=embed)
            await interaction.response.send_message("Succesfully made a poll with 5 choices", ephemeral=True)
            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            await msg.add_reaction("3️⃣")
            await msg.add_reaction("4️⃣")
            await msg.add_reaction("5️⃣")
            return

        if choice7 == None:
            embed = discord.Embed(title=f"{question}", colour=discord.Color.blue(
            ), timestamp=interaction.created_at)
            embed.add_field(
                name=f" :one: {choice1} \n\n:two: {choice2} \n\n:three: {choice3} \n\n:four: {choice4} \n\n:five: {choice5}\n\n:six: {choice6}", value="")
            embed.set_footer(
                text=f"Requested by {interaction.user}")
            msg = await interaction.channel.send(embed=embed)
            await interaction.response.send_message("Succesfully made a poll with 6 choices", ephemeral=True)
            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            await msg.add_reaction("3️⃣")
            await msg.add_reaction("4️⃣")
            await msg.add_reaction("5️⃣")
            await msg.add_reaction("6️⃣")
            return

        if choice8 == None:
            embed = discord.Embed(title=f"{question}", colour=discord.Color.blue(
            ), timestamp=interaction.created_at)
            embed.add_field(
                name=f" :one: {choice1} \n\n:two: {choice2} \n\n:three: {choice3} \n\n:four: {choice4} \n\n:five: {choice5}\n\n:six: {choice6} \n\n:seven: {choice7}", value="")
            embed.set_footer(
                text=f"Requested by {interaction.user}")
            msg = await interaction.channel.send(embed=embed)
            await interaction.response.send_message("Succesfully made a poll with 7 choices", ephemeral=True)
            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            await msg.add_reaction("3️⃣")
            await msg.add_reaction("4️⃣")
            await msg.add_reaction("5️⃣")
            await msg.add_reaction("6️⃣")
            await msg.add_reaction("7️⃣")
            return

        if choice9 == None:
            embed = discord.Embed(title=f"{question}", colour=discord.Color.blue(
            ), timestamp=interaction.created_at)
            embed.add_field(
                name=f" :one: {choice1} \n\n:two: {choice2} \n\n:three: {choice3} \n\n:four: {choice4} \n\n:five: {choice5}\n\n:six: {choice6} \n\n:seven: {choice7} \n\n:eight: {choice8}", value="")
            embed.set_footer(
                text=f"Requested by {interaction.user}")
            msg = await interaction.channel.send(embed=embed)
            await interaction.response.send_message("Succesfully made a poll with 8 choices", ephemeral=True)
            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            await msg.add_reaction("3️⃣")
            await msg.add_reaction("4️⃣")
            await msg.add_reaction("5️⃣")
            await msg.add_reaction("6️⃣")
            await msg.add_reaction("7️⃣")
            await msg.add_reaction("8️⃣")
            await msg.add_reaction("9️⃣")
            return

        if choice10 == None:
            embed = discord.Embed(title=f"{question}", colour=discord.Color.blue(
            ), timestamp=interaction.created_at)
            embed.add_field(
                name=f" :one: {choice1} \n\n:two: {choice2} \n\n:three: {choice3} \n\n:four: {choice4} \n\n:five: {choice5}\n\n:six: {choice6} \n\n:seven: {choice7} \n\n:eight: {choice8} \n\n:nine; {choice9}", value="")
            embed.set_footer(
                text=f"Requested by {interaction.user}")
            msg = await interaction.channel.send(embed=embed)
            await interaction.response.send_message("Succesfully made a poll with 9 choices", ephemeral=True)
            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            await msg.add_reaction("3️⃣")
            await msg.add_reaction("4️⃣")
            await msg.add_reaction("5️⃣")
            await msg.add_reaction("6️⃣")
            await msg.add_reaction("7️⃣")
            await msg.add_reaction("8️⃣")
            await msg.add_reaction("9️⃣")
            return

        else:
            embed = discord.Embed(title=f"{question}", colour=discord.Color.blue(
            ), timestamp=interaction.created_at)
            embed.add_field(
                name=f" :one: {choice1} \n\n:two: {choice2} \n\n:three: {choice3} \n\n:four: {choice4} \n\n:five: {choice5}\n\n:six: {choice6} \n\n:seven: {choice7} \n\n:eight: {choice8} \n\n:nine: {choice9} \n\n:keycap_ten: {choice10}", value="")
            embed.set_footer(
                text=f"Requested by {interaction.user}")
            msg = await interaction.channel.send(embed=embed)
            await interaction.response.send_message("Succesfully made a poll with 10 choices", ephemeral=True)
            await msg.add_reaction("1️⃣")
            await msg.add_reaction("2️⃣")
            await msg.add_reaction("3️⃣")
            await msg.add_reaction("4️⃣")
            await msg.add_reaction("5️⃣")
            await msg.add_reaction("6️⃣")
            await msg.add_reaction("7️⃣")
            await msg.add_reaction("8️⃣")
            await msg.add_reaction("9️⃣")
            await msg.add_reaction("🔟")
            return
        
async def setup(bot):
    await bot.add_cog(poll(bot))