import re
def check_num(string):
        text = re.compile(r".*[0-9]$")
        if text.search(string):
         return True
        else:
         return False
print(check_num('abcdef'))
print(check_num('abcdef6'))
