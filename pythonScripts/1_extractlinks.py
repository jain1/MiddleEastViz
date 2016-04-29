#generating ".tsv" files from GDELT ".csv" files

import requests, os
import lxml.html as lh
import os.path
import urllib
import zipfile
import glob
import operator


gdelt_base_url = 'http://data.gdeltproject.org/events/'
local_path = os.getcwd()+os.path.sep

country_code = 'SYR'

# get the list of all the links on the gdelt file page
page = requests.get(gdelt_base_url+'index.html')
doc = lh.fromstring(page.content)
link_list = doc.xpath("//*/ul/li/a/@href")

# separate out those links that begin with 2015
file_list = [x for x in link_list if x[0:4]=='2015']
#print(file_list)

infilecounter = 0

for compressed_file in file_list:
    print (compressed_file)
    
    # if we dont have the compressed file stored locally, go get it. Keep trying if necessary.
    while not os.path.isfile(local_path+compressed_file): 
        print ('downloading,',end =" ")
        urllib.request.urlretrieve(url=gdelt_base_url+compressed_file, 
                           filename=local_path+compressed_file)
        
    # extract the contents of the compressed file to a temporary directory    
    print ('extracting,',end =" ")
    z = zipfile.ZipFile(file=local_path+compressed_file, mode='r')    
    z.extractall(path=local_path+'tmp/')
    
    # parse each of the csv files in the working directory, 
    print ('parsing,',end =" ")
    for infile_name in glob.glob(local_path+'tmp/*'):
        outfile_name = local_path+os.path.basename(infile_name)[0:8]+'.tsv'
        
        # open the infile and outfile
        with open(infile_name, mode='r') as infile, open(outfile_name, mode='w') as outfile:
            for line in infile:
                # extract lines with our interest country code
                if country_code in operator.itemgetter(7, 17)(line.split('\t')):    
                    outfile.write(line)
                        
        # delete the temporary file
        os.remove(infile_name)
        # delete zip file
        os.remove(compressed_file)
    infilecounter +=1
    print ('done')
print("parsed",infilecounter," files")