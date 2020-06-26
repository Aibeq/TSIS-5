import re
def check_num(string):
        text = re.compile(r"^1")
        if text.search(string):
         return True
        else:
         return False
print(check_num('1-5624895'))
print(check_num('9-5624895'))
