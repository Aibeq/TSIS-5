import re
def check_string(text):
        string = 'ab{2,3}?'
        if re.search(string,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(check_string("ac"))
print(check_string("aabb"))
print(check_string("aabbbbbc"))