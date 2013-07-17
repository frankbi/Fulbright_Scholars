import requests
import re
from bs4 import BeautifulSoup

# TODO
# Loop through the different starts
url = 'http://us.fulbrightonline.org/component/filter'
payload = {'view': 'searchresult', \
	'format': 'raw', \
	'sort': 'default', \
	'seq': 'default', \
	'year[]': '', \
	'start': '0'}

r = requests.post(url, data=payload)

soup = BeautifulSoup(r.text)

fulbright_info = []
content = soup.findAll('p', style=re.compile('font-size: 24px;'))
start = 0
end = 5
for rows in content:
	if rows.string.strip() != 'Search Results':
		name = rows.string.strip()
		name = re.sub(r'\s+', ' ', name)	
		scholar = []
		scholar.append(name)
		scholar_details = soup.findAll('td', style=re.compile('color: #565758'))
		for person in scholar_details[start:end]:
			scholar_info = person.string.strip()
			scholar.append(scholar_info)
			start += 1
			end += 1
		fulbright_info.append(scholar)
print fulbright_info
