# importing necessary modules
import requests, zipfile
from io import BytesIO
print('Downloading started')
import time
import sys
import os
import fnmatch
import shutil
import re
import time
import datetime
import time
#import StringIO
import pickle


def url_checker(url):
    get = requests.get(url)
    URLReport.write('get'+ str(get)+ '\n')
    if get.status_code==200:
        return ("Yes")
    elif get.status_code == 404:
        #URLReport.write('get'+ str(get)+ '\n')
        return ("No")
    elif get.status_code == 11001:
        #URLReport.write('get'+ str(get)+ '\n')
        return ("No")
    else:
        return ("No")

def filenameHeader(CurrentFile, previousFileA):
    if CurrentFile == "New":
        #CurrentFile = fileB
        lastSlashFile = CurrentFile.rfind("\\") + 1
        BaseFile = CurrentFile[lastSlashFile:]
        #print('New')
        URLReport.write("-----Incorrect URLS for " + BaseFile + "(New)----------\n")
    elif CurrentFile == previousFileA:
        print('Still working on the same file')
    else:
        #print('else')
        CurrentFile = fileB
        lastSlashFile = CurrentFile.rfind("\\") + 1
        BaseFile = CurrentFile[lastSlashFile:]
        URLReport.write("-----Incorrect URLS for " + BaseFile + " ----------\n")

def PreviousFileDeterminer(CurrentFile):
    #print ("Determing the previos file")
    #print ('Currentfile:' + CurrentFile)
    lastSlashFile = CurrentFile.rfind("\\") + 1
    BaseFile = CurrentFile[lastSlashFile:]
    #print ("Basefile: " + BaseFile)
    return BaseFile





path="C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/sldu"
OutPath="C:/Users/mattp/Desktop/WorkFiles/MissingUrlReport"
ReportCounter=0
CurrentFile="New"
PrevFile=''
loopCounter=0
indCounter=0
gcoBracketType=""
doubleSlashInd= "No"
xlinkTitlInd= "No"
geoPlatformInd= "No"
doubleInd= "No"

lastslash=path.rfind("/")+1
theme=path[lastslash:]
#print ('theme: ' + theme )
newPath= path[0:lastslash-1]
#print ('newPath:' + newPath)
lastslash2=newPath.rfind("/")+1
Year=newPath[lastslash2:]
#print ("Year: " + Year)

ReportFile ="MissingURLs_" + Year +"_" + theme + ".txt"
ReportFileFull = OutPath + "/" + ReportFile

ExcessEA='EXCESSEADir'
EsxcessEADir=path + "//" +ExcessEA
countFiles=0

if os.path.exists(path):
    print ("1: The " + path + " directory exists")
else:
    print ("2: Could not find " + path + ". Please make sure the path is correct")
    #exit(1)

#create a list  or an array. This array uses the os.path modules, part of the os modules
#os.path.join joins or merges one or more path components
#os.walk

configfiles =[os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.endswith('.xml')]
pathName =os.path.dirname(path)
#print (pathName)

URLReport=open(ReportFileFull,"w")
URLReport.write("The following URLs are invalid for the " + Year+ ' _ ' + theme+ "Tiger/Line files.\n\n")
time.sleep(10)

