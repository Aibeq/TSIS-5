import re  

target_string = 'Python Exercises, PHP exercises.'  

replace = ":"

pattern = "[ ,.]"


print(re.sub(pattern, replace, target_string) )