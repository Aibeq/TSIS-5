import re
string = "PHP Exercises"
print(string)
redata = re.compile(re.escape('php'), re.IGNORECASE)
new_string = redata.sub('php', 'PHP Exercises')
print("Using 'php' replace PHP") 
print("New Text: ",new_string)