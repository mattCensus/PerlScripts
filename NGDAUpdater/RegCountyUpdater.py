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
from MetadataDateModules import metadataDateUpdater
from MetadataDateModules import TodaysDate
from FirstAlternativeTitle import FirstAlternativeTitle
from RestServiceFiller import RestServiceFiller
from WMSFiller import WMSFiller
from ThemeDir import ThemeDir
from EAFileFiller import EAFileFiller
from eaTitle import eaTitle
from FipsToState import Fips2StateName
from FipsToState import Fips2StateFips
from FipsToState import Fips2StateAbbr
from FileNameCorrector import FileNameCorrector

datesupdated = []
NewFileArray = []
NationalPlace = []
StateArray =[]
CountyArray=[]
DatesUpdated = 0
FileCounter = 0
EndDateStamp = 'no'

# getting today's date using the datetime module
#print('1. Getting the date')
time.sleep(5)
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

#path = 'C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2020files/PL2020/XMLFiles/CountyMetadataFiles/addrfn4'
path = 'C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2020files/FE2020/county/linearwater'
#C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020files\PL2020\XMLFiles\CountyMetadataFiles
#       C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020files\ver2\fe_2020\Regular\addr\tl_2020_41001_addr.shp.iso.xml
#     C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020files\ver2\fe_2020\stateNGDA\anrc\tl_2020_02_anrc.shp.iso.xml
# C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020 files\ver2\fe_2020\NationalNGDA
SeriesTheme=' Linear Hydrography County-based Shapefile'

configfiles = [os.path.join(dirpath, f)
               for dirpath, dirnames, files in os.walk(path)
               for f in files if f.endswith('.xml')]

#print('2 before the date stamp module')
#time.sleep(5)
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


#print('3: pre eaUrl module')
#time.sleep(5)
def eaUrl(Pass):
    Theme = Pass
    # print("Now in the eaUrl Module\n")
    # print("Now working on:" + Theme)
    EATheme = str(ThemeDir(Theme))
    FirstPartUrl = 'https://meta.geo.census.gov/data/existing/decennial/GEO/GPMB/TIGERline/'
    YearDir = 'TIGER2020'
    EAFileName = 'tl_2020_' + EATheme + '.shp.ea.iso.xml'
    FinalEaFile = FirstPartUrl + '/' + YearDir + "/" + EATheme + '/' + EAFileName + '\n'
    return FinalEaFile


if os.path.exists(path):
    print("The " + path + " directory exists")
    time.sleep(5)
else:
    print("Could not find " + path + ". Please make sure the path is correct")
    sys.exit(1)

#print('4: pre keywordCounter module')
time.sleep(5)
def keywordCounter(input):
    file = input
    KeywordModCounter = 0
    ReadFile = open(file, "r", encoding="utf8")
    for line in ReadFile:
        if re.search('<gmd:keyword>', line, flags=0):
            KeywordModCounter += 1
        else:
            continue
    FinalKeyword = KeywordModCounter - 3
    return FinalKeyword

