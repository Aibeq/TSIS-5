import re
def check_string(text):
        string = 'a.*?b$'
        if re.match(string,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(check_string("aabbbbd"))
print(check_string("aab_Abbbc"))
print(check_string("accddbbjjjb"))