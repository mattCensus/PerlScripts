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
from FirstAlternativeTitle import FirstAlternativeTitle
from RestServiceFiller import RestServiceFiller
from WMSFiller import WMSFiller
from ThemeDir import ThemeDir
from EAFileFiller import EAFileFiller
from eaTitle import eaTitle
from FileNameCorrector import FileNameCorrector
from RestServiceFiller import restExist
from FileNameCorrector import RealfileName

# this takes a batch produced file and makes it adhere to the latest FGDC Guidelines

datesupdated = []
NewFileArray = []
NationalPlace = []
StateArray =[]
CountyArray=[]
DatesUpdated = 0
FileCounter = 0
EndDateStamp = 'no'
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

path='C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2020files/FE2020/National/zcta510'

#     C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020files\FE2020\National\aiannh
#     C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020files\ver2\fe_2020\stateNGDA\anrc\tl_2020_02_anrc.shp.iso.xml
# C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020 files\ver2\fe_2020\NationalNGDA
#C:\Users\mattp\Desktop\WorkFiles\XMLFiles\2020files\FE2020\National\aiannh

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


def eaUrl(Pass):
    Theme = Pass
    #print("Now in the eaUrl Module\n")
    #print("Now working on:" + Theme)
    EATheme = str(ThemeDir(Theme))
    FirstPartUrl='https://meta.geo.census.gov/data/existing/decennial/GEO/GPMB/TIGERline/'
    YearDir='fe_2020'
    EAFileName='tl_2020_' + EATheme + '.shp.ea.iso.xml'
    FinalEaFile= FirstPartUrl + '/' + YearDir + "/" + EATheme + '/' + EAFileName +'\n'
    return FinalEaFile


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


#ReadFile.close()
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
                    ZipDot=ZipFileName.find('.')
                    preZIP=ZipFileName[0:ZipDot]
                    DescFile= preZIP+ '.shp.iso.xml'
                    NewFile.write('<gmd:description>\n')
                    NewFile.write(' <gco:CharacterString> This zip file contains the ' + DescFile + ' shapefile </gco:CharacterString>\n')
                    NewFile.write('</gmd:description>\n')

                else:
                    NewFile.write(line)

            elif re.search('<gco:CharacterString>TIGER/Line Shapefile',line,flags=0):
                #NewFile.write('<!-- if #8 -->\n')
                if FirstTitle == 'Yes':
                    FirstTitle = 'No'
                    TitleEndCharacterString = 'yes'
                    mainTitle = line
                    lastComma = line.rfind(',') + 1
                    if re.search('</gco:CharacterString>', line, flags=0):
                        # NewFile.write('<!-- Stop5a -->')
                        closingTagLoc = line.find('</')
                        mainTheme = line[lastComma:closingTagLoc]
                    else:
                        mainTheme = line[lastComma:]
                    Geography = line[68:lastComma - 1]
                    # print ('Geography:' +  Geography)
                    PrimaryAlternateTitle = '<gco:CharacterString>TIGER/Line Shapefile, Current, ' + Geography + mainTheme + '</gco:CharacterString>\n'
                    # NewFile.write('<!-- Stop5b -->')

                    NewFile.write(PrimaryAlternateTitle)
                    # NewFile.write('<!-- Check 1 -->\n')

                    NewFile.write('</gmd:title>\n')
                    NewFile.write(' <gmd:alternateTitle>\n')
                    if re.search('</gco:CharacterString>', mainTitle, flags=0):
                        # NewFile.write('<!-- Stop6 -->')
                        NewFile.write(mainTitle)
                    else:
                        NewFile.write(mainTitle + '</gco:CharacterString>')
                    NewFile.write(' </gmd:alternateTitle>\n')
                    FirstAlternativeTitle
                    FirstAlternativeTitle(mainTheme, NewFile)
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
                    WMSFiller(mainTheme, NewFile)
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
                    EAFileFiller(mainTheme, NewFile)
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



           # elif re.search(' <gmd:edition>',line,flags=0):
                #NewFile.write('<!-- if #12 -->\n')
            #    NewFile.write(line)
             #   NewFile.write('                  <gco:CharacterString>2020</gco:CharacterString>')
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
            elif re.search(' codeListValue="download!!!!!">download!!!',line,flags=0):
                NewFile.write('codeListValue="download">download')











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
NewFile.close()
sys.exit(1)