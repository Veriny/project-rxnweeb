import discord
from discord.ext.commands import bot
from discord.ext import commands
import json
import random
import math

client = discord.Client()
bot = commands.Bot(command_prefix = "#/")
bot.remove_command('help')
direct = "/home/ubuntu/rxn-weeb-res/"
file = open(direct + "token.txt", 'r')
BOT_TOKEN = file.readline()
file.close()

itemNames = ['0', 'Nut', 'Thunder Bomb', 'Magic Gelatin', 'Big City Burger', 'Beefsteak', 'Mystical Stick', '7', '8', '9', '10', '11', '12', '13', '14', 'HP UP', 'MP UP', 'Egg of Light', 'Magic Cake', 'Lucky Stick', '20', '21', '22', '23', '24', 'Flex Tape', 'Luxury Banana', 'UFO', 'No-U Noodles', 'LootBox', 'Common Lootbox', 'Epic Lootbox', 'Legendary Lootbox']
itemImgs = ['0',
             '1',
             '2',
             '3',
             '4',
             '5',
             '6',
             '7',
             '8',
             '9',
             '10',
             '11',
             '12',
             '13',
             '14',
             '15',
             '16',
             '17',
             '18',
             '19',
             '20',
             '21',
             '22',
             '23',
             '24',
             'https://cf3.s3.souqcdn.com/item/2017/03/27/22/31/62/00/item_XL_22316200_30168803.jpg', #Flex Tape (Item 25)
             'https://vignette.wikia.nocookie.net/earthbound/images/c/cd/Luxury_Banana_Inventory.png/revision/latest?cb=20110611033706', #Luxury Banana (Item 26)
             '27',
             'https://vignette.wikia.nocookie.net/earthbound/images/d/d3/CupOfLifenoodles.png/revision/latest?cb=20150809113803', #NO-U Noodles (Item 28)
             '29',
             '30',
             '31',
             '32']
NUMBER_OF_COMMONS = 6
NUMBER_OF_RARES = 19
NUMBER_OF_LEGENDARIES = 28

@bot.event
async def on_ready():
    print('Ready to give out some spicy XP')

@bot.event
async def on_member_join(member):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code

    await update_data(users, member)

    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)

@bot.event
async def on_command_error(error, ctx):
    print("caught error!")
    # Anything in ignored will return and prevent anything happening.
    msgchannel = ctx.message.channel
    ignored = ("#play", "#summon", "#leave", "#stop")

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
        emb = (discord.Embed(description = "There was an error."))
        emb.set_image(url="https://i.imgur.com/wacULpT.gif")
        emb.set_author(name="Something went wrong!")
        # await bot.send_message(msgchannel, embed=emb)
        await bot.send_message(msgchannel, "``` %s ```" % str(error))
        print("Caught error")

@bot.event
async def on_message(message):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, message.author)
    await add_experience(users, message.author, randomNumber())
    await level_up(users, message.author, message.channel)
    
    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)
    print("got message")
    await bot.process_commands(message)


@bot.command(pass_context = True)
async def resetstats(ctx):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, ctx.message.author)
    users[ctx.message.author.id]['experience'] = 0
    users[ctx.message.author.id]['level'] = 1
    users[ctx.message.author.id]['MaxHP'] = 1200
    users[ctx.message.author.id]['MaxMP'] = 70
    users[ctx.message.author.id]['HP'] = 1200
    users[ctx.message.author.id]['MP'] = 70

    await bot.say("stats reset")

    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)

@bot.command(pass_context = True)
async def snoop(ctx, userName: discord.User):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, userName)
    await update_data(users, ctx.message.author)
    await get_stats(users, userName, ctx.message.channel)
    
    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)

@bot.command(pass_context = True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def goodjuju(ctx, userName: discord.User):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, userName)
    await update_data(users, ctx.message.author)
    if userName == ctx.message.author:
        await bot.say("Nice try. You vain bastard.")
    else:
        users[userName.id]['Item32'] += 1
        emb = discord.Embed(description = "{} got a Good Juju from {}. {} has recieved {} Good Jujus in the past.".format(userName.mention, ctx.message.author.mention, userName.mention, users[userName.id]['Item32']))
        emb.set_image(url="https://i.imgur.com/bn2FyN3.gif")
        emb.set_author(name = "Good Juju!")
        await bot.say(embed = emb)

    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)

