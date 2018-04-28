import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep,strftime
from sys import stdout
import os
import json
import sys

class auth(unittest.TestCase):
	"""docstring for auth"""
	def setUp(self):
		self.driver = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)

	def test_search_install(self):
		driver = self.driver
		driver.get('https://github.com/authzforce/fiware')
		version = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/div[2]/div/div/div[4]/div[1]/a[1]').get_attribute('data-name')
		print("version authzforce-ce-server :")
		print(version)
		print("")
		git = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/div/div/div[1]/div[1]/div/input').get_attribute('value')
		os.system('git clone ' + git)
		sleep(5)
		os.system('docker build -t authzforce-ce-server ./fiware/docker/')
		sleep(3)
		os.system('docker run -d -p 8080:8080 --name authzforce authzforce-ce-server')
		print("please wait : ")
		for i in range(0,11):
		    stdout.write("\r%d" % (i*10) + "%")
		    stdout.flush()
		    sleep(1)
		stdout.write("\n")
		os.system('curl -s --request GET http://0.0.0.0:8080/authzforce-ce/domains')
		print("---------------------------------------------------------------------")
		sleep(5)
		fecha = strftime("%d/%m/%y")
		hora = strftime("%H:%M:%S")
		host_name = os.popen("hostname").readline()
		resultado = os.popen("docker ps").readlines()
		contenedor =[host_name,fecha,hora,version,resultado[1].split()[11],resultado[1].split()[0],resultado[1].split()[7]]
		r = open('report.txt','w')
		r.write(str(contenedor[1]+','+contenedor[2]+','+contenedor[3]+','+contenedor[4]+','+contenedor[5]+','+contenedor[6]+','+contenedor[0]))

	def tearDown(self):
		self.driver.quit()
		os.system('docker rm -f authzforce')
	

if __name__ == "__main__":
	log_file = 'log_file.txt'
	f = open(log_file, 'w')
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()

#Samuel Castillo Texocotitla