#generating alldays.json which contains overall data for year 2015. 
#this json is used by the first visualization

import json
from collections import defaultdict

f = open("2015normalized.json",'r')
jobj = json.loads(f.read())
f.close()

finallist = []
syriadict = {}
oppndict = {}
#syrianeighbs = ['RUSSIA','ISIS','TURKEY','USA','IRAQ','IRAN','UK','Syrian "rebels"','Syrian Oppn','LEBANON','FRANCE','JORDAN','ISRAEL','SAUDI ARABIA','Iraqi Kurdistan','GERMANY',"United Nations",'JAPAN',"Al Qaeda",'Palestine','EGYPT','CHINA','YEMEN','KUWAIT','AFGHANISTAN','PAKISTAN','The EU','UAE']
#QATAR removed upon raising numsources to 40
syrianeighbs = []
oppneighbs = []

#get neighbours for node "SYRIA" and "Syrian Oppn"
for item in jobj:
	if item["Actor2Name"] == "SYRIA":
		if item["Actor1Name"] not in syrianeighbs:
			syrianeighbs.append(item["Actor1Name"])
	if item["Actor1Name"] == "SYRIA":
		if item["Actor2Name"] not in syrianeighbs:
			syrianeighbs.append(item["Actor2Name"])
	if item["Actor2Name"] == "Syrian Oppn":
		if item["Actor1Name"] not in oppneighbs:
			oppneighbs.append(item["Actor1Name"])
	if item["Actor1Name"] == "Syrian Oppn":
		if item["Actor2Name"] not in oppneighbs:
			oppneighbs.append(item["Actor2Name"])

#remove SYRIA from oppn neighbour list to remove redundancy
if 'SYRIA' in oppneighbs:
	oppneighbs.remove('SYRIA')
#print(oppneighbs)

countrywisedict = {}
oppncountrywisedict = {}

syriadict["name"] = "SYRIA"
syriadict["imports"] = []
syriadict["values"] = []
syriadict["eventCounts"] = []
syriadict["goldsteinAvg"] = []

oppndict["name"] = "Syrian Oppn"
oppndict["imports"] = []
oppndict["values"] = []
oppndict["eventCounts"] = []
oppndict["goldsteinAvg"] = []

for item in jobj:
	if item["Actor1Name"] == "SYRIA":
		if item["Actor2Name"] not in countrywisedict.keys():
			countrywisedict[item["Actor2Name"]] = {}
			countrywisedict[item["Actor2Name"]]["values"] = 0
			countrywisedict[item["Actor2Name"]]["goldsteinAvg"] = 0
			countrywisedict[item["Actor2Name"]]["eventCounts"] = 0
		countrywisedict[item["Actor2Name"]]["values"] += item["QuadClass"]
		countrywisedict[item["Actor2Name"]]["goldsteinAvg"] += item["GoldsteinScale"]
		countrywisedict[item["Actor2Name"]]["eventCounts"] += 1
	elif item["Actor2Name"] == "SYRIA":
		if item["Actor1Name"] not in countrywisedict.keys():
			countrywisedict[item["Actor1Name"]] = {}
			countrywisedict[item["Actor1Name"]]["values"] = 0
			countrywisedict[item["Actor1Name"]]["goldsteinAvg"] = 0
			countrywisedict[item["Actor1Name"]]["eventCounts"] = 0
		countrywisedict[item["Actor1Name"]]["values"] += item["QuadClass"]
		countrywisedict[item["Actor1Name"]]["goldsteinAvg"] += item["GoldsteinScale"]
		countrywisedict[item["Actor1Name"]]["eventCounts"] += 1
	elif item["Actor1Name"] == "Syrian Oppn":
		if item["Actor2Name"] not in oppncountrywisedict.keys():
			oppncountrywisedict[item["Actor2Name"]] = {}
			oppncountrywisedict[item["Actor2Name"]]["values"] = 0
			oppncountrywisedict[item["Actor2Name"]]["goldsteinAvg"] = 0
			oppncountrywisedict[item["Actor2Name"]]["eventCounts"] = 0
		oppncountrywisedict[item["Actor2Name"]]["values"] += item["QuadClass"]
		countrywisedict[item["Actor2Name"]]["goldsteinAvg"] += item["GoldsteinScale"]
		oppncountrywisedict[item["Actor2Name"]]["eventCounts"] += 1

#print(countrywisedict)
for country in syrianeighbs:
	countrywisedict[country]["values"] = format(countrywisedict[country]["values"]/countrywisedict[country]["eventCounts"],'.4f')
	countrywisedict[country]["goldsteinAvg"] = format(countrywisedict[country]["goldsteinAvg"]/countrywisedict[country]["eventCounts"],'.4f')
	syriadict["imports"].append(country)
	syriadict["values"].append(countrywisedict[country]["values"])
	syriadict["goldsteinAvg"].append(countrywisedict[country]["goldsteinAvg"])
	syriadict["eventCounts"].append(countrywisedict[country]["eventCounts"])
for country in oppneighbs:
	oppncountrywisedict[country]["values"] = format(oppncountrywisedict[country]["values"]/oppncountrywisedict[country]["eventCounts"],'.4f')
	oppncountrywisedict[country]["goldsteinAvg"] = format(oppncountrywisedict[country]["goldsteinAvg"]/oppncountrywisedict[country]["eventCounts"],'.4f')
	oppndict["imports"].append(country)
	oppndict["values"].append(oppncountrywisedict[country]["values"])
	oppndict["goldsteinAvg"].append(oppncountrywisedict[country]["goldsteinAvg"])
	oppndict["eventCounts"].append(oppncountrywisedict[country]["eventCounts"])

finallist.append(syriadict)
finallist.append(oppndict)

json.dump(finallist, open('alldays.json','w'),indent=4)
print("generated alldays.json")