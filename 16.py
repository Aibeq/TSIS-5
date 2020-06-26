import re
 
sampleIP = '192.168.01.01'
 
print( re.sub('\.[0]*', '.', sampleIP) )