import re

class Template:
  # Todo: back end work to build variables into user input 
  # such that: ".new "person" "tom"" "person is good" -> in back end it would look like this : "person_1 is good". 
  # this way the template static is built once new template is called and variables are built in

  def __init__(self):
    self.name = ""
    self.keywords_list = []
    self.keyword_map = {}
    self.text = ""

  def new_template(self, ctx, name, keywords=[], text=""):
    self.name = name
    '''
    Actually I think that I have a better idea. Instead I'm going to make the text based on what the user provides as arguments. 
    Ex:
    Roster:
    - [player]
    - [player]
    - [player]

    each player argument that the user gives I'll put it into a queue and pop them out in the same order they went input

    In this way I won't need the amount of keywords

    Okay so I'm going to use Regex to filter out these wordsth
    the patter that I'm looking for is = '\[\w\]'
    '''    


    # okay coming back to this let me figure out what ths does
    # this finds the matches of my desired word and the # of occurense, it then prints the matches and the count. 
  
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
        #print(text)
    self.text = text
    #print(text.format(person="lucas"))


    #for match in matches:
     # print("finding matches: " + str(match)) 


    self.keywords_list = keywords 
    print(self.keyword_map)

    
    #self.text = text.split(' ')
    #print(self.text)
    
   
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

    

    
    
    
 