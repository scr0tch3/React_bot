import disnake
from disnake.ext import commands
import random
import os
import json

TOKEN = "MTIwNjI0MjExNjgyOTg0NzU5Mg.Gg4unf.yPK25jXRe1qC2TF_T-KOM19--GVlG3OHQUkAXk"

bot = commands.Bot(command_prefix="!", help_command=None, intents=disnake.Intents.all(), test_guilds=[1159839672550297675]) 

@bot.event
async def on_ready():
    print(f"Bot {bot.user} is ready to work!")
    await bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name="Чебупели"))

@bot.command()
async def злиться(ctx):
    with open("bd.json", 'r') as f:
        data = json.load(f)
        angry_gifs = data.get("angry", [])
        if angry_gifs:
            random_gif = random.choice(angry_gifs)
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            embed.set_image(url=random_gif)
            await ctx.send(f"{ctx.author.mention} злится...", embed=embed)

@bot.command()
async def улыбаться(ctx):
    directory = "smiles"
    files = os.listdir(directory)
    random_image = random.choice(files)
    file_path = os.path.join(directory, random_image)
    with open(file_path, 'rb') as f:
        picture = disnake.File(f)
        await ctx.send(f"{ctx.author.mention} улыбается:", file=picture)

@bot.command()
async def укусить(ctx):
    directory = "bite"
    files = os.listdir(directory)
    random_image = random.choice(files)
    file_path = os.path.join(directory, random_image)
    with open(file_path, 'rb') as f:
        picture = disnake.File(f)
        await ctx.send(f"{ctx.author.mention} кусает  :", file=picture)

@bot.command()
async def плакать(ctx):
    directory = "cry"
    files = os.listdir(directory)
    random_image = random.choice(files)
    file_path = os.path.join(directory, random_image)
    with open(file_path, 'rb') as f:
        picture = disnake.File(f)
        await ctx.send(f"{ctx.author.mention} плачет:", file=picture)

@bot.command()
async def танцевать(ctx):
    directory = "dance"
    files = os.listdir(directory)
    random_image = random.choice(files)
    file_path = os.path.join(directory, random_image)
    with open(file_path, 'rb') as f:
        picture = disnake.File(f)
        await ctx.send(f"{ctx.author.mention} танцует:", file=picture)

@bot.command()
async def обнять(ctx):
    directory = "hug"
    files = os.listdir(directory)
    random_image = random.choice(files)
    file_path = os.path.join(directory, random_image)
    with open(file_path, 'rb') as f:
        picture = disnake.File(f)
        await ctx.send(f"{ctx.author.mention} обнимает  :", file=picture)

@bot.command()
async def поцеловать(ctx):
    directory = "kiss"
    files = os.listdir(directory)
    random_image = random.choice(files)
    file_path = os.path.join(directory, random_image)
    with open(file_path, 'rb') as f:
        picture = disnake.File(f)
        await ctx.send(f"{ctx.author.mention} целует  :", file=picture)

@bot.command()
async def смеятся(ctx):
    directory = "laugh"
    files = os.listdir(directory)
    random_image = random.choice(files)
    file_path = os.path.join(directory, random_image)
    with open(file_path, 'rb') as f:
        picture = disnake.File(f)
        await ctx.send(f"{ctx.author.mention} смеёться:", file=picture)

@bot.command()
async def гладить(ctx):
    directory = "pat"
    files = os.listdir(directory)
    random_image = random.choice(files)
    file_path = os.path.join(directory, random_image)
    with open(file_path, 'rb') as f:
        picture = disnake.File(f)
        await ctx.send(f"{ctx.author.mention} гладит  :", file=picture)

@bot.command()
async def ударить(ctx):
    directory = "slap"
    files = os.listdir(directory)
    random_image = random.choice(files)
    file_path = os.path.join(directory, random_image)
    with open(file_path, 'rb') as f:
        picture = disnake.File(f)
        await ctx.send(f"{ctx.author.mention} бьёт :", file=picture)

bot.run(TOKEN)
