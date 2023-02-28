import discord
from discord.ext import commands

class events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):

        try:
            synced = await self.bot.tree.sync()
            print(f"Synced {len(synced)} command(s)")
        except Exception as e:
            print(e)
        print(f'Logged in as {self.bot.user} (ID: {self.bot.user.id})')

        print('Servers connected to:')
        for guild in self.bot.guilds:
            print(guild.name)

        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="/help"))
    
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content == ("<@896518702550376489>"):
            embed = discord.Embed(color=discord.Color.blue())
            embed.add_field(
                name="", value=f"Watching over {len(self.bot.guilds)} server\n\n > [Invite](https://discord.com/api/oauth2/authorize?client_id=1068237563598491648&permissions=8&scope=bot) \n> [Support](https://discord.gg/YHuvDfmBnv)", inline=True)
            await message.reply(embed=embed)
        if message.content == ("896518702550376489"):
            embed = discord.Embed(color=discord.Color.blue())
            embed.add_field(
                name="", value=f"Watching over {len(self.bot.guilds)} server\n\n > [Invite](https://discord.com/api/oauth2/authorize?client_id=1068237563598491648&permissions=8&scope=bot) \n> [Support](https://discord.gg/YHuvDfmBnv)", inline=True)
            await message.reply(embed=embed)

    @commands.Cog.listener()
    async def on_member_join(self, ctx):
        embed = discord.Embed(
            title=f"Welcome to {ctx.guild.name}!", color=discord.Color.blue())
        embed.add_field(
            name="", value=f"Bot info:\n> [Invite](https://discord.com/api/oauth2/authorize?client_id=1068237563598491648&permissions=8&scope=bot) \n> [Support](https://discord.gg/YHuvDfmBnv)", inline=True)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(events(bot))