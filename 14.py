import re
def check_string(text):
        string = '^[a-zA-Z0-9_]*$'
        if re.search(string,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(check_string("Frozen weather"))
print(check_string("Car_is_red_1"))