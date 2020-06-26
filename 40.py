import re 
  
def remove(string): 
    pattern = re.compile(r'\s+') 
    return re.sub(pattern, '', string) 
      
# Driver Program 
string = 'Python   Exercises'
print(remove(string)) 