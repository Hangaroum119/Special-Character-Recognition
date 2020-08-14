import time
from sklearn.neural_network import MLPClassifier

import numpy as np
import json
import pickle
import datetime

Path_data = json.loads(open('test_Path.json','r').read())
Addr_data = json.loads(open('uni_path.json','r').read())

start = time.time()
list_IMG = []
list_key = []
for icon in Path_data.keys():
	for path in Path_data[icon]:
		file_data = open(path,'r')

		list_data = []
		data = []
		
		lines = file_data.readlines()
		file_data.close()
	
		for i in range(len(lines)):
			data = lines[i].strip().split(" ")
			data = list(map(float,data))
			list_data += data
		#print(list_data)
		#print(' ')
		#print(' ')
		list_IMG += [list_data]
		list_key += [int(Addr_data[icon])]

list_IMG = np.array(list_IMG)
list_key = np.array(list_key)

clf_mlp = MLPClassifier(activation = 'relu',
			alpha = 0.001,hidden_layer_sizes=(70,70),
			max_iter = 1000)
print('Start fit')
print('Start time : ',end='')
print(datetime.datetime.now())

clf_mlp.fit(list_IMG,list_key)

print('End time : ',end='')
print(datetime.datetime.now())

pickle.dump(clf_mlp, open('IMG_MLP.pkl','wb'))
print('Modeling Success')

