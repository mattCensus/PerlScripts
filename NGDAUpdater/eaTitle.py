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
This module inserts the EA Tile in the ContentInfo Section
'''

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
    elif re.search('2020 Place', Theme, flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Current Place State-based Shapefile</gco:CharacterString>\n'
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
        return'<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Current Unified School Districts Shapefile State-based Shapefile</gco:CharacterString>\n'
    elif re.search('Current Unified School Districts Shapefile',Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Current Unified School Districts Shapefile State-based Shapefile</gco:CharacterString>\n'
    elif re.search('Address Range-Feature', Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Address Range-Feature Name County-based Relationship File</gco:CharacterString>'
    elif re.search('Address Range-Feature',Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Address Range-Feature County-based Shapefile</gco:CharacterString>\n'
    elif re.search('Address Ranges County-based Relationship',Theme,flags=0):
        return'<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Address Ranges County-based Relationshi Shapefile State-based Shapefile</gco:CharacterString>\n'
    elif re.search('Area Landmark',Theme,flags=0):
        return'<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Area Landmark State-based Shapefile</gco:CharacterString>\n'
    elif re.search('Area Hydrography',Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Area Hydrography County-based Shapefile</gco:CharacterString>\n'
    elif re.search('All Lines',Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile All Lines County-based Shapefile</gco:CharacterString>\n'
    elif re.search('Topological Faces-Area Landmark',Theme,flags=0):
        return'<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Topological Faces-Area Landmark State-based Relationship File</gco:CharacterString>'
    elif re.search('Topological Faces-Area Hydrography', Theme, flags=0):
        return '<gco:CharacterString>Feature Catolog for the 2013 Current Topological Faces-Area Hydrography Relationship File</gco:CharacterString>'
    elif re.search('Topological Faces',Theme,flags=0):
        return'<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Topological Faces (Polygons With All Geocodes) County-based Shapefile</gco:CharacterString>\n'
    elif re.search('Topological Faces-Area Landmark', Theme, flags=0):
        return'gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Topological Faces-Area Landmark State-based Relationship File</gco:CharacterString>'
    elif re.search('Feature Names',Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Feature Names County-based Relationship File</gco:CharacterString>\n'
    elif re.search('Linear Hydrography',Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Linear Hydrography County-based Shapefile</gco:CharacterString>'
    elif re.search(' Point Landmark',Theme,flags=0):
        return'<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Point Landmark State-based Shapefile</gco:CharacterString>'
    elif re.search('Primary and Secondary Roads',Theme,flags=0):
        return '<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile Primary and Secondary Roads State-based Shapefile</gco:CharacterString>'
    elif re.search('All Roads',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile All Roads County-based Shapefile</gco:CharacterString>')
    elif re.search ('2010 Census County and Equivalent',Theme, flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2010 Census County and Equivalent State-based Shapefile</gco:CharacterString>')
    elif re.search('2020 Census County and Equivalent',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2020 Census County and Equivalent State-based Shapefile</gco:CharacterString>')
    elif re.search('2010 Census County Subdivision',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2010 Census County Subdivision State-based Shapefile</gco:CharacterString>')
    elif re.search('2020 Census County Subdivision',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2020 Census County Subdivision State-based Shapefile</gco:CharacterString>')
    elif re.search('2010 Census Elementary School District',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2010 Census Elementary School District State-based Shapefile</gco:CharacterString>')
    elif re.search('2020 Census Elementary School District',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2020 Census Elementary School District State-based Shapefile</gco:CharacterString>')
    elif re.search('2010 Census Place State-based',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2010 Census Place  State-based Shapefile</gco:CharacterString>')
    elif re.search('2020 Census Place',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2010 Census Place  State-based Shapefile</gco:CharacterString>')
    elif re.search('2010 Census Secondary School District',Theme,flags=0):
        return('<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2010 Census Secondary School District State-based Shapefile</gco:CharacterString>')
    elif re.search('2020 Census Secondary School District', Theme, flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 TIGER/Line Shapefile 2020 Census Secondary School District State-based Shapefile</gco:CharacterString>')
    elif re.search('2010 Census  State and Equivalent',Theme, flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2010 TIGER/Line Shapefile 2010 Census  State and Equivalent State-based Shapefile</gco:CharacterString>')
    elif re.search('2020 Census  State and Equivalent',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 Census  State and Equivalent  State and Equivalent State-based Shapefile</gco:CharacterString>')
    elif re.search('2020 Census  SubMinor Civil Division',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 Census SubMinor Civil Division State-based Shapefile</gco:CharacterString>')
    elif re.search('2010 Census  Block',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2010 Census Block State-based Shapefile</gco:CharacterString>')
    elif re.search('2020 Census  Block',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 Census Block State-based Shapefile</gco:CharacterString>')
    elif re.search('2010 Census Tract',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2010 Census Tract State-based Shapefile</gco:CharacterString>')
    elif re.search('2010 Census  Census Tract', Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 Census Tract State-based Shapefile</gco:CharacterString>')
    elif re.search('2010 Census  Urban Growth Area (UGA)',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2010 Census  Urban Growth Area (UGA) State-based Shapefile</gco:CharacterString>')
    elif re.search('2010 Census  Urban Growth Area (UGA)',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2010 Census  Urban Growth Area (UGA) State-based Shapefile</gco:CharacterString>')
    elif re.search('UGA',Theme, flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 Census  Urban Growth Area (UGA) State-based Shapefile</gco:CharacterString>')
    elif re.search('2010 Census Unified School Districts', Theme, flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2010 Census Unified School Districts State-based Shapefile</gco:CharacterString>')
    elif re.search('2020 Census Unified School Districts',Theme, flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 Census Unified School Districts State-based Shapefile</gco:CharacterString>')
    elif re.search('VTD',Theme, flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 Census  Voting District State-based (VTD) State-based Shapefile</gco:CharacterString>')
    elif re.search('Current Consolidated City State-base', Theme, flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 Current Consolidated City State-base Shapefile</gco:CharacterString>')
    elif re.search('Current Elementary School Districts State-based',Theme, flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 Current Elementary School Districts State-based Shapefile</gco:CharacterString>')
    elif re.search('Current Estate State-based Shapefile', Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 Current Estate State-based Shapefile</gco:CharacterString>')
    elif re.search('Secondary School Districts Shapefile',Theme, flags=0):
        return ('<gco:CharacterString>Feature Catalog for the 2020 Secondary School Districts Shapefile</gco:CharacterString>')
    elif re.search('Current Subbarrio (Subminor Civil Division)',Theme,flags=0):
        return ('<gco:CharacterString>Feature Catalog for the Current Subbarrio (Subminor Civil Division) Shapefile</gco:CharacterString>')
    else:
        return '<gco:CharacterString> The theme is ' + Theme +'(eatitle)</gco:CharacterString>\n'