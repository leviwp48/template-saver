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
    new_template.new_template(ctx, name, keywords_list, message)

    self.saved_templates.append(new_template)
    await ctx.send("Template was saved!")

  @commands.command(name="view")
  async def view(self, ctx):
    template_count = 1
    template_list = "Saved templates: \n================ \n"
    
    #for i in self.saved_templates:
      #template_list = template_list + "[" + str(template_count) + "] " + i + "\n"
      #template_count+=1
    for template in self.saved_templates:
      template_list = template_list + str(template_count) + ": " + template.name + '\n'
      template_count += 1
    await ctx.send(template_list)


  @commands.command(name="use")
  async def use(self,ctx, name, keywords):
    tracker = 0
    for template in self.saved_templates:
      if name == template.name:
        print("going to use")
        await ctx.send(self.saved_templates[tracker].use(keywords)) 
      tracker += 1
      return


  @commands.command(name="confirm")
  async def confirm(self, ctx, answer):
    if answer == "yes":
      return True 
    else:
      return False 
    
def setup(bot):
	bot.add_cog(TemplateSaver(bot))
