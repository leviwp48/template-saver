import os
from keep_alive import keep_alive
from discord.ext import commands

bot = commands.Bot(
	command_prefix=".",  # Change to desired prefix
	case_insensitive=True  # Commands aren't case-sensitive
)

bot.author_id = 149926769602854913  # Change to your discord id!!!

@bot.event 
async def on_ready(ctx):  # When the bot is ready
    await ctx.send("Template saver ready for Template saving!") # Prints the bot's username and identifier

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command not found. You can view the available commands with **.help**.")

extensions = [
	'cogs.cog_example',  # Same name as it would be if you were importing it
  'cogs.basic_functions',
  'cogs.template_saver'
]

if __name__ == '__main__':  # Ensures this is the file being ran
	for extension in extensions:
		bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("DISCORD_BOT_SECRET") 
bot.run(token)  # Starts the bot