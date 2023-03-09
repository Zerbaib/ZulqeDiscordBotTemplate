import discord
from discord.ext import commands, tasks
import random
import asyncio

class Giveaways(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.giveaways = {}
        self.check_giveaway_loop.start()

    @commands.command(name='giveaway')
    async def giveaway(self, ctx, time, prize):
        """Starts a new giveaway"""
        try:
            time = int(time) # time is in second
            if time <= 0:
                raise ValueError
        except ValueError:
            await ctx.send("Invalid time")
            return

        embed = discord.Embed(
            title="🎉 New giveaway 🎉",
            description=f"React with 🎉 to enter!\nTime left: {time} seconds\nPrize: {prize}"
        )

        message = await ctx.send(embed=embed)
        await message.add_reaction("🎉")

        self.giveaways[message.id] = {
            "prize": prize,
            "entries": set(),
            "end_time": asyncio.get_event_loop().time() + time
        }

    @tasks.loop(seconds=5)
    async def check_giveaway_loop(self):
        """Checks if any giveaways have ended"""
        now = asyncio.get_event_loop().time()

        for message_id, giveaway in list(self.giveaways.items()):
            if now >= giveaway['end_time']:
                message = await self.bot.get_channel(giveaway['channel_id']).fetch_message(message_id)

                if len(giveaway['entries']) > 0:
                    winner = random.choice(list(giveaway['entries']))
                    await message.channel.send(f"🎉 Congratulations {winner.mention}, you won the **{giveaway['prize']}**!")
                else:
                    await message.channel.send("Nobody entered the giveaway 😢")

                del self.giveaways[message_id]

    @giveaway.error
    async def giveaway_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Please provide the time and prize for the giveaway")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Invalid time")

def setup(bot):
    bot.add_cog(Giveaways(bot))