@bot.command(pass_context = True)
@commands.cooldown(1, 60, commands.BucketType.user)
async def badjuju(ctx, userName: discord.User):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, userName)
    await update_data(users, ctx.message.author)
    if userName == ctx.message.author:
        await bot.say("Nice try. Do you hate yourself?")
    else:
        users[userName.id]['Item31'] += 1
        emb = discord.Embed(description = "{} got a Bad Juju from {}. {} has recieved {} Bad Jujus in the past.".format(userName.mention, ctx.message.author.mention, userName.mention, users[userName.id]['Item31']))
        emb.set_image(url="https://i.kym-cdn.com/photos/images/original/001/168/989/4e1.png")
        emb.set_author(name = "Bad Juju!")
        await bot.say(embed = emb)
    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)

@bot.command(pass_context = True)
async def checkjuju(ctx):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, ctx.message.author)
    person = ctx.message.author
    badJujus = users[person.id]['Item31']
    goodJujus = users[person.id]['Item32']
    try:
        ratio = goodJujus / badJujus
    except ZeroDivisionError:
        ratio = 1
    emb = discord.Embed(description = "How is your juju?")
    emb.add_field(name = "Good Jujus Recieved", value = goodJujus)
    emb.add_field(name = "Bad Jujus Recieved", value = badJujus)

    if ratio >= .70:
        emb.set_author(name="People seem to like you!")
    elif .30 <= ratio < .70:
        emb.set_author(name="Idk, people seem indifferent towards you.")
    else:
        emb.set_author(name="People seem to hate you!")

    await bot.say(embed = emb)
    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)


@bot.command(pass_context = True)
async def stats(ctx):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, ctx.message.author)
    await get_stats(users, ctx.message.author, ctx.message.channel)
    
    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)


@bot.command(pass_context = True)
@commands.cooldown(1, 600, commands.BucketType.user)
async def refresh(ctx):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, ctx.message.author)
    await refresh(users, ctx.message.author, ctx.message.channel)
    
    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)
    print("All refreshed.")

#@bot.command(pass_context = True)
#async def heal(ctx):
#    with open('userstres.json', 'r') as f:
#        users = json.load(f)
#    #Code
#    await update_data(users, ctx.message.author)
#    await refresh(users, ctx.message.author, ctx.message.channel)
#    if users[user.id]['MP'] < 20:
#        await bot.send_message(ctx.message.channel, "Not enough MP: it costs 20, fool.")
#    elif users[ctx.message.author.id]['HP'] < 0:
#        await bot.send_message(ctx.message.channel, "You are dead. You cannot attack. Try #refresh")
#    else:
#        users[user.id]['MP'] -= 20
#        await heal(users, ctx.message.author, ctx.message.channel, 400)
#    with open('userstres.json', 'w' ) as f:
#        json.dump(users, f)
#    print("All refreshed.")


@bot.command(pass_context = True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def attack(ctx, userName: discord.User):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, ctx.message.author)
    await update_data(users, userName)

    if users[ctx.message.author.id]['HP'] > 0:
        await attack(users, ctx.message.author, userName, ctx.message.channel, 250)
    else:
        await bot.send_message(ctx.message.channel, "You are dead. You cannot attack. Try #refresh")

    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)

@bot.command(pass_context = True)
@commands.cooldown(1, 1500, commands.BucketType.user)
async def lootbox(ctx):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, ctx.message.author)

    if users[ctx.message.author.id]['HP'] > 0:
        await openbox(users, ctx.message.author, ctx.message.channel)
    else:
        await bot.send_message(ctx.message.channel, "You are dead. You cannot open lootboxes. Try #refresh")

    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)

@bot.command(pass_context = True)
@commands.cooldown(1, 1500, commands.BucketType.user)
async def search(ctx):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, ctx.message.author)

    if users[ctx.message.author.id]['HP'] > 0:
        await gain(users, ctx.message.author, ctx.message.channel)
    else:
        await bot.send_message(ctx.message.channel, "You are dead. You cannot get coins. Try #refresh")

    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)

