from discord_bot import TOKEN, Client_bot
from music import Music
import discord
from discord.ext import commands
import asyncio
from zipfile import ZipFile


async def main():
    with ZipFile('ffmpeg.zip') as myzip:
        myzip.extractall(path=None, members=None, pwd=None)
    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='!', intents=intents)
    await bot.add_cog(Client_bot(bot))
    await bot.add_cog(Music(bot))
    await bot.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(main())
