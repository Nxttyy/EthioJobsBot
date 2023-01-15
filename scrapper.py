import requests
from bs4 import BeautifulSoup

headers =  {
				# "name": "Accept",
				# "value": "*/*",

				# "name": "Accept-Encoding",
				# "value": "gzip, deflate, br",
			
				# "name": "Accept-Language",
				# "value": "en-US,en;q=0.5",
			
				# "name": "Connection",
				# "value": "keep-alive",
			
				"User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0"
			}

r = requests.get('https://www.ethiojobs.net', headers=headers)
print(r)

soup = BeautifulSoup(r.content, 'html.parser')

ss = soup.find_all('div', class_="table-responsive")
# print(s.prettify())

def getLatestJobs():

	latestJobs = []

	for s in ss:
		# print(s)
		tables = s.find_all('table')
		# print(tables.prettify())

	for table in tables:
		tbs = table.find_all('tbody')
		# print(tbs)

	for tb in tbs:
		trs = tb.find_all('tr')

	for tr in trs:
		tds = tr.find_all('td')
		# for i in tds:
		# 	print(i)
		# print("\n")
		for td in tds:
			as_ = td.find('a')
			if as_:
				small = td.find('small')

				jobTitle = as_.text
				link = as_.get('href')
				company = small.text
			else:

				spans = td.find('span')
				if spans:
					small2 = td.find('small')

					location = spans.text
					date = small2.text
		latestJobs.append({"Job-Title":jobTitle, "Company":company, "Location":location, "Date":date, "Link":link})

	return latestJobs

