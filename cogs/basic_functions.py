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
    await ctx.send(" \n How to use this bot: \n\n=================================\n**Make a new Template**: \n\nUse the ***.new*** command with the following arguments *(each between quotes)* \n- Template name\n- Keywords to use in a comma separated list \n- Text for the Template with your keywords embedded between quotes -> Like so: '[*keyword*]' \n\n \t**Example**: .new \"Event Members\", \"member, event\", \"\n\t\tList of members for [event]: \n \t\t* [member] \n \t\t* [member]\" \n\n***Remember to put arguments between quotes*** \n=================================  \n\n=================================\n**View any saved Templates**: \n\nUse the ***.view*** command and you'll see your saved Templates\n=================================\n\n=================================\n**Use any saved Templates**: \n \n___NOTE: You will need to enter your values in the same order as they appear in the text. In this case, \"[event]\" comes first, so you would enter the value for the event first___ \n\nUse the ***.use*** command with the following arguments *(each between quotes)* \n- Template name\n- Words to insert into template (in a comma separated list)\n\n\t**Example**: .use \"Event Members\", \"Game Night, Joe, Lucas\"\n\tThis will result in: \n\tList of members for Game Night: \n\t* Joe\n\t* Lucas \n\n ***Remember to put arguments between quotes*** \n=================================")

def setup(bot):
	bot.add_cog(BasicCommands(bot))
