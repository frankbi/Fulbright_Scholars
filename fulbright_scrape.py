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
# content = soup.findAll('td', attrs={'style': 'color:  #565758'})

fulbright_info = []
content = soup.findAll('p', style=re.compile("font-size: 24px;"))
for rows in content:
	if rows.string.strip() != "Search Results":
		names = rows.string.strip()
		# TODO
		# Need to cut down on whitespace between first and last names		
		a = []
		a.append(names)
			# TODO
			# Append the remaining information to a before push to 2D
		fulbright_info.append(a)
print fulbright_info[0]
