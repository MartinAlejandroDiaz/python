import wget
from xml.etree.ElementTree import parse

def main():
	download = wget.download(url="https://curso-python-0-pruebas-pentest-joomla.000webhostapp.com/administrator/manifests/files/joomla.xml")
	archivo = parse("joomla.xml")
	for element in archivo.findall('version'):
		ver = element.text
	print('\n\n' + ver)
if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("Saliendo")
		exit()