@bot.command(pass_context = True)
@commands.cooldown(1, 1500, commands.BucketType.user)
async def steal(ctx, userName: discord.User):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, ctx.message.author)
    await update_data(users, userName)

    if users[ctx.message.author.id]['HP'] > 0:
        await steal(users, ctx.message.author, userName, ctx.message.channel, random.randint(1, 100))
    else:
        await bot.send_message(ctx.message.channel, "You are dead. You cannot steal. Try #refresh")

    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)

@bot.command(pass_context = True)
async def inventory(ctx):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, ctx.message.author)
    user = ctx.message.author
    emb = (discord.Embed(description='This is your inventory.', colour=0x3DF270))
    emb.set_author(name = "Inventory")
    emb.add_field(name = "Nut (common)", value = " x%s" % users[user.id]['Item1'])
    emb.add_field(name = "Thunder Bomb (common)", value = " x%s" % users[user.id]['Item2'])
    emb.add_field(name = "Magic Gelatin (common)", value = " x%s" % users[user.id]['Item3'])
    emb.add_field(name = "Big City Burger (common)", value = " x%s" % users[user.id]['Item4'])
    emb.add_field(name = "Beefsteak (common)", value = " x%s" % users[user.id]['Item5'])
    emb.add_field(name = "Mystical Stick (common)", value = " x%s" % users[user.id]['Item6'])
    #rares
    emb.add_field(name = "HP UP (rare)", value = " x%s" % users[user.id]['Item15'])
    emb.add_field(name = "MP UP (rare)", value = " x%s" % users[user.id]['Item16'])
    emb.add_field(name = "Egg of Light (rare)", value = " x%s" % users[user.id]['Item17'])
    emb.add_field(name = "Magic Cake (rare)", value = " x%s" % users[user.id]['Item18'])
    emb.add_field(name = "Lucky Stick (rare)", value = " x%s" % users[user.id]['Item19'])
    #legends
    emb.add_field(name = "Flex Tape (LEGENDARY)", value = " x%s" % users[user.id]['Item25'])
    emb.add_field(name = "Luxury Banana (LEGENDARY)", value = " x%s" % users[user.id]['Item26'])
    emb.add_field(name = "UFO (LEGENDARY)", value = " x%s" % users[user.id]['Item27'])
    emb.add_field(name = "Victor's NO-U noodles (LEGENDARY)", value = " x%s" % users[user.id]['Item28'])
    await bot.say(embed=emb)
    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)


@bot.command(pass_context = True)
async def give(ctx, userName: discord.User):
    with open('userstres.json', 'r') as f:
        users = json.load(f)
    #Code
    await update_data(users, ctx.message.author)
    await update_data(users, userName)
    message = ctx.message
    args = message.content.split(" ")
    itemVal = int(" ".join(args[2:]))
    if message.author.id == "383116010971987971":
        users[userName.id]['Item{}'.format(itemVal)] += 1
        bot.say("Gave {} a {}.".format(userName.mention, itemNames[itemVal]))
        print("Gave Item!")

    else:
        bot.say("You are not BuπitoDrΛgon. This incident will be reported.")


    with open('userstres.json', 'w' ) as f:
        json.dump(users, f)



