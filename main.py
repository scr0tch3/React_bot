import disnake
from disnake.ext import commands
import random
import os
import json
import env


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
async def укусить(ctx, member: disnake.Member):
    with open("bd.json", 'r') as f:
        data = json.load(f)
        bite_gifs = data.get("bite", [])
        if bite_gifs:
            random_gif = random.choice(bite_gifs)
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            embed.set_image(url=random_gif)
            await ctx.send(f"{ctx.author.mention} кусает {member.mention}:", embed=embed)


@bot.command()
async def плакать(ctx):
    with open("bd.json", 'r') as f:
        data = json.load(f)
        cry_gifs = data.get("cry", [])
        if cry_gifs:
            random_gif = random.choice(cry_gifs)
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            embed.set_image(url=random_gif)
            await ctx.send(f"{ctx.author.mention} плачет...", embed=embed)

@bot.command()
async def танцевать(ctx):
    with open("bd.json", 'r') as f:
        data = json.load(f)
        dance_gifs = data.get("dance", [])
        if dance_gifs:
            random_gif = random.choice(dance_gifs)
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            embed.set_image(url=random_gif)
            await ctx.send(f"{ctx.author.mention} танцует...", embed=embed)

@bot.command()
async def обнять(ctx, member: disnake.Member):
    with open("bd.json", 'r') as f:
        data = json.load(f)
        hug_gifs = data.get("hug", [])
        if hug_gifs:
            random_gif = random.choice(hug_gifs)
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            embed.set_image(url=random_gif)
            await ctx.send(f"{ctx.author.mention} обнимает {member.mention}:", embed=embed)

@bot.command()
async def поцеловать(ctx, member: disnake.Member):
    with open("bd.json", 'r') as f:
        data = json.load(f)
        kiss_gifs = data.get("kiss", [])
        if kiss_gifs:
            random_gif = random.choice(kiss_gifs)
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            embed.set_image(url=random_gif)
            await ctx.send(f"{ctx.author.mention} целует {member.mention}:", embed=embed)

@bot.command()
async def смеяться(ctx):
    with open("bd.json", 'r') as f:
        data = json.load(f)
        laugh_gifs = data.get("laugh", [])
        if laugh_gifs:
            random_gif = random.choice(laugh_gifs)
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            embed.set_image(url=random_gif)
            await ctx.send(f"{ctx.author.mention} смеётся...", embed=embed)

@bot.command()
async def погладить(ctx, member: disnake.Member):
    with open("bd.json", 'r') as f:
        data = json.load(f)
        pat_gifs = data.get("pat", [])
        if pat_gifs:
            random_gif = random.choice(pat_gifs)
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            embed.set_image(url=random_gif)
            await ctx.send(f"{ctx.author.mention} гладит {member.mention}:", embed=embed)


@bot.command()
async def ударить(ctx, member: disnake.Member):
    with open("bd.json", 'r') as f:
        data = json.load(f)
        slap_gifs = data.get("slap", [])
        if slap_gifs:
            random_gif = random.choice(slap_gifs)
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            embed.set_image(url=random_gif)
            await ctx.send(f"{ctx.author.mention} ударяет {member.mention}:", embed=embed)


@bot.command()
async def улыбаться(ctx):
    with open("bd.json", 'r') as f:
        data = json.load(f)
        smile_gifs = data.get("smile", [])
        if smile_gifs:
            random_gif = random.choice(smile_gifs)
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            embed.set_image(url=random_gif)
            await ctx.send(f"{ctx.author.mention} улыбается...", embed=embed)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send(f'{ctx.author.mention} Неопознанная команда. Пожалуйста, проверьте правильность ввода.')

bot.run(env.TOKEN)
