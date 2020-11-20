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

    new_template = Template()
    new_template.new_template(ctx, name, keywords_list, message)

    self.saved_templates.append(new_template)
    await ctx.send("Template was saved!")

  @new.error
  async def new_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("Missing a required argument, there may be a quote out of place.")

  @commands.command(name="view")
  async def view(self, ctx):
    template_count = 1
    template_list = "Saved templates: \n================ \n"
       
    for template in self.saved_templates:
      template_list = template_list + str(template_count) + ": " + template.name + '\n'
      template_count += 1
    await ctx.send(template_list)

  @view.error
  async def view_error(self, ctx, error):
    if isinstance(error, commands.CheckAnyFailure):
      await ctx.send("Not sure what happend here :[")
  
  @commands.command(name="use")
  async def use(self, ctx, name, keywords):
    print("tyring to use")
    tracker = 0
    for template in self.saved_templates:
      print(" using tempalte : " + template.name)
      if name == template.name:
        print("going to use")
        await ctx.send(self.saved_templates[tracker].use(keywords)) 
      tracker += 1
    return
    
  @use.error
  async def use_error(self, ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
      await ctx.send("Missing a required argument, there may be a quote out of place.")
    #should have an error if a template doesn't exist

def setup(bot):
	bot.add_cog(TemplateSaver(bot))
