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
These modules takes the fips codes and turn them into a State Code, State Name and State Postal Abbreviation.
It consists of the following modules:
Fips2StateFips: Takes a county fips code and turns it into a state FIPS Code
Fips2StateName: Takes a county fips code and turns it into a state Name
Fips2StateAbbr: Takes a county fips code and turns it into a state Postal Abbreviation
  
'''

'''
Alabama 	            01 	AL
Alaska 	                02 	AK
Arizona 	            04 	AZ
Arkansas 	            05 	AR
California 	            06 	CA
Colorado 	            08 	CO
Connecticut             09 	CT
Delaware 	            10 	DE
District of Columbia 	11 	DC
Florida 	            12 	FL
Georgia 	            13 	GA
Hawaii 	                15 	HI
Idaho 	                16 	ID
Illinois 	            17 	IL
Indiana 	            18 	IN
Iowa 	                19 	IA
Kansas 	                20 	KS
Kentucky 	            21 	KY
Louisiana 	            22 	LA
Maine 	                23 	ME
Maryland 	            24 	MD
Massachusetts 	        25 	MA
Michigan 	            26 	MI
Minnesota 	            27 	MN
Mississippi 	        28 	MS
Missouri 	            29 	MO
Montana 	            30 	MT
Nebraska 	            31 	NE
Nevada 	                32 	NV
New Hampshire 	        33 	NH
New Jersey 	            34 	NJ
New Mexico 	            35 	NM
New York 	            36 	NY
North Carolina 	        37 	NC
North Dakota 	        38 	ND
Ohio 	                39 	OH
Oklahoma 	            40 	OK
Oregon 	                41 	OR
Pennsylvania 	        42 	PA
Rhode Island 	        44 	RI
South Carolina 	        45 	SC
South Dakota 	        46 	SD
Tennessee 	            47 	TN
Texas 	                48 	TX
Utah 	                49 	UT
Vermont 	            50 	VT
Virginia 	            51 	VA
Washington 	            53 	WA
West Virginia 	        54 	WV
Wisconsin 	            55 	WI
Wyoming 	            56 	WY

American Samoa 	                                60 	AS 	1
Federated States of Micronesia               	64 	FM 	3
Guam 	                                        66 	GU 	1
Marshall Islands 	                            68 	MH 	3
Commonwealth of the Northern Mariana Islands 	69 	MP 	1
Palau 	                                        70 	PW 	3
Puerto Rico 	                                72 	PR 	1
U.S. Minor Outlying Islands 	                74 	UM 	2
U.S. Virgin Islands 	                        78 	VI 	1

