from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup
import re
import discord
from discord.ext.commands import Bot
from classifier import classifier
from convert_to_jpg import convert


Client = discord.Client()
bot_prefix = "!"
client = Bot(command_prefix=bot_prefix, description='One true Path.')


@client.event
async def on_ready():
    print('Bot Online!')
    print('Name: {CJ|Music}'.format(client.user.name))
    print('ID: {359689815798579200}'.format(client.user.id))


@client.command(pass_context=True)
async def ping(ctx):
    await client.say('Pong!')


@client.command(pass_context=True)
async def dani(ctx):
    members = client.get_all_members()
    for member in members:
        if not str(member).find('faelight'):
            fae = member.id
        if not str(member).find('tacit'):
            tacit = member.id
    website = urlopen('https://www.masterypoints.com/highscores/champion/lulu/0/na').read()
    soup = BeautifulSoup(website, 'html.parser')
    top_list = soup.findAll("tr")
    for player in top_list:
        find = re.search(r'faelight', str(player))
        if find:
            dani_rank = str(player.td.string)
            dani_mastery = str(player)
            break
    await client.say('<@{}> is number {} on the list of top NA Lulu\'s.'.format(fae, dani_rank))


@client.command(pass_context=True)
async def tacit(ctx):
    members = client.get_all_members()
    for member in members:
        if not str(member).find('tacit'):
            tacit = member.id
    await client.say('<@{}> is a feeder.'.format(tacit))


@client.command(pass_context=True)
async def classify(ctx):
    print(ctx.message.content)
    print(ctx.message.attachments)
    for attachment in ctx.message.attachments:
        print(attachment)
    url = ctx.message.attachments[0]
    name = url['filename']
    url = url['url']
    import aiohttp
    with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            image = await resp.read()
            with open('images/' + str(name), "wb") as f:
                f.write(image)
    name = convert(name)
    returned_name = classifier(name)
    await client.say('That is a picture of ' + returned_name + '.')


client.run('MzU5Njg5ODE1Nzk4NTc5MjAw.DKUVPQ.mOsm-yUILtoAjhzAzrUmzVHtvLk')
