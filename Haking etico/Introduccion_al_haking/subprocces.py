import os
import subprocess

a = open(os.devnull,'w')
p = subprocess.call(['ping','1.1.1.1'],stdout=a,stderr=subprocess.STDOUT)
if p == 0:
	print("El comando se ejecuto correctamente")
else:
	print("Fallo la ejecucion del comando")
#os.system("ping 1.1.1.1")