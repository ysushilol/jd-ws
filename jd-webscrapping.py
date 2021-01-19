import pandas as pd
import requests
from bs4 import BeautifulSoup

headers = {
                "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;x64; rv:66.0) Gecko/20100101 Firefox/66.0", 
                "Accept-Encoding":"gzip, deflate","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
                "DNT":"1","Connection":"close", 
                "Upgrade-Insecure-Requests":"1"
                }
prodict = {}
def get_product_links(URL):
	#to populate a dictionary
	page = requests.get(URL, headers  = headers)
	soup = BeautifulSoup(page.content, 'html.parser')

	results = soup.find_all(class_ = 'p-name p-name-type-2')

	for c in results:
	    title = c.em.get_text()
	    link = c.find('a', href = True)
	    if title and link and link['href']:
	    	prodict[title] = link['href']
for i in range(1, 48):
	URL = 'https://search.jd.com/search?activity_id=200048246895&psort=2&stock=1&ev=exprice_1-100%5E&psort=2&page='+str(i) + '&s=61&click=0'
	get_product_links(URL)

print(prodict)
