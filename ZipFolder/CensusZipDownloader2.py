import urllib.request
from urllib.request import Request, urlopen, URLError
import requests
#import urllib
import os
from bs4 import BeautifulSoup
import time
import shutil
# importing required modules
from zipfile import ZipFile

#url = 'https://www2.census.gov/geo/tiger/TIGER2021/ADDR/tl_2021_01001_addr.zip'

# download the file contents in binary format

cwd = os.getcwd()
newdir = "C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip"
print ("The current Working directory is " + cwd)

if os.path.exists(newdir):
    print("Directory already exists")
else:
    os.mkdir( newdir);
    print ("Created new directory " + newdir)

Zipfiles = newdir + 'zipfiles.txt'
newfile = open(Zipfiles,'w')
print ("Newfile is:   "+ str(newfile))


print ("Running script.. ")
#Set variable for page to be open and url to be concatenated
urlDownloadpage = "https://www2.census.gov/geo/tiger/TIGER2021/ADDRFEAT/"
page = urllib.request.urlopen('https://www2.census.gov/geo/tiger/TIGER2021/ADDRFEAT/').read()
baseDirectory="C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip"

try:
    os._exists(baseDirectory)
    print (baseDirectory + " esists!")
    os.chdir(baseDirectory)
except:
    print ('Could not find the directory')

#cwd = os.getcwd()
#print ("The current Working directory is " + cwd)

#File extension to be looked for.
extension = ".zip"

#Use BeautifulSoup to clean up the page
soup = BeautifulSoup(page,features="html5lib")
soup.prettify()

#Find all the links on the page that end in .zip
for anchor in soup.findAll('a', href=True):
    links = urlDownloadpage + anchor['href']
    if links.endswith(extension):
        newfile.write(links + '\n')
newfile.close()

newfile = open(Zipfiles , 'r')
for url in newfile:
    print ('Url is: '+ url)
    req = requests.get(url)
    actualZip=url.split('/')[-1]
    print ('actualZip is: ' + actualZip)
    fullZip= 'C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip/'  + actualZip
    newlineloc=fullZip.find('\\')
    fullZipB=fullZip[0:newlineloc]
    print ('fullSip is: '+ fullZipB)

    with open(fullZipB, "wb") as zip:
        # extracting all the files
        print('Extracting all the files now...')
        zip.write(req.content)





#with open("C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip/tl_2021_01001_addr.zip", "wb") as zip:
#    zip.write(r.content)

'''
  with open(fullZipB, "wb") as zip:
        # extracting all the files
        print('Extracting all the files now...')
        #zip.write(req.content)
        
  with ZipFile(fullZipB, 'r') as zip:
        # printing all the contents of the zip file
        zip.printdir()

        # extracting all the files
        print('Extracting all the files now...')
        zip.extractall()
        print('Done!')
        
'''

print ("Done")