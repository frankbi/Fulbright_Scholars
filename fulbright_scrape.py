from bs4 import BeautifulSoup
import requests
import re
import csv

# Global variables
fulbright_info = []

c = csv.writer(open('Fulbright_Scholars.csv', 'wb'), quoting = csv.QUOTE_ALL)
c.writerow(['Grantee','Institution','State','Field','County','Year'])

def getData(start):
	url = 'http://us.fulbrightonline.org/component/filter'
	payload = {'view': 'searchresult', \
		'format': 'raw', \
		'sort': 'default', \
		'seq': 'default', \
		'year[]': '', \
		'start': start}
		# 27300

	r = requests.post(url, data=payload)
	soup = BeautifulSoup(r.text)
	return soup

soup = getData(0)

content = soup.findAll('p', style=re.compile('font-size: 24px;'))
print len(content)
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

for i in range(0, 20):
	name = fulbright_info[i][0]
	school = fulbright_info[i][1]
	state = fulbright_info[i][2]
	field = fulbright_info[i][3]
	country = fulbright_info[i][4]
	year = fulbright_info[i][5]
	# print name + " " + school + " " + state + " " + field + " " + country + " " + year
	c.writerow([name,school,state,field,country,year])
