import re
words = ["Python PHP", "Java JavaScript", "c c++", "Platon Phantom"]

for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        
        if m:
            print(m.groups())