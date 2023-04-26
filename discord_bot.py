import discord
import base64
from discord.ext import commands
import os
from chatgpt import chatgpt_response


TOKEN = input('Enter Discord token')

class Client_bot(commands.Cog):
    @commands.command()
    async def ai(self, ctx, messege):
        bot_response = chatgpt_response(prompt=messege)
        await ctx.send(bot_response)

