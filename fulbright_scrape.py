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
	'year[]': '1991', \
	'start': '0'}

r = requests.post(url, data=payload)

soup = BeautifulSoup(r.text)

fulbright_info = []
content = soup.findAll('p', style=re.compile('font-size: 24px;'))
for rows in content:
	if rows.string.strip() != "Search Results":
		names = rows.string.strip()
		names = re.sub(r'\s+', ' ', names)	
		a = []
		a.append(names)

		crat = soup.findAll('td', style=re.compile('color: #565758'))
		for z in crat:
			asdf = z.string.strip()
			a.append(asdf)		
		# Append the remaining information to a before push to 2D
		fulbright_info.append(a)
print fulbright_info[0]
