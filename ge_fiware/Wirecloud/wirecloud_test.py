from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest
import os
import time
import json

class wirecloud(unittest.TestCase):
	"""docstring for ClassName"""
	def setUp(self):
		self.driver = webdriver.Remote(
					command_executor='http://localhost:4444/wd/hub',
				    desired_capabilities=DesiredCapabilities.CHROME)
	def test(self):	
		driver=self.driver
		driver.get('https://github.com/Wirecloud/docker-wirecloud')
		clone = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/summary').click()
		gitclone = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/div/div/div[1]/div[1]/div/input').get_attribute('value')
		clone = driver.find_element_by_xpath('.//*[@id="js-repo-pjax-container"]/div[2]/div[1]/div[5]/details/summary').click()
		hub = driver.find_element_by_link_text("dev-composable").click()
		time.sleep(3)

		compose = driver.find_element_by_link_text("docker-compose.yml").click()
		time.sleep(3)

		version = driver.find_element_by_xpath('.//*[@id="LC1"]').text
		driver.quit()

		print('--------------------------------')
		print ('instalando ' + version)
		print('--------------------------------')
		
		os.system('git clone ' + gitclone)
		os.chdir('docker-wirecloud/dev-composable')
		os.system('docker-compose up -d')
		time.sleep(3)
		os.system('docker-compose exec wirecloud manage.py migrate')
		print('--------------------------------------------------------')
		#print('Ingrese username: admin | mail: admin@gamail.com | password: admin')
		#print('--------------------------------------------------------')
		#os.system('docker-compose exec wirecloud manage.py createsuperuser')
		os.system('docker-compose ps')
		time.sleep(5)

		wirecloud = self.driver 
		time.sleep(5)
		#sign_in = wirecloud.find_element_by_link_text("Sign in").click()
		#time.sleep(5)
		#user = wirecloud.find_element_by_xpath('.//*[@id="wc-login-form"]/div/div/input[3]').send_keys('admin')
		#password = wirecloud.find_element_by_xpath('.//*[@id="wc-login-form"]/div/div/div/div[1]/input').send_keys('admin')
		#log_in = wirecloud.find_element_by_xpath('.//*[@id="wc-login-form"]/div/div/div/div[2]/input').click()
		#time.sleep(3)
		#user_name = wirecloud.find_element_by_xpath('.//*[@id="wc-user-menu"]').text
		#time.sleep(3)
		#wirecloud.quit()

		#print('--------------------------------')
		#print ('Ingreso con el usuario: ' + user_name)
		print('--------------------------------')
		

		date = time.strftime("%y-%m-%d")
		hour = time.strftime("%H:%M:%S")
		
		host = os.popen('hostname')
		host_name = host.readline()
		
		resultados = os.popen('docker ps')
		datos = resultados.readlines()
		resultados = os.popen('docker-compose ps')
		datos1 =resultados.readlines()

		containers = [host_name,date,hour,version,datos1[2].split()[0],datos[1].split()[0],datos1[2].split()[4],datos1[3].split()[0],datos[2].split()[0],datos1[3].split()[5],datos1[4].split()[0],datos[3].split()[0],datos1[4].split()[3],datos1[5].split()[0],datos[4].split()[0],datos1[5].split()[2]]
		
		os.system('docker-compose down')

		os.chdir('../')
		os.chdir('../')
		f = open ('report.txt','w')
		f.write(containers[1]+","+containers[2]+","+containers[3]+
			","+containers[4]+","+containers[5]+","+containers[6]+
			","+containers[7]+","+containers[8]+","+containers[9]+
			","+containers[10]+","+containers[11]+","+containers[12]+
			","+containers[13]+","+containers[14]+","+containers[15]+
			","+containers[0])


if __name__=="__main__":
		test_file = 'test.txt'
		f = open(test_file,'w')
		runner = unittest.TextTestRunner(f)
		unittest.main(testRunner=runner)
		f.close()
# Gustavo Bautista Gutierrez 
