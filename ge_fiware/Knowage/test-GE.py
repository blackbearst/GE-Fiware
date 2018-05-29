import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from sys import stdout
from time import sleep,strftime
import os

class knowage(unittest.TestCase):
	"""docstring for knowage"""
	def setUp(self):
		self.driver = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)

	def test_search_install(self):
		driver = self.driver
		driver.get('https://github.com/KnowageLabs/Knowage-Server-Docker')
		git = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/div/div/div[1]/div[1]/div/input').get_attribute('value')
		os.system('git clone ' + git)
		sleep(5)
		os.system('cd Knowage-Server-Docker/6.1.1/ && docker-compose up -d')
		print("please wait : ")
		for i in range(0,101):
		    stdout.write("\r%d" % (i) + "%")
		    stdout.flush()
		    sleep(1)
		stdout.write("\n")
		os.system('curl http://0.0.0.0:8080/knowage')
		driver.get('http://localhost:8080/knowage')
		sleep(15)
		user = driver.find_element_by_id('userID')
		password = driver.find_element_by_id('password')
		user.send_keys('biadmin')
		password.send_keys('biadmin')
		password.submit()
		sleep(10)
		driver.find_element_by_xpath('//*[@id="divContainer"]/a[1]').click()
		sleep(3)
		driver.find_element_by_xpath('//*[@id="sidebar"]/div[1]/a').click()
		sleep(3)
		driver.find_element_by_xpath('//*[@id="settings-dropdown"]/li[4]/a').click()
		sleep(8)
		fecha = strftime("%d/%m/%y")
		hora = strftime("%H:%M:%S")
		version = "6.1.1"
		host_name = os.popen("hostname").readline()
		resultado = os.popen("docker ps").readlines()
		contenedor =[host_name,fecha,hora,version,resultado[1].split()[11],resultado[1].split()[0],resultado[1].split()[7],resultado[2].split()[10],resultado[2].split()[0],resultado[2].split()[6]]
		r = open('report.txt','w')
		r.write(str(contenedor[1]+','+contenedor[2]+','+contenedor[3]+','+contenedor[4]+','+contenedor[5]+','+contenedor[6]+','+contenedor[7]+','+contenedor[8]+','+contenedor[9]+','+contenedor[0]))


	def tearDown(self):
		self.driver.quit()
		os.system('cd Knowage-Server-Docker/6.1.1/ && docker-compose down')

if __name__ == "__main__":
	log_file = 'log_file.txt'
	f = open(log_file, 'w')
	runner = unittest.TextTestRunner(f)
	unittest.main(testRunner=runner)
	f.close()

#Samuel Castillo Texocotitla