async def update_data(users, user):
    if not user.id in users:
        #stats
        users[user.id] = {}
        users[user.id]['experience'] = 0
        users[user.id]['level'] = 1
        users[user.id]['MaxHP'] = 1200
        users[user.id]['MaxMP'] = 70
        users[user.id]['HP'] = 1200
        users[user.id]['MP'] = 70
        users[user.id]['Offense'] = 10
        users[user.id]['Defense'] = 10
        users[user.id]['Shields'] = 0
        users[user.id]['Charges'] = 0
        users[user.id]['NoU'] = 0
        users[user.id]['WeebCoins'] = 0
        #Item Thingies - Commons
        users[user.id]['Item1'] = 0 #Nut - Restores 100 HP
        users[user.id]['Item2'] = 0 #Thunder Bomb - Deals 75 damage to an enemy
        users[user.id]['Item3'] = 0 #Magic Gelatin - Restores 20 MP
        users[user.id]['Item4'] = 0 #Big City Burger - Restores 500 HP
        users[user.id]['Item5'] = 0 #Beefsteak - Restores 300 HP
        users[user.id]['Item6'] = 0 #Mystical Stick - Deals 100 damage to an enemy
        users[user.id]['Item7'] = 0
        users[user.id]['Item8'] = 0
        users[user.id]['Item9'] = 0
        users[user.id]['Item10'] = 0
        users[user.id]['Item11'] = 0
        users[user.id]['Item12'] = 0
        users[user.id]['Item13'] = 0
        users[user.id]['Item14'] = 0
        #Item thingies - Epics
        users[user.id]['Item15'] = 0 #HP UP - Raise max HP by 50
        users[user.id]['Item16'] = 0 #MP UP - Raise max MP by 15
        users[user.id]['Item17'] = 0 #Egg of Light - Raise offense by 3
        users[user.id]['Item18'] = 0 #Magic Cake - Raise defense by 3
        users[user.id]['Item19'] = 0 #Lucky Stick - Has a 1% chance of doing 10,000 damage. Otherwise does 100.
        users[user.id]['Item20'] = 0
        users[user.id]['Item21'] = 0
        users[user.id]['Item22'] = 0
        users[user.id]['Item23'] = 0
        users[user.id]['Item24'] = 0
        #Item Thingies - Legendaries
        users[user.id]['Item25'] = 0 #Flex Tape - Adds 10 shields
        users[user.id]['Item26'] = 0 #Luxury Banana - Basically the golden apple of reaction-weeb. Heals 10,000 HP, can go over max
        users[user.id]['Item27'] = 0 #UFO - Steals 5000 weeb coins from any user, guranteed. In fact, the victim can go into debt.
        users[user.id]['Item28'] = 0 #NO-U noodles - The next attack the eater recieves is reflected at the attacker x10
        #Lootboxes
        users[user.id]['Item29'] = 0 #Lootbox
        users[user.id]['Item30'] = 0 #Common lootbox
        users[user.id]['Item31'] = 0 #BadJuju
        users[user.id]['Item32'] = 0 #GoodJuju


async def add_experience(users, user, exp):
    users[user.id]['experience'] += exp
    if users[user.id]['level'] > 6:
        users[user.id]['experience'] += (exp * users[user.id]['level'])

async def refresh(users, user, channel):
    users[user.id]['HP'] = users[user.id]['MaxHP']
    users[user.id]['MP'] = users[user.id]['MaxMP']
    emb = (discord.Embed(description="%s your health and MP are maxxed out." % user.mention, colour=0x3DF270))
    emb.set_author(name="Refreshed!")
    await bot.send_message(channel, embed=emb)

async def get_stats(users, user, channel):
    experience = users[user.id]['experience']
    lvl = users[user.id]['level']
    currentHealth = users[user.id]['HP']
    maxHealth = users[user.id]['MaxHP']
    currentMana = users[user.id]['MP']
    maxMana = users[user.id]['MaxMP']
    neededfornext = ((lvl + 1) ** 4) - experience
    emb = (discord.Embed(description="{} weeb points are required for the next level.".format(neededfornext), colour=0x3DF270))
    emb.set_author(name="Weeb points: {}, LVL: {}, Coins: {}".format(experience, lvl, users[user.id]['WeebCoins']))
    emb2 = (discord.Embed(description="HP: {} out of {} \n MP: {} out of {}".format(currentHealth, maxHealth, currentMana, maxMana), colour=0x3DF270))
    emb2.set_author(name="Health Info:")
    await bot.send_message(channel, embed=emb)
    await bot.send_message(channel, embed=emb2)

