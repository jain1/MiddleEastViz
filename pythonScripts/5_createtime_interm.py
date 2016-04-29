#generating intermediate file for timeline data -  contains events ordered by dates as keys

import json
from collections import defaultdict


f = open("2015normalized.json",'r')
jobj = json.loads(f.read())
f.close()

finaldict = {}
urllist = []
idgen = 0

for item in jobj:
	key = item["SQLDATE"]
	if item["SQLDATE"] not in finaldict.keys():
		finaldict[item["SQLDATE"]] = []
	item.pop('SQLDATE',0)
	idgen+=1
	item['id']=idgen
	urllist.append(item['SOURCEURL'])
	finaldict[key].append(item)

json.dump(finaldict, open('timeline_interm.json','w'),sort_keys=True,indent=4)
json.dump(urllist, open('urllist.json','w'),indent=4)
print("generated timeline_interm.json and urllist.json")