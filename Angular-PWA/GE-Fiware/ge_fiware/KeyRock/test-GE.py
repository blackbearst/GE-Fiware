import unittest
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from time import sleep,strftime
from sys import stdout
import os
import json
import sys

class idm(unittest.TestCase):
	"""docstring for idm"""
	def setUp(self):
		self.driver = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)

	def test_search_install(self):
		driver = self.driver
		driver.get('https://github.com/ging/fiware-idm')
		version = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div[4]/div[1]/div/div/div[4]/div[1]/a').get_attribute('data-name')
		print('version : ' + version)
		git = driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div[1]/div[4]/details/div/div/div[1]/div[1]/div/input').get_attribute('value')
		os.system('git clone ' + git)
		os.system('cd ./fiware-idm/extras/docker && docker-compose up -d')
		sleep(10)
		driver.get('http://localhost:3000')
		sleep(10)
		fecha = strftime("%d/%m/%y")
		hora = strftime("%H:%M:%S")
		host_name = os.popen("hostname").readline()
		resultado = os.popen("docker ps").readlines()
		contenedor =[host_name,fecha,hora,version,resultado[1].split()[14],resultado[1].split()[0],resultado[1].split()[7],resultado[2].split()[11],resultado[2].split()[0],resultado[1].split()[7]]
		r = open('report.txt','w')
		r.write(str(contenedor[1]+','+contenedor[2]+','+contenedor[3]+','+contenedor[4]+','+contenedor[5]+','+contenedor[6]+','+contenedor[7]+','+contenedor[8]+','+contenedor[9]+','+contenedor[0]))


	def tearDown(self):
		self.driver.quit()
		os.system('cd ./fiware-idm/extras/docker && docker-compose down')

if __name__ == "__main__":
	log_file = 'log_file.txt'
	f = open(log_file, 'w')
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()

#Samuel Castillo Texocotitla