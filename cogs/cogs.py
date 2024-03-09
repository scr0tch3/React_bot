import disnake
from disnake.ext import commands
import random
import os
import json


class cogs(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Bot {self.bot.user} is ready to work!")
        await self.bot.change_presence(activity=disnake.Activity(type=disnake.ActivityType.playing, name="Чебупели"))

    @commands.command()
    async def злиться(self, ctx):
        with open("bd.json", 'r') as f:
            data = json.load(f)
            angry_gifs = data.get("angry", [])
            if angry_gifs:
                random_gif = random.choice(angry_gifs)
                embed = disnake.Embed()
                embed.colour = disnake.Colour.gold()
                embed.set_image(url=random_gif)
                await ctx.send(f"{ctx.author.mention} злится...", embed=embed)

    @commands.command()
    async def укусить(self, ctx, member: disnake.Member):
        with open("bd.json", 'r') as f:
            data = json.load(f)
            bite_gifs = data.get("bite", [])
            if bite_gifs:
                random_gif = random.choice(bite_gifs)
                embed = disnake.Embed()
                embed.colour = disnake.Colour.gold()
                embed.set_image(url=random_gif)
                await ctx.send(f"{ctx.author.mention} кусает {member.mention}:", embed=embed)

    @commands.command()
    async def плакать(self, ctx):
        with open("bd.json", 'r') as f:
            data = json.load(f)
            cry_gifs = data.get("cry", [])
            if cry_gifs:
                random_gif = random.choice(cry_gifs)
                embed = disnake.Embed()
                embed.colour = disnake.Colour.gold()
                embed.set_image(url=random_gif)
                await ctx.send(f"{ctx.author.mention} плачет...", embed=embed)

    @commands.command()
    async def танцевать(self, ctx):
        with open("bd.json", 'r') as f:
            data = json.load(f)
            dance_gifs = data.get("dance", [])
            if dance_gifs:
                random_gif = random.choice(dance_gifs)
                embed = disnake.Embed()
                embed.colour = disnake.Colour.gold()
                embed.set_image(url=random_gif)
                await ctx.send(f"{ctx.author.mention} танцует...", embed=embed)

    @commands.command()
    async def обнять(self, ctx, member: disnake.Member):
        with open("bd.json", 'r') as f:
            data = json.load(f)
            hug_gifs = data.get("hug", [])
            if hug_gifs:
                random_gif = random.choice(hug_gifs)
                embed = disnake.Embed()
                embed.colour = disnake.Colour.gold()
                embed.set_image(url=random_gif)
                await ctx.send(f"{ctx.author.mention} обнимает {member.mention}:", embed=embed)

    @commands.command()
    async def поцеловать(self, ctx, member: disnake.Member):
        with open("bd.json", 'r') as f:
            data = json.load(f)
            kiss_gifs = data.get("kiss", [])
            if kiss_gifs:
                random_gif = random.choice(kiss_gifs)
                embed = disnake.Embed()
                embed.colour = disnake.Colour.gold()
                embed.set_image(url=random_gif)
                await ctx.send(f"{ctx.author.mention} целует {member.mention}:", embed=embed)

    @commands.command()
    async def смеяться(self, ctx):
        with open("bd.json", 'r') as f:
            data = json.load(f)
            laugh_gifs = data.get("laugh", [])
            if laugh_gifs:
                random_gif = random.choice(laugh_gifs)
                embed = disnake.Embed()
                embed.colour = disnake.Colour.gold()
                embed.set_image(url=random_gif)
                await ctx.send(f"{ctx.author.mention} смеётся...", embed=embed)

    @commands.command()
    async def погладить(self, ctx, member: disnake.Member):
        with open("bd.json", 'r') as f:
            data = json.load(f)
            pat_gifs = data.get("pat", [])
            if pat_gifs:
                random_gif = random.choice(pat_gifs)
                embed = disnake.Embed()
                embed.colour = disnake.Colour.gold()
                embed.set_image(url=random_gif)
                await ctx.send(f"{ctx.author.mention} гладит {member.mention}:", embed=embed)

    @commands.command()
    async def ударить(self, ctx, member: disnake.Member):
        with open("bd.json", 'r') as f:
            data = json.load(f)
            slap_gifs = data.get("slap", [])
            if slap_gifs:
                random_gif = random.choice(slap_gifs)
                embed = disnake.Embed()
                embed.colour = disnake.Colour.gold()
                embed.set_image(url=random_gif)
                await ctx.send(f"{ctx.author.mention} ударяет {member.mention}:", embed=embed)

    @commands.command()
    async def улыбаться(self, ctx):
        with open("bd.json", 'r') as f:
            data = json.load(f)
            smile_gifs = data.get("smile", [])
            if smile_gifs:
                random_gif = random.choice(smile_gifs)
                embed = disnake.Embed()
                embed.colour = disnake.Colour.gold()
                embed.set_image(url=random_gif)
                await ctx.send(f"{ctx.author.mention} улыбается...", embed=embed)

    @commands.command()
    async def ятебявротебал(self, ctx):
        with open("hum.jpg", 'rb') as f:
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            embed.set_image("hum.jpg")
            await ctx.send(f":smiling_face_with_3_hearts:", embed=embed)

    @commands.command()
    async def da(self, ctx):
        image_filename = "hum.jpg"
        with open(image_filename, "rb") as image_file:
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            file = disnake.File("hum.jpg")
            embed.set_image(file)
            await ctx.send("da", embed=embed)

    @commands.command()
    async def шанс(self, ctx):
        chances = random.randint(1, 100)
        answerbad = "лох"
        answergood = "умница"
        combobad = f"Ваш шанс равен {chances} и вы {answerbad}"
        combogood = f"Ваш шанс равен {chances} и вы {answergood}"
        if (chances <= 50):
            await ctx.send(combobad)
        else:
            await ctx.send(combogood)

    @commands.command()
    async def f(self, ctx, member: disnake.Member):    #ship
        with open("hum.jpg", 'r') as f:
            embed = disnake.Embed()
            embed.colour = disnake.Colour.gold()
            embed.set_image("hum.jpg")
            await ctx.sendImage("hum.jpg")


    # @commands.command()
    # async def love(ctx, member1: disnake.Member, member2: disnake.Member):
    #     love_percentage = random.randint(0, 100)

    #     with open("bd.json", 'r') as f:
    #         data = json.load(f)
    #         if 0 <= love_percentage <= 30:
    #             gif_key = "low"
    #         elif 30 <= love_percentage <= 50:
    #             gif_key = "mid"
    #         else:
    #             gif_key = "high"

    #         ship_gifs = data.get("ship", {}).get(gif_key, [])
    #         if ship_gifs:
    #             random_gif = random.choice(ship_gifs)
    #             embed = disnake.Embed(title="❤️ Любовный калькулятор ❤️",
    #                                 description=f"{member1.mention} + {member2.mention} = {love_percentage}% ❤️",
    #                                 color=0xff69b4)  # Розовый цвет
    #             embed.set_image(url=random_gif)
    #             await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f'{ctx.author.mention} Неопознанная команда. Пожалуйста, проверьте правильность ввода.')


def setup(bot):
    bot.add_cog(cogs(bot))