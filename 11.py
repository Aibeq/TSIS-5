import re
def check_string(text):
        string = '\w+\S*$'
        if re.search(string,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(check_string("Car is red."))
print(check_string("Car is red. "))