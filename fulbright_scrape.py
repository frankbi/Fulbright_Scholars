import requests
from bs4 import BeautifulSoup

url = 'http://us.fulbrightonline.org/component/filter'
payload = {'view': 'searchresult', \
	'format': 'raw', \
	'sort': 'default', \
	'seq': 'default', \
	'year[]': '1991', \
	'start': '0'}

r = requests.post(url, data=payload)

soup = BeautifulSoup(r.text)
# content = soup.findAll('td', attrs={'style': 'color:  #565758'})
content = soup.findAll('td')
for rows in content:
	print rows
