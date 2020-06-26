from datetime import datetime

oldformat = '20200626'
datetimeobject = datetime.strptime(oldformat,'%Y%m%d')

newformat = datetimeobject.strftime('%Y-%m-%d')
print (newformat)

newformat2 = datetimeobject.strftime('%d-%m-%Y')
print (newformat2)
