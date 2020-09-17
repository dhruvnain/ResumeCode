import requests
from bs4 import BeautifulSoup
from googlesearch import search
import time

def ratecheker():
	URL1='https://www.google.com/search?q=sensex+price&oq=Sensex+Price&aqs=chrome.0.0l4.2979j1j8&sourceid=chrome&ie=UTF-8'
	URL2='https://www.google.com/search?q=nifty+price&oq=Nifty+Price&aqs=chrome.0.0l8.3725j1j8&sourceid=chrome&ie=UTF-8'

	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

	Nifty = requests.get(URL2, headers = headers)
	Sensex = requests.get(URL1, headers = headers)

	soup1 = BeautifulSoup(Nifty.content, 'html.parser')
	soup2 = BeautifulSoup(Sensex.content, 'html.parser')

	Nifty_change = soup1.find(jsname='qRSVye').get_text()
	Nifty_price = soup1.find(jsname='vWLAgc').get_text()


	Sensex_change = soup2.find(jsname='qRSVye').get_text()
	Sensex_price = soup2.find(jsname='vWLAgc').get_text()

	print("Nifty         :",Nifty_price)
	print("Nifty Change  :",Nifty_change)

	print("Sensex         :",Sensex_price)
	print("Sensex Change  :",Sensex_change)

while (True):
	ratecheker()
	print("*****************************************************************************")
	time.sleep(1)
