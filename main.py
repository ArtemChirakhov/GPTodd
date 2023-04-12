import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

class Cog_Todd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print("Cog is ready")

    @commands.command(name="chat")
    async def chat(self, message):
        if message.author == bot.user:
            return
        await message.channel.send("Ready to chat")
        self.chat = True

class Client_Todd(discord.Client):
    async def on_ready(self):
        print("Bot is ready")

    async def on_message(self, message):
        if message.author == self.user:
            return
        message.channel.send("Hello")

bot = commands.Bot(command_prefix='/', intents=intents)
TOKEN = open("TOKEN.txt").readline()

async def main():
    await bot.add_cog(Cog_Todd(bot))
    await bot.start(TOKEN)


asyncio.run(main())
