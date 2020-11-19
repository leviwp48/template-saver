import discord
from discord.ext import commands

class BasicCommands(commands.Cog, name='Basic Commands'):
  
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name="ping")
  async def ping(self, ctx):
    await ctx.send("pong")

  @commands.command(name="how")
  async def how(self, ctx):
    await ctx.send("How to use this bot: \n\nMake a new Template: Use the ***.use*** command with the following arguments (each between quotes): Template name, Keywords to use in a comma separated list, Text for the Template with your keywords embeded between '[*keyword*]'. \n \t**Example**: .use('Event Member', 'member, event', '\n\t\tList of members for [event]: \n \t\t* [member] \n \t\t* [member]') \n\n***Remember to put arguments between quotes***  \n\n View any saved Templates \n\n Use any saved Templates")

def setup(bot):
	bot.add_cog(BasicCommands(bot))
