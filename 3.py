import re
def check_string(text):
        string = 'ab+?'
        if re.match(string,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(check_string("ac"))
print(check_string("abc"))
print(check_string("abbc"))