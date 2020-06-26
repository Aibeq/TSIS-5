import re
literals = [ 'fox', 'dog', 'horse' ]
string = ('The quick brown fox jumps over the lazy dog.')

for lit in literals :
    if re.search(lit,string,flags=1):
        print ("The word",lit,"exist")
    else :
        print("The word",lit,"doesn't exist")