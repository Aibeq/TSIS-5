import re
def check_string(my_string):
	regex = re.compile(r"[A-Za-z0-9.]")
	string = regex.search(my_string)
	
	return not bool(string)
print(check_string("A"))
print(check_string("*&%@#!}{"))

