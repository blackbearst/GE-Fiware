from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import os
import time
import unittest

class Wilma(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Remote(
				command_executor='http://localhost:4444/wd/hub',
				desired_capabilities=DesiredCapabilities.CHROME)
	def test(self):
		driver = self.driver
		driver.get("https://github.com/ging/fiware-pep-proxy")
		
		branch = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/div[1]/button').click()
		tags = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/div[1]/div/div/div[2]/div[2]/ul/li[2]').click()
		version = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/div[1]/div/div/div[4]/div[1]/a[1]').get_attribute('data-name')	
		ver = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/div[1]/div/div/div[4]/div[1]/a[1]').click()
		clone = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/summary').click()
		gitclone = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/div/div/div[1]/div[1]/div/input').get_attribute('value')
		clone = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/summary').click()
		extras = driver.find_element_by_link_text("extras").click()
		time.sleep(3) 
		docker = driver.find_element_by_link_text("docker").click()
		time.sleep(3)

		buildWilma = driver.find_element_by_xpath('.//*[@id="readme"]/article/pre[1]/code').text
		runWilma = driver.find_element_by_xpath('.//*[@id="readme"]/article/pre[4]/code').text
		driver.quit() 

		print('--------------------------------')
		print ('install version '+ version)
		print('--------------------------------')
		time.sleep(3)
		#os.system('mkdir Docker')
		#os.chdir("Docker")
		os.system('git clone ' + gitclone)
		os.chdir("fiware-pep-proxy")
		dir = os.getcwd()
		runWilma1 = runWilma.replace('/home/root/workspace/fiware-pep-proxy', dir) 
		print('--------------------------------')
		os.system("mv config.js.template config.js")
		os.system(runWilma1)
		os.chdir("extras/docker")
		os.system(buildWilma)
		print('--------------------------------')
		os.system('docker start pep-proxy')
		os.system('docker ps -l')
		print('--------------------------------')
		time.sleep(5)
		os.system('curl http://localhost:80') 
		print(' ')
		print('--------------------------------')


		os.chdir('../')
		os.chdir('../')
		os.chdir('../')
		
		date = time.strftime("%y-%m-%d")
		hour = time.strftime("%H:%M:%S")
		
		host = os.popen('hostname')
		host_name = host.readline()
		
		resultados = os.popen('docker ps -l') 
		datos = resultados.readlines()
		containers = [host_name,date,hour,version,datos[1].split()[12],datos[1].split()[0],datos[1].split()[8]]
		
		os.system('docker rm -f pep-proxy')

		f = open ('report.txt','w')
		f.write(containers[1]+","+containers[2]+","+containers[3]+
			","+containers[4]+","+containers[5]+","+containers[6]+
			","+containers[0])



if __name__=="__main__":
		test_file = 'test.txt'
		f = open(test_file,'w')
		runner = unittest.TextTestRunner(f)
		unittest.main(testRunner=runner)
		f.close()
# Gustavo Bautista Gutierrez
