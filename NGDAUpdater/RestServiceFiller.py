import os
import fnmatch
import shutil
import re
import datetime
import time
#import StringIO
import pickle
import sys

'''
This module inserts the REST URL 
'''

def RestServiceFiller (Pass,File):
    Theme = Pass
    NewFile = File
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


def restExist (Pass,File):
    Theme = Pass
    NewFile = File
    #print("Now in the restExist Module\n")
    #print("Now working on (restExist):" + Theme+ "\n")
    #NewFile.write(' <gmd:alternateTitle>\n')
    if re.search('AIANNH', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                        <gco:CharacterString>TIGERweb/AIANNHA (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains all the Current American Indian/Alaska Native/Native Hawaiian Areas National layers</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('AITS', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                        <gco:CharacterString>TIGERweb/AIANNHA (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains all the Tribal Subdivision and Oklahoma Tribal Statistical Areas layers</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('BG', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                        <gco:CharacterString>TIGERweb/Tracts_Blocks (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the 2010 Census Block Groups layer</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('CBSA', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/CBSA (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the Current Metropolitan Statistical Area/Micropolitan Statistical Area (CBSA) Layers</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Congressional District', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                     <gco:CharacterString>TIGERweb/Legislative (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the 116th Congressional layer</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('CNECTA', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/CBSA (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the Combined New England City and Town Areas layers</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('estate', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/Places_CouSub_ConCity_SubMCD (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the estates layers</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current County and Equivalent', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                        <gco:CharacterString>TIGERweb/State_County (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the Counties and Equivalent Layer</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('CSA', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/CBSA (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the Current Combined Statistical Area (CSA)</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Metropolitan Division', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/CBSA (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the Current Metropolitan Divisions</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('NECTA Division National', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/CBSA (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the Current New England City and Town Area divisions layer</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('NECTA', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/CBSA (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the Current New England City and Town Areas layer</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current State and Equivalent', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                        <gco:CharacterString>TIGERweb/State_County (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the States and Equivalents Layers</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Tribal Block Group', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/TribalTracts (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the Tribal Block Group Layers</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Tribal Census Tract', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/TribalTracts (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the Tribal Census Tracts Layers</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Census  Urban Area', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                       <gco:CharacterString>TIGERweb/Urban (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                       <gco:CharacterString>This Rest Service contains the 2010 Census Urban Area Clusters</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('ZCTA5', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/PUMA_TAD_TAZ_UGA_ZCTA (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the Zip Code Tabulation Layer</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current County Subdivision',Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/Places_CouSub_ConCity_SubMCD (MapServer) (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the County Sudivisions</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Current Place',Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/Places_CouSub_ConCity_SubMCD (MapServer) (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the places</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('PUMA',Theme,flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/PUMA_TAD_TAZ_UGA_ZCTA (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the 2010 Public Use Microdata Area layer</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('(SLD) Lower Chamber',Theme,flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write(
            '                      <gco:CharacterString>TIGERweb/Legislative (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write(
            '                        <gco:CharacterString>This Rest Service contains the state legislative districts - lower chamber (House of Representatives) layer</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('Upper Chamber', Theme, flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/Legislative (MapServer)</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the state legislative districts - upper chamber (Senate) layer</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('2010 Census',Theme,flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/Tracts_Blocks (MapServer)a</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains the 2010 Census Block layers</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('2020 Census County Subdivision',Theme,flags=0):
        NewFile.write('                    <gmd:name>\n')
        NewFile.write(        '                      <gco:CharacterString>TIGERweb/Places_CouSub_ConCity_SubMCD (MapServer) (MapServer)</gco:CharacterString>')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains 2020 Census County Subdivision </gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    else:
        NewFile.write('                    <gmd:name>\n')
        NewFile.write('                      <gco:CharacterString>TIGERweb/</gco:CharacterString>\n')
        NewFile.write('                    </gmd:name>\n')
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Rest Service contains' +Theme + 'FILL IN HERE!!!!</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')


