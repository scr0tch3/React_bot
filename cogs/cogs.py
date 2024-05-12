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
    async def wanted(self, ctx, member1: disnake.Member, member2: disnake.Member):
        chances = random.uniform(1, 100)
        formatted_number = "{:.2f}".format(chances)
        wanted = Image.open('img/wanted.jpg')

        text = ImageDraw.Draw(wanted)
        member1_name = ImageDraw.Draw(wanted)
        member2_name = ImageDraw.Draw(wanted)
        font = ImageFont.truetype("arialmt.ttf", 26)

        avatar_url1 = member1.avatar.url
        response1 = requests.get(avatar_url1)
        avatar1 = Image.open(io.BytesIO(response1.content))
        avatar1 = avatar1.resize((150, 150))

        avatar_url2 = member2.avatar.url
        response2 = requests.get(avatar_url2)
        avatar2 = Image.open(io.BytesIO(response2.content))
        avatar2 = avatar2.resize((150, 150))

        wanted.paste(avatar1, (50, 50))
        wanted.paste(avatar2, (370, 50))
        text.text((240, 130), f"{formatted_number}%", font=font)
        member1_name.text((85, 28), f"{member1.display_name}", font=font)
        member2_name.text((400, 27), f"{member2.display_name}", font=font)


        img_byte_array = io.BytesIO()
        wanted.save(img_byte_array, format='PNG')
        img_byte_array.seek(0)

        with open("phrases.json", 'r', encoding='utf-8') as f:
            data = json.load(f)

            if chances <= 25:
                phrases1 = data.get("0-25", [])
                random_pr1 = random.choice(phrases1)
                random_pr1 = random_pr1.replace("{member.mention}", member1.mention).replace("{member2.mention}",
                                                                                             member2.mention)
                await ctx.send(f"{random_pr1}", file=disnake.File(img_byte_array, filename='ship.png'))
            elif 25 < chances <= 50:
                phrases2 = data.get("25-50", [])
                random_pr2 = random.choice(phrases2)
                random_pr2 = random_pr2.replace("{member.mention}", member1.mention).replace("{member2.mention}",
                                                                                             member2.mention)
                await ctx.send(f"{random_pr2}", file=disnake.File(img_byte_array, filename='ship.png'))
            elif 50 < chances:
                phrases3 = data.get("50-75", [])
                random_pr3 = random.choice(phrases3)
                random_pr3 = random_pr3.replace("{member.mention}", member1.mention).replace("{member2.mention}",
                                                                                             member2.mention)
                await ctx.send(f"{random_pr3}", file=disnake.File(img_byte_array, filename='ship.png'))
            else:
                phrases4 = data.get("75-100", [])
                random_pr4 = random.choice(phrases4)
                random_pr4 = random_pr4.replace("{member.mention}", member1.mention).replace("{member2.mention}",
                                                                                             member2.mention)
                await ctx.send(f"{random_pr4}", file=disnake.File(img_byte_array, filename='ship.png'))

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
    async def gg(self, ctx):
        embed = disnake.Embed()
        embed.colour = disnake.Colour.gold()
        embed.set_image("https://i.pinimg.com/564x/c8/4b/48/c84b481f32d0deff182c3638df29acfc.jpg")
        await ctx.send(embed=embed)


    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
         if isinstance(error, commands.CommandNotFound):
             await ctx.send(f'{ctx.author.mention} Неопознанная команда. Пожалуйста, проверьте правильность ввода.')

def setup(bot):
    bot.add_cog(cogs(bot))
