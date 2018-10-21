import discord
from discord.ext import commands
import praw
import random
import psutil
import os
import urllib
import asyncio

client = commands.Bot(command_prefix = '#/')

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
    await client.change_presence(game=discord.Game(name='#/help for help'))



@client.event
async def on_message(message):
    if message.content == "omae wa mou shindeiru":
        await client.send_message(message.channel, "NANI?!?!?")
    await client.process_commands(message)


@client.event
async def on_message(message):
    print("message sent")
    if message.content.upper().startswith("IM"):
        args = message.content.split(" ")
        await client.send_message(message.channel, "Hi, %s, I'm Reaction-Weeb!" % (" ".join(args[1:])))
        print("Dad")
    if message.content.upper().startswith("I'M"):
        args = message.content.split(" ")
        await client.send_message(message.channel, "Hi, %s, I'm Reaction-Weeb!" % (" ".join(args[1:])))
        print("Dad")
    await client.process_commands(message)


@client.event
async def on_message(message):
    if message.author.id == "195244363339530240":
        await client.send_message(message.channel, "ducking weeb")
    await client.process_commands(message)



# @client.event
# async def on_message(message):
#     if message.content == "#lowhealth":
#         await client.send_message(message.channel, "<@325512357780389889>, <@%s> requires healing!" % (message.author.id))
#     await client.process_commands(message)


@client.command()
async def ping():
    await client.say('I hear you.')


@client.command(pass_context = True)
async def lowhealth(ctx):
    await client.say("<@325512357780389889>, <@%s> requires healing!" % ctx.message.author.id)


@client.command(pass_context = True)
async def kms(ctx):
    emb = (discord.Embed(description="<@%s> wants to die" % ctx.message.author.id, colour=0x3DF270))
    emb.set_image(url="https://i.redditmedia.com/dlqIcnjfOA9CD_S-B4eWEMq1lMbjfuu4gZ973F_-LnI.png?w=576&s=993a9dd2728bf345c9b871427b58e204")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def thisisfine(ctx):
    emb = (discord.Embed(description="<@%s> is fine" % ctx.message.author.id, colour=0x3DF270))
    emb.set_image(url="https://i.kym-cdn.com/entries/icons/mobile/000/018/012/this_is_fine.jpg")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def challenge(ctx):
    emb = (discord.Embed(description="<@%s> respectfully contests that claim." % ctx.message.author.id, colour=0x3DF270))
    emb.set_image(url="http://www.elachieve.org/images/Sec._Dis._Cards_front.jpg")
    await client.say(embed=emb)


