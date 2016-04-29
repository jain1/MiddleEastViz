#generate urltitle.json which contains all title tags related the url per event to generate headlines
#deadlinks and other errors give empty string as title

import json,lxml,urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup

f = open("urllist.json",'r')
start_urls = json.loads(f.read())
f.close()

urltitlelist = []
counter = 0

#with open("urltitle.json",'a') as outfile:
for i in start_urls:
    title = ''
    try:
        soup = BeautifulSoup(urlopen(i))
        if (soup.title is not None) and (soup.title.string is not None):
            title = soup.title.string
            print(counter,": ", title.strip())
            urltitlelist.append(title.strip())
            line = '"'+title+'",'
            #outfile.write(line)
            counter +=1
        else:
            print(counter, ": title is null")
            urltitlelist.append('')
            line = '"",'
            #outfile.write(line)
            counter +=1
    except:
        print(counter, ": error")
        urltitlelist.append(title)
        line = '"",'
        #outfile.write(line)
        counter +=1

json.dump(urltitlelist, open('urltitle.json','w'),indent=4)
print("generated urltitle.json")