import json
import os
import numpy as np
import test

print('------------- install AuthzForce -------------')
os.system("python test-GE.py")

report = np.genfromtxt('report.txt',delimiter=',',dtype=str)
test = np.genfromtxt('log_file.txt',delimiter='\t',dtype=str)

reporte = {
			'GE-name' : "authzforce",
			'host_name' : report[6],
			'execution_time' : test[len(test)-2],
			'test' : test[len(test)-1], 
			'date' : report[0],
			'time' : report[1],
			'version' : report[2],
			'containers' : [{
				'container_name' : report[3],
				'container_ID' : report[4],
				'status' : report[5]
				}]
			}
with open('../report/report.json','a') as file:
			json.dump(reporte, file, indent=2)

f = open('../report/report.json','a')
f.write('\n')
f.close()
