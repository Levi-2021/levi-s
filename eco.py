from discord.ext import commands
import sqlite3

class eco(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS main (
            user_id INTERGER, wallet INTERGER, bank INTERGER
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS animals (
            "user_id", "fox", "wolf", "cat", "raccoon", "tiger", "Lion", "leapard", "deer", "zebra", "unicorn"
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS tools (
            "user_id", "pistol", "rod", "pick", "anti_rob_token"
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS fish(
            "user_id", "normal_fish", "tropical_fish", "fish_cake", "blowfish"
        )''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS mine(
            "user_id", "coal", "copper", "iron", "gold", "diamond"
        )''')


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        
        author = message.author
        db = sqlite3.connect("main.sqlite")
        cursor = db.cursor()
        cursor.execute(f"SELECT user_id FROM main WHERE user_id = {author.id}")
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO main(user_id, wallet, bank) VALUES(?, ?, ?)", (author.id, 0, 1000))
        
        cursor.execute(f"SELECT user_id FROM tools WHERE user_id = {author.id}")
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO tools (user_id, pistol, rod, pick, anti_rob_token) VALUES (?,?,?,?,?)", (author.id, 1, 1, 1, 1))
        
        cursor.execute(f"SELECT user_id FROM animals WHERE user_id = {author.id}")
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO animals(user_id, fox, wolf, cat, raccoon, tiger, Lion, leapard, deer, zebra, unicorn) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (author.id, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))

        cursor.execute(f"SELECT user_id FROM fish WHERE user_id = {author.id}")
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO fish (user_id, normal_fish, tropical_fish, fish_cake, blowfish ) VALUES (?,?,?,?,?)", (author.id, 0, 0, 0, 0))

        cursor.execute(f"SELECT user_id FROM mine WHERE user_id = {author.id}")
        result = cursor.fetchone()
        if result is None:
            cursor.execute("INSERT INTO mine (user_id, coal, copper, iron, gold, diamond) VALUES (?,?,?,?,?,?)", (author.id, 0, 0, 0, 0, 0))

        
        
        db.commit()
        cursor.close()
        db.close()
        
async def setup(bot):
    await bot.add_cog(eco(bot))