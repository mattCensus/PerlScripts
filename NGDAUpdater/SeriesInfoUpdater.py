import os
import fnmatch
import shutil
import re
import datetime
import time
# import StringIO
import pickle
import sys
import MetadataDateModules
from MetadataDateModules import metadataDateUpdater
from MetadataDateModules import TodaysDate
from FirstAlternativeTitle import FirstAlternativeTitle
from RestServiceFiller import RestServiceFiller
from WMSFiller import WMSFiller
from ThemeDir import ThemeDir
from EAFileFiller import EAFileFiller
from eaTitle import eaTitle
from FileNameCorrector import FileNameCorrector
from RestServiceFiller import restExist
from FileNameCorrector import RealfileName

datesupdated = []
NewFileArray = []
NationalPlace = []
DatesUpdated = 0
FileCounter = 0
EndDateStamp = 'no'

# getting today's date using the datetime module
PresentDate = datetime.datetime.now()
PresentDate.day

if PresentDate.hour > 12:
    PresentHour = PresentDate.hour - 12
    AmPm = 'PM"'
else:
    PresentHour = PresentDate.hour
    AmPm = 'AM'

presentTime = str(PresentHour) + ":" + str(PresentDate.minute) + ":" + str(PresentDate.second) + AmPm

if PresentDate.day < 10:
    day = "0" + str(PresentDate.day)
else:
    day = PresentDate.day

if PresentDate.month < 10:
    month = "0" + str(PresentDate.month)
else:
    month = PresentDate.month

PresentDate2 = str(PresentDate.year) + "-" + str(month) + "-" + str(day)

path = 'C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2020files/PL2020/XMLFiles/CountyMetadataFiles/addr'
#file:/C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2020files/FE2020/StatesNew/arealm/
# C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020files\PL2020\XMLFiles\stateMetadataFiles\aiannh10
#     C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020files\ver2\fe_2020\stateNGDA\anrc\tl_2020_02_anrc.shp.iso.xml
# C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020 files\ver2\fe_2020\NationalNGDA
SeriesTheme='Address Ranges County-based Relationship File'

if os.path.exists(path):
    print("The " + path + " directory exists")
else:
    print("Could not find " + path + ". Please make sure the path is correct")
    sys.exit(1)

configfiles = [os.path.join(dirpath, f)
               for dirpath, dirnames, files in os.walk(path)
               for f in files if f.endswith('.xml')]


def DateStampMod(DateStampInd, CurrentDate, ContentIfoInd):
    print('Now working on ' + CurrentDate)
    if ContentIfoInd == 'yes':
        NewFile.write(line)
        EndDateStamp = 'No'
        return EndDateStamp
    elif DateStampInd == 'yes':
        NewFile.write('<gco:Date>' + PresentDate2 + '</gco:Date>\n')
        NewFile.write('</gmd:dateStamp>')
        EndDateStamp = 'No'
        return EndDateStamp
    else:
        NewFile.write('<gmd:dateStamp>')
        NewFile.write('<gco:Date>' + PresentDate2 + '</gco:Date>\n')
        NewFile.write('</gmd:dateStamp>')
        EndDateStamp = 'No'
        return EndDateStamp


def eaUrl(Pass):
    Theme = Pass
    # print("Now in the eaUrl Module\n")
    # print("Now working on:" + Theme)
    EATheme = str(ThemeDir(Theme))
    FirstPartUrl = 'https://meta.geo.census.gov/data/existing/decennial/GEO/GPMB/TIGERline/'
    YearDir = 'Tiger2020'
    EAFileName = 'tl_2020_' + EATheme + '.shp.ea.iso.xml'
    FinalEaFile = FirstPartUrl + '/' + YearDir + "/" + EATheme + '/' + EAFileName + '\n'
    return FinalEaFile


if os.path.exists(path):
    print("The " + path + " directory exists")
else:
    print("Could not find " + path + ". Please make sure the path is correct")
    sys.exit(1)


def keywordCounter(input):
    file = input
    KeywordModCounter = 0
    ReadFile = open(file, "r")
    for line in ReadFile:
        if re.search('<gmd:keyword>', line, flags=0):
            KeywordModCounter += 1
        else:
            continue
    FinalKeyword = KeywordModCounter - 3
    return FinalKeyword


for file in configfiles:
    transferOptionsCounter = 0
    linkageCounter = 0
    editionCounter = 0
    FileCounter += 1
    gmdDateCounter = 0
    KeywordModCounter = 0
    KeywordGood = 'yes'
    keywordCounter = 0
    NationalPlace.clear()
    nationalPlaceInd = 'no'
    keywordind = 'no'
    InCitInd = 'no'
    TitleEndCharacterString = 'no'
    DescriptiveKeywordsInd = 'off'
    MafTigerInd = 'no'
    dotLocation = file.find(".")
    preDot = file[0:dotLocation]
    postDot = file[dotLocation:]
    ContentIfoInd = 'no'
    FirstTitle = 'Yes'
    endTitleCounter = 0
    datasetUriind = 'no'
    OutFile = preDot + "_corrected_" + postDot
    characterSetCounter = 0

    # finalKeyword=int(keywordCounter(file))
    #print(' PrePlace' + str(PrePlace))
    #print('StateKeywords' + str(StateKeywords))

    print("preDot: " + preDot)
    time.sleep(5)
    print("PostDot: " + postDot)
    time.sleep(5)
    print("Outfile" + OutFile)
    time.sleep(5)
    print("File: " + file)
    time.sleep(5)
    print("Now Working on: " + file)
    time.sleep(5)
    print ("Outfile=" + OutFile)
    time.sleep(5)
    ReadFile = open(file, "r", encoding="utf8")
    with  open(OutFile, "w", encoding="utf8") as NewFile:
        for line in ReadFile:
            if re.search('</gmd:characterSet>', line, flags=0):
                if characterSetCounter == 0:
                    NewFile.write(line)
                    NewFile.write('<gmd:parentIdentifier>\n')
                    NewFile.write(
                        '<gco:CharacterString>TIGER/Line Shapefile, 2020, Series Information for the' + SeriesTheme + ' </gco:CharacterString>\n')
                    NewFile.write('</gmd:parentIdentifier>\n')
                    characterSetCounter += 1
                else:
                    NewFile.write(line)
            else:
                NewFile.write(line)

for newFile in NewFileArray:
    # print (newFile)
    newFileCorrectLoc = newFile.find('_corrected')
    preCorret = newFile[0:newFileCorrectLoc]
    postCorrect = newFile[newFileCorrectLoc + 11:]
    DestFile = preCorret + postCorrect
    # print(preCorret)
    # print (postCorrect)
    shutil.copyfile(newFile, DestFile)
    # newFile.close

'''
for newFile in NewFileArray:
    os.remove(newFile)
'''

print("Done! " + str(FileCounter) + " files have been processed at " + presentTime + "!")

sys.exit(1)