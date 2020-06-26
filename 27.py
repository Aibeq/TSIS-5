import re
# Sample string.
string = "1 One, 2 Two, 3 Three"
result = re.split("\D+", string)
# Print results.
for element in result:
    print(element)
    