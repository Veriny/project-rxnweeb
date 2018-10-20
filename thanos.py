import discord
from discord.ext import commands
# import praw
import random
import asyncio
#usertest

client = commands.Bot(command_prefix = '#/')
direct = "/home/ubuntu/rxn-weeb-res/"
file = open(direct + "token.txt", 'r')
BOT_TOKEN = file.readline()
file.close()

@client.event
async def on_message(message):
    print("message detected")
    if "Join the ongoing SCP-3008 game to use game commands." in message.content and message.author.id == '402648842438311946':
        await client.send_message(message.channel, "+3008.join")
    await client.process_commands(message)

@client.command(pass_context = True)
async def angrypings(ctx):
    for i in range (1, 10000):
        await client.say("<@287439639130800130> DO WE NEED TO PRINT OUR NOTES")
        await asyncio.sleep(3)





#@client.command(pass_context = True)
#async def summon(ctx):
#    channel = ctx.message.author.voice.voice_channel
#    await client.join_voice_channel(channel)
#    emb = (discord.Embed(description="I have entered the voice channel %s" % ctx.message.author.voice.voice_channel, colour=0x3DF270))
#    emb.set_author(name="Alert")
#
#    await client.say(embed=emb)
#
#
#@client.command(pass_context = True)
#async def leave(ctx):
#    server = ctx.message.server
#    voice_client = client.voice_client_in(server)
#    await voice_client.disconnect()
#    emb = (discord.Embed(description="I have left the voice channel.",
#                         colour=0x3DF270))
#    emb.set_author(name="Alert")
#    await client.say(embed=emb)
#
#
#@client.command(pass_context = True)
#async def snap(ctx):
#    emb = (discord.Embed(description="Hear me and rejoice! You have had the privilege of being saved by Reaction-Weeb. Daniel Z, Your Mother, Alex, Jeremy, Brian, Andrew, you may think this is suffering. No... it is salvation. The universal scales tip toward balance because of your sacrifice. Smile... for even in death, you have become children of Thanos.", colour=0x3DF270))
#    emb.set_image(url="https://i.redditmedia.com/T__GG9xyW-YuX1a4KU152MjQf8fZti1enmkpllRk8JI.jpg?w=990&s=8ba79bcfceaee17c22fe2f0db51d27f6")
#    emb.set_author(name="With all the Infinity Stones, I shall bring balance to Bad Midnight Crewju")
#    await client.say(embed=emb)
#    #await client.kick(ctx.message.server.get_member('195244363339530240')) #kawaiibottest
#    await client.kick(ctx.message.server.get_member('198666284806832128')) #Daniel Z.
#    await client.kick(ctx.message.server.get_member('391388122732167178')) #AlexA
#    await client.kick(ctx.message.server.get_member('421145267732217856')) #Jeremy
#    #await client.kick(ctx.message.server.get_member('402162742536044554')) Brian
#    await client.kick(ctx.message.server.get_member('333836140752666627')) #Andrew
#    await client.kick(ctx.message.server.get_member('458488732006481930')) #Your Mother
#    #emb.set_author(name="With all the Infinity Stones, I shall bring balance to Bad Midnight Crewju.")
client.run(BOT_TOKEN)
