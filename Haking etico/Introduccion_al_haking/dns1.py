import dns.resolver

def main():

# Obtiene todas las consultas posibles (aveces no funciona por eso siempre tener alternativas)
		try:
			a = dns.resolver.query("google.com",ANY)
			for q in a:
				print(q)
		except:
			print("No pude obtener la consulta")

# Obtiene todas las consultas de la lista
#	consultas = ['A','AAAA','NS','SOA','MX','MF','MS','TEXT','CNAME']
#	for c in consultas:
#		try:
#			a = dns.resolver.query("google.com",c)
#			for q in a:
#				print(q)
#		except:
#			print("No pude obtener la consulta")


# Unica consulta
#	try:
#		a = dns.resolver.query("google.com","CNAME")
#		for q in a:
#			print(q)
#	except:
#		print("No pude obtener la consulta")

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		exit()