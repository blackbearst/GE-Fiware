import numpy as np
import json
import os
import time

print('------------- install Kurento -------------')
os.system('python kurento_test.py')
report = np.genfromtxt('report.txt',delimiter=',',dtype=str)
test = np.genfromtxt('test.txt',delimiter='\t',dtype=str)
os.chdir('../')
os.chdir('report')

reporte = {
			'GE-name' : "kurento",
			'host_name' : report[6],
			'execution_time' : test[2],
			'test' : test[3], 
			'date' : report[0],
			'time' : report[1],
			'version' : report[2],
			'containers' : [{
				'container_name' : report[3],
				'container_ID' : report[4],
				'status' : report[5]
				}]
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
os.system('cd .. && cd Kurento && rm test.txt && rm report.txt') 
