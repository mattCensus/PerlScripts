# importing necessary modules
import requests, zipfile
from io import BytesIO

#https://www2.census.gov/geo/tiger/TIGER2021/ADDR/tl_2021_01001_addr.zip

print('Downloading started')
county= '01001'
#Defining the zip file URL
#url = 'https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-zip-file.zip'
AddrMain='https://www2.census.gov/geo/tiger/TIGER2021/ADDR/'
fullADDR=AddrMain + 'tl_2021_' + county + '_addr.zip'
print ('fullADDr: ' + fullADDR)
#ADDRpage =requests.get(fullADDR)

ADDRFEATRpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/ADDRFEAT')
ADDRFNpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/ADDRFN')
AREAWATERpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER')
EDGESpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/EDGES')
FACESpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/FACES')
FACESAHpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/FACESAH')
FEATNAMESpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/FEATNAMES')
LINEARWATERpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/LINEARWATER')
ROADSpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/ROADS')


# Split URL to get the file name
filename = fullADDR.split('/')[-1]
print ('filename: ' + filename)

# Downloading the file by sending the request to the URL
req = requests.get(fullADDR)
print('Downloading Completed')

# extracting the zip file contents
zipfile= zipfile.ZipFile(BytesIO(req.content))
zipfile.extractall('C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip')