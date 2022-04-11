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
This module inserts the WMS URL for download
'''

def WMSFiller(Pass, File):
    Theme = Pass
    NewFile = File
    AppProfile1 = '                     <gmd:applicationProfile>\n'
    AppProfile2 = '                        <gco:CharacterString>http://opengis.net/spec/wms</gco:CharacterString>\n'
    AppProfile3 = '                     </gmd:applicationProfile>\n'
    FinalAppProfile = AppProfile1 + AppProfile2 + AppProfile3
    Name1='                    <gmd:name>\n'
    Name2='                        <gco:CharacterString>TIGERweb/tigerWMS_Current (MapServer)</gco:CharacterString>\n'
    Name3='                    </gmd:name>\n'
    FinalAppName = Name1 + Name2 + Name3
    Current1='                     <gmd:linkage>\n'
    Current2='                        <gmd:URL>https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer</gmd:URL>\n'
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
    elif re.search('All Roads', Theme, flags=0):
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for primary and secondary roads. This URL is to be used in mapping software like ArcMap. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification. </gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')
    else:
        NewFile.write(FinalCurrentWMS)
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This web mapping service contains the layer for the '+ Theme+ '. This URL is to be used in mapping software like ArcMap. To use this in a web browser, see the OGC Web Mapping Specification.</gco:CharacterString>')
        NewFile.write('                     </gmd:description>\n')