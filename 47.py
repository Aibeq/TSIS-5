import re 
newData = "Insta, is_an-awesome ! app + too"
  
print(re.split(', |_|-|!|\+', newData)) 