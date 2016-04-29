#generating timeline.json to use in 2nd visualization. It contains event data grouped by date

import json

f = open("timeline_interm.json",'r')
jobj = json.loads(f.read())
f.close()

def getSyrianNeighbours(daylist):
	#print(daylist)
	syriaimports = []
	for item in daylist:
		#print (item)
		if item["Actor2Name"] == "SYRIA":
			if item["Actor1Name"] not in syriaimports:
				syriaimports.append(item["Actor1Name"])
		if item["Actor1Name"] == "SYRIA":
			if item["Actor2Name"] not in syriaimports:
				syriaimports.append(item["Actor2Name"])
	return syriaimports

def getOppnNeighbours(daylist):
	oppimports = []
	for item in daylist:
		if item["Actor2Name"] == "Syrian Oppn":
			if item["Actor1Name"] not in oppimports:
				oppimports.append(item["Actor1Name"])
		if item["Actor1Name"] == "Syrian Oppn":
			if item["Actor2Name"] not in oppimports:
				oppimports.append(item["Actor2Name"])

	if 'SYRIA' in oppimports:
		oppimports.remove('SYRIA')
	return oppimports

def generateDilist(daylist,syriaimports,oppimports):
	
	dilist = []

	syriadict = {}
	syriadict["name"] = "SYRIA"
	syriadict["imports"] = []
	syriadict["values"] = []
	syriadict["eventCounts"] = []
	syriadict["goldsteinAvg"] = []
	syriadict["urllists"] = []
	syriadict["titlelists"] = []
	
	oppndict = {}
	oppndict["name"] = "Syrian Oppn"
	oppndict["imports"] = []
	oppndict["values"] = []
	oppndict["eventCounts"] = []
	oppndict["goldsteinAvg"] = []
	oppndict["urllists"] = []
	oppndict["titlelists"] = []
	
	countrywisedict = {}
	oppncountrywisedict = {}	
	
	for item in daylist:
		if item["Actor1Name"] == "SYRIA":
			if item["Actor2Name"] not in countrywisedict.keys():
				countrywisedict[item["Actor2Name"]] = {}
				countrywisedict[item["Actor2Name"]]["values"] = 0
				countrywisedict[item["Actor2Name"]]["goldsteinAvg"] = 0
				countrywisedict[item["Actor2Name"]]["eventCounts"] = 0
				countrywisedict[item["Actor2Name"]]["titles"] = []
				countrywisedict[item["Actor2Name"]]["urls"] = []
			countrywisedict[item["Actor2Name"]]["values"] += item["QuadClass"]
			countrywisedict[item["Actor2Name"]]["goldsteinAvg"] += item["GoldsteinScale"]
			countrywisedict[item["Actor2Name"]]["eventCounts"] += 1
			countrywisedict[item["Actor2Name"]]["titles"].append(item["title"])
			countrywisedict[item["Actor2Name"]]["urls"].append(item["SOURCEURL"])
		elif item["Actor2Name"] == "SYRIA":
			if item["Actor1Name"] not in countrywisedict.keys():
				countrywisedict[item["Actor1Name"]] = {}
				countrywisedict[item["Actor1Name"]]["values"] = 0
				countrywisedict[item["Actor1Name"]]["goldsteinAvg"] = 0
				countrywisedict[item["Actor1Name"]]["eventCounts"] = 0
				countrywisedict[item["Actor1Name"]]["titles"] = []
				countrywisedict[item["Actor1Name"]]["urls"] = []
			countrywisedict[item["Actor1Name"]]["values"] += item["QuadClass"]
			countrywisedict[item["Actor1Name"]]["goldsteinAvg"] += item["GoldsteinScale"]
			countrywisedict[item["Actor1Name"]]["eventCounts"] += 1
			countrywisedict[item["Actor1Name"]]["titles"].append(item["title"])
			countrywisedict[item["Actor1Name"]]["urls"].append(item["SOURCEURL"])
		elif item["Actor1Name"] == "Syrian Oppn":
			if item["Actor2Name"] not in oppncountrywisedict.keys():
				oppncountrywisedict[item["Actor2Name"]] = {}
				oppncountrywisedict[item["Actor2Name"]]["values"] = 0
				oppncountrywisedict[item["Actor2Name"]]["goldsteinAvg"] = 0
				oppncountrywisedict[item["Actor2Name"]]["eventCounts"] = 0
				oppncountrywisedict[item["Actor2Name"]]["titles"] = []
				oppncountrywisedict[item["Actor2Name"]]["urls"] = []
			oppncountrywisedict[item["Actor2Name"]]["values"] += item["QuadClass"]
			oppncountrywisedict[item["Actor2Name"]]["goldsteinAvg"] += item["GoldsteinScale"]
			oppncountrywisedict[item["Actor2Name"]]["eventCounts"] += 1
			oppncountrywisedict[item["Actor2Name"]]["titles"].append(item["title"])
			oppncountrywisedict[item["Actor2Name"]]["urls"].append(item["SOURCEURL"])
	for country in syriaimports:
		countrywisedict[country]["values"] = format(countrywisedict[country]["values"]/countrywisedict[country]["eventCounts"],'.4f')
		countrywisedict[country]["goldsteinAvg"] = format(countrywisedict[country]["goldsteinAvg"]/countrywisedict[country]["eventCounts"],'.4f')
		syriadict["imports"].append(country)
		syriadict["values"].append(countrywisedict[country]["values"])
		syriadict["goldsteinAvg"].append(countrywisedict[country]["goldsteinAvg"])
		syriadict["eventCounts"].append(countrywisedict[country]["eventCounts"])
		syriadict["titlelists"].append(countrywisedict[country]["titles"])
		syriadict["urllists"].append(countrywisedict[country]["urls"])
		#print(country," ",sum(countrywisedict[country]["quadlist"])," ",countrywisedict[country]["eventCounts"])
	for country in oppimports:
		oppncountrywisedict[country]["values"] = format(oppncountrywisedict[country]["values"]/oppncountrywisedict[country]["eventCounts"],'.4f')
		oppncountrywisedict[country]["goldsteinAvg"] = format(oppncountrywisedict[country]["goldsteinAvg"]/oppncountrywisedict[country]["eventCounts"],'.4f')
		oppndict["imports"].append(country)
		oppndict["values"].append(oppncountrywisedict[country]["values"])
		oppndict["goldsteinAvg"].append(oppncountrywisedict[country]["goldsteinAvg"])
		oppndict["eventCounts"].append(oppncountrywisedict[country]["eventCounts"])
		oppndict["titlelists"].append(oppncountrywisedict[country]["titles"])
		oppndict["urllists"].append(oppncountrywisedict[country]["urls"])
		#print(country," ",sum(oppncountrywisedict[country]["quadlist"])," ",oppncountrywisedict[country]["eventCounts"])

	dilist.append(syriadict)
	dilist.append(oppndict)
	return dilist


datedict = {}
for date in jobj.keys():
	dilist = []
	syrianNeighbsList = getSyrianNeighbours(jobj[date])
	oppnNeighbsList = getOppnNeighbours(jobj[date])
	dilist = generateDilist(jobj[date],syrianNeighbsList,oppnNeighbsList)
	datedict[date] = dilist

##############

#print(countrywisedict)
json.dump(datedict, open('timeline.json','w'),sort_keys=True,indent=4)
print("generated timeline.json")