#print ("pre loop")
for fileA in configfiles:
    #print("fileA is : " + fileA)
    loopCounter+=1
    indCounter+=1
    if indCounter == 30:
        perDone=loopCounter/3200
        indCounter=0
        PerDoneFormat= "{:.2f}".format(perDone)
        print (str(PerDoneFormat)+ " of the files Have been Proccessed")


    fileB=os.path.basename(fileA)
    ReadFile = open(fileA, "r", encoding='utf-8')

    for line in ReadFile:

        if re.search("http",line, flags=0):
            #print('line:' + line)
            if re.search('codeList=',line, flags=0):
                #print('line:' + line)
                codelistLoc=line.find('codeList=')+10

                URLA=line[codelistLoc:]

                #print ("Line is" + line)
                #print ("URLA is " + URLA)
                URLALength=len(URLA)-5
                #print ("URALength:" + str(URLALength))

                URLB =URLA[0:URLALength]
                if re.search('#',URLB,flags=0):
                    hashLoc=URLB.find('#')
                    URL=URLB[0:hashLoc]
                else:
                    URL=URLB
                #print ("                    URL: " + URL)
                result=url_checker(URL)

                if result == "No":
                    URLReport.write ("result (for codelist)("+ URL+ ") : " + result +"\n")
                    ReportCounter += 1
                    URLReport.write('ReportCounter #5')
                    print('ReportCounter #5')
                    filenameHeader(fileB, PrevFile)
                    PrevFile = PreviousFileDeterminer(fileB)
                    URLReport.write("       result: " + result +"\n")
                    URLReport.write("       In the codelist\n")
                    URLReport.write("\t"+ str(ReportCounter)+ ":" + line + "\n")
                    URLReport.write('-------------------\n')

            elif re.search('xmlns', line, flags=0):

                equalLocation=line.find("=")+2
                URLA=line[equalLocation:]

                if re.search('>',URLA,flags=0):
                    URLALength = len(URLA) - 3
                else:
                    URLALength=len(URLA)-2

                #URLALength=URLA.rfind("\"")
                URL=URLA[0:URLALength]
                #print ("URL:" + URL)
                result = url_checker(URL)
                #print ("Get the result")

                if result == "No":

                    ReportCounter +=1
                    URLReport.write('ReportCounter #1')
                    print('ReportCounter #1')
                    filenameHeader(fileB, PrevFile)
                    PrevFile = PreviousFileDeterminer(fileB)
                    #URLReport.write('in the XMLNsxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                    #URLReport.write("URLA: " + URLA)
                    #URLReport.write('URLALength: ' +str(URLALength)+ '\n')
                    URLReport.write( "\t"+  str(ReportCounter) + ":" + URL + "(In the xmlns) \n")
                    #URLReport.write('------------------xmlns-\n')
            elif re.search ('xlink:href',line, flags=0):
                equalLocation=line.find("=")+2
                URLA=line[equalLocation:]

                if re.search('>',URLA,flags=0):
                    #URLReport.write('In the xlink end carrot\n')
                    if re.search('xlink:title',line,flags=0):
                        #URLReport.write('In the xlink double title \n')

                        xlinkTitlInd='yes'
                    elif re.search('/',line,flags=0):
                        URLALength = len(URLA) - 4
                    else:
                        URLALength = len(URLA) - 3
                else:
                    URLALength=len(URLA)-2

                #URLALength=URLA.rfind("\"")
                if xlinkTitlInd =='yes':
                    titleLoc=line.find('\"')+41#was 20
                    URLALength=titleLoc
                    #URLReport.write ("URLALength (double title) "+ str(URLALength)+ '\n')

                    URLB=URLA[0:URLALength]
                    quotePos=URLB.find('\"')
                    if quotePos ==0 :
                        URL=URLA[0:URLALength]
                    else:
                        #URLReport.write("\t In the quotePos else\n")
                        URL=URLB[0:quotePos]

                    #URLReport.write ("URL (double title) "+ URL+ '\n')
                #URL=URLA[0:URLALength]
                #print ("URL:" + URL)
                result = url_checker(URL)
                #print ("Get the result")

                if result == "No":

                    ReportCounter +=1
                    URLReport.write('ReportCounter #2')
                    print('ReportCounter #2')
                    filenameHeader(fileB, PrevFile)
                    PrevFile = PreviousFileDeterminer(fileB)
                    #URLReport.write('in the XMLNsxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                    #URLReport.write("URLA: " + URLA)
                    #URLReport.write ("Result" + result)
                    #URLReport.write('URLALength: ' +str(URLALength)+ '\n')
                    URLReport.write( "\t"+ str(ReportCounter) + ":" + URL + " (in the xlink:href) \n")
                    #URLReport.write('------------------xmlns-\n')
            elif re.search('xsi:schemaLocation',line,flags=0):
                equalLocation=line.find("=")+2
                gmiLoc=line.find('gmi')+3
                URLA=line[equalLocation:gmiLoc]

                if re.search('gmi',URLA,flags=0):
                    #print('firts one')
                    URLALength = len(URLA)
                else:
                    #print('second one')
                    URLALength=len(URLA)+1

                '''

                if re.search('>',URLA,flags=0):
                    URLALength = len(URLA) - 3
                else:
                    URLALength=len(URLA)-2
                '''

                #URLALength=URLA.rfind("\"")

                URLfirst=URLA[0:URLALength]
                URLFirstStriped=URLfirst.strip()
                #print('URLLength'+ str(URLALength))
                #print ("URLFirstStriped:" +URLFirstStriped)

                if re.search('//',URLFirstStriped,flags=0):
                    if re.search('https://',URLFirstStriped,flags=0):
                        print ("Accepatable double stash")
                    elif re.search('//tigerweb',URLFirstStriped,flags=0):
                        print ("Accepatable double stash")
                    else:
                        doubleSlashIndOne='Yes'
                        #print ("In the double slash" + '(' + URLFirstStriped + ")\n")
                else:
                    print ("checking: "+ resultURLfirst)
                    resultURLfirst= url_checker(URLFirstStriped)
                    print ("checked: "+ resultURLfirst)




                if re.search('>',URLB,flags=0):
                    URLBLength = len(URLA) - 3
                else:
                    URLBLength=len(URLA)-2

                if doubleSlashIndOne == 'Yes':
                    result ="No"
                    doubleSlashInd= "No"
                elif resultURLfirst == "No":
                    ReportCounter +=1
                    URLReport.write('ReportCounter #3')
                    print('ReportCounter #3')
                    filenameHeader(fileB, PrevFile)
                    PrevFile = PreviousFileDeterminer(fileB)
                    #URLReport.write('in the XMLNsxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                    #URLReport.write("URLA: " + URLA)
                    #URLReport.write('URLALength: ' +str(URLALength)+ '\n')
                    URLReport.write( "\t"+ str(ReportCounter) + ":" + URL + " (In the xsi:schemaLocation)\n")
                    #URLReport.write('------------------xmlns-\n')

                #second part

                #print ("In the second part")
                #print ("gmiloc" + str(gmiLoc))
                #URLB=line[gmiLoc:]
                URLSecond=line[gmiLoc:]
                #print ("URLSecond" + URLSecond)
                if re.search('//',URLSecond,flags=0):
                    doubleSlashInd='Yes'
                else:

                    resultURLSecond=url_checker(URLSecond)



                if doubleSlashInd == 'Yes':
                    result ="No"
                    doubleSlashInd= "No"
                elif resultURLSecond == "No":

                    ReportCounter +=1
                    URLReport.write('ReportCounter #4')
                    print('eportCounter #4')
                    filenameHeader(fileB, PrevFile)
                    PrevFile = PreviousFileDeterminer(fileB)
                    #URLReport.write('in the XMLNsxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n')
                    #URLReport.write("URLA: " + URLA)
                    #URLReport.write('URLALength: ' +str(URLALength)+ '\n')
                    URLReport.write("\t"+ str(ReportCounter) + ":" + URL + "(In the xsi:schemaLocation 2)\n")
                    #URLReport.write('------------------xmlns-\n')

            elif re.search(' <gco:CharacterString>http</gco:CharacterString>', line, flags=0):
                continue
            elif re.search(' <gco:CharacterString>https</gco:CharacterString>', line, flags=0):
                continue
            elif re.search('ordering TIGER/Line Shapefiles', line, flags=0):

                #print ('line: ' + line)
                httpLoc = line.find('https')
                htmlLoc = line.find('tiger-line-file') + 14
                lastBracket=line.rfind('<')

                URLC = line[httpLoc:lastBracket]
                URL=URLC.strip()
                #print ('http:loc: ' + str(httpLoc))
                #print('URL: ' + URL)
                result = url_checker(URL)
                if result == "No":
                    ReportCounter += 1
                    print('URL REport Counter')
                    filenameHeader(fileB, PrevFile)
                    PrevFile = PreviousFileDeterminer(fileB)
                    #URLReport.write('In the ordering section\n')
                    URLReport.write( "\t"+ str(ReportCounter) + ":" + URL + "(In the ordering TIGER/Line Shapefiles \n")
                    #URLReport.write('-------------------\n')

            elif re.search('To obtain more information',line,flags=0):
                URLReport.write('In the to obtain more information\n')
                httpLoc=line.find('https')
                htmlLoc=line.find('html')
                URL=line[hashLoc:htmlLoc]
                result = url_checker(URL)

                if result == "No":

                    ReportCounter += 1
                    URLReport.write('ReportCounter #6')
                    print ('ReportCounter #6')
                    filenameHeader(fileB, PrevFile)
                    PrevFile = PreviousFileDeterminer(fileB)
                    #URLReport.write('In the to obtain more information\n')
                    URLReport.write( "\t"+ str(ReportCounter) + ":" + URL + " (In the To obtain more information\n")
                    #URLReport.write('-------------------\n')


            elif re.search('<gco:CharacterString>',line, flags=0):
                #print('In the gco:CharacterString')
                firstBracket=line.find('>')+1
                if re.search('.zip',line,flags=0):
                    lastBracket = line.find('.zip')+4
                    gcoBracketType="Zip"
                elif re.search('//',line,flags=0):
                    if re.search('//tigerweb',line,flags=0):

                        #print ("Accepatable double stash (tigerweb)")
                        lastBracket=line.rfind('<')
                    elif re.search('.xml',line,flags=0):
                        #print ("Accepatable double stash (xml)")
                        lastBracket=line.rfind('.xml')+4
                        #print ('lastbracket: ' + str(lastBracket))
                    elif re.search('http://www.geoplatform.gov/',line,flags=0):
                        geoPlatformInd="Yes"
                        print ("In the geoplatform")
                    elif re.search('.gov',line,flags=0):
                        #print ("Accepatable double stash (gov)")
                        lastBracket=line.rfind('.gov')+4
                        #print ('lastbracket: ' + str(lastBracket))
                    elif re.search('.html',line,flags=0):
                        #print ("Accepatable double stash (html)")
                        lastBracket=line.rfind('.html')+4
                        #print ('lastbracket: ' + str(lastBracket))

                    elif re.search('.net',line,flags=0):
                        #print ("Accepatable double stash (/wms)")
                        lastBracket=line.rfind('/wms')+4
                        #print ('lastbracket: ' + str(lastBracket))
                    elif re.search('https://geoservices.github.io/',line,flags=0):
                        lastBracket=line.rfind('<')
                        gcoBracketType="io"
                        print ("In the IO")
                    else:
                        lastBracket=line.rfind('<')
                        #print('double slash else')
                        doubleSlashIndOne='Yes'
                        #print ("In the double slash")

                elif re.search('.html',line,flags=0):
                    lastBracket = line.find('.html') + 5
                    gcoBracketType="html"
                    print("in the html")
                elif re.search('https://geoservices.github.io/',line,flags=0):
                    lastBracket=line.rfind('<')
                    gcoBracketType="io"
                    print ("In the IO")
                else:
                    lastBracket=line.rfind('<')
                    gcoBracketType="default"
                    print ('In the first default')

                if doubleSlashInd == 'Yes':
                    result ="No"
                    doubleSlashInd= "No"
                elif geoPlatformInd == 'Yes':
                    ReportCounter += 1
                    #URLReport.write('ReportCounter #7(geoplatformInd)')
                    print ("ReportCounter #7B   " + line)
                    result ="No"
                    URLReport.write("\t"+ str(ReportCounter) + ":" + URL + " (In the gco:CharacterString) \n")
                    URLReport.write( "\t"+ str(ReportCounter) + ":" + URL + " (In the gco:CharacterString) \n")
                    geoPlatformInd ='No'
                else:
                    URL=line[firstBracket:lastBracket]
                    #print ("firstbracket: " + str(firstBracket))
                    #print ("lastBracket: " + str(lastBracket))
                    #print ("Line" + line )
                    URLFinal=URL.strip()
                    #print ('URL (else) (No double slash):' + URL)
                    result = url_checker(URL)

                if result == "No":

                    ReportCounter += 1
                    #URLReport.write('ReportCounter #7')
                    print ('ReportCounter #7A')
                    filenameHeader(fileB, PrevFile)
                    PrevFile = PreviousFileDeterminer(fileB)
                    #URLReport.write('gco:CharacterString line (regular) : ' + line + "\n")
                    #URLReport.write("BracketType " + gcoBracketType + "\n")
                    #URLReport.write('In the gco:CharacterString')
                    URLReport.write( "\t"+ str(ReportCounter) + ":" + URL + " (In the gco:CharacterString) \n")
                    #URLReport.write('-------------------\n')
            elif re.search('<gmd:URL>', line, flags=0):

                #print ("Line: "+ line)
                firstBracket = line.find('>') + 1
                if re.search('hhttps',line,flags=0):
                    doubleInd='Yes'
                    print ("In the double h")
                    if re.search('.zip',line,flags=0):
                        lastBracket = line.find('.zip')+4
                        gcoBracketType="Zip"
                    elif re.search('.html',line,flags=0):
                        lastBracket = line.find('.html') + 5
                        gcoBracketType="html"
                    elif re.search('MapServer',line,flags=0):
                        lastBracket = line.find('MapServer') + 9

                        #print ('In the doubleInd MapServer')
                        gcoBracketType = "MapServer"
                    elif re.search('xml',line,flags=0):
                        lastBracket = line.find('xml')+3
                        gcoBracketType = "xml"
                    else:
                        lastBracket = line.rfind('<')+1#this was change
                elif re.search('.zip',line,flags=0):
                    lastBracket = line.find('.zip')+4
                    gcoBracketType="Zip"
                elif re.search('.html',line,flags=0):
                    lastBracket = line.find('.html') + 5
                    gcoBracketType="html"
                elif re.search('MapServer',line,flags=0):
                    lastBracket = line.find('MapServer') + 9
                    gcoBracketType = "MapServer"
                elif re.search('spatialreference',line,flags=0):
                    lastBracket = line.rfind('/')-1
                    gcoBracketType = "spatialreference"
                    print ('In the spatialreference')
                elif re.search('xml',line,flags=0):
                    lastBracket = line.find('xml')+3
                    gcoBracketType = "xml"

                else:
                    lastBracket = line.rfind('<')+1#this was changed
                URL = line[firstBracket:lastBracket]
                #print('URL;' +URL)
                #print ("doubleInd: " + doubleInd)

                if doubleInd =="Yes":
                    print ("in the doubleInd If structure")
                    ReportCounter += 1
                    URLReport.write('ReportCounter #8')
                    print ('ReportCounter #8')
                    filenameHeader(fileB, PrevFile)
                    PrevFile = PreviousFileDeterminer(fileB)
                    URLReport.write( "\t"+ str(ReportCounter) + ":" + URL + "(In the doubleInd)\n")
                    result='Yes'
                else:
                    result = url_checker(URL)

                if result == "No":

                    ReportCounter += 1
                    #URLReport.write('ReportCounter #9')

                    #print ('ReportCounter #9 for: ' + line)
                    filenameHeader(fileB, PrevFile)
                    PrevFile = PreviousFileDeterminer(fileB)
                    #URLReport.write("In the URL"  + "\n")
                    URLReport.write( "\t"+ str(ReportCounter) + ":" + URL + "(In the gmd:URL)\n")
                    #URLReport.write('-------------------\n')
                elif re.search('http:',line,flags=0):
                    URLReport.write( "\t"+ str(ReportCounter) + ":" + URL + "(In the http) \n")
            else:
                print ("Now working on :" + line)


print ("ReportCounter" + str(ReportCounter))
if ReportCounter == 0:
    URLReport.write("All the URLs are valid for the " + Year+ ' _ ' + theme+ "Tiger/Line files.\n\n")

URLReport.close()
sys.exit(1)