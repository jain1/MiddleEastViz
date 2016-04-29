#generating 2015.json which contains all required events with required attributes for 2015

import csv,json,os,glob
from collections import defaultdict


local_path = os.getcwd()+'/'
allrows = []
#actorcounts = defaultdict(int)
#actorlist = []

#all possible actor names used in the data
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
egypt = ["EGYPT"]
china = ["CHINA"]
yemen = ["YEMEN"]
kuwait =["KUWAIT"]
afghanistan = ["AFGHANISTAN"]
pakistan = ["PAKISTAN"]
qatar = ["QATAR"]
uae = ["UNITED ARAB EMIRATES"]
eu = ["THE EU","THE EUROPEAN UNION"]

megalist = (syria+russia+isis+turkey+usa+iraq+iran+uk+rebel+lebanon+france+jordan
			+israel+saudi+kurd+germany+UNO+japan+alquaeda+palestine+egypt+china+yemen+kuwait+afghanistan
			+pakistan+qatar+eu+uae)

#functions to set QuadClass values to -2,-1,1,2
def p2():
	return 2
def p1():
	return 1
def m1():
	return -1
def m2():
	return -2
def num_to_fns_to_str(argument):
    switcher = {
        "1": p1,
        "2": p2,
        "3": m1,
        "4": m2
    }
    # Get the function from switcher dictionary
    func = switcher.get(argument, lambda: 0)
    # Execute the function
    return func()

#parse through each tsv file to extract required records and columns    
for tsvfilepath in glob.glob(local_path+"2015*.tsv"):
	keyname = os.path.basename(tsvfilepath)[0:8]
	with open(tsvfilepath,'r') as tsvfile:
		reader = csv.reader(tsvfile,delimiter='\t')
		for row in reader:
			# row[16], row[6] = Actor 1&2 Names, row[25] = isRootEvent, row[32] = NumSources, row[30] = GoldsteinScale  
			if (row[16] in megalist) and (row[6] in megalist) and row[25]=='1' and int(row[32])>40 and row[30]!="0.0" and row[6]!="" and row[16]!="":
				temp = {}
				#swap actor names such that Actor 1 is always related to Syria
				if row[17]=="SYR":
					temp["Actor1Code"] = row[15]
					temp["Actor1Name"] = row[16]
					temp["Actor1CountryCode"] = row[17]
					temp["Actor1Type1Code"] = row[22]
					temp["Actor2Code"] = row[5]
					temp["Actor2Name"] = row[6]
					temp["Actor2CountryCode"] = row[7]
					temp["Actor2Type1Code"] = row[12]
				else:
					temp["Actor1Code"] = row[5]
					temp["Actor1Name"] = row[6]
					temp["Actor1CountryCode"] = row[7]
					temp["Actor1Type1Code"] = row[12]
					temp["Actor2Code"] = row[15]
					temp["Actor2Name"] = row[16]
					temp["Actor2CountryCode"] = row[17]
					temp["Actor2Type1Code"] = row[22]
				# actorcounts[temp["Actor1Name"]] += 1
				# actorcounts[temp["Actor2Name"]] += 1
				# if temp["Actor1Name"] not in actorlist:
				# 	actorlist.append(temp["Actor1Name"])
				# if temp["Actor2Name"] not in actorlist:
				# 	actorlist.append(temp["Actor2Name"])
				temp["SQLDATE"] = keyname
				temp["QuadClass"] = num_to_fns_to_str(row[29])
				temp["GoldsteinScale"] = float(row[30])
				temp["NumSources"] = row[32]
				temp["SOURCEURL"] = row[57]
				allrows.append(temp)

#sortedActorCount = sorted(actorcounts.items(),key=lambda tup: tup[1],reverse=True)[:]
#json.dump(sortedActorCount, open('actorCounts.json','w'),indent=4)
#json.dump(actorlist, open('actors.json','w'),indent=4)

newlist = sorted(allrows, key=lambda k: k['SQLDATE'])

json.dump(newlist, open('2015.json','w'),indent=4)
print("generated 2015.json")