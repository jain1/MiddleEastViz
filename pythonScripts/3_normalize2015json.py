#generating 2015normalized.json which contains 1 Actor name instead of below shown variations

import json


f = open("2015.json",'r')
jobj = json.loads(f.read())
f.close()


syria = ["SYRIA","SYRIAN","DAMASCUS","ALEPPO","BASHAR AL ASSAD","LATAKIA"]
russia = ["RUSSIA","RUSSIAN","MOSCOW","SERGEY LAVROV","VLADIMIR PUTIN","RUSSIAN FEDERATION"]
isis = ["ISLAMIC"]
turkey = ["TURKEY","TURKISH","ISTANBUL","ANKARA"]
usa = ["UNITED STATES","OBAMA","WASHINGTON","BARACK OBAMA","AMERICAN","TEXAS","THE US","NEW YORK","THE WHITE HOUSE"]
iraq = ["IRAQ","IRAQI"]
iran = ["IRAN","IRANIAN","TEHRAN"]
uk = ["UNITED KINGDOM","BRITISH","BRITAIN","LONDON","DAVID CAMERON"]
rebel = ["REBEL","REBEL GROUP","REBEL COMMANDER"]
lebanon = ["LEBANON","BEIRUT","LEBANESE"]
france = ["FRANCE","FRENCH","PARIS"]
jordan = ["JORDAN","JORDANIAN"]
israel = ["ISRAEL","ISRAELI","JERUSALEM"]
saudi = ["SAUDI ARABIA","SAUDI"]
kurd = ["KURD"]
germany = ["GERMAN","GERMANY","BERLIN"]
UNO = ["UNITED NATIONS","SECURITY COUNCIL","THE UN","THE SECURITY COUNCIL","UN ENVOY"]
japan = ["JAPAN","JAPANESE"]
alquaeda = ["AL QAIDA","AL QAEDA"]
palestine = ["PALESTINIAN"]
eu = ["THE EU","THE EUROPEAN UNION"]
uae = ["UNITED ARAB EMIRATES"]
egypt = ["EGYPT"]
china = ["CHINA"]
yemen = ["YEMEN"]
kuwait =["KUWAIT"]
afghanistan = ["AFGHANISTAN"]
pakistan = ["PAKISTAN"]
qatar = ["QATAR"]

newlist = []

for item in jobj:
	if "SYROPP" in item["Actor1Code"]:
		item["Actor1Name"] = "Syrian Oppn"
	elif "SYROPP" in item["Actor2Code"]:
		item["Actor2Name"] = "Syrian Oppn"
	if item["Actor1Name"] in syria:
		item["Actor1Name"] = "SYRIA"
	if item["Actor2Name"] in syria:
		item["Actor2Name"] = "SYRIA"
	if item["Actor2Name"] in russia:
		item["Actor2Name"] = "RUSSIA"
	if item["Actor2Name"] in isis:
		item["Actor2Name"] = "ISIS"
	if item["Actor2Name"] in turkey:
		item["Actor2Name"] = "TURKEY"
	if item["Actor2Name"] in usa:
		item["Actor2Name"] = "USA"
	if item["Actor2Name"] in iraq:
		item["Actor2Name"] = "IRAQ"
	if item["Actor2Name"] in iran:
		item["Actor2Name"] = "IRAN"
	if item["Actor2Name"] in uk:
		item["Actor2Name"] = "UK"
	if item["Actor2Name"] in rebel:
		item["Actor2Name"] = 'Syrian "rebels"'
	if item["Actor2Name"] in lebanon:
		item["Actor2Name"] = "LEBANON"
	if item["Actor2Name"] in france:
		item["Actor2Name"] = "FRANCE"
	if item["Actor2Name"] in jordan:
		item["Actor2Name"] = "JORDAN"
	if item["Actor2Name"] in israel:
		item["Actor2Name"] = "ISRAEL"
	if item["Actor2Name"] in saudi:
		item["Actor2Name"] = "SAUDI ARABIA"
	if item["Actor2Name"] in kurd:
		item["Actor2Name"] = "Iraqi Kurdistan"
	if item["Actor2Name"] in germany:
		item["Actor2Name"] = "GERMANY"
	if item["Actor2Name"] in UNO:
		item["Actor2Name"] = "United Nations"
	if item["Actor2Name"] in alquaeda:
		item["Actor2Name"] = "Al Qaeda"
	if item["Actor2Name"] in japan:
		item["Actor2Name"] = "JAPAN"
	if item["Actor2Name"] in palestine:
		item["Actor2Name"] = "Palestine"
	if item["Actor2Name"] in eu:
		item["Actor2Name"] = "The EU"
	if item["Actor2Name"] in uae:
		item["Actor2Name"] = "UAE"
	if not (item["Actor2Name"] == item["Actor1Name"]): #discard rows which have both actors as Syria
		temp = {}
		temp["Actor1Name"] = item["Actor1Name"]
		temp["Actor2Name"] = item["Actor2Name"]
		temp["SQLDATE"] = item["SQLDATE"]
		temp["QuadClass"] = item["QuadClass"]
		temp["GoldsteinScale"] = item["GoldsteinScale"]
		temp["NumSources"] = item["NumSources"]
		temp["SOURCEURL"] = item["SOURCEURL"]
		newlist.append(temp)

#print(newlist)
#actor2list =[]
#actor1list =[]
#counter = 0
#for i in newlist:
#	if i["Actor1Name"]=="Syrian \"rebels\"":
#		actor2list.append(i["Actor2Name"])
#		print("actor2 ",i["Actor2Name"])
#		counter +=1
#	elif i["Actor2Name"]=="Syrian \"rebels\"":
#		actor1list.append(i["Actor1Name"])
#		print("actor1 ",i["Actor1Name"])
#		counter +=1
#print(counter)
#print(actor1list)
#print("printing actor2")
#print(actor2list)

json.dump(newlist, open('2015normalized.json','w'),indent=4)
print("generated 2015normalized.json")