import os
import time

os.system('clear')
#install python, selenium and numpy
print('------------- install numpy and selenium -------------')

num = os.popen('python -c "import numpy"')
numpy = num.readlines()
numpy = []
if numpy:
	os.system('sudo pip install numpy')	
else:
	import numpy
	ver_numpy = numpy.version.version
	print('version numpy is: ' + ver_numpy)

	
sel = os.popen('python -c "import selenium"')
selenium = sel.readlines()
selenium = []
if selenium:
	os.system('sudo pip install selenium')
else:
	import selenium
	ver_selenium = selenium.__version__
	print('version selenium is: ' + ver_selenium)
	
#create dependencies
os.system('cd ge_fiware && mkdir report && cd report && touch report.json')
print('------------- install Selenium and Mongodb -------------')
os.system('docker-compose up -d')
print('------------- status of containers -------------')
os.system('docker-compose ps')
time.sleep(5)
#os.system('cd ge_fiware/Kurento && python Kurento.py') #run KMS
os.system('cd ge_fiware/Orion && python Orion.py') #run Orion
os.system('cd ge_fiware/Wirecloud && python Wirecloud.py') #run Wirecloud
#os.system('cd ge_fiware/Wilma && python Wilma.py') #run Wilma
os.system('cd ge_fiware/AuthzForce && python authzforce.py') #run AuthzForce
#os.system('cd ge_fiware/KeyRock && python keyrock.py') #run KeyRock
#os.system('cd ge_fiware/Knowage && python knowage.py') #run Knowage
print('------------- import report mongodb -------------')
os.system('cd ge_fiware/report && sudo docker cp report.json gefiware_fiware_report_1:/ && sudo docker exec gefiware_fiware_report_1 bash -c "mongoimport --db report_fiware --collection fiware --file report.json"')
print('------------- remove Selenium and Mongodb -------------')
os.system('docker-compose down')
print('------------- report json -------------')
report = open ('./ge_fiware/report/report.json','r')
rep = report.read()
print (rep)
report.close()
os.system('cd ge_fiware/report && sudo rm report.json')
