import os
import fnmatch
import shutil
import re
import datetime
import time
#import StringIO
import pickle
import sys
from ThemeDir import ThemeDir

'''
This module inserts the download URL for the Entity and Attribute File
'''

def EAFileFiller(Pass, File):
    NewFile = File
    Theme = Pass
    AppProfile1 = '                     <gmd:applicationProfile>\n'
    AppProfile2 = '                        <gco:CharacterString>https</gco:CharacterString>\n'
    AppProfile3 = '                     </gmd:applicationProfile>\n'
    FinalAppProfile = AppProfile1 + AppProfile2 + AppProfile3
    Name1 = '                    <gmd:name>\n'
    Name2 = '                        <gco:CharacterString>Entity and Attribute File</gco:CharacterString>\n'
    Name3 = '                    </gmd:name>\n'
    FinalAppName = Name1 + Name2 + Name3
    EAFirstPart = '                        <gmd:URL>https://meta.geo.census.gov/data/existing/decennial/GEO/GPMB/TIGERline/Current_19110/'

    if re.search('AIANNH', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')

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
    elif re.search('Address Ranges',Theme,flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>\n'
        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the Address Ranges County-based Relationship File</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    elif re.search('All Roads', Theme, flags=0):
        NewFile.write('                     <gmd:linkage>\n')
        EATheme = str(ThemeDir(Theme))
        eafileName = 'tl_2020_' + EATheme + '.ea.iso.xml'
        eaUrL = EAFirstPart + '/' + EATheme + '/' + eafileName + '</gmd:URL>\n'
        NewFile.write(eaUrL)
        NewFile.write('                     </gmd:linkage>\n')
        NewFile.write(FinalAppProfile)
        NewFile.write(FinalAppName)
        NewFile.write('                     <gmd:description>\n')
        NewFile.write('                        <gco:CharacterString>This Entity and attribute contains the attributes for the Roads Shapefile</gco:CharacterString>\n')
        NewFile.write('                     </gmd:description>\n')
    else:
        NewFile.write('                     <gmd:linkage>\n')
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