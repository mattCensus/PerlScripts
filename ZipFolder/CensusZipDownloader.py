import urllib.request
from urllib.request import Request, urlopen, URLError
import requests
#import urllib
import os
from bs4 import BeautifulSoup
import time
import shutil

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
urlDownloadpage = "https://www2.census.gov/geo/tiger/TIGER2021/ADDR/"
page = urllib.request.urlopen('https://www2.census.gov/geo/tiger/TIGER2021/ADDR/').read()
baseDirectory="C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip"

try:
    os._exists(baseDirectory)
    print (baseDirectory + " esists!")
    os.chdir(baseDirectory)
except:
    print ('Could not find the directory')

cwd = os.getcwd()
print ("The current Working directory is " + cwd)

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

#Read what is saved in zipfiles.txt and output it to the user
#This is done to create presistent data
newfile = open(Zipfiles , 'r')
for line in newfile:
    print ("line in new file is:"+  line + '/n')
    r = requests.get(line)
    #lastSlashPos=line.rfind("/")
    #zipFile=line[lastSlashPos:]
    #fullDirectory=baseDirectory + "/" + zipFile
    #fullDirectory.strip('\n')
    # Split URL to get the file name
    filename = line.split('/')[-1]
    #fullDirectory=os.path.join(r'C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip',filename)
    FullDirectory= 'C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip' + "/" + filename
    time.sleep(15)
    #print ("the destination directory is " + fullDirectory)
    time.sleep(15)
    with open("C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip/samplezip.zip", "wb") as zip:
        print ("In the open")
        zip.write(r.content)
        time.sleep(15)
    shutil.copyfile('C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip/samplezip.zip',  FullDirectory)
    # Writing the file to the local file system
    #with open(filename, 'wb') as output_file:
     #   output_file.write(req.content)
    #print('Downloading Completed')
    #with open(fullDirectory, "wb") as zip:
     #   zip.write(r.content)


newfile.close()