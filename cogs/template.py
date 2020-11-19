import re

class Template:
  
  def __init__(self):
    self.name = ""
    self.keywords_list = []
    self.keyword_map = {}
    self.text = ""

  def new_template(self, ctx, name, keywords=[], text=""):
    self.name = name  
  
    for key in keywords:
      count = 0
      matches = re.finditer(rf"\[({key})\]", text)
      if matches:
        for match in matches:
          count = count + 1
        self.keyword_map[key] = count
      else:
        print("no match")
      
    for key in self.keyword_map:
      temp_count = self.keyword_map[key]
      while temp_count != 0:
        text = text.replace("[" + key + "]", "{" + key + "}", 1)
        temp_count -= 1
       
    self.text = text

    self.keywords_list = keywords 
    print(self.keyword_map)
  
  def show(self):
    return self.text
  
  def use(self, keywords):
    temp_keywords = keywords.split(', ')
    print(temp_keywords)
    text_to_send = self.text
    key_count = 0
    for word in self.keywords_list:
      print(word) 
      count = self.keyword_map[word]
      while count > 0:
        text_to_send = text_to_send.replace("{" + word + "}", temp_keywords[key_count], 1)
        key_count += 1
        count -= 1
    return text_to_send

    

    
    
    
 