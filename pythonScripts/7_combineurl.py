#modify timeline_interm.json to include scraped headlines

import json

f = open("timeline_interm.json",'r')
jobj = json.loads(f.read())
f.close()

f = open("urltitle.json",'r')
urltitlelist = json.loads(f.read())
f.close()

urltitledict = {}

total = len(urltitlelist)
print("length of title list: ",total)

for i in range(0,total):
	urltitledict[i+1] = urltitlelist[i]

for i in jobj.keys():
	for j in jobj[i]:
		j['title'] = urltitledict[j['id']]

json.dump(jobj, open('timeline_interm.json','w'),sort_keys=True,indent=4)
print("modified timeline_interm.json")