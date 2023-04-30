import discord
from discord.ext import commands
from yt_dlp import YoutubeDL


class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.is_playing = False
        self.is_paused = False
        self.queue = []
        self.YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
        self.FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5',
                               'options': '-vn'}
        self.voicechannel = None

    def youtube_search(self, item):
        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                info = ydl.extract_info("ytsearch:%s" % item, download=False)['entries'][0]
            except Exception:
                return False
        print(info['formats'][8]['url'])
        return {'source': info['formats'][8]['url'], 'title': info['title']}

    def playing_next(self):
        if len(self.queue) > 0:
            self.is_playing = True
            link = self.queue[0][0]['source']
            self.queue.pop(0)
            self.voicechannel.play(discord.FFmpegPCMAudio(link, **self.FFMPEG_OPTIONS), after=lambda e: self.playing_next())
        else:
            self.is_playing = False

    async def music_play(self, ctx):
        if len(self.queue) > 0:
            self.is_playing = True
            link = self.queue[0][0]['source']
            if not self.voicechannel.is_connected() or self.voicechannel == None:
                self.voicechannel = await self.queue[0][1].connect()
                if self.voicechannel == None:
                    await ctx.send("Не могу подключится к каналу")
                    return
            else:
                await self.voicechannel.move_to(self.queue[0][1])

            self.queue.pop(0)
            self.voicechannel.play(discord.FFmpegPCMAudio(link, **self.FFMPEG_OPTIONS), after=lambda e: self.playing_next())
        else:
            self.is_playing = False

    @commands.command(name="play", aliases=["p", "playing"], help="Играет музыку из видео на ютубе")
    async def play(self, ctx, *args):
        query = " ".join(args)
        voice_channel = ctx.author.voice.channel
        if voice_channel is None:
            await ctx.send("Подключён к каналу")
        elif self.is_paused:
            self.voicechannel.resume()
        else:
            song = self.youtube_search(query)
            if type(song) == type(True):
                await ctx.send(
                    "Не могу скачать песню")
            else:
                await ctx.send("Песня добавлена в очередь")
                self.queue.append([song, voice_channel])
                if self.is_playing == False:
                    await self.music_play(ctx)

    @commands.command(name="pause", help="Ставит музыку на паузу")
    async def pause(self, ctx, *args):
        if self.is_playing:
            self.is_playing = False
            self.is_paused = True
            self.voicechannel.pause()
        elif self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.voicechannel.resume()

    @commands.command(name="resume", aliases=["r"], help="Возобновляет проигрывание музыкт")
    async def resume(self, ctx, *args):
        if self.is_paused:
            self.is_paused = False
            self.is_playing = True
            self.voicechannel.resume()

    @commands.command(name="skip", aliases=["s"], help="Пропусает музыку")
    async def skip(self, ctx):
        if self.voicechannel != None and self.voicechannel:
            self.voicechannel.stop()
            await self.music_play(ctx)

    @commands.command(name="queue", aliases=["q"], help="Показывает количество песен в очереди")
    async def queue(self, ctx):
        value = ""
        for i in range(0, len(self.queue)):
            if (i > 4): break
            value += self.queue[i][0]['title'] + "\n"
        if value != "":
            await ctx.send(value)
        else:
            await ctx.send("No music in queue")

    @commands.command(name="clear", aliases=["c", "bin"], help="Очищает очередь и музыку")
    async def clear(self, ctx):
        if self.voicechannel != None and self.is_playing:
            self.voicechannel.stop()
        self.queue = []
        await ctx.send("Music queue cleared")

    @commands.command(name="leave", aliases=["disconnect", "l", "d"], help="Выйти из канала")
    async def dc(self, ctx):
        self.is_paused = False
        self.is_playing = False
        await self.voicechannel.disconnect()
