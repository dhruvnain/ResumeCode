import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.in/Apple-MWP22HN-A-AirPods-Pro/dp/B07ZRXF7M8/ref=sr_1_1_sspa?dchild=1&keywords=apple+airpods+pro&qid=1600289814&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNTVTNTU2TkcwQzYzJmVuY3J5cHRlZElkPUEwNjE0MzU1MVNMWVRGRFpVVDNFTiZlbmNyeXB0ZWRBZElkPUEwMDM5MzIwM0lNR0hWSTlBWEs1RyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'}
def check_rate():

	page = requests.get(URL, headers = headers)

	soup = BeautifulSoup(page.content, 'html.parser')

	title = soup.find(id="productTitle").get_text()
	price = soup.find(id="priceblock_ourprice").get_text()
	title=title.strip()
	n=''
	for i in price[2:9]:
		if ord(i)>= 48 and ord(i)<=57:
			n=n+i;
	cost=float(n)
	print(title)
	print(cost)
	if cost>=21000:
		send_mail()


def send_mail():
	server = smtplib.SMTP('smtp.gmail.com', 587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('', '')

	subject = "Price fell down and i have fallen down for you"
	body = "prices have fallen"+ "Open the link :"+"https://www.amazon.in/Apple-MWP22HN-A-AirPods-Pro/dp/B07ZRXF7M8/ref=sr_1_1_sspa?dchild=1&keywords=apple+airpods+pro&qid=1600289814&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzNTVTNTU2TkcwQzYzJmVuY3J5cHRlZElkPUEwNjE0MzU1MVNMWVRGRFpVVDNFTiZlbmNyeXB0ZWRBZElkPUEwMDM5MzIwM0lNR0hWSTlBWEs1RyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="
	msg = f"subject: {subject}\n\n{body}"

	server.sendmail('d6563190@gmail.com','pratha.srivastava_ug22@ashoka.edu.in', msg)

	print('email sent')

	server.quit()

check_rate()

