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
This module inserts the NGDA Alternate Title for NGDA files
'''

def FirstAlternativeTitle (Pass,File):
    Theme = Pass
    NewFile=File
    #print("Now in the FirstAlternativeTitle Module\n")
    #print("Now working on:" + Theme)
    NewFile.write(' <gmd:alternateTitle>\n')

    if re.search('AIANNH',Theme, flags=0):
        NewFile.write('<gco:CharacterString>>National Geospatial Data Asset (NGDA) American Indian/Alaska Native/Native Hawaiian (AIANNH) Homeland Areas</gco:CharacterString>\n')
    elif re.search('AITS',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) American Indian Tribal Subdivision</gco:CharacterString>\n')
    elif re.search('BG',Theme, flags=0):
        NewFile.write('National Geospatial Data Asset (NGDA) Block Group')
    elif re.search('CBSA',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Metropolitan Statistical Area/Micropolitan Statistical Area (CBSA)</gco:CharacterString>\n')
    elif re.search('estate', Theme, flags=0):
        NewFile.write('National Geospatial Data Asset (NGDA) Estate (U.S. Virgin Islands)\n')
    elif re.search('Congressional District',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) 115th Congressional District</gco:CharacterString>\n')
    elif re.search('CNECTA',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Combined New England City and Town Area</gco:CharacterString>\n')
    elif re.search('Current County and Equivalent',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) County and Equivalent</gco:CharacterString>\n')
    elif re.search('CSA',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Combined Statistical Area</gco:CharacterString>\n')
    elif re.search('Current Metropolitan Division',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Metropolitan Division</gco:CharacterString>\n')
    elif re.search('NECTA Division National',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) NECTA Division</gco:CharacterString>\n')
    elif re.search('NECTA',Theme,flags=0):
        NewFile.write(' <gco:CharacterString>National Geospatial Data Asset (NGDA) New England City and Town Area</gco:CharacterString>\n')
    elif re.search('Current State and Equivalent',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) State and Equivalent</gco:CharacterString>\n')
    elif re.search('Current Tribal Block Group',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Tribal Block Group</gco:CharacterString>\n')
    elif re.search('Current Tribal Census Tract',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Tribal Census Tract</gco:CharacterString>\n')
    elif re.search('Census  Urban Area',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Urban Area</gco:CharacterString>\n')
    elif re.search('ZCTA5',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) ZIP Code Tabulation Area</gco:CharacterString>\n')
    elif re.search('Current County Subdivision', Theme, flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) County Subdivision</gco:CharacterString>\n')
    elif re.search('Current Place', Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Place</gco:CharacterString>\n')
    elif re.search('PUMA',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Public Use Microdata Area (PUMA)</gco:CharacterString>')
    elif re.search('(SLD) Lower Chamber',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) State Legislative District (SLD) Lower Chamber</gco:CharacterString>')
    elif re.search('Upper Chamber', Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) State Legislative District (SLD) Upper Chamber</gco:CharacterString>')
    elif re.search('2010 Census  Block',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Census Block</gco:CharacterString>\n')
    elif re.search ('2020 Census  Block', Theme, flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Census Block</gco:CharacterString>\n')
    elif re.search('Current Census Tract',Theme, flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Census Tract</gco:CharacterString>')
    elif re.search('All Roads',Theme,flags=0):
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA) Roads (All Roads)</gco:CharacterString>')
    else:
        NewFile.write('<gco:CharacterString>National Geospatial Data Asset (NGDA)' + Theme + '</gco:CharacterString>\n')
    NewFile.write('</gmd:alternateTitle>\n')
    #NewFile.write('<!-- End of the module-->')