async def level_up(users, user, channel):
    experience = users[user.id]['experience']
    lvl_start = users[user.id]['level']
    lvl_end = int(experience ** (1/4))
    if lvl_start < lvl_end and user.id != '456689119662309395':
        emb = (discord.Embed(description='{} has leveled up to level {} | HP + 250, MP +10, Offense +1, Defense +2'.format(user.mention, lvl_end), colour=0x3DF270))
        emb.set_author(name="Level Up!")
        users[user.id]['MaxHP'] += 250
        users[user.id]['MaxMP'] += 10
        users[user.id]['Offense'] += 1
        users[user.id]['Defense'] += 1
        emb.set_image(url="https://vignette.wikia.nocookie.net/konosuba/images/0/00/KZMA_LVL_16.png/revision/latest?cb=20160726024901")
        users[user.id]['level'] = lvl_end

#damage(Item)
async def damage(users, attacker, victim, channel, damageAmount):
    if users[victim.id]['NoU'] > 0:
        users[attacker.id]['HP'] -= damageAmount * 10
        emb = (discord.Embed(description='NO U! {} took {} damage!'.format(attacker.mention, damageAmount * 10), colour=0x3DF270))
        emb.set_author(name="R E D I R E C T")
        await bot.send_message(channel, embed=emb)
        users[victim.id]['NoU'] -= 1
        if users[attacker.id]['HP'] < 0:
            upxp = users[attacker.id]['level'] * 100
            coinsup = users[attacker.id]['level'] * 50
            emb = (discord.Embed(description='{} has slain {}! Gained {} XP points. Gained {} weeb coins.'.format(victim.mention, attacker.mention, upxp, coinsup), colour=0x3DF270))
            emb.set_author(name="Blood!")
            users[victim.id]['experience'] += upxp
            users[victim.id]['WeebCoins'] += coinsup
            await bot.send_message(channel, embed=emb)
        return
    if users[victim.id]['HP'] > 0:
        users[victim.id]['HP'] -= damageAmount
        emb = (discord.Embed(description='{} took {} damage!'.format(victim.mention, damageAmount), colour=0x3DF270))
        emb.set_author(name="Hit!")
        await bot.send_message(channel, embed=emb)
    #Check if the victim is dead
        if users[victim.id]['HP'] < 0:
            upxp = users[victim.id]['level'] * 100
            coinsup = users[victim.id]['level'] * 50
            emb = (discord.Embed(description='{} has slain {}! Gained {} XP points. Gained {} weeb coins.'.format(attacker.mention, victim.mention, upxp, coinsup), colour=0x3DF270))
            emb.set_author(name="Blood!")
            await bot.send_message(channel, embed=emb)
            users[attacker.id]['experience'] += upxp
            users[attacker.id]['WeebCoins'] += coinsup
    else:
        emb = (discord.Embed(description='{} is already dead.'.format(victim.mention), colour=0x3DF270))
        emb.set_author(name="Don't kick them while they're down.")

#damage(Attack)
async def attack(users, attacker, victim, channel, damageAmount):
    damageAmount = damageAmount + int(round(damageAmount * (users[attacker.id]['Offense'])) / 100)
    damageAmount = damageAmount + int(round(damageAmount * (users[attacker.id]['Defense'])) / 100)
    if users[victim.id]['NoU'] > 0:
        users[attacker.id]['HP'] -= damageAmount * 10
        emb = (discord.Embed(description='NO U! {} took {} damage!'.format(attacker.mention, damageAmount * 10), colour=0x3DF270))
        emb.set_author(name="R E D I R E C T")
        await bot.send_message(channel, embed=emb)
        if users[attacker.id]['HP'] < 0:
            upxp = users[attacker.id]['level'] * 100
            coinsup = users[attacker.id]['level'] * 50
            emb = (discord.Embed(description='{} has slain {}! Gained {} XP points. Gained {} weeb coins.'.format(victim.mention, attacker.mention, upxp, coinsup), colour=0x3DF270))
            emb.set_author(name="Blood!")
            users[victim.id]['experience'] += upxp
            users[victim.id]['WeebCoins'] += coinsup
            await bot.send_message(channel, embed=emb)
        return
    if users[victim.id]['HP'] > 0:
        users[victim.id]['HP'] -= damageAmount
        emb = (discord.Embed(description='{} took {} damage!'.format(victim.mention, damageAmount), colour=0x3DF270))
        emb.set_author(name="Hit!")
        await bot.send_message(channel, embed=emb)
        #Check if the victim is dead
        if users[victim.id]['HP'] < 0:
            upxp = users[victim.id]['level'] * 100
            coinsup = users[victim.id]['level'] * 50
            emb = (discord.Embed(description='{} has slain {}! Gained {} XP points. Gained {} weeb coins.'.format(attacker.mention, victim.mention, upxp, coinsup), colour=0x3DF270))
            emb.set_author(name="Blood!")
            users[attacker.id]['experience'] += upxp
            users[attacker.id]['WeebCoins'] += coinsup
            await bot.send_message(channel, embed=emb)
    else:
        emb = (discord.Embed(description='{} is already dead.'.format(victim.mention), colour=0x3DF270))
        emb.set_author(name="Don't kick them while they're down.")

