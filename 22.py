import re
string = 'Python exercises'
pattern='exercises'
for p in  re.finditer(pattern,string):
    s = p.start()
    e = p.end()
    print ("Found", pattern, "at",s,":",e)