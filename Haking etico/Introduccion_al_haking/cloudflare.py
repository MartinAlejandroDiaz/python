import requests

def main():
	word = "cloudflare"
	url = requests.get("https://www.cloudflare.com/es-es/")
	cabeceras = dict(url.headers)
	verify = False
	print(cabeceras)
	for c in cabeceras:
		if word in cabeceras[c].lower():
			verify = True
			break
	if verify == True:
		print("cloudflare presente")
	else:
		print("El sitio no tiene cloudflare")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()
