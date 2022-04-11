# importing the necessary modules
import requests
from bs4 import BeautifulSoup

# Creating a new file to store the zip file links
newfile = open('zipfiles.txt','w')

#Set variable for page to be opened and url to be concatenated
page =requests.get('https://www2.census.gov/geo/tiger/TIGER2021/ADDR/')
baseurl= 'https://www2.census.gov/'

newdir = "C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/"
#Use BeautifulSoup to clean up the page
soup = BeautifulSoup(page.content)
soup.prettify()

#Find all the links on the page that end in .zip and write them into the text file
for anchor in soup.findAll('a', href=True):
    links = anchor['href']
    if links.endswith('.zip'):
        newfile.write(links + '\n')
newfile.close()

#Fetching the links for the zip file and downloading the files
with open('zipfiles.txt', 'r') as links:
    for link in links:
        if link:
            filename1= link.split('/')[-1]
            filename= newdir+ "/"+ filename1[:-1]
            link = baseurl + link
            print(filename + ' file started to download')
            response = requests.get(link[:-1])

            # Writing the zip file into local file system
            with open(filename,'wb') as output_file:
                output_file.write(response.content)
            print(filename + 'file is downloaded')