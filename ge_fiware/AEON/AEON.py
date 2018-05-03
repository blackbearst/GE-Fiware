#!/usr/bin/python
#TSG
import os
import subprocess
import json
import time
#import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

os.system('clear')
print('------------- install AEON -------------')

starting_point = time.time()
#Utilizando docker-compose
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)

#*************************************************************************************************************************************
# Create a new instance of the Chrome driver sin docker-compose
#driver = webdriver.Chrome()


# go to the catalogue fiware enablers page
driver.get("https://github.com/atos-ari-aeon/fiware-cloud-messaging-platform")
driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/summary').click()

clone = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/div/div/div[1]/div[1]/div/input').get_attribute('value')
time.sleep(3)
driver.quit()
os.system("git clone '"+clone+"'")
os.chdir("fiware-cloud-messaging-platform/docker")
os.system("sed -i 's/192.168.59.103/127.0.0.1/g' docker-compose.yml")
os.system("chmod +x deploy_aeon.sh")
time.sleep(10)
#os.system("sed -i 's/aeon up/aeon up -d/deploy_aeon.sh")

#os.system("./deploy_aeon.sh")
os.system('gnome-terminal -e "bash deploy_aeon.sh"')
#Esperando para clonar
time.sleep(500)

#Teniendo clonado la carpeta
#time.sleep(150)
#os.system("curl http://localhost:8080")

#prueba = webdriver.Chrome()
driver = webdriver.Remote("http://127.0.0.1:4444/wd/hub", DesiredCapabilities.CHROME)
driver.get("http://localhost:8080")
time.sleep(10)
driver.quit()
#*************************************************************************************************************************************


elapsed_time = time.time() - starting_point
#Redondeando el numero
elapsed_time_int = int(elapsed_time)
#Obteniendo minutos y segundos
elapsed_time_minutes = elapsed_time_int/60
elapsed_time_seconds = elapsed_time_int%60
sleep(3)
os.system("cd ..")
sleep(3)
os.system("cd ..")

#print tiempo.total_seconds()

#Formatenado informacion de contenedores
sleep(10)
list_cont = "docker ps -a --no-trunc --format 'table {{.ID}}\t{{.Names}}\t{{.Status}}'"
sleep(3)
list_image = "docker images --no-trunc --format 'table {{.Repository}}\t{{.Tag}}'"


sleep(3)
#Obteniendo valores de consola
servicios = subprocess.Popen(list_cont, stdout=subprocess.PIPE, stderr=None, shell=True)
sleep(3)
imagenes = subprocess.Popen(list_image, stdout=subprocess.PIPE, stderr=None, shell=True)

sleep(3)
out_cont = servicios.communicate()[0]
sleep(3)
out_image = imagenes.communicate()[0]

cont_spl = out_cont.split()
image_spl = out_image.split()
#up = out_cont.count("Up")
#ex = out_cont.count("Exited")
#cre = out_cont.count("Created")
up = 0
ex = 0
cre = 0

#print out_image
sleep(3)
for i in range(len(image_spl)):
	if image_spl[i] == 'aeon_dashboard':
		version = image_spl[i+1]


#Host
sleep(3)
host = subprocess.Popen('hostname', stdout=subprocess.PIPE, stderr=None, shell=True)
usr = host.communicate()[0]
usuario = usr.split()


fecha = time.strftime("%y-%m-%d")
hora = time.strftime("%X")


#JSON file
aeon={}
aeon['GE'] = 'AEON'
aeon['Date'] = fecha
aeon['Time'] = hora
aeon['Version']= version
aeon['Host'] = usuario[0]
sleep(3)

#rest
#events,rest/events
#events/rabbitmq,rabbitmq,rest/rabbitmq
#dashboard,rest/dashboard
#events/mongo,mongo,rest/mongo

aeon['Services']=[]
for i in range(len(cont_spl)):
	if cont_spl[i] == 'Exited' and (cont_spl[i-1] == 'rest' or cont_spl[i-1] == 'events,rest/events' or cont_spl[i-1] == 'events/rabbitmq,rabbitmq,rest/rabbitmq' or cont_spl[i-1] == 'dashboard,rest/dashboard' or cont_spl[i-1] == 'events/mongo,mongo,rest/mongo'):
		aeon['Services'].append({'Container_ID': cont_spl[i-2],'Name':cont_spl[i-1],'Status':cont_spl[i]})
		ex = ex + 1
	if cont_spl[i] == 'Up' and (cont_spl[i-1] == 'rest' or cont_spl[i-1] == 'events,rest/events' or cont_spl[i-1] == 'events/rabbitmq,rabbitmq,rest/rabbitmq' or cont_spl[i-1] == 'dashboard,rest/dashboard' or cont_spl[i-1] == 'events/mongo,mongo,rest/mongo'):
		aeon['Services'].append({'Container_ID': cont_spl[i-2],'Name':cont_spl[i-1],'Status':cont_spl[i]})	
		up = up + 1
	if cont_spl[i] == 'Created' and (cont_spl[i-1] == 'rest' or cont_spl[i-1] == 'events,rest/events' or cont_spl[i-1] == 'events/rabbitmq,rabbitmq,rest/rabbitmq' or cont_spl[i-1] == 'dashboard,rest/dashboard' or cont_spl[i-1] == 'events/mongo,mongo,rest/mongo'):
		aeon['Services'].append({'Container_ID': cont_spl[i-2],'Name':cont_spl[i-1],'Status':cont_spl[i]})		
		cre = cre + 1
#aeon['Services'] = [{'Container_ID': cont_spl[4],'Name':cont_spl[5],'Status':cont_spl[6]}, {'Container_ID': cont_spl[12],'Name':cont_spl[13],'Status':cont_spl[14]}, {'Container_ID': cont_spl[20],'Name':cont_spl[21],'Status':cont_spl[22]} ,{'Container_ID': cont_spl[26],'Name':cont_spl[27],'Status':cont_spl[28]}, {'Container_ID': cont_spl[32],'Name':cont_spl[33],'Status':cont_spl[34]}]

res="Faild"
#Prueba
if up>ex:
	res="Successfully"

aeon['Services Exited'] = ex
aeon['Services Up'] = up
aeon['Services Created'] = cre
aeon['Test'] = res
#aeon['Test Time'] = tiempo.total_seconds()
aeon['Test Time'] = 'Run test in '+str(elapsed_time_minutes)+' minutes '+str(elapsed_time_seconds)+' seconds'

#File build JSON
with open('report.json', 'a') as outfile:
    archivo = json.dump(aeon,outfile)
os.system("echo  '\n' >> ge.json")
os.system("cat report.json")

#Deteniendo servicios
sleep(3)
#os.system("sudo docker stop $(sudo docker ps -a -q)")
os.system("sudo docker stop rest")
sleep(1)
os.system("sudo docker stop events,rest/events")
sleep(1)
os.system("sudo docker stop events/rabbitmq,rabbitmq,rest/rabbitmq")
sleep(1)
os.system("sudo docker stop dashboard,rest/dashboard")
sleep(1)
os.system("sudo docker stopevents/mongo,mongo,rest/mongo")
sleep(3)
#os.system("sudo docker rm $(sudo docker ps -a -q)")
os.system("sudo docker rm rest")
sleep(1)
os.system("sudo docker rm events,rest/events")
sleep(1)
os.system("sudo docker rm events/rabbitmq,rabbitmq,rest/rabbitmq")
sleep(1)
os.system("sudo docker rm dashboard,rest/dashboard")
sleep(1)
os.system("sudo docker rm events/mongo,mongo,rest/mongo")

#Torres Salinas Gustavo