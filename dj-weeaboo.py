import discord
from discord.ext import commands
# import praw
import random
from bs4 import BeautifulSoup
import urllib
import youtube_dl


client = commands.Bot(command_prefix = '#/')
client.remove_command('help')

direct = "/home/ubuntu/rxn-weeb-res/"
file = open(direct + "token.txt", 'r')
BOT_TOKEN = file.readline()
file.close()


#discord.opus.load_opus()
players = {}
reactplayers = {}
queues = {}
songnames = {}
songstates = {}
def songstatesfalse(id):
    songstates[id] = False
    print("Success")
def songstatestrue(id):
    songstates[id] = True

#global isSongPlaying
#isSongPlaying = False
#
#def noSongPlaying():
#    isSongPlaying = False
#def checkSongPlaying():
#    return isSongPlaying
#def setSongPlaying():
#    isSongPlaying = True

#def checkQueue(id):
#    print("running!")
#    if queues[id] != []:
#        print("preparing to play")
#        player = queues[id].pop(0)
#        name = songnames[id].pop(0)
#        players[id] = player
#        player.start()
#        emb = (discord.Embed(description="Playing %s" % name, colour=0x3DF270))
#        emb.set_author(name="Oh, oh, oh, time to ACCELERATE!")
#        emb.set_image(url="https://i.redditmedia.com/lbzVawWH28H24h5W2K7xp4FwSLkmcsf9YTtCpPha5LA.jpg?w=1024&s=248fb824508b404bb84de45efc12d185")


@client.command(pass_context = True)
async def summon(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    emb = (discord.Embed(description="I have entered the voice channel %s" % ctx.message.author.voice.voice_channel, colour=0x3DF270))
    emb.set_author(name="Alert")
    await client.say(embed=emb)

@client.event
async def on_ready():
    print("ready to play some weeb music")
    await client.say("time to play some weeb music.")



@client.command(pass_context = True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
    emb = (discord.Embed(description="I have left the voice channel.",
                         colour=0x3DF270))
    emb.set_author(name="Alert")
    await client.say(embed=emb)


@client.command()
async def test():
    await client.say("This bot is still operational.")


@client.command(pass_context=True)
async def play(ctx):
    if ctx.message.server.id not in songstates:
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        args = ctx.message.content.split(" ")
        query = urllib.parse.quote(" ".join(args[1:]))
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        vids = []
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            vids.append('https://www.youtube.com' + vid['href'])
        player = await voice_client.create_ytdl_player(vids[0], after= lambda: songstatesfalse(ctx.message.server.id))
        players[server.id] = player
        songstates[server.id] = True
        print(songstates[server.id])
        player.start()
        songstatestrue(id)
        print(songstates[server.id])
        emb = (discord.Embed(description="Playing %s" % " ".join(args[1:]), colour=0x3DF270))
        emb.set_author(name="Oh, oh, oh, time to ACCELERATE!")
        emb.set_image(url="https://i.redditmedia.com/lbzVawWH28H24h5W2K7xp4FwSLkmcsf9YTtCpPha5LA.jpg?w=1024&s=248fb824508b404bb84de45efc12d185")
        await client.say(embed=emb)
    elif songstates[ctx.message.server.id] == False:
        server = ctx.message.server
        voice_client = client.voice_client_in(server)
        args = ctx.message.content.split(" ")
        query = urllib.parse.quote(" ".join(args[1:]))
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        vids = []
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
            vids.append('https://www.youtube.com' + vid['href'])
        player = await voice_client.create_ytdl_player(vids[0], after= lambda: songstatesfalse(ctx.message.server.id))
        players[server.id] = player
        player.start()
        songstates[server.id] = True
        print(songstates[server.id])
        songstatestrue(id)
        print(songstates[server.id])
        emb = (discord.Embed(description="Playing %s" % " ".join(args[1:]), colour=0x3DF270))
        emb.set_author(name="Oh, oh, oh, time to ACCELERATE!")
        emb.set_image(url="https://i.redditmedia.com/lbzVawWH28H24h5W2K7xp4FwSLkmcsf9YTtCpPha5LA.jpg?w=1024&s=248fb824508b404bb84de45efc12d185")
        await client.say(embed = emb)
    else:
        emb = (discord.Embed(description = "There are many possibilities for why an error occurred"))
        emb.set_image(url="https://i.imgur.com/wacULpT.gif")
        emb.set_author(name="Something went wrong!")
        emb.add_field(name="Song already playing", value = "Unfortunately, Reaction-Weeb's creator cannot afford a better ECS,and Reaction-Weeb is given a very limited amount of disk space. Therefore, it is unwise to implement a queue system to the bot.")
        emb.add_field(name="Reaction-Weeb is not in a voice channel", value = "Please enter a voice channel and use #summon to add Reaction-Weeb")
        emb.add_field(name="You aren't in a voice channel.", value = "Music won't play when you're not in a voice channel, genius.")
        await client.say(embed=emb)




#    if ctx.message.server.id in queues and ctx.message.server.id in songnames:
#        queues[ctx.message.server.id].append(player)
#        songnames[ctx.message.server.id].append("%s" % " ".join(args[1:]))
#        if len(queues[ctx.message.server.id]) > 0:
#            emb = (discord.Embed(description="%s added to queue" % " ".join(args[1:]), colour=0x3DF270))
#            emb.set_author(name="Alert")
#            await client.say(embed=emb)
#        else:
#            checkQueue(ctx.message.server.id)
#    else:
#        queues[ctx.message.server.id] = [player]
#        songnames[ctx.message.server.id] = [player]


@client.command(pass_context = True)
async def volume(ctx, volume):
    id = ctx.message.server.id
    players[id].volume = int(volume) / 100
    emb = (discord.Embed(description="Volume changed to %s" % volume,
                     colour=0x3DF270))
    emb.set_author(name="Alert")
    await client.say(embed=emb)



@client.command(pass_context = True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()
    emb = (discord.Embed(description="I have ceased making noise.",
                     colour=0x3DF270))
    emb.set_author(name="Alert")
    await client.say(embed=emb)

#@client.event
#async def on_command_error(error, ctx):
#    print("caught error!")
#    # Anything in ignored will return and prevent anything happening.
#    msgchannel = ctx.message.channel
#    ignored = ("#play", "#summon", "#leave", "#stop")
#
#    if isinstance(error, commands.CommandInvokeError):
#        emb = (discord.Embed(description = "There are many possibilities for why an error occurred"))
#        emb.set_image(url="https://i.imgur.com/wacULpT.gif")
#        emb.set_author(name="Something went wrong!")
#        emb.add_field(name="Song already playing", value = "Unfortunately, Reaction-Weeb's creator cannot afford a better ECS,and Reaction-Weeb is given a very limited amount of disk space. Therefore, it is unwise to implement a queue system to the bot.")
#        emb.add_field(name="Reaction-Weeb is not in a voice channel", value = "Please enter a voice channel and use #summon to add Reaction-Weeb")
#        emb.add_field(name="You aren't in a voice channel.", value = "Music won't play when you're not in a voice channel, genius.")
#        await client.send_message(msgchannel, embed=emb)
#
#        print("Caught error")



client.run(BOT_TOKEN)
