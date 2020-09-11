import os
from subprocess import check_output
import subprocess

a = check_output('systeminfo',stderr=subprocess.STDOUT)
n = open('test.txt','w+')
n.write(a)
print("Hola :)")
n.close()