import re
def url(str):
    str = 'https://auth.mywebsite.org / user / python program / http://www.mywebsite.org/'
   # findall() has been used
   # with valid conditions for urls in string
   url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
   
   # Driver Code
   print(str)
   print("Url is :: ", url(str))