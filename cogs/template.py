class Template:
  
  def __init__(self):
    self.keywords_dict = {}
    self.text = ""

  def new_template(self, ctx, keywords=[], keywords_amount=[], text=""):
    
    if(len(keywords) != len(keywords_amount)):
      return
    
    count = 0

    while(count < len(keywords)): 
      self.keywords_dict[keywords[count]] = keywords_amount[count]

      print("adding to dict: " + keywords[count] + " : " + keywords_amount[count])
      
      count += 1
      
    self.text = text

  def show(self):
    return self.text
    

    
    
    
