import os
import fnmatch
import shutil
import re
import datetime
import time
#import StringIO
import pickle
import sys
import MetadataDateModules
from  MetadataDateModules import metadataDateUpdater
from  MetadataDateModules import TodaysDate
datesupdated=[]
NewFileArray=[]
NationalPlace=[]
DatesUpdated=0
FileCounter=0
EndDateStamp='no'

# getting today's date using the datetime module
PresentDate = datetime.datetime.now()
PresentDate.day


if PresentDate.hour > 12:
    PresentHour = PresentDate.hour -12
    AmPm='PM"'
else:
    PresentHour =PresentDate.hour
    AmPm ='AM'

presentTime= str(PresentHour) + ":" + str(PresentDate.minute) + ":" + str(PresentDate.second) + AmPm

if PresentDate.day < 10:
    day = "0" + str(PresentDate.day)
else:
    day = PresentDate.day

if PresentDate.month < 10:
    month = "0" + str(PresentDate.month)
else:
    month = PresentDate.month

PresentDate2 = str(PresentDate.year) + "-" + str(month) + "-" + str(day)

path='C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2020files/ver2/fe_2020/stateNGDA/unsd'
#     C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020files\ver2\fe_2020\stateNGDA\anrc\tl_2020_02_anrc.shp.iso.xml
# C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020 files\ver2\fe_2020\NationalNGDA

configfiles = [os.path.join(dirpath, f)
               for dirpath, dirnames, files in os.walk(path)
               for f in files if f.endswith('.xml')]

def DateStampMod(DateStampInd, CurrentDate,ContentIfoInd):
    print('Now working on '+ CurrentDate)
    if ContentIfoInd == 'yes':
        NewFile.write(line)
        EndDateStamp = 'No'
        return EndDateStamp
    elif DateStampInd == 'yes':
        NewFile.write('<gco:Date>' + PresentDate2 + '</gco:Date>\n')
        NewFile.write('</gmd:dateStamp>')
        EndDateStamp= 'No'
        return EndDateStamp
    else:
        NewFile.write('<gmd:dateStamp>')
        NewFile.write('<gco:Date>' + PresentDate2 + '</gco:Date>\n')
        NewFile.write('</gmd:dateStamp>')
        EndDateStamp = 'No'
        return EndDateStamp


