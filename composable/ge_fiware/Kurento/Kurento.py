import numpy as np
import json
import os
import time

#os.system('touch report.txt && touch test.txt')
os.system('clear')
print('------------- install Kurento -------------')
os.system('python kurento_test.py')
report = np.genfromtxt('report.txt',delimiter=',',dtype=str)
test = np.genfromtxt('test.txt',delimiter='\t',dtype=str)
os.chdir('../')
os.chdir('report')

reporte = {
			'host_name' : report[3],
			'execution_time' : test[2],
			'test' : test[3], 
			'date' : report[0],
			'hour' : report[1],
			'version' : report[2],
			}
with open('report.json','a') as file:
			json.dump(reporte, file, indent=2)

f = open('report.json','a')
f.write('\n')
f.close()

print('------------- report json -------------')
print(reporte)
#reporte = open('report.json','r')
#rep = reporte.read()
#print (rep)
time.sleep(2)

#os.chdir('../')
#os.system('cd .. && cd Kurento && rm test.txt && rm report.txt') 
