import discord
from discord.ext import commands
from discord import app_commands
from discord.ui import Button, View
import random
import sqlite3

class bj(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="black-jack", description="Play black jack for 💸💸💸")
    @app_commands.describe(amount="Amount of 💸 you want to bet")
    async def bj(self, interaction:discord.Interaction, amount:int):

        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()

        cursor.execute(f"SELECT * FROM main WHERE user_id = {interaction.user.id}")
        data = cursor.fetchone()

        wallet = data[1]
        bank  = data[2]

        cursor.execute("UPDATE main SET wallet = ? WHERE user_id = ?", (wallet - amount, interaction.user.id))
        
        if wallet < amount:
            await interaction.response.send_message("You don't have that much money in your wallet")
            return
        
        if amount < 0:
            return

        dealer_card = []
        cards = []
        first_card = random.randint(2,11)
        seconds_card = random.randint(2,11)
        dealer1 = random.randint(2,11)
        dealer2 = random.randint(2,11)
        cards.append(first_card)
        cards.append(seconds_card)
        dealer_card.append(dealer1)
        dealer_card.append(dealer2)

        hit = Button(label="Hit", style=discord.ButtonStyle.blurple)
        stand = Button(label="Stand", style=discord.ButtonStyle.blurple)
        hit2 = Button(label="Hit", style=discord.ButtonStyle.blurple)
        stand2 = Button(label="Stand", style=discord.ButtonStyle.blurple)
        stand3 = Button(label="Stand", style=discord.ButtonStyle.blurple)

        view = View()
        hit.disabled = False
        stand.disabled = False
        view.add_item(hit)
        view.add_item(stand)

        view2 = View()
        hit2.disabled = True
        stand2.disabled = True
        view2.add_item(hit2)
        view2.add_item(stand2)

        player_cards = first_card + seconds_card
        dealer_total = dealer1 + dealer2

        if first_card == 11:
            if seconds_card == 11:
                first_card = 1

        if player_cards == 21:
            embed = discord.Embed(title="You Won!", color=discord.Color.green())
            embed.add_field(name="Your Hand", value=f"🃏 21", inline=False)
            embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
            await interaction.response.send_message(embed=embed, view=view2)
            cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank + amount * 2 , interaction.user.id))
            db.commit()
            cursor.close()
            db.close()
            return

        embed = discord.Embed(title="🃏 Black Jack 🃏", color=discord.Color.blue())
        embed.add_field(name="Your Hand", value=f"🃏 {player_cards}", inline=False)
        embed.add_field(name="Dealers Hand", value=f"🃏 *Unknown Cards*")
        await interaction.response.send_message(embed=embed, view=view)

        async def hit_call(interaction:discord.Interaction):
            view3 = View()
            hit.disabled = False
            stand3.disabled = False
            view3.add_item(hit)
            view3.add_item(stand3)
            new_card = random.randint(2,11)
            cards.append(new_card)

            sum = 0;    
            for i in range(0, len(cards)):    
                sum = sum + cards[i];    
            player_cards_ = sum

            if player_cards_ == 21:
                embed = discord.Embed(title="You Won!", color=discord.Color.green())
                embed.add_field(name="Your Hand", value=f"🃏 {player_cards_}", inline=False)
                embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                await interaction.response.edit_message(embed=embed, view=view2)
                cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank + amount * 2 , interaction.user.id))
                db.commit()
                cursor.close()
                db.close()
                return

            elif player_cards_ > 21:
                embed = discord.Embed(title="You Lost", color=discord.Color.red())
                embed.add_field(name="Your Hand", value=f"🃏 {player_cards_}", inline=False)
                embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                await interaction.response.edit_message(embed=embed, view=view2)
                return

            elif player_cards_ < 21:
                embed = discord.Embed(title="🃏 Black Jack 🃏", color=discord.Color.blue())
                embed.add_field(name="Your Hand", value=f"🃏 {player_cards_}", inline=False)
                embed.add_field(name="Dealers Hand", value=f"🃏 *Unknown Cards*")
                await interaction.response.edit_message(embed=embed, view=view3)

                async def stand3_call(interaction:discord.Interaction):
                    dealer_total = random.randint(18, 24)

                    if dealer_total == 21:
                        embed = discord.Embed(title="You Lost", color=discord.Color.red())
                        embed.add_field(name="Your Hand", value=f"🃏 {player_cards_}", inline=False)
                        embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                        await interaction.response.edit_message(embed=embed, view=view2)
                        return

                    if dealer_total > 21:

                        embed = discord.Embed(title="You Won!", color=discord.Color.green())
                        embed.add_field(name="Your Hand", value=f"🃏 {player_cards_}", inline=False)
                        embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                        await interaction.response.edit_message(embed=embed, view=view2)
                        cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank + amount * 2 , interaction.user.id))
                        db.commit()
                        cursor.close()
                        db.close()
                        return

                    if dealer_total > 17:
                        if player_cards_ > dealer_total:
                            embed = discord.Embed(title="You Won!", color=discord.Color.green())
                            embed.add_field(name="Your Hand", value=f"🃏 {player_cards_}", inline=False)
                            embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                            await interaction.response.edit_message(embed=embed, view=view2)
                            cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank + amount * 2 , interaction.user.id))
                            db.commit()
                            cursor.close()
                            db.close()
                            return
                        
                        if dealer_total > player_cards_:
                            embed = discord.Embed(title="You Lost", color=discord.Color.red())
                            embed.add_field(name="Your Hand", value=f"🃏 {player_cards_}", inline=False)
                            embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                            await interaction.response.edit_message(embed=embed, view=view2)
                            return
                        
                        if dealer_total == player_cards_:

                            embed = discord.Embed(title="You Tied", color=discord.Color.red())
                            embed.add_field(name="Your Hand", value=f"🃏 {player_cards_}", inline=False)
                            embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                            await interaction.response.edit_message(embed=embed, view=view2)
                            cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank + amount, interaction.user.id))
                            db.commit()
                            cursor.close()
                            db.close()
                            return

                stand3.callback = stand3_call

        hit.callback = hit_call

        async def stand_call(interaction:discord.Interaction):
            dealer_total = random.randint(18, 24)
            try:
                if dealer_total == 21:
                    embed = discord.Embed(title="You Lost", color=discord.Color.red())
                    embed.add_field(name="Your Hand", value=f"🃏 {player_cards}", inline=False)
                    embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                    await interaction.response.edit_message(embed=embed, view=view2)
                    return

                if dealer_total > 21:

                    embed = discord.Embed(title="You Won!", color=discord.Color.green())
                    embed.add_field(name="Your Hand", value=f"🃏 {player_cards}", inline=False)
                    embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                    await interaction.response.edit_message(embed=embed, view=view2)
                    cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank + amount * 2 , interaction.user.id))
                    db.commit()
                    cursor.close()
                    db.close()
                    return

                if dealer_total > 17:
                    if player_cards > dealer_total:
                        embed = discord.Embed(title="You Won!", color=discord.Color.green())
                        embed.add_field(name="Your Hand", value=f"🃏 {player_cards}", inline=False)
                        embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                        await interaction.response.edit_message(embed=embed, view=view2)
                        cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank + amount * 2 , interaction.user.id))
                        db.commit()
                        cursor.close()
                        db.close()
                        return
                    
                    if dealer_total > player_cards:
                        embed = discord.Embed(title="You Lost", color=discord.Color.red())
                        embed.add_field(name="Your Hand", value=f"🃏 {player_cards}", inline=False)
                        embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                        await interaction.response.edit_message(embed=embed, view=view2)
                        return
                    
                    if dealer_total == player_cards:

                        embed = discord.Embed(title="You Tied", color=discord.Color.red())
                        embed.add_field(name="Your Hand", value=f"🃏 {player_cards}", inline=False)
                        embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                        await interaction.response.edit_message(embed=embed, view=view2)
                        cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank + amount, interaction.user.id))
                        db.commit()
                        cursor.close()
                        db.close()
                        return
            except:
                if dealer_total == 21:
                    embed = discord.Embed(title="You Lost", color=discord.Color.red())
                    embed.add_field(name="Your Hand", value=f"🃏 {player_cards}", inline=False)
                    embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                    await interaction.response.edit_message(embed=embed, view=view2)
                    return

                if dealer_total > 21:

                    embed = discord.Embed(title="You Won!", color=discord.Color.green())
                    embed.add_field(name="Your Hand", value=f"🃏 {player_cards}", inline=False)
                    embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                    await interaction.response.edit_message(embed=embed, view=view2)
                    cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank + amount * 2 , interaction.user.id))
                    db.commit()
                    cursor.close()
                    db.close()
                    return

                if dealer_total > 17:
                    if player_cards > dealer_total:
                        embed = discord.Embed(title="You Won!", color=discord.Color.green())
                        embed.add_field(name="Your Hand", value=f"🃏 {player_cards}", inline=False)
                        embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                        await interaction.response.edit_message(embed=embed, view=view2)
                        cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank + amount * 2 , interaction.user.id))
                        db.commit()
                        cursor.close()
                        db.close()
                        return
                    
                    if dealer_total > player_cards:
                        embed = discord.Embed(title="You Lost", color=discord.Color.red())
                        embed.add_field(name="Your Hand", value=f"🃏 {player_cards}", inline=False)
                        embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                        await interaction.response.edit_message(embed=embed, view=view2)
                        return
                    
                    if dealer_total == player_cards:

                        embed = discord.Embed(title="You Tied", color=discord.Color.red())
                        embed.add_field(name="Your Hand", value=f"🃏 {player_cards}", inline=False)
                        embed.add_field(name="Dealers hand", value=f"🃏 {dealer_total}")
                        await interaction.response.edit_message(embed=embed, view=view2)
                        cursor.execute("UPDATE main SET bank = ? WHERE user_id = ?", (bank + amount , interaction.user.id))
                        db.commit()
                        cursor.close()
                        db.close()
                        return

        stand.callback = stand_call


        db.commit()
        cursor.close()
        db.close()
        return


async def setup(bot):
    await bot.add_cog(bj(bot))