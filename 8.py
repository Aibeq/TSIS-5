import re
def check_string(text):
        string = '^[a-z]+_[a-z]+$'
        if not re.match(string,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(check_string("aab_cbbbc"))
print(check_string("aab_Abbbc"))
print(check_string("Aaab_abbbc"))