from collections import OrderedDict
import numpy as np
import json
import os
import time

print('------------- install Wilma -------------')
os.system('python wilma_test.py')
report = np.genfromtxt('report.txt',delimiter=',',dtype=str)
test = np.genfromtxt('test.txt',delimiter='\t',dtype=str)
os.chdir('../report')

reporte = OrderedDict()
reporte['GE-name'] = "wilma pep proxy"
reporte['Version'] = report[2]
reporte['Host_name'] = report[6]
reporte['Test'] = test[len(test)-1]
reporte['Execution_time'] = test[len(test)-2]
reporte['Date'] = report[0]
reporte['Time'] = report[1]
reporte['Containers'] = OrderedDict()
reporte['Containers']['Container_name'] = report[3]
reporte['Containers']['Container_ID'] = report[4]
reporte['Containers']['Status'] = report[5]

with open('report.json','a') as file:
	json.dump(reporte, file, indent=4)

f = open('report.json','a')
f.write('\n')
f.close() 

print('------------- report json -------------')
print(reporte)
time.sleep(3)
os.system('cd ../Wilma && rm report.txt')
