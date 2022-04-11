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
This module takes the name from the Title element aaaaa retruns the themed directory for purpose of file dierectories
'''

def ThemeDir (Pass):
    Theme = Pass
    print("Now in theThemeDir Module\n")
    print("Now working on:" + Theme)
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
    elif re.search ('2010 Census County and Equivalent State-based',Theme, flags=0):
        return 'county2010'
    elif re.search('Census County and Equivalent State-based', Theme, flags=0):
        return 'county'
    elif re.search('Current County Subdivision',Theme,flags=0):
        return'cousub'
    elif re.search('Current Place',Theme,flags=0):
        return 'place'
    elif re.search('2010 Census Place',Theme,flags=0):
        return 'place10'
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
    elif re.search('Address Range-Feature', Theme, flags=0):
        return 'addrfn'
    elif re.search('Address Range-Feature', Theme, flags=0):
        return 'addrfeat'
    elif re.search('Address Ranges',Theme,flags=0):
        return 'addr'
    elif re.search('Area Landmark', Theme, flags=0):
        return'arealm'
    elif re.search('Area Hydrography', Theme, flags=0):
        return 'areawater'
    elif re.search('All Lines', Theme, flags=0):
        return 'edges'
    elif re.search('Topological Faces-Area Landmark', Theme, flags=0):
        return'facesal'
    elif re.search('Topological Faces-Area Hydrography', Theme, flags=0):
        return 'facesah'
    elif re.search('Topological Faces', Theme, flags=0):
        return 'faces'
    elif re.search('Feature Names', Theme, flags=0):
        return 'featnames'
    elif re.search('Linear Hydrography', Theme, flags=0):
        return 'linearwater'
    elif re.search(' Point Landmark', Theme, flags=0):
        return 'pointlm'
    elif re.search('Primary and Secondary Roads', Theme, flags=0):
        return 'prisecroads'
    elif re.search('All Roads', Theme, flags=0):
        return 'roads'
    elif re.search ('Census County Subdivision',Theme, flags=0):
        return 'cousub'
    elif re.search ('2010 Census Elementary School District' ,Theme, flags=0):
        return 'elsd2010'
    elif re.search('Census Elementary School District', Theme, flags=0):
        return 'elsd'
    elif re.search('Current Elementary School Districts',Theme, flags=0):
        return 'elsd'
    elif re.search('2010 Census Secondary School District',Theme,flags=0):
        return 'scsd10'
    elif re.search('2021 Census Secondary School District',Theme,flags=0):
        return 'scsd'
    elif re.search('Current Secondary School Districts Shapefile State-based',Theme,flags=0):
        return 'scsd'
    elif re.search('2010 Census  State and Equivalent', Theme,flags=0):
        return'state10'
    elif re.search('2020 Census  State and Equivalent',Theme,flags=0):
        return'state'
    elif re.search('2020 Census  SubMinor Civil Division',Theme, flags=0):
        return 'subbarrio20'
    elif re.search('2010 Census  Block', Theme, flags=0):
        return 'tabblock10'
    elif re.search('2010 Census  Block', Theme, flags=0):
        return 'tabblock20'
    elif re.search('2010 Census Tract', Theme, flags=0):
        return "tract10"
    elif re.search ('2010 Census  Urban Growth Area (UGA)',Theme,flags=0):
        return 'uga2010'
    elif re.search('2010 Census  Urban Growth Area (UGA)',Theme,flags=0):
        return 'uga2010'
    elif re.search('UGA', Theme, flags=0):
        return 'UGA'
    elif re.search('2010 Census Unified School Districts', Theme, flags=0):
        return 'unsd10'
    elif re.search('Current Consolidated City State-based',Theme,flags=0):
        return 'concity'
    else:
        return 'Theme:   (' + Theme + ')'
