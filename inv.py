import sqlite3
import discord
from discord.ext import commands
from discord import app_commands
import sqlite3
import itertools

class inv(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="inventory", description="Open your inventory")
    async def inv(self, interaction:discord.Interaction, member:discord.Member = None):
        if member is None:
            member = interaction.user

        animal_list = [None,"🦊 Fox", "🐺 Wolf", " 🐱Cat", "🦝 Raccoon", "🐯 Tiger", "🦁 Lion", "🐆 Leopard","🦌 Deer", "🦓 Zebra", "🦄 Unicorn"]
        tools_list = [None, "🔫 Pistol", "🎣 Rod", "⛏️ Pick", "🛠️ Anti Rob Token "]
        fish_list = [None,"🐟 Normal Fish", "🐠 Tropical Fish", " 🍥 Fish Cake", "🐡 Blowfish"]
        ore_list = [None,"Coal", "copper", "Iron", "Gold", "💎 Diamond"]

        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        cursor.execute(f"SELECT * FROM animals WHERE user_id = {member.id}")
        animals = cursor.fetchone()

        cursor.execute(f"SELECT * FROM fish WHERE user_id = {member.id}")
        fish = cursor.fetchone()

        cursor.execute(f"SELECT * FROM tools WHERE user_id = {member.id}")
        tools = cursor.fetchone()

        cursor.execute(f"SELECT * FROM mine WHERE user_id = {member.id}")
        ores = cursor.fetchone()

        animals_ = [f"{i} x{j}" for i, j in itertools.zip_longest(animal_list, animals) if j > 0 and j < 100000000000000000]
        tools_ = [f"{i} x{j}" for i, j in itertools.zip_longest(tools_list, tools) if j > 0 and j < 100000000000000000]
        fish_ = [f"{i} x{j}" for i, j in itertools.zip_longest(fish_list, fish) if j > 0 and j < 100000000000000000]
        ores_ = [f"{i} x{j}" for i, j in itertools.zip_longest(ore_list, ores) if j > 0 and j < 100000000000000000]

        animals_ = "\n".join(animals_) if len(animals_) > 0 else "*No animals in inventory*"
        tools_ = "\n".join(tools_) if len(tools_) > 0 else "*No tools in inventory*"
        fish_ = "\n".join(fish_) if len(fish_) > 0 else "*No fishes in inventory*"
        ores_ = "\n".join(ores_) if len(ores_) > 0 else "*No ores in inventory*"

        embed = discord.Embed(title="", color=discord.Color.blue())
        embed.set_author(icon_url=member.display_avatar.url, name=f"{member.name} Inventoy")
        embed.add_field(name="Animals", value=animals_)
        embed.add_field(name="Fishes", value=fish_)
        embed.add_field(name="Tools", value=tools_)
        embed.add_field(name="Ores", value=ores_)
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(inv(bot))