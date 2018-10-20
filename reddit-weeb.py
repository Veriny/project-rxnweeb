import discord
from discord.ext import commands
import praw
import random


client = commands.Bot(command_prefix = '#')

client.remove_command('help')

direct = "/home/ubuntu/rxn-weeb-res/"
file = open(direct + "token.txt", 'r')
BOT_TOKEN = file.readline()
file.close()

reddit = praw.Reddit(client_id='Wcu7Lk3PQ9LV1A',
                     client_secret='FBqR2NccNSBrRbLFRy-zaq4PLxY',
                     user_agent='Reaction-Weeb')
@client.event
async def on_ready():
    print("ready to post some weeb shit")

@client.event
async def on_message(message):
    print("Got message")
    if "R/" in message.content.upper():
        print("Got reddit")
        args = message.content.split("/")
        memes_submissions = reddit.subreddit("".join(args[1:])).hot()
        post_to_pick = random.randint(1, 75)
        for i in range(0, post_to_pick):
                submission = next(x for x in memes_submissions if not x.stickied)
        emb = (discord.Embed(description="%s" % submission.url, colour=0x3DF270))
        emb.set_image(url="%s" % submission.url)
        emb.set_author(name="%s" % submission.title)
        await client.send_message(message.channel, embed=emb)
client.run(BOT_TOKEN)