@client.command(pass_context = True)
async def hahaha(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://i.redd.it/4ajfe9xdjaf11.gif")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def jazz(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://cdn.discordapp.com/attachments/448673389905838111/503308417297809432/image0.jpg")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def angeryping(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://cdn.discordapp.com/attachments/400525440084738048/487099610205126656/who_pinged_me_1.gif")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def invite(ctx):
    emb = (discord.Embed(description="https://discordapp.com/oauth2/authorize?client_id=456689119662309395&scope=bot&permissions=387072", colour=0x3DF270))
    await client.say(embed=emb)

@client.command(pass_context = True)
async def angery(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://media1.tenor.com/images/d27c7d3ce2a5524d1d9b2683369a32f8/tenor.gif")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def stare(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://cdn.discordapp.com/attachments/440741884013576202/478437581223231497/azustare.png")
    await client.say(embed=emb)

#@client.command(pass_context=True)
#async def highnoon(ctx):
##    url = "http://itshighnoonsomewhere.com/"
##    webpage = urllib.request.urlopen(url)
##    asyncio.sleep(100)
##    html = webpage.read()
##    print(html)
##    soup = BeautifulSoup(html)
#    print("Well now...")
#    display = Display(visible=0, size=(800, 800))
#    display.start()
#    browser = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")
#    browser.get("http://itshighnoonsomewhere.com/")
#    location = browser.find_element_by_class("where")
#    emb = (discord.Embed(description="It's high noon in {}".format(where), colour=0x3DF270))
#    emb.set_author(name = "It's high noon somewhere in the world...")
#    await client.say(embed=emb)


@client.command(pass_context = True)
async def hmmm(ctx):
    emb = (discord.Embed(description="<@%s> had a big thought" % ctx.message.author.id, colour=0x3DF270))
    emb.set_image(url="https://orig00.deviantart.net/3c92/f/2017/106/3/f/ritsu_gets_thinking_by_tsumangokotobuki-db61gpd.png")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def infinitegay(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://cdn.discordapp.com/attachments/387757281812545539/474309377000603648/Screenshot_2018-08-01-15-14-09.png")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def manofculture(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://archive-media.nyafuu.org/wsr/image/1451/88/1451882173413.jpg")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def dial911(ctx):
    emb = (discord.Embed(description="<@%s> is calling the police" % ctx.message.author.id, colour=0x3DF270))
    emb.set_image(url="https://cdn.discordapp.com/attachments/437851940018454528/473511740471115786/image.jpg")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def everyonespam(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://cdn.discordapp.com/attachments/265828729970753537/468754159743795220/ezgif-4-562d8684c9.gif")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def stronk(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="http://pm1.narvii.com/6051/aca49f9f02b38ccd7f6650de9e7c8a5572f365ed_00.jpg")
    await client.say(embed=emb)



@client.command(pass_context = True)
async def fyourself(ctx, userName: discord.User):
    try:
        emb = (discord.Embed(description="<@%s>" % userName.id, colour=0x3DF270))
        emb.set_image(url="https://thumbs.gfycat.com/AncientJoyfulKusimanse-size_restricted.gif")
        await client.say(embed=emb)
    except MissingRequiredArgument:
        emb = (discord.Embed(description = "You probably didn't specify a user!"))
        emb.set_image(url="https://i.imgur.com/wacULpT.gif")
        emb.set_author(name="Something went wrong!")
        await client.say(embed=emb)
        await client.say("```\n %s ```" % str(e))
        await client.say("```\n %s ```" % traceback.format_exc())
        print("Caught error")

@client.event
async def on_command_error(error, ctx):
    print("caught error!")
    # Anything in ignored will return and prevent anything happening.
    msgchannel = ctx.message.channel
    ignored = ("#play", "#summon", "#leave", "#stop")

    if isinstance(error, commands.DisabledCommand):
        emb = (discord.Embed(description = "That command has been disabled."))
        emb.set_image(url="https://i.imgur.com/wacULpT.gif")
        emb.set_author(name="Something went wrong!")
        await client.send_message(msgchannel, embed=emb)
        print("Caught error")

    elif isinstance(error, commands.MissingRequiredArgument):
        emb = (discord.Embed(description = "Specify a user. #command <@user>"))
        emb.set_image(url="https://i.imgur.com/wacULpT.gif")
        emb.set_author(name="Something went wrong!")
        await client.send_message(msgchannel, embed=emb)
        print("Caught error")

    elif isinstance(error, commands.CommandNotFound):
        print("Successfully ignored the command.")
    else:
        emb = (discord.Embed(description = "%s" % str(error)))
        emb.set_image(url="https://i.imgur.com/wacULpT.gif")
        emb.set_author(name="Something went wrong!")
        await client.send_message(msgchannel, embed=emb)
        print("Caught error")

    



@client.command(pass_context = True)
async def noquality(ctx, userName: discord.User):
    emb = (discord.Embed(description="<@%s>" % userName.id, colour=0x3DF270))
    emb.set_image(url="https://i.redditmedia.com/PwDwBZwb2NhxE0xCfkgk1A9rAIzxQWt5fs3aep-HZUs.png?w=1024&s=a03ecdf5598b2623fb9fa6f0076954d2")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def bless(ctx, userName: discord.User):
    emb = (discord.Embed(description="Have a nice day, <@%s>" % userName.id, colour=0x3DF270))
    emb.set_image(url="https://cdn.discordapp.com/attachments/448672224388448257/471896036919738369/image.png")
    await client.say(embed=emb)


@client.command(pass_context = True)
async def sexualselection(ctx, userName: discord.User):
    emb = (discord.Embed(description="<@%s>" % userName.id, colour=0x3DF270))
    emb.set_image(url="https://i.redditmedia.com/4gONvinIEdUGUMPtJvlrBTUh4r4xLPV5hEruyDzT7AA.png?w=682&s=1ac946a7b00a19cda2d4d569c6d8e895")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def kys(ctx, userName: discord.User):
    emb = (discord.Embed(description="<@%s>, there's a better place for you." % userName.id, colour=0x3DF270))
    emb.set_image(url="https://i.imgur.com/Ea7l73m.jpg")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def avatar(ctx, userName: discord.User):
    emb = (discord.Embed(description="<@%s>" % userName.id, colour=0x3DF270))
    emb.set_image(url="%s" % userName.avatar_url)
    await client.say(embed=emb)

@client.command(pass_context = True)
async def status(ctx):
    memebers = 0
    emb = (discord.Embed(description="Reaction-Weeb started off as a joke, but Veriny#0925 decided to take it seriously. Sorta.", colour=0x3DF270))
    emb.set_thumbnail(url="%s" % client.user.avatar_url)
    emb.set_author(name = "Reaction-Weeb")
    emb.add_field(name = "Guilds", value = "Reaction-Weeb is on %s guilds. Please don't add me, I only bring misery." % len(client.servers))
    emb.add_field(name = "CPU usage", value = "%s percent" % psutil.cpu_percent())
    tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])
    emb.add_field(name = "RAM usage", value = """
        Total Memory = {} MB
        Used Memory = {} MB
        Free Memory = {} MB
        """.format(tot_m, used_m, free_m))
    emb.add_field(name = "Library", value = "discord.py")
    emb.add_field(name = "Running on", value = "ubuntu, AWS")
    for server in client.servers:
        for member in server.members:
            memebers += 1
    emb.add_field(name = "Souls in stone (User Count)", value = "%s" % memebers)
    emb.add_field(name = "Special Thanks <3", value = "<@173182884625121281> (Help w/ Bug Fixes), <@461154347280236544> (Help w/ Bug Fixes)")
    emb.set_footer(text = "The most useless discord bot in the world.")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def delet(ctx, userName: discord.User):
    emb = (discord.Embed(description="<@%s>" % userName.id, colour=0x3DF270))
    emb.set_image(url="https://vignette.wikia.nocookie.net/a-hat-in-time/images/1/1a/Delet_this.jpg/revision/latest?cb=20171026150039")
    await client.say(embed=emb)


@client.command(pass_context = True)
async def smug(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://i.pinimg.com/originals/3f/94/5c/3f945cd4b008c5c952d6a0ce792b4da2.jpg")
    await client.say(embed=emb)


@client.command(pass_context = True)
async def what(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://i.redditmedia.com/UZRQ-iXHDsdJMh6ozvJw-6AK6cjzJJOR7lz_AO7IrM0.jpg?w=480&s=e7aee6e7f55d502ece0e9c5386630881")
    await client.say(embed=emb)


@client.command(pass_context = True)
async def shrug(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="http://i.imgur.com/3KZzO9h.png")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def omegadelet(ctx, userName: discord.User):
    emb = (discord.Embed(description="<@%s>" % userName.id, colour=0x3DF270))
    emb.set_image(url="https://pbs.twimg.com/media/DgDvhAuU0AA1NiO.jpg:large")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def stab(ctx, userName: discord.User):
    emb = (discord.Embed(description="<@%s>" % userName.id, colour=0x3DF270))
    emb.set_image(url="https://pbs.twimg.com/media/DgCSun7XkAAh9ji.jpg:large")
    await client.say(embed=emb)


@client.command(pass_context = True)
async def orca(ctx, userName: discord.User):
    emb = (discord.Embed(description="<@%s>" % userName.id, colour=0x3DF270))
    emb.set_image(url="https://pbs.twimg.com/media/DgA5iz9UcAE2UE9.jpg:large")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def dislike(ctx, userName: discord.User):
    emb = (discord.Embed(description="<@%s>" % userName.id, colour=0x3DF270))
    emb.set_image(url="https://pbs.twimg.com/media/DgAcVt4UcAE1y1z.jpg:large")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def disgust(ctx, userName: discord.User):
    emb = (discord.Embed(description="<@%s>" % userName.id, colour=0x3DF270))
    emb.set_image(url="https://i.kym-cdn.com/photos/images/original/001/093/821/a84.jpg")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def delete(ctx, userName: discord.User):
    emb = (discord.Embed(description="<@%s>" % userName.id, colour=0x3DF270))
    emb.set_image(url="https://i.redditmedia.com/oQDHfNh0fotxt4jsos2cH-D0MyUVYH0JH14pgCDfQxA.jpg?w=548&s=4036166d1d3ca9bf3d7327a299968565")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def fyou(ctx, userName: discord.User):
    emb = (discord.Embed(description="<@%s>" % userName.id, colour=0x3DF270))
    emb.set_image(url="https://pbs.twimg.com/media/DgAS2foUcAA5XKu.jpg:large")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def pathetic(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://pbs.twimg.com/media/DgDTOMnX4AA8vjA.jpg:large")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def sigh(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://i.redd.it/8vsv67vqn0511.gif")
    await client.say(embed=emb)

@client.command(pass_context = True)
async def refuse(ctx):
    emb = (discord.Embed(description="", colour=0x3DF270))
    emb.set_image(url="https://pbs.twimg.com/media/C57jpscWUAEErwF.jpg")
    await client.say(embed=emb)


#help command
#@client.command(pass_context = True)
#async def help(ctx):
#    emb = discord.Embed(description="""
#    Here are your commands, <@%s>!
#    #kms- self explanatory
#    #lowhealth- 199/200 HP? Ping Steven for healing.
#    #fyourself <@user>- Rude command to tell someone to frick themself
#    #noquality <@user>- Point out someone's lack of quality
#    #sexualselection <@user>- For people who will fall victim to sexual selection
#    #delet <@user>- When someone posts something weird and deserving of deletion
#    #omegadelet <@user>- DELETE THIS RIGHT NOW
#    #smug- Be smug
#    #what- When someone says something utterly depraved
#    #shrug- Shrug it off...
#    #stab <@user>- Those are bold words for someone in stabbing range...
#    #orca <@user>- When someone needs to stop
#    #dislike <@user>- Everyone disliked that.
#    #disgust <@user>- Be disgusted beyond words.
#    #delete <@user>- Another delete command, but more weeb.
#    #fyou <@user>- Frick you m9
#    #pathetic- pathetic.
#    #sigh- sigh of relief (Thanks to Kyle.C!)
#    #refuse- I REFUSE TO LOSE TO ANIME
#    """ % ctx.message.author.id, colour=0x3DF270)
#    emb.set_author(name="General Commands:")
#    emb2 = discord.Embed(description="""
#    These commands pull random posts from their respective subreddits
#    #me_irl - me_irl
#    #anime_irl - anime_irl
#    #softwaregore - softwaregore
#    #weebmeme - animemes
#    #cute - awww
#    #sad or #depression - 2meirl4meirl
#    #hmmm - hmmm
#    #DiWHY - DiWHY
#        """, colour=0x3DF270)
#    emb2.set_author(name="Reddit Commands:")
#    emb3 = discord.Embed(description="""
#    Want to play some music? Use these commands
#    #summon- Summons Reaction-Weeb to you voice channel
#    #play <Search Terms>- Search youtube for a song and play it (YOU MUST USE #SUMMON FIRST)
#    #volume <number>- Change the volume
#    #stop- Stops the music
#        """)
#    emb3.set_author(name="Music Commands:")
#    await client.say(embed = emb)
#    await client.say(embed = emb2)
#    await client.say(embed = emb3)



@client.command(pass_context = True)
async def help(ctx):
    emb = discord.Embed(description="{}, here are your commands".format(ctx.message.author.mention), colour=0x3DF270)
    emb.set_author(name="Reaction-Weeb's Commands")
    emb.add_field(name="Reddit Commands:", value = """
        r/<any subreddit> -> returns a post from that subreddit
        """)
    emb.add_field(name="Reaction Commands", value= """
        #/kms- self explanatory
        #/kys <@user>
        #/infinitegay
        #/thisisfine
        #/manofculture
        #/lowhealth
        #/fyourself <@user>
        #/noquality <@user>
        #/sexualselection <@user>
        #/delet <@user>
        #/angeryping
        #/omegadelet <@user>
        #/smug- Be smug
        #/what- what
        #/shrug- Shrug
        #/stab <@user>
        #/orca <@user>- When someone needs to stop
        #/dislike <@user>- Everyone disliked that.
        #/disgust <@user>- Be disgusted beyond words.
        #/delete <@user>- delet
        #/fyou <@user>
        #/pathetic
        #/hmmm - the big think
        #/bless <@user>
        #/stronk - flex
        #/dial911
        #/everyonespam - enough spam
        #/jazz
        #/angeryping
        """)
    emb.add_field(name="RPG Commands:", value = """
        #/attack <@user>
        #/refresh - Heals MP and HP
        #/lootbox
        #/search - Get some weeb coins
        #/steal <@user>
        #/stats - Get your stats
        #/snoop <@user> - Get not your stats
        #/inventory
        """)
    emb.add_field(name="Music commands:", value = """
        #/summon - Summon the bot to your music channel
        #/play <song name>
        #/volume <int>
        #/stop
        """)
    emb.add_field(name = "Utility Commands:", value = """
        #avatar <@user>
        #status
        #goodjuju/#badjuju <@user>
        #checkjuju
        """)
    emb.add_field(name = "Canvas Commands:", value = """
        #/canvasid <id>
        #/canvastoken <token>
        #/canvashw
        #/hw <class>""")

    await client.say(embed=emb)

# Reddit Commands



#
#@client.command()
#async def me_irl():
#    memes_submissions = reddit.subreddit('me_irl').hot()
#    post_to_pick = random.randint(1, 50)
#    for i in range(0, post_to_pick):
#        submission = next(x for x in memes_submissions if not x.stickied)
#
#    emb = (discord.Embed(description="r/me_irl", colour=0x3DF270))
#    emb.set_image(url="%s" % submission.url)
#    emb.set_author(name="%s" % submission.title)
#    await client.say(embed=emb)
#
#
#@client.command()
#async def anime_irl():
#    memes_submissions = reddit.subreddit('anime_irl').hot()
#    post_to_pick = random.randint(1, 50)
#    for i in range(0, post_to_pick):
#        submission = next(x for x in memes_submissions if not x.stickied)
#
#    emb = (discord.Embed(description="r/anime_irl", colour=0x3DF270))
#    emb.set_image(url="%s" % submission.url)
#    emb.set_author(name="%s" % submission.title)
#
#    await client.say(embed=emb)
#
#
#@client.command()
#async def softwaregore():
#    memes_submissions = reddit.subreddit('softwaregore').hot()
#    post_to_pick = random.randint(1, 50)
#    for i in range(0, post_to_pick):
#        submission = next(x for x in memes_submissions if not x.stickied)
#
#    emb = (discord.Embed(description="r/softwaregore", colour=0x3DF270))
#    emb.set_image(url="%s" % submission.url)
#    emb.set_author(name="%s" % submission.title)
#
#    await client.say(embed=emb)
#
#
#@client.command()
#async def weebmeme():
#    memes_submissions = reddit.subreddit('Animemes').hot()
#    post_to_pick = random.randint(1, 50)
#    for i in range(0, post_to_pick):
#        submission = next(x for x in memes_submissions if not x.stickied)
#
#    emb = (discord.Embed(description="r/animemes", colour=0x3DF270))
#    emb.set_image(url="%s" % submission.url)
#    emb.set_author(name="%s" % submission.title)
#
#    await client.say(embed=emb)
#
#
#@client.command()
#async def cute():
#    memes_submissions = reddit.subreddit('aww').hot()
#    post_to_pick = random.randint(1, 50)
#    for i in range(0, post_to_pick):
#        submission = next(x for x in memes_submissions if not x.stickied)
#
#    emb = (discord.Embed(description="r/aww", colour=0x3DF270))
#    emb.set_image(url="%s" % submission.url)
#    emb.set_author(name="%s" % submission.title)
#
#    await client.say(embed=emb)
#
#
#@client.command()
#async def depression():
#    memes_submissions = reddit.subreddit('2meirl4meirl').hot()
#    post_to_pick = random.randint(1, 50)
#    for i in range(0, post_to_pick):
#        submission = next(x for x in memes_submissions if not x.stickied)
#
#    emb = (discord.Embed(description="r/2meirl4meirl", colour=0x3DF270))
#    emb.set_image(url="%s" % submission.url)
#    emb.set_author(name="%s" % submission.title)
#
#    await client.say(embed=emb)
#
#
#@client.command()
#async def sad():
#    memes_submissions = reddit.subreddit('2meirl4meirl').hot()
#    post_to_pick = random.randint(1, 50)
#    for i in range(0, post_to_pick):
#        submission = next(x for x in memes_submissions if not x.stickied)
#
#    emb = (discord.Embed(description="r/2meirl4meirl", colour=0x3DF270))
#    emb.set_image(url="%s" % submission.url)
#    emb.set_author(name="%s" % submission.title)
#
#    await client.say(embed=emb)
#
#@client.command()
#async def roses():
#    memes_submissions = reddit.subreddit('boottoobig').hot()
#    post_to_pick = random.randint(1, 50)
#    for i in range(0, post_to_pick):
#        submission = next(x for x in memes_submissions if not x.stickied)
#
#    emb = (discord.Embed(description="r/boottoobig", colour=0x3DF270))
#    emb.set_image(url="%s" % submission.url)
#    emb.set_author(name="%s" % submission.title)
#
#    await client.say(embed=emb)
#
#
#@client.command()
#async def diwhy():
#    memes_submissions = reddit.subreddit('DiWHY')
#    post_to_pick = random.randint(1, 50)
#    for i in range(0, post_to_pick):
#        submission = next(x for x in memes_submissions if not x.stickied)
#    emb = (discord.Embed(description="r/DiWHY", colour=0x3DF270))
#    emb.set_image(url="%s" % submission.url)
#    emb.set_author(name="%s" % submission.title)
#    await client.say(embed=emb)

# @bot.event
# async def on_message(message):
#     if message.author.id == "231245405722116096":
#         await bot.send_message(message.channel, "<@231245405722116096>, go back to League.")
# @bot.event
# async def on_message(message):
#     if message.author.id == "383116010971987971":
#         await bot.send_message(message.channel, "<@383116010971987971>, this is a test.")


client.run(BOT_TOKEN)





#async def send_pages(ctx, pages: list):
#        """Pagniates a message. Requires context argument and a list of pages."""
#
#        message = await ctx.send(embed=pages[0])
#
#        if len(pages) > 1:
#            # adds page selectors to message
#            await message.add_reaction('◀')
#            await asyncio.sleep(1)
#            await message.add_reaction('▶')
#            await asyncio.sleep(1)
#
#        pag = 0
#
#        for _ in range(200):
#        # runs the paginator for 300 seconds
#        try:
#        # waits for a reaction, times out after 2 seconds
#        embed = pages[pag]
#        reaction, user = await ctx.client.wait_for("reaction_add", check=lambda r, u: r.message.id == message.id, timeout=2)
#
#        # checks for reactions, changes page depending on the reaction
#        if reaction.emoji == '◀' and pag > 0:
#        pag = pag - 1
#        embed = pages[pag]
#        elif reaction.emoji == '▶' and len(pages) - 1 > pag:
#        pag = pag + 1
#        embed = pages[pag]
#
#        # updates the message with the new page if a reaction is received
#        # raises an exception if no reaction is received
#        await message.edit(embed=embed)
#
#        # removes the users reaction
#        await message.remove_reaction(reaction.emoji, user)
#        except asyncio.TimeoutError:
#        # the bot will ignore timeout errors caused by the "wait for" event
#        pass
#
#        # clears reactions when finished
#        await message.clear_reactions()
#
#    
