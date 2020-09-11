import json
import urllib

def main():
	url = urllib.urlopen("https://curso--python-0-pruebas.000webhostapp.com/wp-json/wp/v2/users")
	for u in json.loads(url.read()):
		user = u['slug']
	print(user)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()