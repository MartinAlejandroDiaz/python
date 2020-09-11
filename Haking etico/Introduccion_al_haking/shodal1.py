import sys
from shodan import Shodan

def main():
	api = Shodan('T3YseGLAzQ6pmPAW4qfVyHKAi20gHfX6')
	h = api.host('84.199.0.254')
	print(h)
	print('''
		Direccion: {}
		Ciudad: {}
		ISP: {}
		Organizacion: {}
		Puertos: {}

		'''.format(h['ip_str'],h['city'],h['isp'],h['org'],h['ports']))

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()