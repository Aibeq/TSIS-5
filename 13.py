import re
def check_string(text):
        string = '\Bz\B'
        if re.search(string,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(check_string("Frozen weather"))
print(check_string("Car is red."))