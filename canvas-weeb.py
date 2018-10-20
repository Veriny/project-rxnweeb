import discord
from discord.ext.commands import bot
from discord.ext import commands
import json
import random
import math
from canvasapi import Canvas
import asyncio

client = discord.Client()
bot = commands.Bot(command_prefix = "#/")
bot.remove_command('help')
direct = "/home/ubuntu/rxn-weeb-res/"
file = open(direct + "token.txt", 'r')
BOT_TOKEN = file.readline()
file.close()


async def update_data(users, user):
    if not user.id in users:
        users[user.id] = {}
        users[user.id]['token'] = 0
        users[user.id]['ID'] = 0

@bot.command(pass_context=True)
async def canvastoken(ctx):
    with open(direct + 'canvas.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, ctx.message.author)
    args = ctx.message.content.split(" ")
    users[ctx.message.author.id]['token'] = (args[1])
    await bot.say("""Token successfully added to database \n **Your token may or may not be valid - If #/canvashw fails, it may be because your token is invalid.**
        """)
    with open('canvas.json', 'w' ) as f:
        json.dump(users, f)

@bot.command(pass_context=True)
async def canvasid(ctx):
    with open(direct + 'canvas.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, ctx.message.author)
    args = ctx.message.content.split(" ")
    users[ctx.message.author.id]['ID'] = args[1]
    await bot.say("""ID successfully added to database \n **Your ID may or may not be valid - If #/canvashw fails, it may be because your ID is invalid.**
        """)
    with open(direct + 'canvas.json', 'w' ) as f:
        json.dump(users, f)

@bot.command(pass_context=True)
async def canvashw(ctx):
    with open(direct + 'canvas.json', 'r') as f:
        users = json.load(f)
    # Import the Canvas class
    await update_data(users, ctx.message.author)
    emb = discord.Embed(description = "Please wait, Reaction-Weeb is sending a request to canvas...", colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
    await bot.say(embed=emb)
    id = users[ctx.message.author.id]['ID']
    token = users[ctx.message.author.id]['token']
    API_URL = "https://smuhsd.instructure.com/api/v1/courses"
    # Canvas API key
    API_KEY = token
    canvas = Canvas(API_URL, API_KEY)
    #the magic happens here
    user = canvas.get_user(int(id))
    print(id)
    async def printassigns(course):
        ass = course.get_assignments()
        m = list(ass)
        q = m[-5:]
        q.reverse()
        string = ""
        for assignment in q:
            string = string + ("%s \n" % assignment)
        emb = discord.Embed(description = string, colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
        emb.set_author(name = "{} ({})".format(course.name, course.id))
        await bot.say(embed = emb)
    courses = user.get_courses()
    for c in courses:
        print(c.name)
        await printassigns(c)
    emb = discord.Embed(description = "Enjoy your homework <3", colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
    await bot.say(embed=emb)
    with open(direct + 'canvas.json', 'w' ) as f:
        json.dump(users, f)


#@bot.command
#async def canvassearch(ctx):
#    with open('canvas.json', 'r') as f:
#        users = json.load(f)
#    #Code
#    args = ctx.message.content.split(" ")
#    query = args[1:]
#    emb = discord.Embed(description = "Please wait, Reaction-Weeb is sending a request to canvas...", colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
#    await bot.say(embed=emb)
#    id = users[ctx.message.author.id]['ID']
#    token = users[ctx.message.author.id]['token']
#    API_URL = "https://smuhsd.instructure.com/api/v1/courses"
#    # Canvas API key
#    API_KEY = token
#    canvas = Canvas(API_URL, API_KEY)
#    user = canvas.get_user(id)
#    courses = user.courses
#    cout = 0
#    for course in courses:
#        if query.upper() in course.name.upper():
#            printassigns(course)
#    async def printassigns(course):
#        ass = course.get_assignments()
#        m = list(ass)
#        q = m[-10:]
#        q.reverse()
#        string = ""
#        for assignment in q:
#            string = string + ("%s \n" % assignment)
#        emb = discord.Embed(description = string, colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
#        emb.set_author(name = "{} ({})".format(course.name, course.id))
#        await bot.say(embed = emb)
#
#
#    with open('canvas.json', 'w' ) as f:
#        json.dump(users, f)



@bot.event
async def on_command_error(error, ctx):
    print("caught error!")
    # Anything in ignored will return and prevent anything happening.
    msgchannel = ctx.message.channel
    if isinstance(error, commands.DisabledCommand):
        emb = (discord.Embed(description = "That command has been disabled."))
        emb.set_image(url="https://i.imgur.com/wacULpT.gif")
        emb.set_author(name="Something went wrong!")
        await bot.send_message(msgchannel, embed=emb)
        print("Caught error")

    elif isinstance(error, commands.MissingRequiredArgument):
        emb = (discord.Embed(description = "Specify a user. #command <@user>"))
        emb.set_image(url="https://i.imgur.com/wacULpT.gif")
        emb.set_author(name="Something went wrong!")
        await bot.send_message(msgchannel, embed=emb)
        print("Caught error")

    elif isinstance(error, commands.CommandNotFound):
        print("Successfully ignored the command.")
    else:
        emb = (discord.Embed(description = "There was an error. Please contact Veriny or try reentering your bot token and user ID. For other reaction-weeb related help, please try #/help"))
        emb.set_image(url="https://i.imgur.com/wacULpT.gif")
        emb.set_author(name="%s" % str(error))
        await bot.send_message(msgchannel, embed=emb)
        # await bot.send_message(msgchannel, embed=emb)
        print("Caught error")

@bot.command(pass_context=True)
async def grades(ctx):
    with open(direct + 'canvas.json', 'r') as f:
        users = json.load(f)
    # Import the Canvas class
    await update_data(users, ctx.message.author)
    emb = discord.Embed(description = "Please wait, Reaction-Weeb is sending a request to canvas...", colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
    await bot.say(embed=emb)
    id = users[ctx.message.author.id]['ID']
    token = users[ctx.message.author.id]['token']
    API_URL = "https://smuhsd.instructure.com/api/v1/courses"
    # Canvas API key
    API_KEY = token
    canvas = Canvas(API_URL, API_KEY)
    #the magic happens here
    user = canvas.get_user(int(id))
    en = user.get_enrollments()
    emb = discord.Embed(description="%s's report card" % ctx.message.author.mention, colour= discord.Color(random.randint(0x000000, 0xFFFFFF)))
    emb.set_author(name="No straight A++, no meal for a week.")
    for e in en:
        Name = canvas.get_course(e.course_id).name
        grade = e.grades['current_score']
        if grade == None:
            verdict = ""
        else:
            if grade > 93:
                verdict = "A"
            else:
                verdict = "F"
        emb.add_field(name = Name, value = "{} | {}".format(verdict, grade))
    await bot.say(embed=emb)
    with open(direct + 'canvas.json', 'w' ) as f:
            json.dump(users, f)


bot.run(BOT_TOKEN)

