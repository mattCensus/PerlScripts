#Date Created: 04/12/15
#Usage: Used to scrape a website for links that end in .zip and list them
#Requirements: BeautifulSoup lib
#Notes:

import urllib.request
from urllib.request import Request, urlopen, URLError
#import urllib
import os
from bs4 import BeautifulSoup


#Create a new directory to put the files into
#Get the current working directory and create a new directory in it named test
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
url = "https://www2.census.gov/geo/tiger/TIGER2021/ADDR/"
page = urllib.request.urlopen('https://www2.census.gov/geo/tiger/TIGER2021/ADDR/').read()

#File extension to be looked for.
extension = ".zip"

#Use BeautifulSoup to clean up the page
soup = BeautifulSoup(page,features="html5lib")
soup.prettify()

#Find all the links on the page that end in .zip
for anchor in soup.findAll('a', href=True):
    links = url + anchor['href']
    if links.endswith(extension):
        newfile.write(links + '\n')
newfile.close()

#Read what is saved in zipfiles.txt and output it to the user
#This is done to create presistent data
newfile = open(Zipfiles , 'r')
for line in newfile:
    print ("line in new file is:"+  line + '/n')
newfile.close()

#Read through the lines in the text file and download the zip files.
#Handle exceptions and print exceptions to the console
with open('zipfiles.txt', 'r') as url:
    for line in url:
        if line:
            try:
                #ziplink = line
                #Removes the first 48 characters of the url to get the name of the file
                #zipfile = line[48:]
                #Removes the last 4 characters to remove the .zip
                #zipfile2 = zipfile[:3]
                try:
                    print ("Trying to reach " + line)
                    response = urllib.request.urlopen(line)
                    print ("Attempt successful")
                except:
                    print ("An error occured")
            except URLError as e:
                if hasattr(e, 'reason'):
                    print ('We failed to reach a server.')
                    print ('Reason: ', e.reason)
                    continue
                elif hasattr(e, 'code'):
                    print ('The server couldn\'t fulfill the request.')
                    print ('Error code: ', e.code)
                    continue
            else:
                zipcontent = response.read()
                print('Reading the zipcontent')
                #completeName = os.path.join(newdir, zipfile2+ ".zip")
                #completeName= os.path.join(ziplink)
                #print ("Complete name is :" + completeName)
                line.strip()
                completeName =  line
                print ("Complete name is :" + completeName)
                try:
                    with open (completeName, 'w') as f:
                        print ("downloading.. " + zipfile)
                        f.write(zipcontent)
                        f.close()
                except Exception as e:
                    print(e.args)
                    print(e.with_traceback)
print ("Script completed")