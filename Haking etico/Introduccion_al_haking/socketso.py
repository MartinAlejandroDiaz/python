import socket

s = socket.socket()
try:
#	s.connect(("scanme.nmap.org",22))
	s.connect(("dlptest.com",21))
	banner = s.recv(1024)
	print(banner)
except:
	print("Ocurrio un error en la coneccion")