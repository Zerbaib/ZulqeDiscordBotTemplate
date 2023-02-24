from discord.ext import commands
import discord
import psutil

class general(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.bot.latency * 1000)}ms')
    
    @commands.command()
    async def sysinfo(self, ctx):
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        maxmem = psutil.virtual_memory().total
        maxmemmb = maxmem / 1000000
        networkup = psutil.net_io_counters().bytes_sent / 1000000
        networkdown= psutil.net_io_counters().bytes_recv / 1000000
        embed = discord.Embed(title="System Information", description="System Information", color=0xeee657)
        embed.add_field(name="CPU Usage", value=f"{cpu}%", inline=True)
        embed.add_field(name="Memory Usage", value=f"{mem}%", inline=True)
        embed.add_field(name="Max Memory", value=f"{round(maxmemmb)} MB", inline=True)
        embed.add_field(name="Network Upload", value=f"{round(networkup)} MB <:arup:1078271325543612466>", inline=True)
        embed.add_field(name="Network Download", value=f"{round(networkdown)} MB <:ardown:1078271587385610260>", inline=True)
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(general(bot))