#healing
async def heal(users, user, channel, healamount):
    users[user.id]['HP'] += healamount
    emb = (discord.Embed(description='{} healed {} HP!'.format(user.mention, healamount), colour=0x3DF270))
    emb.set_author(name="Needed healing.")
    await bot.send_message(channel, embed=emb)

#stealing
async def steal(users, theif, victim, channel, stealamount):
    users[theif.id]['WeebCoins'] += stealamount
    users[victim.id]['WeebCoins'] -= stealamount
    emb = (discord.Embed(description='{} stole {} coins from {}'.format(theif.mention, stealamount, victim.mention), colour=0x3DF270))
    emb.set_author(name="A theft has occured!")
    await bot.send_message(channel, embed=emb)

#gain coins
async def gain(users, user, channel):
    coingain = random.randint(75, 250)
    users[user.id]['WeebCoins'] += coingain
    emb = (discord.Embed(description='{} recieved {} weeb coins'.format(user.mention, coingain), colour=0x3DF270))
    emb.set_author(name="cash cash moneyyyy")
    await bot.send_message(channel, embed=emb)

#raise a stat
async def statup(users, user, channel, upamount, stat):
    users[user.id][stat] += upamount
    emb = (discord.Embed(description='{} increased {} in the {} category!'.format(user.mention, upamount, stat), colour=0x3DF270))
    emb.set_author(name="Yea bois")
    await bot.send_message(channel, embed=emb)

#lower a stat
async def statdown(users, user, channel, downamount, stat):
    users[user.id][stat] += downamount
    emb = (discord.Embed(description='{} decreased {} in the {} category!'.format(user.mention, downamount, stat), colour=0x3DF270))
    emb.set_author(name="Aw rip")
    await bot.send_message(channel, embed=emb)

#lootbox
async def openbox(users, user, channel):
    itemvalue = random.randint(1, 1000)
    if 1 <= itemvalue <= 700:
        itemvalue = random.randint(1, NUMBER_OF_COMMONS)
        users[user.id]['Item{}'.format(itemvalue)] += 1
        emb = (discord.Embed(description='{} got {} - Common'.format(user.mention, itemNames[itemvalue]), colour=0x3DF270))
        emb.set_author(name= "You opened a lootbox...")
        await bot.send_message(channel, embed = emb)
    elif 701 <= itemvalue <= 975:
        itemvalue = random.randint(15, NUMBER_OF_RARES)
        users[user.id]['Item{}'.format(itemvalue)] += 1
        emb = (discord.Embed(description='{} got {} - Rare'.format(user.mention, itemNames[itemvalue]), colour=0x3DF270))
        emb.set_author(name= "You opened a lootbox...")
        await bot.send_message(channel, embed = emb)
    elif 976 <= itemvalue <= 1000:
        itemvalue = random.randint(25, NUMBER_OF_LEGENDARIES)
        users[user.id]['Item{}'.format(itemvalue)] += 1
        emb = (discord.Embed(description='{} got {} - LEGENDARY!'.format(user.mention, itemNames[itemvalue]), colour=0x3DF270))
        emb.set_author(name= "You opened a lootbox...")
        await bot.send_message(channel, embed = emb)


def randomNumber():
    return random.randint(5, 14)


bot.run(BOT_TOKEN)
