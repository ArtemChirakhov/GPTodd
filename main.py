import asyncio
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

class Cog_Todd(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="chat")
    async def chat(self, message):
        await message.channel.send("Ready to chat")

bot = commands.Bot(command_prefix='/', intents=intents)
TOKEN = open("TOKEN.txt").readline()

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    for guild in bot.guilds:
        print(
            f'{bot.user} подключились к чату:\n'
            f'{guild.name}(id: {guild.id})')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await message.channel.send("Hello")



async def main():
    await bot.add_cog(Cog_Todd(bot))
    await bot.start(TOKEN)


asyncio.run(main())
