import io
import disnake
from disnake.ext import commands
import random
import os
import json
from PIL import Image, ImageDraw, ImageFont
import requests


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
    async def wanted(self, ctx, member1: disnake.Member, member2: disnake.Member, ):

        wanted = Image.open('wanted.jpg')
        text = ImageDraw.Draw(wanted)
        font = ImageFont.truetype("arialmt.ttf", 26)

        avatar_url1 = member1.avatar.url
        response1 = requests.get(avatar_url1)
        avatar1 = Image.open(io.BytesIO(response1.content))
        avatar1 = avatar1.resize((150, 150))

        avatar_url2 = member2.avatar.url
        response2 = requests.get(avatar_url2)
        avatar2 = Image.open(io.BytesIO(response2.content))
        avatar2 = avatar2.resize((150, 150))

        # heart = Image.open("Heart.png")
        #   heart.resize((100, 100))
        # heart_without_background = heart.convert("L")

        chances = random.uniform(1, 100)
        formatted_number = "{:.2f}".format(chances)

        #     if (chances <= 50):
        #
        #         heart = answerbad
        #       else:
        #          heart = answergood

        wanted.paste(avatar1, (50, 50))
        wanted.paste(avatar2, (370, 50))
        # wanted.paste(wanted, heart, (235, 80), mask=heart)
        text.text((245, 115), f"{formatted_number}%", font=font)

        embed = disnake.Embed()
        embed.colour = disnake.Colour.gold()
        embed.set_image(wanted)

        img_byte_array = io.BytesIO()
        wanted.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)

        await ctx.send(f"Шанс {member1.mention} & {member2.mention} = {formatted_number}%", file=disnake.File(img_byte_array, filename='ship.png'))

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
        embed = disnake.Embed()
        embed.colour = disnake.Colour.gold()
        embed.set_image("https://i.pinimg.com/564x/61/21/80/6121801643f5dcb27ee14c2173b5ed35.jpg")
        await ctx.send(embed=embed)

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
