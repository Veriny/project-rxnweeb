import discord
from discord.ext import commands
# import praw
import random


client = commands.Bot(command_prefix ="#")

client.remove_command('help')

direct = "/home/ubuntu/rxn-weeb-res/"
file = open(direct + "token.txt", 'r')
BOT_TOKEN = file.readline()
file.close()


@client.event
async def on_ready():
    print("ready to post some weeb shit")

@client.event
async def on_message(message):
    if message.author.id == "287439639130800130":    
        emb = (discord.Embed(description="<@287439639130800130>", colour=0x3DF270))
        emb.set_image(url="https://pbs.twimg.com/media/DgA5iz9UcAE2UE9.jpg:large")
        await client.say(embed=emb)

#@client.event
#async def on_message(message):
#    print("message detected")
#    if "NICE" in message.content.upper():
#        if message.content == "Nice.":
#            await client.add_reaction(message, '\u2B06')
#        else:
#            await client.add_reaction(message, '\u2B07')
#    if message.content.upper().startswith("|'M"):
#        args = message.content.split(" ")
#        await client.send_message(message.channel, "Hi, %s, I'm Reaction-Weeb!" % (" ".join(args[1:])))
#    if message.content.upper().startswith("L'M"):
#        args = message.content.split(" ")
#        await client.send_message(message.channel, "Hi, %s, I'm Reaction-Weeb!" % (" ".join(args[1:])))
#    if message.content.upper().startswith("|M"):
#        args = message.content.split(" ")
#        await client.send_message(message.channel, "Hi, %s, I'm Reaction-Weeb!" % (" ".join(args[1:])))
#    if message.content.upper().startswith("IM"):
#        args = message.content.split(" ")
#        await client.send_message(message.channel, "Hi, %s, I'm Reaction-Weeb!" % (" ".join(args[1:])))
#        print("Dad")
#    if message.content.upper().startswith("I'M"):
#        args = message.content.split(" ")
#        await client.send_message(message.channel, "Hi, %s, I'm Reaction-Weeb!" % (" ".join(args[1:])))
#        print("Dad")
#    if message.content.upper().startswith("LM"):
#        args = message.content.split(" ")
#        await client.send_message(message.channel, "Hi, %s, I'm Reaction-Weeb!" % (" ".join(args[1:])))
#    await client.process_commands(message)




client.run(BOT_TOKEN)
