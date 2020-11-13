import discord
from discord.ext import commands
from .template import Template

class TemplateSaver(commands.Cog, name='Template Saver'):
  
  saved_templates = [] 
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command(name="new")
  async def new(self, ctx, name, keywords, message):
    
    keywords_list = []
    for key in keywords.split(', '):
      keywords_list.append(key)

    #print("keywords: " + str(keywords_list))
    #print("message: " + message)

    new_template = Template()
    new_template.new_template(ctx, name,keywords_list, message)

    await ctx.send(new_template.show)

    self.saved_templates.append(new_template)

  @commands.command(name="view")
  async def view(self, ctx):
    template_count = 1
    
    #for i in self.saved_templates:
      #template_list = template_list + "[" + str(template_count) + "] " + i + "\n"
      #template_count+=1
    print(self.saved_templates)
    await ctx.send(f"Saved templates: \n================ \n {template_count}: {self.saved_templates[0].name}")

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
