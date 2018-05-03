import os
import time

os.system('clear')


#install python, pip and numpy
print('------------- install pip, numpy and selenium -------------')
os.system('sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get install -y python.pip && pip install numpy && pip install selenium ')

"""
#install Selenium and chrome
print('------------- install Selenium and chrome -------------')
os.system('cd extras && chmod 777 install_selenium.sh && chmod 777 start-chrome.sh')
os.system('cd extras && ./install_selenium.sh && ./start-chrome.sh')

#install Docker
print('------------- install Docker -------------')
os.system('sudo apt-get install -y linux-image-extra-$(uname -r) linux-image-extra-virtual && \
    sudo apt-get update -y && \
    sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common && \
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
    sudo apt-key fingerprint 0EBFCD88 && \
	sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" && \
    sudo apt-get update -y && \
    sudo apt-get install -y docker-ce && \
    cat /etc/gshadow && \
    sudo adduser root docker && \
    sudo docker run hello-world')
 
"""
os.system('cd ge_fiware && mkdir report && cd report && touch report.json')
print('------------- install Selenium and Mongodb -------------')
os.system('sudo docker-compose up -d')
#os.system('sudo docker build -t mongo/ge_fiware_report . && sudo docker-compose up -d')
print('------------- status of containers -------------')
os.system('sudo docker-compose ps')
time.sleep(5)
os.system('clear')
#dir = os.getcwd()
os.system('cd ge_fiware && cd Kurento && python Kurento.py') #run KMS
os.system('cd ge_fiware && cd Orion && python Orion.py') #run Orion
os.system('cd ge_fiware && cd AuthzForce && python authzforce.py') #run AuthzForce
os.system('cd ge_fiware && cd KeyRock && python keyrock.py') #run KeyRock
os.system('cd ge_fiware && cd Knowage && python knowage.py') #run Knowage
os.system('clear')
print('------------- import report mongodb -------------')
os.system('cd ge_fiware/report && sudo docker cp report.json gefiware_fiware_report_1:/ && sudo docker exec gefiware_fiware_report_1 bash -c "mongoimport --db report_fiware --collection fiware --file report.json"')
print('------------- remove Selenium and Mongodb -------------')
os.system('sudo docker-compose rm -s -f')
print('------------- report json -------------')
report = open ('./ge_fiware/report/report.json','r')
rep = report.read()
print (rep)
report.close()
os.system('cd ge_fiware/report && sudo rm report.json')
