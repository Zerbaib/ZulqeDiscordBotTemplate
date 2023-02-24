import discord
from discord.ext import commands


class help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title="Help", description="Here are all the commands you can use", color=0xeee657)
        embed.add_field(name="ping", value="Returns your bots ping! (MS)", inline=False)
        embed.add_field(name="help", value="Returns this message", inline=False)
        embed.add_field(name="hug", value="Hugs a user", inline=False)
        embed.add_field(name="kiss", value="Kisses a user", inline=False)
        embed.add_field(name="slap", value="Slaps a user", inline=False)
        embed.add_field(name="pat", value="Pats a user", inline=False)
        embed.add_field(name="owoify", value="OwOifies a message", inline=False)
        embed.add_field(name="sysinfo", value="Returns system information", inline=False)
        embed.add_field(name="purge", value="Deletes a specified amount of messages (**Needs manage messages perm**)", inline=False)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(help(bot))
