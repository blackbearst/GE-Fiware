import unittest
from time import sleep,strftime
import subprocess
import os

class auth(unittest.TestCase):
	"""docstring for auth git (https://github.com/authzforce/fiware.git)"""

	def test_search_install(self):
		os.system('cd ./fiware && git pull')
		version = subprocess.check_output("cd ./fiware && git describe --tags", shell=True).strip()
		sleep(5)
		os.system('docker build -t authzforce-ce-server ./fiware/docker/')
		sleep(3)
		os.system('docker run -d -p 8080:8080 --name authzforce authzforce-ce-server')
		sleep(11)
		os.system('curl -s --request GET http://0.0.0.0:8080/authzforce-ce/domains')
		print("---------------------------------------------------------------------")
		sleep(5)
		fecha = strftime("%d/%m/%y")
		hora = strftime("%H:%M:%S")
		host_name = os.popen("hostname").readline()
		resultado = os.popen("docker ps").readlines()
		contenedor =[host_name,fecha,hora,version,resultado[1].split()[11],resultado[1].split()[0],resultado[1].split()[7]]
		r = open('report.txt','w')
		r.write(contenedor[1]+","+contenedor[2]+","+contenedor[3]+","+contenedor[4]+","+contenedor[5]+","+contenedor[6]+","+contenedor[0])

	def tearDown(self):
		os.system('docker rm -f authzforce')
	
if __name__ == "__main__":
	log_file = 'log_file.txt'
	f = open(log_file, 'w')
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()

#Samuel Castillo Texocotitla