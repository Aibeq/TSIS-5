import re 
string = '**//Python Exercises// - 12. '
#/d matches any decimal digit
#/W Matches any non-alphanumeric character except underscore(_)
result = re.sub('[\W_]+', '',string) 
print ( result) 