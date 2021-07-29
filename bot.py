import discord
from discord.ext import commands
import requests
import json
from json import load
from requests.models import Response
import addloc
import updateloc
import searchlocation
import calctime

client = commands.Bot(command_prefix = ".", intents = discord.Intents.all())

client.load_extension("welcAndrem")

#Loading API keys
#with open("token.json", "r") as file:
#    DISCORD = load(file)["discord"]

#Message client on ready
@client.event
async def on_ready():
    print("TimeZone is ready to go")

@client.command()
async def helloTZ(ctx):
    await ctx.send ("Wassup!")

@client.command()
async def addlocation(ctx, member:discord.Member,*,location):
    userlocation = location
    username = member
    member = str(member)
    num = addloc.add(member,location)
    if num == 0:
        embed = discord.Embed(title = f"This user is already registered, if you want to update your location, please use the updatelocation command.",colour=0xDC143C)
        await ctx.send(embed = embed)
    if num == 1:
        embed = discord.Embed(title = f""+member+" Your location has been registered as "+location+".",colour=0xDC143C)
        await ctx.send(embed = embed)

@client.command()
async def updatelocation(ctx, member:discord.Member,*,location):
    userlocation = location
    username = member
    member = str(member)
    num = updateloc.update(member,location)
    if num == 0:
        embed = discord.Embed(title = f"This user is not registered, if you want to add your location, please use the addlocation command.",colour=0xDC143C)
        await ctx.send(embed = embed)
    if num == 1:
        embed = discord.Embed(title = f""+member+" Your location has been updated to "+location+".",colour=0xDC143C)
        await ctx.send(embed = embed)

@client.command()
async def location(ctx, member:discord.Member):
    location = searchlocation.location(member)
    await ctx.send(f"The location of {member.mention} is {location}")
    
@client.command()
async def Time(ctx, member:discord.Member):
    location = searchlocation.location(member)
    request = requests.get(f"http://api.positionstack.com/v1/forward?access_key=ff59914e692647971925876876ff66bc&query={location}")
    response = request.json()
    lat = response["data"][0]["latitude"]
    long = response["data"][0]["longitude"]
    final = calctime.time(lat, long)
    Time = final[1]
    Date = final[0]
    embed = discord.Embed(title = f"The date in {member}'s location is {Date} and time is {Time}",colour=0xDC143C)
    await ctx.send(embed = embed)



client.run(Your-Discord-Token-Here)