def RestServiceFiller (Pass):
    Theme = Pass
    print("Now in the RestServiceFiller Module\n")
    print("Now working on (RestServiceFiller):" + Theme+ "\n")
    #NewFile.write(' <gmd:alternateTitle>\n')
    AppProfile1 ='                     <gmd:applicationProfile>\n'
    AppProfile2 ='                        <gco:CharacterString>https://www.geoplatform.gov/spec/esri-map-rest</gco:CharacterString>\n'
    AppProfile3='                     </gmd:applicationProfile>\n'
    FinalAppProfile= AppProfile1 + AppProfile2 + AppProfile3
    NewFile.write('Them: ' + Theme)

    if re.search('AIANNH', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/AIANNHA/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                        <gco:CharacterString>TIGERweb/AIANNHA (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains all the Current American Indian/Alaska Native/Native Hawaiian Areas National layers</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('AITS', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/AIANNHA/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                        <gco:CharacterString>TIGERweb/AIANNHA (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains all the Tribal Subdivision and Oklahoma Tribal Statistical Areas layers</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('BG', theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Tracts_Blocks/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write(
            '                        <gco:CharacterString>TIGERweb/Tracts_Blocks (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write(
            '                        <gco:CharacterString>This Rest Service contains the 2010 Census Block Groups layer</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('CBSA', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/CBSA/MapServer/WMSServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/CBSA (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the Current Metropolitan Statistical Area/Micropolitan Statistical Area (CBSA) Layers</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Congressional District', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                       <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Legislative/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                     <gco:CharacterString>TIGERweb/Legislative (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the 116th Congressional layer</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('CNECTA', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/CBSA/MapServer/WMSServer</gmd:URL>')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/CBSA (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the Combined New England City and Town Areas layers</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('estate'):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Places_CouSub_ConCity_SubMCD/MapServer</gmd:URL>')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/Places_CouSub_ConCity_SubMCD (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the estates layers</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')

    elif re.search('Current County and Equivalent', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer</gmd:URL>')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                        <gco:CharacterString>TIGERweb/State_County (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the Counties and Equivalent Layer</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('CSA', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/CBSA/MapServer/WMSServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/CBSA (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the Current Combined Statistical Area (CSA)</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Metropolitan Division', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/CBSA/MapServer/WMSServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/CBSA (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the Current Metropolitan Divisions</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('NECTA Division National', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/CBSA/MapServer/WMSServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/CBSA (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the Current New England City and Town Area divisions layer</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('NECTA', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/CBSA/MapServer/WMSServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/CBSA (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the Current New England City and Town Areas layer</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current State and Equivalent', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/State_County/MapServer</gmd:URL>')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                        <gco:CharacterString>TIGERweb/State_County (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the States and Equivalents Layers</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Tribal Block Group', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                       <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/TribalTracts/MapServer</gmd:URL>')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/TribalTracts (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the Tribal Block Group Layers</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')

    elif re.search('Current Tribal Census Tract', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                       <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/TribalTracts/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/TribalTracts (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the Tribal Census Tracts Layers</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Census  Urban Area', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Urban/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/Urban (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the 2010 Census Urban Area Clusters</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('ZCTA5', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('<gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/PUMA_TAD_TAZ_UGA_ZCTA/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/PUMA_TAD_TAZ_UGA_ZCTA (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the Zip Code Tabulation Layer</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current County Subdivision',Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('<gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Places_CouSub_ConCity_SubMCD/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/Places_CouSub_ConCity_SubMCD (MapServer) (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the County Sudivisions</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Place',Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('<gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Places_CouSub_ConCity_SubMCD/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/Places_CouSub_ConCity_SubMCD (MapServer) (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the places</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('PUMA',Theme,flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('<gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/PUMA_TAD_TAZ_UGA_ZCTA/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/PUMA_TAD_TAZ_UGA_ZCTA (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the 2010 Public Use Microdata Area layer</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('(SLD) Lower Chamber',Theme,flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('<gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Legislative/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write(
            '                      <gco:CharacterString>TIGERweb/Legislative (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write(
            '                        <gco:CharacterString>This Rest Service contains the state legislative districts - lower chamber (House of Representatives) layer</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Upper Chamber', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write(
            '<gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Legislative/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/Legislative (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the state legislative districts - upper chamber (Senate) layer</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('2010 Census',Theme,flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('<gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/Tracts_Blocks/MapServer</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/Tracts_Blocks (MapServer)a</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the 2010 Census Block layers</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    else:
        NewFile.write('                     <gmd:linkage>\n')
        NewFile.write('<gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb</gmd:URL>\n')
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains FILL IN HERE!!!!</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')





def WMSFiller(Pass):
    Theme = Pass
    AppProfile1 = '                     <gmd:applicationProfile>\n'
    AppProfile2 = '                        <gco:CharacterString>http://opengis.net/spec/wms</gco:CharacterString>\n'
    AppProfile3 = '                     </gmd:applicationProfile>\n'
    FinalAppProfile = AppProfile1 + AppProfile2 + AppProfile3
    Name1='                    <gmd:name>\n'
    Name2='                        <gco:CharacterString>TIGERweb/tigerWMS_Current (MapServer)</gco:CharacterString>\n'
    Name3='                    </gmd:name>\n'
    FinalAppName = Name1 + Name2 + Name3
    Current1='                     <gmd:linkage>\n'
    Current2='                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/services/TIGERweb/tigerWMS_Current/MapServer/WMSServer</gmd:URL>\n'
    Current3='                     </gmd:linkage>\n'
    FinalCurrentWMS = Current1 + Current2 + Current3
    if re.search('AIANNH', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for Current American Indian/Alaska Native/Native Hawaiian Areas. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification. </gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('AITS', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for Current American Indian Tribal Subdivision. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('BG', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write(
            '                        <gco:CharacterString>This web mapping service contains the layer forBlock Groups. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('CBSA', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This web mapping service Service contains the Current Metropolitan Statistical Area/Micropolitan Statistical Area (CBSA) Layers. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Congressional District', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for 116th Congressional Districts. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('CNECTA', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for the Combined New England City and Town Areas. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current County and Equivalent', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for the Current County and Equivalent. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('CSA', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This web mapping service contains the layer for the Current Combined Statistical Area (CSA). This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search ('estates', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This web mapping service contains the layer for the estates in the Virgin Islands. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Metropolitan Division', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This web mapping service contains the layer for the Current Metropolitan Division. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('NECTA Division National', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This web mapping service contains the layer for the New England City and Town Area Divisions. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('NECTA', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This web mapping service contains the layer for the Current New England City and Town Areas. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current State and Equivalent', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for the States and Equivalents. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification. </gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Tribal Block Group', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This web mapping service contains the layer for Current Tribal Block Groups. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')

    elif re.search('Current Tribal Census Tract', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for Current Tribal Census Tracts. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Census  Urban Area', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>TThis web mapping service contains the layer for the 2010 Census Urban Area Clusters. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('ZCTA5', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for the Zip Code Tabulation Areas. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current County Subdivision',Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for the County Sudivisions. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification. </gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Place',Theme,flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for the places. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification. </gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('PUMA',Theme,flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for the 2010 Public Use Microdata Areas. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification. </gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('(SLD) Lower Chamber',Theme,flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for state legislative districts - lower chamber. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification. </gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Upper Chamber', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for state legislative districts - upper chamber. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification. </gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('2010 Census  Block', Theme,flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for 2010 Census Blocks. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification. </gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('2020 Census  Block', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for 2020 Census Blocks. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification. </gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Census Tract', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for 2010 Census Tracts. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification. </gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    else:
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for the '+ Theme+ '. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')

def ThemeDir (Pass):
    Theme = Pass
    #print("Now in theThemeDir Module\n")
    #print("Now working on:" + Theme)
    if re.search('AIANNH',Theme, flags=0):
        return 'aiannh'
    elif re.search('aitsn',Theme,flags=0):
        return 'aitsn'
    elif re.search('BG',Theme,flags=0):
        return'bg'
    elif re.search('CBSA',Theme,flags=0):
        return 'cbsa'
    elif re.search('Congressional District',Theme,flags=0):
        return 'cd116'
    elif re.search('CNECTA',Theme,flags=0):
        return 'cnecta'
    elif re.search('Current County and Equivalent',Theme,flags=0):
        return 'county'
    elif re.search('CSA',Theme,flags=0):
        return 'csa'
    elif re.search('Current Metropolitan Division',Theme,flags=0):
        return 'metdiv'
    elif re.search('NECTA Division National',Theme,flags=0):
        return 'nectadiv'
    elif re.search('NECTA',Theme,flags=0):
        return 'necta'
    elif re.search('Current State and Equivalent',Theme,flags=0):
        return 'state'
    elif re.search('Current Tribal Block Group',Theme,flags=0):
        return 'tbg'
    elif re.search('Current Tribal Census Tract',Theme,flags=0):
        return 'ttract'
    elif re.search('Census  Urban Area',Theme,flags=0):
        return 'uac10'
    elif re.search('ZCTA5',Theme,flags=0):
        return 'zcta510'
    elif re.search('Current Block Group',Theme,flags=0):
        return 'bg'
    elif re.search('Current County Subdivision',Theme,flags=0):
        return'cousub'
    elif re.search('Current Place',Theme,flags=0):
        return 'place'
    elif re.search('PUMA',Theme,flags=0):
        return 'puma10'
    elif re.search('(SLD) Lower Chamber',Theme,flags=0):
        return'sldl'
    elif re.search('Lower Chamber',Theme,flags=0):
        return 'sldl'
    elif re.search('Upper Chamber', Theme, flags=0):
        return'sldu'
    elif re.search('2010 Census  Block',Theme,flags=0):
        return 'tabblock10'
    elif re.search('2020 Census  Block',Theme,flags=0):
        return 'tabblock20'
    elif re.search('Current Census Tract',Theme,flags=0):
        return 'tract'
    elif re.search('Current Unified School Districts Shapefile',Theme,flags=0):
        return'unsd'
    else:
        return 'Fill_in- for(ThemeDir)' + Theme

def EAFileFiller(Pass):
    Theme = Pass
    AppProfile1 = '                     <gmd:applicationProfile>\n'
    AppProfile2 = '                        <gco:CharacterString>https</gco:CharacterString>\n'
    AppProfile3 = '                     </gmd:applicationProfile>\n'
    FinalAppProfile = AppProfile1 + AppProfile2 + AppProfile3
    Name1 = '                    <gmd:name>\n'
    Name2 = '                        <gco:CharacterString>Entity and Attribute File</gco:CharacterString>\n'
    Name3 = '                    </gmd:name>\n'
    FinalAppName = Name1 + Name2 + Name3
    if re.search('AIANNH', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName='tl_2020_'+ EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the the Current American Indian/Alaska Native/Native Hawaiian Areas National (AIANNH) National Shapefile </gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('AITS', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the the Current American Indian Tribal Subdivision (AITS) National Shapefile </gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('BG', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write(
            '                        <gco:CharacterString>This Entity and attribute contains the attributes for the the Current Block Groups State Shapefile </gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Block Group', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write(
            '                        <gco:CharacterString>This Entity and attribute contains the attributes for the the Current Block Groups State Shapefile </gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('CBSA', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Entity and attribute contains the attributes for the the Current Metropolitan Statistical Area/Micropolitan Statistical Area (CBSA) National Shapefile</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif (re.search('estates', Theme, flags=0)):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Entity and attribute contains the attributes for the the Current estates state Shapefile</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Congressional District', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the the 116th Congressional District National Shapefile</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('CNECTA', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the the Current Combined New England City and Town Area (CNECTA) National Shapefile</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current County and Equivalent', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the the Current County and Equivalent National Shapefile </gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('CSA', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Entity and attribute contains the attributes for the the Current Combined Statistical Area (CSA) National Shapefile</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Metropolitan Division', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Entity and attribute contains the attributes for the the Current Metropolitan Division National Shapefile</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('NECTA Division National', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Entity and attribute contains the attributes for the Current NECTA Division National Shapefile</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('NECTA', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Entity and attribute contains the attributes for the Current New England City and Town Area (NECTA) National Shapefile</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current State and Equivalent', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the Current State and Equivalent National Shapefile </gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Tribal Block Group', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Entity and attribute contains the attributes for the Current Tribal Block Group National Shapefile</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')

    elif re.search('Current Tribal Census Tract', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the Current Tribal Census Tract National Shapefile</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Census  Urban Area', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Entity and attribute contains the attributes for the Census Urban Area National Shapefile</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('ZCTA5', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme= str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL= EAFirstPart + '/'+ EATheme + '/' + eafileName+ '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the Census 5-Digit ZIP Code Tabulation Area (ZCTA5) National Shapefile</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current County Subdivision',Theme,flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>\n'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write(
            '                        <gco:CharacterString>This Entity and attribute contains the attributes for the Current County Subdivision State Shapefiles</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Place',Theme,flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write(
            '                        <gco:CharacterString>This Entity and attribute contains the attributes for the place State Shapefiles</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('PUMA',Theme,flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the PUMA State Shapefiles</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Upper Chamber',Theme,flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>\n'
        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the PUMA State Shapefiles</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('2010 Census  Block',Theme,flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>\n'
        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the Tabblock10 State Shapefiles</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('2020 Census  Block',Theme,flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>\n'
        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the Tabblock10 State Shapefiles</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Census Tract',Theme,flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>\n'
        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the Tract State Shapefiles</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Unified School Districts Shapefile',Theme,flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>\n'
        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write(
            '                        <gco:CharacterString>This Entity and attribute contains the attributes for the Unified School Districts  State Shapefiles</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    else:
        NewFile.write('                     <gmd:linkage>\n')
        EAFirstPart = '                        <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>'

        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>' + Theme + '</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')

def eaUrl(Pass):
    Theme = Pass
    #print("Now in the eaUrl Module\n")
    #print("Now working on:" + Theme)
    EATheme = str(ThemeDir(Theme))
    FirstPartUrl='https://meta.geo.census.gov/data/existing/decennial/GEO/GPMB/TIGERline/'
    YearDir='Tiger2020'
    EAFileName='tl_2020_' + EATheme + '.shp.ea.iso.xml'
    FinalEaFile= FirstPartUrl + '/' + YearDir + "/" + EATheme + '/' + EAFileName +'\n'
    return FinalEaFile



def eaTitle(Pass):
    Theme = Pass
    #print("Now in the eaTitle Module\n")
    #print("Now working on:" + Theme)
    if re.search('AIANNH', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 Current American Indian/Alaska Native/Native Hawaiian Areas National (AIANNH) National Shapefile</gco:CharacterString>\n'
    elif re.search('AITS', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 Current American Indian Tribal Subdivision (AITS) National Shapefile</gco:CharacterString>\n'
    elif re.search ('BG', Theme, flags=0):
        return 'Feature Catalog for the 2020 TIGER/Line Shapefile Current Block Group State-based Shapefile\n'
    elif re.search('CBSA', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 Current Metropolitan Statistical Area/Micropolitan Statistical Area (CBSA) National Shapefile</gco:CharacterString>\n'
    elif re.search('Congressional District', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 116th Congressional District National Shapefile</gco:CharacterString>\n'
    elif re.search('CNECTA', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the Current 2020 Combined New England City and Town Area (CNECTA) National Shapefile</gco:CharacterString>\n'
    elif re.search('Current County and Equivalent', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 Current County and Equivalent National Shapefile</gco:CharacterString>\n'
    elif re.search('CSA', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 Current Combined Statistical Area (CSA) National Shapefile</gco:CharacterString>\n'
    elif re.search('Current Metropolitan Division', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 Current Metropolitan Division National Shapefile</gco:CharacterString>\n'
    elif re.search('NECTA Division National', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 Current NECTA Division National Shapefile</gco:CharacterString>\n'
    elif re.search('NECTA', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 Current New England City and Town Area (NECTA) National Shapefile</gco:CharacterString>\n'
    elif re.search('Current State and Equivalent', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 Current State and Equivalent National Shapefile</gco:CharacterString>\n'
    elif re.search('Current Tribal Block Group', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 Current Tribal Block Group National Shapefile</gco:CharacterString>\n'
    elif re.search('Current Tribal Census Tract', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 Current Tribal Census Tract National Shapefile</gco:CharacterString>\n'
    elif re.search('Census  Urban Area', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2010 Census Urban Area National Shapefile</gco:CharacterString>\n'
    elif re.search('ZCTA5', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 2010 Census 5-Digit ZIP Code Tabulation Area (ZCTA5) National Shapefile</gco:CharacterString>\n'
    elif re.search('estate', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Current Estate State-based Shapefile (U.S. Virgin Islands only)</gco:CharacterString>\n'
    elif re.search('Current Block Group', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Current Block Group State-based Shapefile</gco:CharacterString>\n'
    elif re.search('Current County Subdivision', Theme, flags=0):
        return'<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Current County Subdivision State-based Shapefile</gco:CharacterString>\n'
    elif re.search('Current Place',Theme,flags=0):
        return'<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Current Place State-based Shapefile</gco:CharacterString>\n'
    elif re.search('PUMA',Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Public Use Microdata Area (PUMA) State-based Shapefile</gco:CharacterString>\n'
    elif re.search('Lower Chamber',Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Current State Legislative District (SLD) Lower Chamber State-based Shapefile</gco:CharacterString>\n'
    elif re.search('Upper Chamber',Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Current State Legislative District (SLD) Upper Chamber State-based Shapefile</gco:CharacterString>\n'
    elif re.search('2010 Census  Block',Theme,flags=0):
        return'<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2010 Census Block  state based Shapefile</gco:CharacterString>\n'
    elif re.search('2020 Census  Block',Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2020 Census Block  state based Shapefile</gco:CharacterString>\n'
    elif re.search('Current Census Tract',Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2020 tracts  state based Shapefile</gco:CharacterString>\n'
    elif re.search('unsd',Theme,flags=0):
        return'<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Current Unified School Districts Shapefile State-based</gco:CharacterString>\n'
    elif re.search('Current Unified School Districts Shapefile',Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Current Unified School Districts Shapefile State-based</gco:CharacterString>\n'
    else:
        return '<gco:CharacterString> The theme is ' + Theme +'(eatitle)</gco:CharacterString>\n'


if os.path.exists(path):
    print("The " + path + " directory exists")
else:
    print("Could not find " + path + ". Please make sure the path is correct")
    sys.exit(1)

def keywordCounter(input):
    file=input
    KeywordModCounter=0
    ReadFile = open(file, "r")
    for line in ReadFile:
        if re.search('<gmd:keyword>',line,flags=0):
            KeywordModCounter+=1
        else:
            continue
    FinalKeyword= KeywordModCounter-3
    return FinalKeyword



for file in configfiles:
    transferOptionsCounter=0
    linkageCounter=0
    editionCounter=0
    FileCounter += 1
    gmdDateCounter=0
    KeywordModCounter=0
    KeywordGood = 'yes'
    keywordCounter =0
    NationalPlace.clear()
    nationalPlaceInd = 'no'
    keywordind = 'no'
    InCitInd = 'no'
    TitleEndCharacterString ='no'
    DescriptiveKeywordsInd='off'
    MafTigerInd = 'no'
    dotLocation = file.find(".")
    preDot = file[0:dotLocation]
    postDot = file[dotLocation:]
    ContentIfoInd = 'no'
    FirstTitle = 'Yes'
    endTitleCounter=0
    datasetUriind = 'no'
    OutFile = preDot + "_corrected_" + postDot

    ReadFileA = open(file, "r")
    for line in ReadFileA:
        if re.search('<gmd:keyword>', line, flags=0):
            KeywordModCounter += 1
        else:
            continue
    PrePlace = KeywordModCounter -6
    StateKeywords= PrePlace +3
    ReadFileA.close()

    #finalKeyword=int(keywordCounter(file))
    print (' PrePlace' + str( PrePlace))
    print ('StateKeywords' + str(StateKeywords))

    #print("preDot: " + preDot)
    #print("PostDot: " + postDot)
    #print("Outfile" + OutFile)
    #print("File: " + file)
    print("Now Working on: " + file)
    #print ("Outfile=" + OutFile)
    ReadFile = open(file, "r")
    with  open(OutFile, "w") as NewFile:
        for line in ReadFile:
            if re.search('gmd:linkage',line,flags=0):
                linkageCounter+=1
                #NewFile.write('<!-- if #1 -->\n')
                if linkageCounter == 1:
                    LinkageInd='yes'
                    NewFile.write(line)
                else:
                    NewFile.write(line)
            elif re.search('<gco:CharacterString>MAF/TIGER</gco:CharacterString>', line, flags=0):
                NewFile.write(line)
                MafTigerInd = 'yes'
                NewFile.write('<!-- MafTigerind: ' + MafTigerInd + ' -->\n')
            elif re.search('gmd:URL',line, flags=0):
                #NewFile.write('<!-- if #2 -->\n')
                print("---------------------------------\n")
                #print ("LinkageInd: " + LinkageInd + "\n")
                if LinkageInd =="yes":
                    #NewFile.write(line)
                    lastSlash=line.rfind("/tl")+1
                    lastEndtag=line.find("</gmd:URL>")
                    ZipFileName=line[lastSlash: lastEndtag]
                    ThemeURL=str(ThemeDir( mainTheme))
                    '''
                    # NewFile.write('<!-- ZipFileName ' + ZipFileName + '-->')
                    #NewFile.write('<!-- ThemeURL' + ThemeURL + '-->')
                    '''
                    FinalZip=' <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/'+ ThemeURL +'/' + ZipFileName + '</gmd:URL>\n'
                    LinkageInd="No"
                   # print('In the LinkageId section\n')
                    #print(line)
                    #print ('ZipFileName: ' + ZipFileName)
                    LinkageInd='No'
                    #NewFile.write('<!--- What is going on here? -->')
                    NewFile.write(FinalZip)
                else:
                    NewFile.write(line)
            elif re.search('<gco:CharacterString>.shp.iso.xml',line, flags=0):
                #NewFile.write('<!-- if #3 -->\n')
                NewFile.write('     <gco:CharacterString>' + file + '</gco:CharacterString>')
            elif re.search ('codeListValue=""',line,flags=0):
                #NewFile.write('<!-- if #4 -->\n')
                NewFile.write('                        codeListValue="dataset"/>')
            elif re.search('<gmd:MD_GeometricObjectTypeCode',line,flags=0):
                #NewFile.write('<!-- if #5 -->\n')
                lastCarrot=line.find('>')-1
                maipart=line[0:lastCarrot]
                GMTC=maipart+'" codeListValue="complex">complex</gmd:MD_GeometricObjectTypeCode>'
                NewFile.write(GMTC)
            elif re.search('</gmd:featureTypes>',line,flags=0):
                #NewFile.write('<!-- if #6 -->\n')
                NewFile.write(line)
                NewFile.write('         <gmd:featureCatalogueCitation>')
                NewFile.write('           <gmd:CI_Citation>\n')
                NewFile.write('              <gmd:title>\n')
                NewFile.write(str(eaTitle(mainTheme)))
                NewFile.write('               </gmd:title>\n')
                NewFile.write('               <gmd:date>\n')
                NewFile.write('                  <gmd:CI_Date>\n')
                NewFile.write('                    <gmd:date>\n')
                NewFile.write('                        <gco:Date>2020</gco:Date>\n')
                NewFile.write('                   </gmd:date>\n')
                NewFile.write('                     <gmd:dateType>\n')
                NewFile.write('                        <gmd:CI_DateTypeCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_DateTypeCode" codeListValue="publication" codeSpace="002"/>\n')
                NewFile.write('                     </gmd:dateType>\n')
                NewFile.write('                  </gmd:CI_Date>\n')
                NewFile.write('               </gmd:date>\n')
                NewFile.write('               <gmd:citedResponsibleParty xlink:href="https://www.ngdc.noaa.gov/docucomp/1df27e57-4768-42de-909b-52f530601fba" xlink:title="U.S Department of Commerce, U.S Census Bureau, Geography Division (distributor)"/>')
                NewFile.write('              <gmd:otherCitationDetails>\n')
                EAFile = str(eaUrl(mainTheme))
                NewFile.write('                  <gco:CharacterString>' + EAFile + '</gco:CharacterString>\n')
                NewFile.write('               </gmd:otherCitationDetails>\n')
                NewFile.write('            </gmd:CI_Citation>\n')
                NewFile.write('        </gmd:featureCatalogueCitation>\n')



            elif re.search('</gmd:protocol>',line,flags=0):
                #NewFile.write('<!-- if #7 -->\n')

                if transferOptionsCounter == 0:
                    NewFile.write(line)
                    NewFile.write(' <gmd:applicationProfile>\n')
                    NewFile.write(' <gco:CharacterString>ZIP</gco:CharacterString>\n')
                    NewFile.write('</gmd:applicationProfile>\n')
                    NewFile.write('<gmd:name>\n')
                    NewFile.write('<gco:CharacterString>'+ ZipFileName + '</gco:CharacterString>\n')
                    NewFile.write(' </gmd:name>\n')
                    NewFile.write('<gmd:description>\n')
                    NewFile.write(' <gco:CharacterString> This zip file contains the ' + file + ' shapefile </gco:CharacterString>\n')
                    NewFile.write('</gmd:description>\n')

                else:
                    NewFile.write(line)

            elif re.search('<gco:CharacterString>TIGER/Line Shapefile',line,flags=0):
                #NewFile.write('<!-- if #8 -->\n')
                if FirstTitle == 'Yes':
                    FirstTitle ='No'
                    TitleEndCharacterString='yes'
                    mainTitle=line
                    lastComma=line.rfind(',')+1
                    if re.search('</gco:CharacterString>',line,flags=0):
                        closingTagLoc=line.find('</')
                        mainTheme = line[lastComma:closingTagLoc]
                    else:
                        mainTheme=line[lastComma:]
                    Geography=line[68:lastComma-1]
                    #print ('Geography:' +  Geography)
                    PrimaryAlternateTitle = '<gco:CharacterString>TIGER/Line Shapefile, Current, ' + Geography + mainTheme + '</gco:CharacterString>\n'

                    NewFile.write(PrimaryAlternateTitle)
                    #NewFile.write('<!-- Check 1 -->\n')

                    NewFile.write('</gmd:title>\n')
                    NewFile.write(' <gmd:alternateTitle>\n')
                    if re.search('</gco:CharacterString>',mainTitle,flags=0):
                        NewFile.write(mainTitle)
                    else:
                        NewFile.write(mainTitle+ '</gco:CharacterString>')
                    NewFile.write(' </gmd:alternateTitle>\n')
                    FirstAlternativeTitle(mainTheme)
                else:
                    NewFile.write(line)

            elif re.search('</gmd:transferOptions>', line, flags=0):
                #NewFile.write('<!-- if #9 -->\n')
                #print('In the transfer options section')
                #print('transferOptionsCounter' + str(transferOptionsCounter: ) + "\n")
                #NewFile.write('<!-- transferOptionsCounter ' + str(transferOptionsCounter) +'-->')
                if transferOptionsCounter == 1:
                    NewFile.write(line)
                    NewFile.write('         <gmd:transferOptions>\n')
                    NewFile.write('           <gmd:MD_DigitalTransferOptions>\n')
                    NewFile.write('               <gmd:onLine>\n')
                    NewFile.write('                 <gmd:CI_OnlineResource>\n')
                    WMSFiller(mainTheme)
                    NewFile.write('                     <gmd:function>\n')
                    NewFile.write('                       <gmd:CI_OnLineFunctionCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_OnlineFunctionCode"\n')
                    NewFile.write('                                                  codeListValue="search">search\n')
                    NewFile.write('                       </gmd:CI_OnLineFunctionCode>\n')
                    NewFile.write('                    </gmd:function>\n')
                    NewFile.write('                 </gmd:CI_OnlineResource>\n')
                    NewFile.write('               </gmd:onLine>\n')
                    NewFile.write('           </gmd:MD_DigitalTransferOptions>\n')
                    NewFile.write('         </gmd:transferOptions>\n')

                    transferOptionsCounter += 1
                    NewFile.write('         <gmd:transferOptions>\n')
                    NewFile.write('           <gmd:MD_DigitalTransferOptions>\n')
                    NewFile.write('               <gmd:onLine>\n')
                    NewFile.write('                 <gmd:CI_OnlineResource>\n')
                    EAFileFiller(mainTheme)
                    NewFile.write('                     <gmd:function>\n')
                    NewFile.write(
                        '                       <gmd:CI_OnLineFunctionCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_OnlineFunctionCode"\n')
                    NewFile.write('                                        codeListValue="download">download\n')
                    NewFile.write('                       </gmd:CI_OnLineFunctionCode>\n')
                    NewFile.write('                    </gmd:function>\n')
                    NewFile.write('                 </gmd:CI_OnlineResource>\n')
                    NewFile.write('               </gmd:onLine>\n')
                    NewFile.write('           </gmd:MD_DigitalTransferOptions>\n')
                    NewFile.write('         </gmd:transferOptions>\n')


                else:
                    NewFile.write(line)
                    transferOptionsCounter += 1
            elif re.search('</gmd:title>',line,flags=0):
                #NewFile.write('<!-- if #10 -->\n')
                if endTitleCounter ==0:
                    endTitleCounter+=1
                else:
                    NewFile.write(line)
            elif re.search('</gco:CharacterString>',line,flags=0):
                #NewFile.write('<!-- if #11 TitleEndCharacterString:' + TitleEndCharacterString + '\n nationalPlaceInd: '  + nationalPlaceInd +'-->\n')
                if TitleEndCharacterString == 'yes':
                    NewFile.write('<!-- 11az -->')
                    TitleEndCharacterString='no'
                    continue
                elif KeywordGood == 'no':
                    NewFile.write('<!-- 11a -->')
                    if keywordind== 'yes':
                        NewFile.write('<!-- if #11b -->\n')
                        print(line)
                        #print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
                        #print('keywordCounter: ' + str(keywordCounter))
                        #print('KeywordGood = ' + KeywordGood)
                        #print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
                        if KeywordGood == 'yes':
                            NewFile.write('<!-- 11c -->')
                            if re.search('State or Equivalent Entity',line,flags=0):
                                StateEntityCounter+=1
                                if StateEntityCounter >1:
                                    continue
                                else:
                                    NewFile.write(line)
                                    print('Printing the Keyword!!!!!!!!!!!!!!')
                                    keywordind='no'
                            else:
                                NewFile.write(line)
                                print('Printing the Keyword!!!!!!!!!!!!!!')
                                keywordind = 'no'
                        else:
                            #print('Now writing' + line + 'to the NationalPlace ')
                            #NewFile.write('<!-- Now writing' + line + 'to the NationalPlace ')
                            NationalPlace.append(line)
                            keywordind = 'no'
                    elif re.search('<gco:CharacterString>MAF/TIGER</gco:CharacterString>', line, flags=0):
                        NewFile.write(line)
                        MafTigerInd = 'yes'
                        #NewFile.write('<!-- MafTigerind: ' + MafTigerInd + ' -->\n')
                    else:
                        continue
                elif datasetUriind =='yes':
                    doubleSlashLoc=line.find('//')
                    postSlash=line[doubleSlashLoc:]
                    newUrl='<gco:CharacterString>https:' + postSlash
                    NewFile.write(newUrl)
                    datasetUriind = 'no'
                elif InCitInd == 'yes':
                    InCitInd ='no'
                    continue
                else:
                    NewFile.write(line)

                    '''
                     #NewFile.write('<!-- if #11a -->\n')
                print(line)
                print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
                print ('keywordCounter: ' + str(keywordCounter))
                print ('KeywordGood = ' + KeywordGood)
                print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')
                if  KeywordGood =='yes':
                    NewFile.write(line)
                    print('Printing the Keyword!!!!!!!!!!!!!!')
                else:
                    print('Now writing' + line + 'to the NationalPlace ')
                    NationalPlace.append(line)
                    
                    '''



            elif re.search(' <gmd:edition>',line,flags=0):
                #NewFile.write('<!-- if #12 -->\n')
                NewFile.write(line)
                NewFile.write('                  <gco:CharacterString>2020</gco:CharacterString>')
            elif re.search('http://www2.census.gov/geo/tiger/TIGER2020',line,flags=0):
                #NewFile.write('<!-- if #13 -->\n')
                semiLoc=line.rfind(':')
                lastpart=line[semiLoc:]
                CorrectedHttp='      <gco:CharacterString>https' + lastpart
                #NewFile.write('<!-- string corrected -->')


            elif re.search(' </gmd:edition>',line, flags=0):
                #NewFile.write('<!-- if #14 -->\n')
                editionCounter+=1
                #print('editionCounter: ' + str(editionCounter))
                if editionCounter ==1:
                    NewFile.write(line)
                    NewFile.write('              <gmd:identifier>\n')
                    NewFile.write('               <gmd:MD_Identifier>\n')
                    NewFile.write('                     <gmd:code>\n')
                    NewFile.write('                        <gco:CharacterString>https://www.census.gov</gco:CharacterString>\n')
                    NewFile.write('                        </gmd:code>\n')
                    NewFile.write('                  </gmd:MD_Identifier>\n')
                    NewFile.write('               </gmd:identifier>\n')
                else:
                    NewFile.write(line)
            elif re.search('<gmd:extent/>',line, flags=0):
                #NewFile.write('<!-- if #15 -->\n')
                NewFile.write('                <gmd:extent>\n')
                NewFile.write('                        <gml:TimePeriod gml:id="timePeriod">\n')
                NewFile.write('                           <gml:beginPosition>2019-06</gml:beginPosition>\n')
                NewFile.write('                           <gml:endPosition>2020-05</gml:endPosition>\n')
                NewFile.write('                       </gml:TimePeriod>\n')
                NewFile.write('                </gmd:extent>\n')
            elif re.search('<gml:beginPosition/>',line,flags=0):
                #NewFile.write('<!-- if #16 -->\n')
                NewFile.write('                           <gml:beginPosition>2019-06</gml:beginPosition>\n')
            elif re.search('<gml:endPosition/>',line,flags=0):
                #NewFile.write('<!-- if #17 -->\n')
                NewFile.write('                           <gml:endPosition>2020-05</gml:endPosition>\n')
            elif  re.search('<gmd:keyword>',line, flags=0):
                #NewFile.write('<!-- if #18 -->\n')
                #NewFile.write('<!-- if #18' + line + '-->\n')
                keywordCounter+=1
                #print('00000000000000000000000000000000000000000000000000000')
                #print('keywordCounter: ' + str(keywordCounter))
                #print(line)
                keywordind='yes'
                if keywordCounter <=PrePlace:
                    KeywordGood='yes'
                    NewFile.write(line)
                    DescriptiveKeywordsInd='off'
                elif keywordCounter<StateKeywords:
                    KeywordGood = 'no'
                    DescriptiveKeywordsInd='off'
                else:
                    if re.search('State or Equivalent Entity',line,flags=0):
                        continue
                    else:
                        NewFile.write(line)
                        KeywordGood = 'yes'
                        DescriptiveKeywordsInd = 'on'
            elif re.search('                 <gco:CharacterString>',line,flags=0):
                #NewFile.write('<!-- if #19 -->\n')
                print(line)
                #print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
                #print ('keywordCounter: ' + str(keywordCounter))
                #print ('KeywordGood = ' + KeywordGood)
                #print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')

                if re.search('>ANSI INCITS 38:2009', line, flags=0):
                    #newLine = line + '</gco:CharacterString>'
                    #(ANSI INCITS 38-2009), Federal Information Processing Series (FIPS) – States/State Equivalents'
                    NewFile.write('<gco:CharacterString>National Standard Codes (ANSI INCITS 38-2009)</gco:CharacterString>' )
                elif re.search('<gco:CharacterString>MAF/TIGER</gco:CharacterString>', line, flags=0):
                    NewFile.write(line)
                    MafTigerInd='yes'
                    NewFile.write('<!-- MafTigerind: ' + MafTigerInd+ ' -->\n')


                else:
                    NewFile.write(line)


            elif re.search('</gmd:keyword>',line,flags=0):
                #NewFile.write('<!-- if #20 -->\n')
                #print('Ending the keyword tag')
                if KeywordGood =='no':
                    continue
                else:
                    NewFile.write(line)

            elif re.search('</gmd:descriptiveKeywords>',line,flags=0):
                #NewFile.write('<!-- if #21 -->\n')
                NewFile.write('<!-- Working with gmd:descriptiveKeywords DescriptiveKeywordsInd: ' +  DescriptiveKeywordsInd + '-->')
                if DescriptiveKeywordsInd=='on':
                    NewFile.write(line)
                    NewFile.write('         <gmd:descriptiveKeywords>')
                    NewFile.write('            <gmd:MD_Keywords>\n')
                    for item in NationalPlace:
                        #NewFile.write('<!-- item: ' + item + " -->")
                        if item != 'State or Equivalent Entity':
                            NewFile.write('              <gmd:keyword>\n')
                            NewFile.write(item + '\n')
                            NewFile.write('              </gmd:keyword>\n')
                    NewFile.write('               <gmd:type>\n')
                    NewFile.write('                  <gmd:MD_KeywordTypeCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_KeywordTypeCode"\n')
                    NewFile.write('                                         codeListValue="place"/>\n')
                    NewFile.write('              </gmd:type>\n')
                    NewFile.write('              <gmd:thesaurusName>\n')
                    NewFile.write('                  <gmd:CI_Citation>\n')
                    NewFile.write('                     <gmd:title>\n')
                    NewFile.write('                       <gco:CharacterString>ISO 3166 Codes for the representation of names of countries and their subdivisions</gco:CharacterString>\n')
                    NewFile.write('                    </gmd:title>\n')
                    NewFile.write('                     <gmd:date gco:nilReason="unknown"/>\n')
                    NewFile.write('                  </gmd:CI_Citation>\n')
                    NewFile.write('             </gmd:thesaurusName>\n')
                    NewFile.write('          </gmd:MD_Keywords>\n')
                    NewFile.write('         </gmd:descriptiveKeywords>\n')
                    DescriptiveKeywordsInd='off'
                else:
                    NewFile.write(line)


            elif re.search ('<gmd:dataSetURI>',line,flags=0):
                datasetUriind='yes'
                NewFile.write(line)
            elif re.search('ANSI INCITS 31:2009',line,flags=0):
                #NewFile.write('<!--ANSI INCITS 31:2009 -->\n')
                InCitInd='yes'
                continue
            elif re.search ('(Formerly FIPS 8-6)',line, flags=0):
                #NewFile.write('<!--ANSI INCITS 31:2009 -->\n')
                continue

            elif re.search ('<gmd:date>',line,flags=0):
                if re.search ('<gmd:date gco:nilReason="unknown"/>',line, flags=0):
                    NewFile.write(line)
                elif MafTigerInd =='yes':
                    NewFile.write(' <gmd:date gco:nilReason="unknown"/>')
                else:
                    NewFile.write(line)
            elif re.search('<gmd:CI_Date>',line,flags=0):
                if MafTigerInd =='yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('<gco:Date>Unpublished material</gco:Date>',line,flags=0):
                if MafTigerInd =='yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('</gmd:date>',line,flags=0):
                if MafTigerInd == 'yes':
                    gmdDateCounter+=1
                    if gmdDateCounter ==1:
                        continue
                    else:
                        MafTigerInd='no'
                else:
                    NewFile.write(line)
            elif re.search('<gmd:dateType>',line,flags=0):
                if MafTigerInd == 'yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search(' <gmd:CI_DateTypeCode',line, flags=0):
                if MafTigerInd =='yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('codeListValue="publication date"',line, flags=0):
                if MafTigerInd == 'yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('</gmd:CI_DateTypeCode>',line, flags=0):
                if MafTigerInd == 'yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('</gmd:dateType>',line, flags=0):
                if MafTigerInd == 'yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('</gmd:CI_Date>',line, flags=0):
                if MafTigerInd == 'yes':
                    continue
                else:
                    NewFile.write(line)










            else:
                NewFile.write(line)
            #print(line)
    NewFileArray.append(OutFile)
    NewFile.close()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")


for newFile in NewFileArray:
    #print (newFile)
    newFileCorrectLoc=newFile.find('_corrected')
    preCorret=newFile[0:newFileCorrectLoc]
    postCorrect=newFile[newFileCorrectLoc+11:]
    DestFile= preCorret+postCorrect
    #print(preCorret)
    #print (postCorrect)
    shutil.copyfile(newFile,DestFile)
    #newFile.close

'''
for newFile in NewFileArray:
    os.remove(newFile)
'''

print ("Done! "+ str(FileCounter) + " files have been processed at "+ presentTime + "!")

sys.exit(1)