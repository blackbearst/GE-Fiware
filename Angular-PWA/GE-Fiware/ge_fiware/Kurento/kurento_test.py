from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import strftime
import time
import unittest
import json 
import os

class kurento(unittest.TestCase):
	"""docstring for kurento"""
	def setUp(self):
		self.driver = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)

	def test_search_install(self):
		driver =self.driver
		driver.get("https://github.com/Kurento/kurento-docker")
		clone = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/summary').click()
		gitclone = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/div/div/div[1]/div[1]/div/input').get_attribute('value')
		clone = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/summary').click()
		docker =  driver.find_element_by_link_text("docker").click()

		time.sleep(3)
		buildKMS = driver.find_element_by_xpath('.//*[@id="readme"]/article/pre[1]/code').text
		curl = driver.find_element_by_xpath('.//*[@id="readme"]/article/p[15]').text
		dockerfile =  driver.find_element_by_link_text("Dockerfile").click()

		time.sleep(3)
		version = driver.find_element_by_xpath('.//*[@id="LC3"]/span').text
		version =version[24:29]
		driver.quit() 
		
		print('--------------------------------')
		print ('Version ' + version)
		print('--------------------------------')
		#os.system('mkdir Docker')
		#os.system('mkdir report')
		#os.chdir("Docker")
		os.system('git clone ' + gitclone)
		os.chdir("kurento-docker/docker")
		buildKMS1 = buildKMS.replace("sudo docker build","docker build")
		buildKMS2 = buildKMS1.replace("sudo docker run","docker run -d --name kms -p 8888:8888")
		os.system(buildKMS2)
		print('-----------------------------------------------------------')
		os.system('docker ps -l')
		print('-----------------------------------------------------------')
		time.sleep(5)
		os.system(curl)
		time.sleep(5)
		print('-----------------------------------------------------------')


		os.chdir('../')
		os.chdir('../')
		#os.chdir('../')
		
		fecha = strftime("%y-%m-%d")
		hora = strftime("%H:%M:%S")

		host =  os.popen("hostname")
		host_name = host.readline()

		resultado = os.popen("docker ps -l").readlines()
		contenedor =[host_name,fecha,hora,version,resultado[1].split()[10],resultado[1].split()[0],resultado[1].split()[6]]
		#print(version)
		#print(contenedor)
		os.system('docker rm kms -f')

		f = open('report.txt','w')
		f.write(contenedor[1]+","+contenedor[2]+","+contenedor[3]+","+contenedor[4]+","+contenedor[5]+","+contenedor[6]+","+contenedor[0])
		
if __name__=="__main__":
	#log_file = 'log_file.txt'
	f = open('test.txt', 'w')
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()
	
# Gustavo Bautista Gutierrez
