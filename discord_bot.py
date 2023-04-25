import discord
import base64
from discord.ext import commands
import os
from dotenv import load_dotenv
from chatgpt import chatgpt_response


load_dotenv()

TOKEN = base64.b64decode(os.getenv('DISCORD_TOKEN')).decode('utf-8')

class Client_bot(commands.Cog):
    @commands.command()
    async def ai(self, ctx, messege):
        bot_response = chatgpt_response(prompt=messege)
        await ctx.send(bot_response)

