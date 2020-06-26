import re
def extract_date(url):
        return re.findall(r'/(\d{4})/(\d{1,2})/(\d{1,2})/', url)
url1= "https://www.w3resource.com/python-exercises/re/2020/06/26/python-re-exercise-24.php"
print(extract_date(url1))