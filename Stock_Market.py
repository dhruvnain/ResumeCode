import requests
from bs4 import BeautifulSoup
from googlesearch import search
import time

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}

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

	print("Sensex        :",Sensex_price)
	print("Sensex Change :",Sensex_change)

"""
while (True):
	ratecheker()
	print("_______________________________________________________________________")
	time.sleep(1)
"""

ratecheker()
def NSE():
	number = int(input("Enter Number of Stocks:"))
	for i in range(number):
		share=str(input("Name your share: "))
		share1 = "nseindia.com/"+share
	#print(share1)
		for j in search(share1, tld="co.in",num =1, stop=1, pause=2):
			stock_price_URL = str(j)
			#print(stock_price_URL)
			Stock_price = requests.get(stock_price_URL, headers = headers)
			#print(Stock_price)
			soup3 = BeautifulSoup(Stock_price.content, 'html.parser')
			kimat = soup3.find(id='responseDiv').get_text().strip().split(":")

		current_cost(kimat,share)
		dayhigh(kimat,share)
		daylow(kimat,share)
		year_low(kimat,share)
		year_high(kimat,share)
		traded_volume(kimat,share)

def daylow(kimat,share):
	for i in kimat:
		if "dayLow" in i:
			index = kimat.index(i)
			#print(kimat[index+1])	
			low = kimat[index+1]
	n=''
	for i in low:
		if (ord(i)>= 48 and ord(i)<=57) or i=='.':
			n=n+i;
	print(f'Day Low : {n}')
	

def dayhigh(kimat,share):
	for i in kimat:
		if "dayHigh" in i:
			index = kimat.index(i)
			#print(kimat[index+1])	
			high= kimat[index+1]
	n=''
	for i in high:
		if (ord(i)>= 48 and ord(i)<=57) or i=='.':
			n=n+i;
	print(f'Day High : {n}')
	

def year_low(kimat,share):
	for i in kimat:
		if "low52" in i:
			index = kimat.index(i)
			#print(kimat[index+1])	
			low = kimat[index+1]
	n=''
	for i in low:
		if (ord(i)>= 48 and ord(i)<=57) or i=='.':
			n=n+i;
	print(f'52 Week Low : {n}')

def year_high(kimat,share):
	for i in kimat:
		if "high52" in i:
			index = kimat.index(i)
			#print(kimat[index+1])	
			high = kimat[index+1]
	n=''
	for i in high:
		if (ord(i)>= 48 and ord(i)<=57) or i=='.':
			n=n+i;
	print(f'52 Week High : {n}')

def traded_volume(kimat,share):
	for i in kimat:
		if "totalTradedValue" in i:
			index = kimat.index(i)
			#print(kimat[index+1])	
			tradedvalue = kimat[index+1]
	n=''
	for i in tradedvalue:
		if (ord(i)>= 48 and ord(i)<=57) or i=='.':
			n=n+i;
	print(f'Total Traded Value: {n} lacs')

def current_cost(kimat,share):
	for i in kimat:
		if "lastPrice" in i:
			index = kimat.index(i)
			#print(kimat[index+1])	
			current_rate = kimat[index+1]
	n=''
	for i in current_rate:
		if (ord(i)>= 48 and ord(i)<=57) or i=='.':
			n=n+i;
	print(f'{share}: {n}')

NSE()


