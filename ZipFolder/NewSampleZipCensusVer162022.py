# importing necessary modules
import requests, zipfile
from io import BytesIO
print('Downloading started')
import time
import sys

def url_checker(url):
	try:
		#Get Url
		get = requests.get(url)
		# if the request succeeds
		if get.status_code == 200:
			return("Yes")
		else:
			return('No')

	#Exception
	except requests.exceptions.RequestException as e:
        # print URL with Errs
		raise SystemExit(f"{url}: is Not reachable \nErr: {e}")

def UrlZip(url):
    import requests, zipfile
    # Split URL to get the file name
    filename = url.split('/')[-1]

    # Downloading the file by sending the request to the URL
    req = requests.get(url)
    print('Downloading ' + url+  ' Completed')

    # extracting the zip file contents
    zipfile = zipfile.ZipFile(BytesIO(req.content))
    zipfile.extractall('C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip')

#https://www2.census.gov/geo/tiger/TIGER2021/EDGES/tl_2021_55141_edges.zip

print('Downloading started')
county= '72054'
#Defining the zip file URL
#url = 'https://www2.census.gov/geo/tiger/TIGER2021/EDGES/tl_2021_49057_edges.zip'

#address Range URL
AddrMain='https://www2.census.gov/geo/tiger/TIGER2021/ADDR/'
fullADDR=AddrMain + 'tl_2021_' + county + '_addr.zip'
print ('fullADDr: ' + fullADDR)
#ADDRpage =requests.get(fullADDR)

#Address Feat
ADDRFEATMain='https://www2.census.gov/geo/tiger/TIGER2021/ADDRFEAT/'
fullADDRFEAT=ADDRFEATMain + 'tl_2021_' + county + '_addrfeat.zip'
#ADDRFEATRpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/ADDRFEAT')
#https://www2.census.gov/geo/tiger/TIGER2021/ADDRFEAT/tl_2021_01001_addrfeat.zip

#addrFN
#ADDRFNpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/ADDRFN')
#https://www2.census.gov/geo/tiger/TIGER2021/ADDRFN/tl_2021_01001_addrfn.zip
ADDRFNMain='https://www2.census.gov/geo/tiger/TIGER2021/ADDRFN/'
fullADDRFNMain=ADDRFNMain + 'tl_2021_' + county + '_addrfn.zip'

#areawater
#AREAWATERpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER')
#https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/tl_2021_01001_areawater.zip
AREAWATERMain='https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/'
fullAREAWATERMain= AREAWATERMain + 'tl_2021_' + county + '_areawater.zip'

#edges
#EDGESpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/EDGES')
#https://www2.census.gov/geo/tiger/TIGER2021/EDGES/tl_2021_01001_edges.zip
EDGESMain='https://www2.census.gov/geo/tiger/TIGER2021/EDGES/'
fullEdgesMain= EDGESMain + 'tl_2021_' + county + '_edges.zip'

#faces
#FACESpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/FACES')
#https://www2.census.gov/geo/tiger/TIGER2021/FACES/tl_2021_01001_faces.zip
FACESMain='https://www2.census.gov/geo/tiger/TIGER2021/FACES/'
fullFACESMain= FACESMain + 'tl_2021_' + county + '_faces.zip'

#FACESAH
#FACESAHpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/FACESAH')
#https://www2.census.gov/geo/tiger/TIGER2021/FACESAH/tl_2021_01001_facesah.zip
FACESAHMain='https://www2.census.gov/geo/tiger/TIGER2021/FACESAH/'
fullFACESAHMain= FACESAHMain + 'tl_2021_' + county + '_facesah.zip'

#FEATNames
#FEATNAMESpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/FEATNAMES')
#https://www2.census.gov/geo/tiger/TIGER2021/FEATNAMES/tl_2021_01001_featnames.zip
FEATNAMESMain='https://www2.census.gov/geo/tiger/TIGER2021/FEATNAMES/'
fullFEATNAMESMain= FEATNAMESMain + 'tl_2021_' + county + '_featnames.zip'

#LInEARWater
#LINEARWATERpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/LINEARWATER')
#https://www2.census.gov/geo/tiger/TIGER2021/LINEARWATER/tl_2021_01001_linearwater.zip
LINEARWATERMain='https://www2.census.gov/geo/tiger/TIGER2021/LINEARWATER/'
FullLINEARWATERMain= LINEARWATERMain + 'tl_2021_' + county + '_linearwater.zip'

#ROADS
#ROADSpage=requests.get('https://www2.census.gov/geo/tiger/TIGER2021/AREAWATER/ROADS')
#https://www2.census.gov/geo/tiger/TIGER2021/ROADS/tl_2021_01001_roads.zip
ROADSMain ='https://www2.census.gov/geo/tiger/TIGER2021/ROADS/'
FullROADSMain= ROADSMain  + 'tl_2021_' + county + '_roads.zip'

#address Range
# Split URL to get the file name

if url_checker(fullADDR) =="Yes":
    UrlZip(fullADDR)
else:
    print ("Unable to download " + fullADDR)


#address Features
if url_checker(fullADDRFEAT) == "Yes":
    UrlZip(fullADDRFEAT)
else:
    print ("Unable to download " + fullADDRFEAT)

if url_checker(fullADDRFNMain) == "Yes":
    UrlZip(fullADDRFNMain)
else:
    print("Unable to download " + fullADDRFNMain)

if url_checker(fullAREAWATERMain)  == "Yes":
    UrlZip(fullAREAWATERMain)
else:
    print("Unable to download " + fullAREAWATERMain)

if url_checker(fullEdgesMain)  == "Yes":
    UrlZip(fullEdgesMain)
else:
    print("Unable to download " + fullEdgesMain)

if url_checker(fullFACESMain) == "Yes":
    UrlZip(fullFACESMain)
else:
    print("Unable to download " + fullFACESMain)

if url_checker(fullFACESAHMain) == "Yes":
    UrlZip(fullFACESAHMain)
else:
    print("Unable to download " + fullFACESAHMain)

if url_checker(fullFEATNAMESMain)  == "Yes":
    UrlZip(fullFEATNAMESMain)
else:
    print("Unable to download " + fullFEATNAMESMain)
    
if url_checker(FullLINEARWATERMain)  == "Yes":
    UrlZip(FullLINEARWATERMain)
else:
    print("Unable to download " + FullLINEARWATERMain)

if url_checker(FullROADSMain)  == "Yes":
    UrlZip(FullROADSMain)
else:
    print("Unable to download " + FullROADSMain)


print ('All the files for county '+ county + ' have been downloaded!')

sys.exit(1)

''' 
# Create a ZipFile Object and load sample.zip in it
with ZipFile('sampleDir.zip', 'r') as zipObj:
   # Get a list of all archived file names from the zip
   listOfFileNames = zipObj.namelist()
   # Iterate over the file names
   for fileName in listOfFileNames:
       # Check filename endswith csv
       if fileName.endswith('.csv'):
           # Extract a single file from zip
           zipObj.extract(fileName, 'temp_csv')
           '''