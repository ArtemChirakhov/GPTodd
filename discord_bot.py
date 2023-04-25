import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from chatgpt import chatgpt_response


load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

class Client_bot(commands.Cog):
    @commands.command()
    async def ai(self, ctx, message):
        bot_response = chatgpt_response(prompt=message)
        await ctx.send(bot_response)
'''    async def on_message(self, message):
        print(message.content)
        if message.author == self.user:
            return
        command, user_message = None, None
        for text in ['/ai', '/bot']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                user_message = message.content.replace(text, '')

        if command == '/ai' or command == '/bot':
            bot_response = chatgpt_response(prompt=user_message)
            await message.channel.send(f'{bot_response}')'''
