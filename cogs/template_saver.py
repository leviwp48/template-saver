import discord
from discord.ext import commands
from .template import Template

class TemplateSaver(commands.Cog, name='Template Saver'):
  
  saved_templates = [] 
  
  def __init__(self, bot):
    self.bot = bot
    

  @commands.command(name="new_template")
  async def new_template(self, ctx, keywords, keywords_amount, message):
    
    keywords_list = []
    for key in keywords.split(', '):
      keywords_list.append(key)
    keywords_amount_list = []
    for amount in keywords_amount.split(', '):
      keywords_amount_list.append(amount)

    print("keywords: " + str(keywords_list))
    print("keywords_amount: " + str(keywords_amount_list))
    print("message: " + message)

    new_template = Template()
    new_template.new_template(ctx, keywords_list, keywords_amount_list, message)

    await ctx.send(new_template.show())

    self.saved_templates.append(new_template)

  @commands.command(name="view_templates")
  async def view_templates(self, ctx):
    template_count = 1
    template_list = ""
    for i in self.saved_templates:
      template_list = template_list + "[" + str(template_count) + "] " + i + "\n"
      template_count+=1

    await ctx.send(f"Saved templates: \n================ \n{template_list}")

  @commands.command(name="use_template")
  async def use_template(self,ctx):
    await ctx.send("hi")

  @commands.command(name="confirm")
  async def confirm(self, ctx, answer):
    if answer == "yes":
      return True 
    else:
      return False 
    
def setup(bot):
	bot.add_cog(TemplateSaver(bot))