'''

def Fips2StateFips(line):
    County=line
    posCount=County.find('>')+1
    lastCarrot=County.rfind('<')-1
    #print ('county' + County)
    #print('posCount' + str(posCount))
    StateFips=line[posCount:lastCarrot]
    #print('stateFips: ' + StateFips)
    State = StateFips[0:2]
    #print ('The state fips code is ' + str(State))
    return State

def Fips2StateName(line):
    County=line
    posCount=County.find('>')+1
    lastCarrot=County.rfind('<')-1
    #print ('county' + County)
    #print('posCount' + str(posCount))
    StateFips=line[posCount:lastCarrot]
    #print('stateFips: ' + StateFips)
    State = StateFips[0:2]
    #print ('The state fips code is ' + str(State))
    if State == ' 01':
        return 'Alabama'
    elif State == '02':
        return 'Alaska'
    elif State =='04':
        return 'Arizona'
    elif State == '05':
        return 'Arkansas '
    elif State == '06 ':
        return'California'
    elif State == '08':
        return'Colorado'
    elif  State =='09':
        return 'Connecticut'
    elif State =='10':
        return 'Delaware '
    elif State =='11':
        return'District of Columbia '
    elif State =='12':
        return 'Florida '
    elif State =='13':
        return 'Georgia'
    elif State ==' 15':
        return 'Hawaii'
    elif State== '16':
        return 'Idaho '
    elif State == '17':
        return 'Illinois'
    elif State =='18':
        return'Indiana'
    elif State =='19':
        return 'Iowa'
    elif State =='20':
        return 'Kansas'
    elif State == '21':
        return 'Kentucky'
    elif State == '22':
        return 'Louisiana'
    elif State == '23':
        return 'Maine'
    elif State == '24':
        return 'Maryland'
    elif State =='25':
        return 'Massachusetts'
    elif State == '26':
        return 'Michigan'
    elif State == '27':
        return 'Minnesota'
    elif State == '28':
        return 'Mississippi'
    elif State == '29':
        return 'Missouri'
    elif State =='30':
        return 'Montana'
    elif State == '31' :
        return 'Nebraska'
    elif State =='32':
        return  'Nevada'
    elif State == '33':
        return 'New Hampshire'
    elif State == '34':
        return 'New Jersey'
    elif State == '35':
        return 'New Mexico'
    elif State == '36':
        return 'New York'
    elif State =='37':
        return 'North Carolina'
    elif State == '38':
        return 'North Dakota'
    elif State == '39':
        return 'Ohio'
    elif State == '40':
        return  'Oklahoma'
    elif State == '41':
        return 'Oregon'
    elif State == '42':
        return 'Pennsylvania'
    elif State == '44':
        return 'Rhode Island'
    elif State == '45':
        return  'South Carolina'
    elif State == '46':
        return 'South Dakota'
    elif State == '47':
        return 'Tennessee'
    elif State == '48':
        return  'Texas'
    elif State == '49':
        return 'Utah'
    elif State == '50':
        return 'Vermont'
    elif State == '51':
        return 'Virginia'
    elif State == '53':
        return 'Washington'
    elif State == '54':
        return 'West Virginia'
    elif State == '55':
        return 'Wisconsin'
    elif State =='56':
        return 'Wyoming'
    elif State == '60':
        return 'American Samoa'
    elif State == '64':
        return 'Federated States of Micronesia'
    elif  State == '66':
        return 'Guam '
    elif State =='68':
        return 'Marshall Islands'
    elif State =='69':
        return 'Commonwealth of the Northern Mariana Islands'
    elif State == '70':
        return 'Palau'
    elif State == '72':
        return 'Puerto Rico'
    elif State == '74':
        return 'U.S. Minor Outlying Islands'
    elif State == '78':
        return 'U.S. Virgin Islands'
    else:
        return'Bad State: ' + State


def Fips2StateAbbr(line):
    County=line
    posCount=County.find('>')+1
    lastCarrot=County.rfind('<')-1
    #print ('county' + County)
    #print('posCount' + str(posCount))
    StateFips=line[posCount:lastCarrot]
    #print('stateFips: ' + StateFips)
    State = StateFips[0:2]
    #print ('The state fips code is ' + str(State))
    if State == ' 01':
        return 'AL'
    elif State == '02':
        return 'AK'
    elif State =='04':
        return 'AZ'
    elif State == '05':
        return 'AR'
    elif State == '06 ':
        return'CA'
    elif State == '08':
        return'CO'
    elif  State =='09':
        return 'CT'
    elif State =='10':
        return 'DE'
    elif State =='11':
        return'DC'
    elif State =='12':
        return 'FL'
    elif State =='13':
        return 'GA'
    elif State ==' 15':
        return 'HI'
    elif State== '16':
        return 'ID'
    elif State == '17':
        return 'IL'
    elif State =='18':
        return'IN'
    elif State =='19':
        return 'IA'
    elif State =='20':
        return 'KS'
    elif State == '21':
        return 'KY'
    elif State == '22':
        return 'LA'
    elif State == '23':
        return 'ME'
    elif State == '24':
        return 'MD'
    elif State =='25':
        return 'MA'
    elif State == '26':
        return 'MI'
    elif State == '27':
        return 'MN'
    elif State == '28':
        return 'MS'
    elif State == '29':
        return 'MO'
    elif State =='30':
        return 'MT'
    elif State == '31' :
        return 'NE'
    elif State =='32':
        return  'NV'
    elif State == '33':
        return 'NH'
    elif State == '34':
        return 'NJ'
    elif State == '35':
        return 'NM'
    elif State == '36':
        return 'NY'
    elif State =='37':
        return 'NC'
    elif State == '38':
        return 'ND'
    elif State == '39':
        return 'OH'
    elif State == '40':
        return  'OK'
    elif State == '41':
        return 'OR'
    elif State == '42':
        return 'PA'
    elif State == '44':
        return 'RI'
    elif State == '45':
        return  'SC'
    elif State == '46':
        return 'SD'
    elif State == '47':
        return 'TN'
    elif State == '48':
        return  'TX'
    elif State == '49':
        return 'UT'
    elif State == '50':
        return 'VT'
    elif State == '51':
        return 'VA'
    elif State == '53':
        return 'WA'
    elif State == '54':
        return 'WV'
    elif State == '55':
        return 'WI'
    elif State =='56':
        return 'WY'
    elif State == '60':
        return 'AS'
    elif State == '64':
        return 'FM'
    elif  State == '66':
        return 'GU '
    elif State =='68':
        return 'MH'
    elif State =='69':
        return 'MP'
    elif State == '70':
        return 'PW'
    elif State == '72':
        return 'PR'
    elif State == '74':
        return 'UM'
    elif State == '78':
        return 'VI'
    else:
        return'Bad State: ' + State