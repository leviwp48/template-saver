import discord
from discord.ext import commands

class BasicCommands(commands.Cog, name='Basic Commands'):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="ping")
  async def ping(self, ctx):
    await ctx.send("pong")

def setup(bot):
	bot.add_cog(BasicCommands(bot))