#print('5: premain module')
#time.sleep(5)
for file in configfiles:
    transferOptionsCounter = 0
    linkageCounter = 0
    editionCounter = 0
    countyNamePos=0
    FileCounter += 1
    gmdDateCounter = 0
    USAbbrPos =0
    typeConter=0
    KeywordModCounter = 0
    descriptiveKeywordsCounter=0
    UnitedStatesPos=0
    StatePos=0
    StateFound ="No"
    KeywordGood = 'yes'
    keywordCounter = 0
    NationalPlace.clear()
    CountyArray.clear()
    StateArray.clear()
    nationalPlaceInd = 'no'
    keywordind = 'no'
    InCitInd = 'no'
    tateFound = 'No'
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
    dateCheck=0
    characterSetCounter=0
    purposeCounter=0
    displayCounter=0
    OutFile = preDot + "_corrected_" + postDot

    #print('6: Pre the Keyword counter')
    #time.sleep(5)

    ReadFileA = open(file, "r", encoding="utf8")

    #print('7: after the first opening')
    #time.sleep(5)
    displayCounter+=1
    if displayCounter==100:
        percentDone=(FileCounter/3234)*100
        print (str(percentDone) + "of the file have benn processed")
        percentDone=0
        displayCounter =0


    for line in ReadFileA:
        #
        #time.sleep(10)
        if re.search('<gmd:keyword>', line, flags=0):
            KeywordModCounter += 1
           #print('8: reading the lines for the first time' + line+ " at counter " + str())

        elif re.search('United States<',line, flags=0) and KeywordModCounter >1:
            UnitedStatesPos=KeywordModCounter
            USAbbrPos=UnitedStatesPos+1
            StatePos=UnitedStatesPos+4
            countyNamePos=UnitedStatesPos+3
           # print('Found the United States' + line + " at" + str(UnitedStatesPos) +' and ' + str(KeywordModCounter))
            if re.search('gco:CharacterString', line, flags=0):
                NationalPlace.append(line)
        elif KeywordModCounter == USAbbrPos and StateFound == 'No' and KeywordModCounter > 0:
            if re.search('gco:CharacterString', line, flags=0):
                NationalPlace.append(line)
        elif KeywordModCounter == countyNamePos and StateFound == 'No' and KeywordModCounter > 0:
            if re.search('gco:CharacterString', line, flags=0):
                CountyArray.append(line)
        elif KeywordModCounter == StatePos and StateFound =='No' and KeywordModCounter>0:
            #print ('Found the state' + line + " at " + str(StatePos))
            StateFound='yes'
            stateName = Fips2StateName(line)
            #print('The state is ' + str(stateName))
            if re.search('gco:CharacterString',line,flags=0):
                CountyArray.append(line)
                StateArray.append(Fips2StateName(line))
                StateArray.append(Fips2StateFips(line))
                StateArray.append(Fips2StateAbbr(line))
            #keywordind ='no'


        else:
            continue
    PrePlace =int(UnitedStatesPos-4)
    StateKeywords = UnitedStatesPos+4
    ReadFileA.close()
    CountyArray.sort

    # finalKeyword=int(keywordCounter(file))
    #print(' PrePlace' + str(PrePlace))
    #print('StateKeywords' + str(StateKeywords))

    #print("preDot: " + preDot)
    time.sleep(5)
    #print("PostDot: " + postDot)
    #
    #print("Outfile" + OutFile)
    #time.sleep(5)
    print("File: " + file)
    #time.sleep(5)
    #print("Now Working on: " + file)
    #print ("Outfile=" + OutFile)
    ReadFile = open(file, "r", encoding="utf8")
    with  open(OutFile, "w") as NewFile:
        for line in ReadFile:
            if re.search('gmd:linkage', line, flags=0):
                linkageCounter += 1
                # NewFile.write('<!-- if #1 -->\n')
                if linkageCounter == 1:
                    LinkageInd = 'yes'
                    NewFile.write(line)
                else:
                    NewFile.write(line)
            elif re.search('<gco:CharacterString>U.S. Department of Commerce, U.S. Census Bureau,',line,flags=0):
                NewFile.write(line)
            elif re.search('<gco:CharacterString>TIGER/Line Shapefile', line, flags=0):
                NewFile.write(line)
                FirstTitle = 'No'
                TitleEndCharacterString = 'yes'
                mainTitle = line
                lastComma = line.rfind(',') + 1
                if re.search('</gco:CharacterString>', line, flags=0):
                    closingTagLoc = line.find('</')
                    mainTheme = line[lastComma:closingTagLoc]
                else:
                    mainTheme = line[lastComma:]
            elif re.search('</gmd:characterSet>', line, flags=0):
                if characterSetCounter == 0:
                    NewFile.write(line)
                    NewFile.write('<gmd:parentIdentifier>\n')
                    NewFile.write(
                        '<gco:CharacterString>TIGER/Line Shapefile, Current, Series Information for the' + SeriesTheme + ' </gco:CharacterString>\n')
                    NewFile.write('</gmd:parentIdentifier>\n')
                    characterSetCounter += 1
                else:
                    NewFile.write(line)
            elif re.search('<gco:CharacterString>MAF/TIGER</gco:CharacterString>', line, flags=0):
                    # ind#1
                    NewFile.write(line)
                    MafTigerInd = 'yes'
                    #NewFile.write('<!-- MafTigerind: ' + MafTigerInd + ' -->\n')
            elif re.search('gmd:URL', line, flags=0):
                # NewFile.write('<!-- if #2 -->\n')
                print("---------------------------------\n")
                # print ("LinkageInd: " + LinkageInd + "\n")
                if LinkageInd == "yes":
                    # NewFile.write(line)
                    lastSlash = line.rfind("/tl") + 1
                    lastEndtag = line.find("</gmd:URL>")
                    ZipFileName = line[lastSlash: lastEndtag]
                    ThemeURL = str(ThemeDir(mainTheme))
                    '''
                    # NewFile.write('<!-- ZipFileName ' + ZipFileName + '-->')
                    #NewFile.write('<!-- ThemeURL' + ThemeURL + '-->')
                    '''
                    FinalZip = ' <gmd:URL>https://www2.census.gov/geo/tiger/TIGER2020/' + ThemeURL + '/' + ZipFileName + '</gmd:URL>\n'
                    LinkageInd = "No"
                    # print('In the LinkageId section\n')
                    # print(line)
                    # print ('ZipFileName: ' + ZipFileName)
                    LinkageInd = 'No'
                    # NewFile.write('<!--- What is going on here? -->')
                    NewFile.write(FinalZip)
                else:
                    NewFile.write(line)
            elif re.search('<gco:CharacterString>.shp.iso.xml', line, flags=0):
                RevFile = FileNameCorrector(file, OutFile)
                # NewFile.write('<!-- if #3 -->\n')
                NewFile.write(RevFile)
            elif re.search(' <gco:CharacterString>.iso.xml', line, flags=0):
                RevFile = FileNameCorrector(file, OutFile)
                # NewFile.write('<!-- if #3 -->\n')
                NewFile.write(RevFile)
            elif re.search('codeListValue=""', line, flags=0):
                # NewFile.write('<!-- if #4 -->\n')
                NewFile.write('                        codeListValue="dataset"/>')
            elif re.search('<gmd:MD_GeometricObjectTypeCode', line, flags=0):
                # NewFile.write('<!-- if #5 -->\n')
                lastCarrot = line.find('>') - 1
                maipart = line[0:lastCarrot]
                GMTC = maipart + '" codeListValue="complex">complex</gmd:MD_GeometricObjectTypeCode>'
                NewFile.write(GMTC)
            elif re.search('</gmd:featureTypes>', line, flags=0):
                # NewFile.write('<!-- if #6 -->\n')
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
                NewFile.write(
                    '                        <gmd:CI_DateTypeCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#CI_DateTypeCode" codeListValue="publication" codeSpace="002"/>\n')
                NewFile.write('                     </gmd:dateType>\n')
                NewFile.write('                  </gmd:CI_Date>\n')
                NewFile.write('               </gmd:date>\n')
                NewFile.write(
                    '               <gmd:citedResponsibleParty xlink:href="https://www.ngdc.noaa.gov/docucomp/1df27e57-4768-42de-909b-52f530601fba" xlink:title="U.S Department of Commerce, U.S Census Bureau, Geography Division (distributor)"/>')
                NewFile.write('              <gmd:otherCitationDetails>\n')
                EAFile = str(eaUrl(mainTheme))
                NewFile.write('                  <gco:CharacterString>' + EAFile + '</gco:CharacterString>\n')
                NewFile.write('               </gmd:otherCitationDetails>\n')
                NewFile.write('            </gmd:CI_Citation>\n')
                NewFile.write('        </gmd:featureCatalogueCitation>\n')



            elif re.search('</gmd:protocol>', line, flags=0):
                # NewFile.write('<!-- if #7 -->\n')

                if transferOptionsCounter == 0:
                    NewFile.write(line)
                    NewFile.write(' <gmd:applicationProfile>\n')
                    NewFile.write(' <gco:CharacterString>ZIP</gco:CharacterString>\n')
                    NewFile.write('</gmd:applicationProfile>\n')
                    NewFile.write('<gmd:name>\n')
                    NewFile.write('<gco:CharacterString>' + ZipFileName + '</gco:CharacterString>\n')
                    NewFile.write(' </gmd:name>\n')
                    NewFile.write('<gmd:description>\n')
                    NewFile.write(
                        ' <gco:CharacterString> This zip file contains the ' + file + ' shapefile </gco:CharacterString>\n')
                    NewFile.write('</gmd:description>\n')

                else:
                    NewFile.write(line)

            #elif re.search('</gmd:title>', line, flags=0):
                # NewFile.write('<!-- if #10 -->\n')
             #   if endTitleCounter == 0:
              #      endTitleCounter += 1
               # else:
                #    NewFile.write(line)


            elif re.search('</gco:CharacterString>', line, flags=0):
                # NewFile.write('<!-- if #11 TitleEndCharacterString:' + TitleEndCharacterString + '\n nationalPlaceInd: '  + nationalPlaceInd +'-->\n')
                if TitleEndCharacterString == 'yes':
                    #NewFile.write('<!-- 11az -->')
                    TitleEndCharacterString = 'no'
                    continue
                elif re.search('<gco:CharacterString>MAF/TIGER</gco:CharacterString>', line, flags=0):
                    # ind#2
                    NewFile.write(line)
                    MafTigerInd = 'yes'
                    # NewFile.write('<!-- MafTigerind: ' + MafTigerInd + ' -->\n')
                elif datasetUriind == 'yes':
                    doubleSlashLoc = line.find('//')
                    postSlash = line[doubleSlashLoc:]
                    newUrl = '<gco:CharacterString>https:' + postSlash
                    NewFile.write(newUrl)
                    datasetUriind = 'no'
                elif keywordind == 'yes':

                    continue
                elif InCitInd == 'yes':
                    InCitInd = 'no'
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



            elif re.search(' <gmd:edition>', line, flags=0):
                # NewFile.write('<!-- if #12 -->\n')
                NewFile.write(line)
                NewFile.write('                  <gco:CharacterString>2020</gco:CharacterString>')
            elif re.search('http://www2.census.gov/geo/tiger/TIGER2020', line, flags=0):
                # NewFile.write('<!-- if #13 -->\n')
                semiLoc = line.rfind(':')
                lastpart = line[semiLoc:]
                CorrectedHttp = '      <gco:CharacterString>https' + lastpart
                # NewFile.write('<!-- string corrected -->')


            elif re.search(' </gmd:edition>', line, flags=0):
                # NewFile.write('<!-- if #14 -->\n')
                editionCounter += 1
                # print('editionCounter: ' + str(editionCounter))
                if editionCounter == 1:
                    NewFile.write(line)
                    NewFile.write('              <gmd:identifier>\n')
                    NewFile.write('               <gmd:MD_Identifier>\n')
                    NewFile.write('                     <gmd:code>\n')
                    NewFile.write(
                        '                        <gco:CharacterString>https://www.census.gov</gco:CharacterString>\n')
                    NewFile.write('                        </gmd:code>\n')
                    NewFile.write('                  </gmd:MD_Identifier>\n')
                    NewFile.write('               </gmd:identifier>\n')
                else:
                    NewFile.write(line)
            elif re.search('<gmd:extent/>', line, flags=0):
                # NewFile.write('<!-- if #15 -->\n')
                NewFile.write('                <gmd:extent>\n')
                NewFile.write('                        <gml:TimePeriod gml:id="timePeriod">\n')
                NewFile.write('                           <gml:beginPosition>2019-06</gml:beginPosition>\n')
                NewFile.write('                           <gml:endPosition>2020-05</gml:endPosition>\n')
                NewFile.write('                       </gml:TimePeriod>\n')
                NewFile.write('                </gmd:extent>\n')
            elif re.search('</gmd:purpose>', line, flags=0):
                if purposeCounter == 0:
                    NewFile.write(line)
                    NewFile.write('<gmd:status>\n')
                    NewFile.write(
                        ' <gmd:MD_ProgressCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_ProgressCode" codeListValue="Completed">Completed</gmd:MD_ProgressCode>\n')
                    NewFile.write('</gmd:status>\n')
                    purposeCounter += 1
            elif re.search('<gml:beginPosition/>', line, flags=0):
                # NewFile.write('<!-- if #16 -->\n')
                NewFile.write('                           <gml:beginPosition>2019-06</gml:beginPosition>\n')
            elif re.search('<gml:endPosition/>', line, flags=0):
                # NewFile.write('<!-- if #17 -->\n')
                NewFile.write('                           <gml:endPosition>2020-05</gml:endPosition>\n')
            elif re.search('<gmd:keyword>', line, flags=0):
                # NewFile.write('<!-- if #18 -->\n')
                # NewFile.write('<!-- if #18' + line + '-->\n')
                keywordCounter += 1
                # print('00000000000000000000000000000000000000000000000000000')
                # print('keywordCounter: ' + str(keywordCounter))
                # print(line)
                #NewFile.write('<!--DescriptiveKeywordsInd: ' + DescriptiveKeywordsInd + ' Keyword counter: '+ str(keywordCounter)+ '  PrePlace:' + str( PrePlace)+ '-->\n')
                #keywordind = 'yes'
                if keywordCounter <   PrePlace:
                    #NewFile.write('<!--- should be inserted -->\n')
                    KeywordGood = 'yes'
                    NewFile.write(line)
                    DescriptiveKeywordsInd = 'off'

                else:
                    #NewFile.write('<!--- should be Notttttttttttttttttttttttttt be inserted -->\n')
                    keywordind = 'yes'
                    DescriptiveKeywordsInd = 'on'
            elif re.search('                 <gco:CharacterString>', line, flags=0):
                # NewFile.write('<!-- if #19 -->\n')
                #print(line)
                # print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
                # print ('keywordCounter: ' + str(keywordCounter))
                # print ('KeywordGood = ' + KeywordGood)
                # print('BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB')

                if re.search('>ANSI INCITS 38:2009', line, flags=0):
                    # newLine = line + '</gco:CharacterString>'
                    # (ANSI INCITS 38-2009), Federal Information Processing Series (FIPS) – States/State Equivalents'
                  continue
                elif re.search('<gco:CharacterString>MAF/TIGER</gco:CharacterString>', line, flags=0):
                    # ind#3
                    NewFile.write(line)
                    MafTigerInd = 'yes'
                    #NewFile.write('<!-- MafTigerind: ' + MafTigerInd + ' -->\n')
                elif typeConter == 2:
                    continue

                else:
                    NewFile.write(line)


            elif re.search('</gmd:keyword>', line, flags=0):
                # NewFile.write('<!-- if #20 -->\n')
                # print('Ending the keyword tag')
                if KeywordGood == 'no':
                    continue
                elif keywordind =='yes':
                    keywordind='no'
                    continue
                else:
                    NewFile.write(line)

            elif re.search('</gmd:descriptiveKeywords>', line, flags=0):

                # NewFile.write('<!-- if #21 -->\n')
                descriptiveKeywordsCounter+=1
                #ewFile.write('<!-- descriptiveKeywordsCounter(counterSection ' + str(descriptiveKeywordsCounter) + '-->')
                #NewFile.write(line)
                if descriptiveKeywordsCounter==2:
                    DescriptiveKeywordsInd = 'off'
                    #NewFile.write('<!-- The new keywords will go here!!!!! -->')
                    typeConter+=1
                    #county
                    NewFile.write('         <gmd:descriptiveKeywords>\n')
                    NewFile.write('            <gmd:MD_Keywords>\n')

                    for item in CountyArray:
                        #NewFile.write('<!-- item:' +  item + '-->\n')
                        if re.search('</gmd:keyword>',line, flags=0):
                            #NewFile.write('<!-- found the bad item-->\n')
                            continue
                        else:
                            NewFile.write('              <gmd:keyword>\n')
                            NewFile.write(item)
                            NewFile.write('              </gmd:keyword>\n')
                    NewFile.write('               <gmd:type>\n')
                    NewFile.write('                  <gmd:MD_KeywordTypeCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_KeywordTypeCode"\n')
                    NewFile.write('                                         codeListValue="place"/>\n')
                    NewFile.write('              </gmd:type>\n')
                    NewFile.write('              <gmd:thesaurusName>\n')
                    NewFile.write('                  <gmd:CI_Citation>\n')
                    NewFile.write('                     <gmd:title>\n')
                    NewFile.write('                       <gco:CharacterString>National Standard Codes (ANSI INCITS 31-2009), Federal Information Processing Series (FIPS) - Counties/County Equivalents</gco:CharacterString>\n')
                    NewFile.write('                    </gmd:title>\n')
                    NewFile.write('                     <gmd:date gco:nilReason="unknown"/>')
                    NewFile.write('                  </gmd:CI_Citation>\n')
                    NewFile.write('              </gmd:thesaurusName>\n')
                    NewFile.write('            </gmd:MD_Keywords>\n')
                    NewFile.write('         </gmd:descriptiveKeywords>\n')


                    #state
                    NewFile.write('         <gmd:descriptiveKeywords>\n')
                    NewFile.write('            <gmd:MD_Keywords>\n')
                    for item in StateArray:
                        if re.search('</gmd:keyword>',line, flags=0):
                            continue
                        else:
                            NewFile.write('              <gmd:keyword>\n')
                            finalItem ='                 <gco:CharacterString>' + item + '</gco:CharacterString>\n'
                            NewFile.write(finalItem)
                            NewFile.write('              </gmd:keyword>\n')
                    NewFile.write('               <gmd:type>\n')
                    NewFile.write('                  <gmd:MD_KeywordTypeCode codeList="http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_KeywordTypeCode"\n')
                    NewFile.write('                                         codeListValue="place"/>\n')
                    NewFile.write('              </gmd:type>\n')
                    NewFile.write('              <gmd:thesaurusName>\n')
                    NewFile.write('                  <gmd:CI_Citation>\n')
                    NewFile.write('                     <gmd:title>\n')
                    NewFile.write(
                        '                       <gco:CharacterString>National Standard Codes (ANSI INCITS 38-2009), Federal Information Processing Series (FIPS) – States/State Equivalents</gco:CharacterString>\n')
                    NewFile.write('                    </gmd:title>\n')
                    NewFile.write('                     <gmd:date gco:nilReason="unknown"/>')
                    NewFile.write('                  </gmd:CI_Citation>\n')
                    NewFile.write('              </gmd:thesaurusName>\n')
                    NewFile.write('            </gmd:MD_Keywords>\n')
                    NewFile.write('         </gmd:descriptiveKeywords>\n')


                    #nation
                    NewFile.write('         <gmd:descriptiveKeywords>\n')
                    NewFile.write('            <gmd:MD_Keywords>\n')
                    for item in  NationalPlace:
                        if len(item)>0:
                            if re.search('</gmd:keyword>', line, flags=0):
                                continue
                            else:
                                NewFile.write('              <gmd:keyword>\n')
                                NewFile.write(item)
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
                    NewFile.write('                     <gmd:date gco:nilReason="unknown"/>')
                    NewFile.write('                  </gmd:CI_Citation>\n')
                    NewFile.write('              </gmd:thesaurusName>\n')
                    NewFile.write('            </gmd:MD_Keywords>\n')
                    NewFile.write('         </gmd:descriptiveKeywords>\n')



                else:
                    NewFile.write(line)
            elif re.search('<gmd:descriptiveKeywords>',line,flags=0):
                #NewFile.write('<!-- descriptiveKeywordsCounter (at opening tag)' + str(descriptiveKeywordsCounter) + '-->\n')
                if descriptiveKeywordsCounter > 0:
                    DescriptiveKeywordsInd = 'on'
                else:
                    NewFile.write(line)
            elif re.search('<gmd:MD_Keywords>',line,flags=0):
                #NewFile.write('<!--DescriptiveKeywordsInd (keywords11111111111)' + DescriptiveKeywordsInd + 'typeConter '+ str(typeConter) + '-->\n')
                if typeConter == 1:
                    continue
                else:
                    NewFile.write(line)
            elif re.search('<gmd:dataSetURI>', line, flags=0):
                datasetUriind = 'yes'
                NewFile.write(line)
            elif re.search('ANSI INCITS 31:2009', line, flags=0):
                # NewFile.write('<!--ANSI INCITS 31:2009 -->\n')
                InCitInd = 'yes'
                continue
            elif re.search('(Formerly FIPS 8-6)', line, flags=0):
                # NewFile.write('<!--ANSI INCITS 31:2009 -->\n')
                continue

            elif re.search('<gmd:date', line, flags=0):
                #NewFile.write('<!-- In the Dateeeeeeeeeeeeee) type counter = ' + str(typeConter) + '-->/n')
                if re.search('<gmd:date gco:nilReason="unknown"/>', line, flags=0):
                    #NewFile.write('<!-- In the Dateeeeeeeeeeeeee) type counter = ' + str(typeConter) + '-->\n')
                    if typeConter == 2:
                        continue
                    else:
                        NewFile.write(line)
                elif MafTigerInd == 'yes':
                    dateCheck+=1
                    if dateCheck <2:
                        NewFile.write(' <gmd:date gco:nilReason="unknown"/>')
                    #NewFile.write('<!-- date check-->\n')
                    #MafTigerInd = 'no'
                else:
                    NewFile.write(line)
            elif re.search('<gmd:CI_Date>', line, flags=0):
                if MafTigerInd == 'yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('<gco:Date>Unpublished material</gco:Date>', line, flags=0):
                if MafTigerInd == 'yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('</gmd:date>', line, flags=0):
                if MafTigerInd == 'yes':
                    gmdDateCounter += 1
                    if gmdDateCounter == 1:
                        continue
                    else:
                        MafTigerInd = 'no'
                else:
                    NewFile.write(line)
            elif re.search('<gmd:dateType>', line, flags=0):
                if MafTigerInd == 'yes':
                    continue
                elif  typeConter == 2:
                    continue
                else:
                    NewFile.write(line)
            elif re.search(' <gmd:CI_DateTypeCode', line, flags=0):
                if MafTigerInd == 'yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('codeListValue="publication date"', line, flags=0):
                if MafTigerInd == 'yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('</gmd:CI_DateTypeCode>', line, flags=0):
                if MafTigerInd == 'yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('</gmd:dateType>', line, flags=0):
                if MafTigerInd == 'yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('</gmd:CI_Date>', line, flags=0):
                if MafTigerInd == 'yes':
                    continue
                else:
                    NewFile.write(line)
            elif re.search('<gmd:type>',line,flags=0):
                typeConter+=1
                if typeConter ==2:
                    continue
                else:
                    NewFile.write(line)
            elif re.search('<gmd:MD_KeywordTypeCode',line,flags=0):
                if typeConter ==2:
                    continue
                else:
                    NewFile.write(line)
            elif re.search('odeListValue="place"/>',line,flags=0):
                if typeConter ==2:
                    continue
                else:
                    NewFile.write(line)
            elif re.search(' </gmd:type>',line,flags=0):
                if typeConter == 2:
                    continue
                else:
                    NewFile.write(line)
            elif re.search('<gmd:thesaurusName>',line,flags=0):
                if typeConter == 2:
                    continue
                else:
                    NewFile.write(line)
            elif re.search('gmd:CI_Citation',line,flags=0):
                if typeConter == 2:
                    continue
                else:
                    NewFile.write(line)
            elif re.search('gmd:title',line,flags=0):
                if typeConter == 2:
                    continue
                else:
                    NewFile.write(line)
            elif re.search ('</gmd:CI_Citation>',line,flags=0):
                if typeConter == 2:
                    continue
                else:
                    NewFile.write(line)
            elif re.search('</gmd:thesaurusName>',line,flags=0):
                if typeConter == 2:
                    continue
                else:
                    NewFile.write(line)
            elif re.search('</gmd:MD_Keywords>',line,flags=0):
                if typeConter == 2:
                    continue
                else:
                    NewFile.write(line)

            else:
                NewFile.write(line)
            # print(line)
    NewFileArray.append(OutFile)
    NewFile.close()
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n")

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