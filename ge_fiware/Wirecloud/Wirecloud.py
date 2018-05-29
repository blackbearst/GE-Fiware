from collections import OrderedDict
import numpy as np
import json
import os
import time

print('------------- install Wirecloud -------------')
os.system('python wirecloud_test.py')
report = np.genfromtxt('report.txt',delimiter=',',dtype=str)
test = np.genfromtxt('test.txt',delimiter='\t',dtype=str)
os.chdir('../report')
#os.chdir('report')


reporte = OrderedDict()
reporte['GE-name'] = "wirecloud"
reporte['Version'] = "latest"
reporte['Host_name'] = report[15]
reporte['Test'] = test[len(test)-1]
reporte['Execution_time'] = test[len(test)-2]
reporte['Date'] = report[0]
reporte['Time'] = report[1]
reporte['Containers'] = OrderedDict()
reporte['Containers']['Container_name 1'] = report[3]
reporte['Containers']['Container_ID 1'] = report[4]
reporte['Containers']['Status 1'] = report[5]
reporte['Containers']['Container_name 2'] = report[6]
reporte['Containers']['Container_ID 2'] = report[7]
reporte['Containers']['Status 2'] = report[8]
reporte['Containers']['Container_name 3'] = report[9]
reporte['Containers']['Container_ID 3'] = report[10]
reporte['Containers']['Status 3'] = report[11]
reporte['Containers']['Container_name 4'] = report[12]
reporte['Containers']['Container_ID 4'] = report[13]
reporte['Containers']['Status 4'] = report[14]

with open('report.json','a') as file:
	json.dump(reporte, file, indent=4)

f = open('report.json','a')
f.write('\n')
f.close() 

print('------------- report json -------------')
print(reporte)
time.sleep(3)
os.system('cd ../Wirecloud && rm report.txt')
