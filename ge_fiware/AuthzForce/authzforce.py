import json
from  collections import OrderedDict
import os
import numpy as np
import test

print('------------- install AuthzForce -------------')
os.system("python test-GE.py")

report = np.genfromtxt('report.txt',delimiter=',',dtype=str)
test = np.genfromtxt('log_file.txt',delimiter='\t',dtype=str)

reporte = OrderedDict()
reporte['GE-name'] = "authzforce"
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

with open('../report/report.json','a') as file:
			file.write(json.dumps(reporte, indent=2))

f = open('../report/report.json','a')
f.write('\n')
f.close()
