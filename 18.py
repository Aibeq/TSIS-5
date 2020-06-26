import re 
  
 
def getNumbers(str): 
    array = re.findall(r'[0-9]+', str) 
    return array 
  
str = "Exercises number 1, 12, 13, and 345 are important"
array = getNumbers(str) 
print(*array)