from discord.ext import commands
import discord
import requests

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hug(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.send("You need to mention a user to hug!")
        data = requests.get("https://nekos.life/api/v2/img/hug").json()
        embed = discord.Embed(title=f"{ctx.author.name} hugs {user}", color=0xeee657)
        embed.set_image(url=data['url'])
        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.send("You need to mention a user to kiss!")
        data = requests.get("https://nekos.life/api/v2/img/kiss").json()
        embed = discord.Embed(title=f"{ctx.author.name} kisses {user}", color=0xeee657)
        embed.set_image(url=data['url'])
        await ctx.send(embed=embed)
    @commands.command()
    async def pat(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.send("You need to mention a user to pat!")
        data = requests.get("https://nekos.life/api/v2/img/pat").json()
        embed = discord.Embed(title=f"{ctx.author.name} pats {user}", color=0xeee657)
        embed.set_image(url=data['url'])
        await ctx.send(embed=embed)
    @commands.command()
    async def slap(self, ctx, user: discord.Member = None):
        if user == None:
            await ctx.send("You need to mention a user to slap!")
        data = requests.get("https://nekos.life/api/v2/img/slap").json()
        embed = discord.Embed(title=f"{ctx.author.name} slaps {user}", color=0xeee657)
        embed.set_image(url=data['url'])
        await ctx.send(embed=embed)
    @commands.command()
    async def owoify(self, ctx, *, text):
        data = requests.get(f"https://nekos.life/api/v2/owoify?text={text}").json()
        await ctx.send(data['owo'])

async def setup(bot):
    await bot.add_cog(fun(bot))
