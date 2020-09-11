import requests
from bs4 import BeautifulSoup

def main():
	a = requests.get("https://who.is/whois/reldsec.org")
	soup = BeautifulSoup(a.text, 'html5lib')
	for l in soup.find_all("pre"):
		print(l.get_text())
		
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()