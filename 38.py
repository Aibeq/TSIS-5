import re
string = '"C++" "Python"'
print (re.findall(r'"(.*?)"', string))