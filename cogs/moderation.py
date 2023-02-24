import discord
from discord.ext import commands
from discord.ext.commands import has_permissions

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: int = 20):
        # clears messages
        try:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f"Deleted {amount} messages")
        except discord.Forbidden:
            await ctx.send("I do not have permission to delete messages")
    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command")
async def setup(bot):
    await bot.add_cog(moderation(bot))
