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
    if get.status_code==200:
        return ("Yes")
    elif get.status_code == 11001:
        return ("No")
    else:
        return ("No")




path="C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/roads"
OutPath="C:/Users/mattp/Desktop/WorkFiles/MissingUrlReport"
ReportCounter=0
CurrentFile="New"

lastslash=path.rfind("/")+1
theme=path[lastslash:]
print ('theme: ' + theme )
newPath= path[0:lastslash-1]
print ('newPath:' + newPath)
lastslash2=newPath.rfind("/")+1
Year=newPath[lastslash2:]
print ("Year: " + Year)

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
print (pathName)

URLReport=open(ReportFileFull,"w")
URLReport.write("The following URLs are invalid for the " + Year+ theme+ "Tiger/Line files.\n\n")


for fileA in configfiles:
    print("fileA is : " + fileA)
    fileB=os.path.basename(fileA)
    ReadFile = open(fileA, "r", encoding='utf-8')

    for line in ReadFile:
        print('line:' + line)
        if re.search("http",line, flags=0):

            if re.search('codeList=',line, flags=0):
                codelistLoc=line.find('codeList=')+10

                URLA=line[codelistLoc:]
                print ("In the codelist")
                #print ("Line is" + line)
                print ("URLA is " + URLA)
                URLALength=len(URLA)-2
                #print ("URALength:" + str(URLALength))

                URLB =URLA[0:URLALength]
                if re.search('#',URLB,flags=0):
                    hashLoc=URLB.find('#')
                    URL=URLB[0:hashLoc]
                else:
                    URL=URLB
                #print ("URL: " + URL)
                result=url_checker(URL)
                #print ("result: " + result)
                if result == "No":
                    ReportCounter += 1
                    if CurrentFile == "New":
                        CurrentFile = fileB
                        lastSlashFile = CurrentFile.rfind("\\") + 1
                        BaseFile = CurrentFile[lastSlashFile:]
                        print('New')
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    elif CurrentFile == fileB:
                        print('elsif')
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    else:
                        print('else')
                        CurrentFile = fileB
                        lastSlashFile = CurrentFile.rfind("\\") + 1
                        BaseFile = CurrentFile[lastSlashFile:]
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    URLReport.write("result: " + result +"\n")
                    URLReport.write(str(ReportCounter)+ ":" + URL + "\n")

            elif re.search('xmlns', line, flags=0):
                equalLocation=line.find("=")+2
                URLA=line[equalLocation:]
                #print("URLA: " + URLA)
                URLALength=len(URLA)-2
                URL=URLA[0:URLALength]
                #print ("URL:" + URL)
                result = url_checker(URL)

                if result == "No":
                    ReportCounter +=1
                    if CurrentFile == "New":
                        CurrentFile = fileB
                        lastSlashFile = CurrentFile.rfind("\\") + 1
                        BaseFile = CurrentFile[lastSlashFile:]
                        print ('New')
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    elif CurrentFile == fileB:
                        print ('elsif')
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    else:
                        print ('else')
                        CurrentFile = fileB
                        lastSlashFile = CurrentFile.rfind("\\") + 1
                        BaseFile = CurrentFile[lastSlashFile:]
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    URLReport.write(str(ReportCounter) + ":" + URL + "\n")
            elif re.search(' <gco:CharacterString>http</gco:CharacterString>', line, flags=0):
                continue
            elif re.search('ordering TIGER/Line Shapefiles', line, flags=0):
                print('In the ordering section')
                print ('line: ' + line)
                httpLoc = line.find('https')
                htmlLoc = line.find('tiger-line-file') + 14
                URL = line[httpLoc:]
                print ('http:loc: ' + str(httpLoc))
                print('URL: ' + URL)
                result = url_checker(URL)

                if result == "No":
                    ReportCounter += 1
                    if result == "No":
                        ReportCounter += 1
                        if CurrentFile == "New":
                            CurrentFile = fileB
                            lastSlashFile = CurrentFile.rfind("\\") + 1
                            BaseFile = CurrentFile[lastSlashFile:]
                            print('New')
                            URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                        elif CurrentFile == fileB:
                            print('elsif')
                            URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                        else:
                            print('else')
                            CurrentFile = fileB
                            lastSlashFile = CurrentFile.rfind("\\") + 1
                            BaseFile = CurrentFile[lastSlashFile:]
                            URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    URLReport.write(str(ReportCounter) + ":" + URL + "\n")

            elif re.search('To obtain more information',line,flags=0):
                httpLoc=line.find('https')
                htmlLoc=line.find('html')
                URL=line[hashLoc:htmlLoc]
                result = url_checker(URL)

                if result == "No":
                    ReportCounter += 1
                    if CurrentFile == "New":
                        CurrentFile = fileB
                        lastSlashFile = CurrentFile.rfind("\\") + 1
                        BaseFile = CurrentFile[lastSlashFile:]
                        print('New')
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    elif CurrentFile == fileB:
                        print('elsif')
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    else:
                        print('else')
                        CurrentFile = fileB
                        lastSlashFile = CurrentFile.rfind("\\") + 1
                        BaseFile = CurrentFile[lastSlashFile:]
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    URLReport.write(str(ReportCounter) + ":" + URL + "\n")


            elif re.search('<gco:CharacterString>',line, flags=0):
                #print('gco:CharacterString line: ' + line)
                firstBracket=line.find('>')+1
                lastBracket=line.rfind('<')-1
                URL=line[firstBracket:lastBracket]
                result = url_checker(URL)

                if result == "No":
                    ReportCounter += 1
                    if CurrentFile == "New":
                        CurrentFile = fileB
                        lastSlashFile = CurrentFile.rfind("\\") + 1
                        BaseFile = CurrentFile[lastSlashFile:]
                        print('New')
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    elif CurrentFile == fileB:
                        print('elsif')
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    else:
                        print('else')
                        CurrentFile = fileB
                        lastSlashFile = CurrentFile.rfind("\\") + 1
                        BaseFile = CurrentFile[lastSlashFile:]
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    URLReport.write(str(ReportCounter) + ":" + URL + "\n")
            elif re.search('<gmd:URL>', line, flags=0):
                print ("In the URL")
                print ("Line: "+ line)
                firstBracket = line.find('>') + 1
                lastBracket = line.rfind('<')
                URL = line[firstBracket:lastBracket]
                print('URL;' +URL)
                result = url_checker(URL)

                if result == "No":
                    ReportCounter += 1
                    if CurrentFile == "New":
                        CurrentFile = fileB
                        lastSlashFile = CurrentFile.rfind("\\") + 1
                        BaseFile = CurrentFile[lastSlashFile:]
                        print('New')
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    elif CurrentFile == fileB:
                        print('elsif')
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    else:
                        print('else')
                        CurrentFile = fileB
                        lastSlashFile = CurrentFile.rfind("\\") + 1
                        BaseFile = CurrentFile[lastSlashFile:]
                        URLReport.write("-----Incorrect URLS for " + BaseFile + "----------\n")
                    URLReport.write(str(ReportCounter) + ":" + URL + "\n")
            else:
                print ("Now working on :" + line)

sys.exit(1)