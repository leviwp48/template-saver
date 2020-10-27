class Template:
  # Todo: back end work to build variables into user input 
  # such that: ".new "person" "tom"" "person is good" -> in back end it would look like this : "person_1 is good". 
  # this way the template static is built once new template is called and variables are built in
  def __init__(self):
    self.keywords_list = []
    self.text = ""

  def new_template(self, ctx, keywords=[], keywords_amount=[], text=""):
    
    if(len(keywords) != len(keywords_amount)):
      return
    
    count = 0

    while(count < len(keywords)): 
      self.keywords_list[count] = 

      print("adding to dict: " + keywords[count] + "  : " + keywords_amount[count])
      
      count += 1
    print(self.keywords_list)
    self.text = text

  def show(self):
    return self.text
    

    
    
    
