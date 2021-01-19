import pandas as pd
import requests
from bs4 import BeautifulSoup

import pandas as pd
import requests
from bs4 import BeautifulSoup

# headers = {
#                 "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64;x64; rv:66.0) Gecko/20100101 Firefox/66.0", 
#                 "Accept-Encoding":"gzip, deflate","Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
#                 "DNT":"1","Connection":"close", 
#                 "Upgrade-Insecure-Requests":"1"
#                 }

headers= {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
             'Accept-Encoding': 'gzip, deflate',
             'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
             'Dnt': '1',
             'Host': 'httpbin.org',
             'Upgrade-Insecure-Requests': '1',
             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '
                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/83.0.4103.97 Safari/537.36',
             'X-Amzn-Trace-Id': 'Root=1-5ee7bbec-779382315873aa33227a5df6'}
prodict = {}
def get_product_links(URL):
	#to populate a dictionary
	page = requests.get(URL, headers  = headers)
	soup = BeautifulSoup(page.content, 'html.parser')

	results = soup.find_all(class_ = 'p-name p-name-type-2')
	for c in results:
	    title = c.em.get_text()
	    link = c.find('a', href = True)
	    if title and link and link.get('href'):
	    	#prodict[title] = link['href']
	    	raw_link = link.get('href')
	    	prod_url = raw_link[2:]

def check_if_has_coupon(url):
	page = requests.get(url, headers  = headers)
	soup = BeautifulSoup(page.content, 'html.parser')
	#available_coupon = soup.find_all('coupon-item current_sku_coupon_itemdong')
	available_coupon = soup.find('div',{'class':'summary-price J-summary-price'})
	return available_coupon

	#logic: coupon-val == 40, condition == '满300元可用'


# for i in range(1, 48):
# 	URL = 'https://search.jd.com/search?activity_id=200048246895&psort=2&stock=1&ev=exprice_1-100%5E&psort=2&page='+str(i) + '&s=61&click=0'
# 	get_product_links(URL)

print(check_if_has_coupon('http://item.jd.com/7213390.html'))

##nn: 对所有available的凑单产品进行筛选，如果有满300减40的券就保留下来
## 主要目标是将filter写在check_if_has_coupon的function中，如果有
