import json
import os

test_Path = {}

for root,dirs,files in os.walk('./IMG'):
	rootlist = []
	for fname in files:
		full_fname = os.path.join(root,fname)
		rootlist += [full_fname]
	if 'U' in root:
		test_Path[root[6:]] = rootlist


json.dump(test_Path,open('test_Path.json','w',encoding = 'utf-8'),ensure_ascii=False,indent = '\t')

