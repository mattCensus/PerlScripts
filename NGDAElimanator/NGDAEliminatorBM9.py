'''
File:SpatialRepresentationTypeUpdater.py
Date Created: 11/30/2018
Created by: Matthew McCready
Description: Updates an ISO metadate by inserting 'textTable' for the spatialRepresentationType. It also updates the
metadata date. It does this creating a new file to write all the changes. It then copies the new file to the old file
and removes the new file.

To do all the things listed above, the following modules were imported:
OS module: provides a way of using operating system dependent functionality.For operations on individual files.
fnmatch module: provides support for Unix shell-style wildcards
shutil module:offers a number of high-level operations on files and collections of files. In particular, functions are
              provided which support file copying and removal. For operations on individual files, see also the os
              module. Used for copy files when represented by a variable
re module: provides regular expression matching operations similar to those found in Perl.
datetime module:  classes for manipulating dates and times in both simple and complex ways
'''
# ! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import fnmatch
import shutil
import re
import datetime
import time
#import StringIO
import pickle

# path="W:/2016TigerFiles/2017Files/bg"
# path="W:/2016TigerFiles/2018Files/roads/Test"
#path = "W:/2016TigerFiles/2017files/ttract"
#path='C:/Users/mattp/Desktop/WorkFiles/XML Files/ISO Files/2017Files/elsd'
#path="C:/Users/mattp/Desktop/WorkFiles/XML Files/ISO Files/2017Files/elsd"
#path="C:/Users/mattp/Desktop/WorkFiles/XML Files/ISO Files/2017Files/ttractpractice"
path='C:/Users/mattp/Desktop/WorkFiles/XML Files/ISO Files/2017Files/practisettract'



# -<gmd:type>


# create a list  or an array. This array uses the os.path modules, part of the os modules
# os.path.join joins or merges one or more path components
# os.walk

configfiles = [os.path.join(dirpath, f)
               for dirpath, dirnames, files in os.walk(path)
               for f in files if f.endswith('.xml')]

# initialize the counter variables
countFiles = 0;
newFileCounter=0;
gmdTypeCounter = 0;
codelIstValueCounter = 0;
linesRemoved = 0;
descriptiveKeywordCounter = 0;
maintainceNoteCounter = 0;
corrIso= 'no'


# getting today's date using the datetime module
PresentDate = datetime.datetime.now()
PresentDate.day

if PresentDate.day < 10:
    day = "0" + str(PresentDate.day)
else:
    day = PresentDate.day

if PresentDate.month < 10:
    month = "0" + str(PresentDate.month)
else:
    month = PresentDate.month

PresentDate2 = str(PresentDate.year) + "-" + str(month) + "-" + str(day)


def gmdTypeCounterFunction(counter, eleName):
    if gmdTypeCounter == 2:
        print ("skipped the %s, the gmdTypeCounter is: %f" % (eleName, counter))
    else:
        nf.write(x)


def descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved):
    if descriptiveKeywordCounter == 1:
        linesRemoved += 1
        # descriptiveKeywordCounter+=1
        # print('descriptive keywords')
    else:
        nf.write(x)
        #print ("wrote to the file")


for fileA in configfiles:
    # print ("fileA= " + fileA)
    countFiles += 1
    descriptiveKeywordCounter = 0
    # opening the original file (fileA) for reading
    f = open(fileA, "r")
    # get the location of .shp using the find string property
    locShp = fileA.find('.shp')
    locDbf =fileA.find('.dbf')
    locSeriesInfo=fileA.find('SeriesInfo')
    print ('locSeriesInfo %s' %locSeriesInfo)
    if locShp >0:
        # get the base string using replace and substring functions
        # replace \ with / so every thing works
        fileA.replace("\\", "/")
        newStringBase = fileA[0:locShp]
        newString = newStringBase + "_newfile.shp.iso.xml"
    elif locDbf >0:
        # get the base string using replace and substring functions
        # replace \ with / so every thing works
        fileA.replace("\\", "/")
        newStringBase = fileA[0:locDbf]
        newString = newStringBase + "_newfile.dbf.iso.xml"

        #  open the file, represented by newString, for writing
    # read through each line in the original file
    # using the re module to find the desired string using a Regular Expression
    #print ("newString %s" % newString)
    nf = open(newString, "w")
    # x is the string, f is the file
    for x in f:
        if re.search('</gmd:descriptiveKeywords>', x, flags=0):
            # nf.write('<!-- At the end of the line -->')
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('descriptiveKeywords', x, flags=0):
            #print ('descriptiveKeywordCounter= %s' % descriptiveKeywordCounter)
            descriptiveKeywordCounter += 1
            # nf.write('<!-- descriptiveKeywordCounter= %s -->' % descriptiveKeywordCounter )
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
            #
            # if descriptiveKeywordCounter==1:
            #   linesRemoved+=1
            #   #descriptiveKeywordCounter+=1
            #   print('descriptive keywords')
            # else:
            #   nf.write(x)
            #   print ("wrote to the file")
        elif re.search('codeSpace="003"> revision', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('MD_Keywords', x, flags=0):
            # nf.write('<!-- in MD_keywords descriptiveKeywordCounter= %s -->' % descriptiveKeywordCounter)
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('keyword', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('gmd:type', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('gmd:MD_KeywordTypeCode', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('gmd:thesaurusName', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('gmd:CI_Citation', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('gmd:title', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('2017-10-02', x, flags=0):
            nf.write("      <gco:Date>%s</gco:Date>\n" % PresentDate2)
        elif re.search('2017-06-01', x, flags=0):
            nf.write("      <gco:Date>%s</gco:Date>\n" % PresentDate2)

        elif re.search('2017-10-12', x, flags=0):
            nf.write("      <gco:Date>%s</gco:Date>\n" % PresentDate2)
        elif re.search('2017-12-14',x,flags=0):
            nf.write("      <gco:Date>%s</gco:Date>\n" % PresentDate2)
        elif re.search('2017-12-19', x, flags=0):
            nf.write("      <gco:Date>%s</gco:Date>\n" % PresentDate2)
        elif re.search('gmd:date', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('gmd:CI_Date', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('gmd:date', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('gco:Date', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('gmd:dateType', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('codeListValue="revision', x, flags=0):
            # nf.write('<!-- codeListValue="revision removal descriptiveKeywordCounter= %s -->' % descriptiveKeywordCounter)
            #print('codeListValue="revision removal')
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('codeListValue="theme"', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('</gmd:date', x, flags=0):
            # nf.write('<!-- </gmd:date descriptiveKeywordCounter= %s -->' % descriptiveKeywordCounter)
            # print('gmd date removal')
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('gmd:dateType', x, flags=0):
            nf.write('<!-- gmd:dateType descriptiveKeywordCounter= %s -->' % descriptiveKeywordCounter)
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('gmd:CI_DateTypeCode ', x, flags=0):
            nf.write('<!-- gmd:CI_DateTypeCode descriptiveKeywordCounter= %s -->' % descriptiveKeywordCounter)
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('gmd:otherCitationDetails', x, flags=0):
            descriptiveKeywordCounterFunction(descriptiveKeywordCounter, linesRemoved)
        elif re.search('</gmd:maintenanceNote>', x, flags=0):
            nf.write(x)
            maintainceNoteCounter = 0
        elif re.search('gmd:maintenanceNote', x, flags=0):
            nf.write(x)
            maintainceNoteCounter = 1

        elif re.search('NGDA', x, flags=0):
            linesRemoved += 1
        elif re.search('Governmental Units', x, flags=0):
            linesRemoved += 1
        elif re.search('National Geospatial Data Asset', x, flags=0):
            linesRemoved += 1
        elif re.search('http://www.fgdc.gov/initiatives/resources/2013-2-1-ngda-data-themes-fgdc-sc-revised.pdf', x,
                       flags=0):
            linesRemoved += 1

        #elif re.search('ANSI INCITS 38:2009', x, flags=0):
            #if re.search('SeriesCollection', f, flags=0):
             #   locAnsi=x.find('ANSI')
              #  locCharacterString=xfing('</gco:CharacterString>')
               # preAnsi=x[0:locAnsi]
               # closingString=x[locCharacterString:]
               # finalAnsiString= preAnsi + "ISO 3166 Codes for the representation of names of countries and their subdivisions" + closingString
               # nf.write(finalAnsiString)
            #else:
         #       nf.write(x)
        elif re.search('ANSI INCITS 38:2009',x,flags=0):
                if locSeriesInfo>0:
                    nf.write('              <gco:CharacterString>ISO 3166 Codes for the representation of names of countries and their subdivisions</gco:CharacterString>')
                    corrIso='yes'
                else:
                    nf.write(x)
           # nf.write('<!-- corrIso: %s --> ' % corrIso)
        elif re.search('ANSI',x,flags=0):
            print("Found ANSI INCITS 454")
            if corrIso=='yes':
                linesRemoved+=1
            else:
                nf.write(x)

        elif re.search('Pe?uela ', x, flags=0):
            print ("Found Penuela")
            locQues = x.find('?')
            preQues = x[0:locQues - 1]
            postQues = x[locQues + 1:]
            newStringPe = preQues + "n" + postQues
            nf.write(x)
        elif re.search('tigerWMS_Current', x, flags=0):
            locWMSCurrent = x.find('tigerWMS_Current')
            preCurrent = x[0:locWMSCurrent]
            postCurrent = x[locWMSCurrent + 16:]
            newString = preCurrent + "tigerWMS_ACS2017" + postCurrent
            nf.write(newString)
        elif re.search('http://www2.census.gov/geo/', x, flags=0):
            locSlash = x.find('//')
            preSlash = x[0:locSlash - 5]  # was 7
            postSlash = x[locSlash:]
            newHttp = preSlash + 'https:' + postSlash
            nf.write(newHttp)
        elif re.search('gco:CharacterString', x, flags=0):
            if maintainceNoteCounter == 1:
                nf.write(
                    '            <gco:CharacterString>This metadata has been modified by removing all the NGDA tags. For this year\'s NGDA files, see the files on the Geospatial Platform </gco:CharacterString>\n')
            elif  corrIso=='yes':
               linesRemoved += 1
               corrIso ='no'
            else:
                nf.write(x)
        else:
            nf.write(x)

#num_files = len([f for f in os.listdir(path)
 #               if os.path.isfile(os.path.join(path, f))])

newFilesList=[os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.endswith('.xml')]

for fileB in newFilesList:
    #print "FileB: %s" % fileB
    if re.search('newfile',fileB,flags=0):
        newFileCounter+=1
        fileToGo=countFiles-newFileCounter
        #print("There are %s files left to copy." % fileToGo)
        #print "we have a match!!!!!!!!!!!!!"
        os.chdir(path)
        LocPreNewfile=fileB.find('newfile')
        FileCBase=fileB[0:LocPreNewfile-1]
        if fileB.find('.shp') > 0:
            FileC= FileCBase + ".shp.iso.xml"
            #print "FileCBase %s" % FileCBase
            #print "FileC: %s " % FileC
        elif fileB.find('dbf')>0:
            FileC = FileCBase + ".dbf.iso.xml"
        os.chdir(path)
        if os.path.exists(fileB):
            #print "fileB %s exists!!!!!!!!!!!!!!!!!!!!!" % fileB
            if os.path.exists(FileC):
                #print "%s exists!!!!!!!!!!!!!!!!!!!!!" % FileC
                shutil.copyfile(fileB, FileC)
                print("countFiles: %s" % countFiles)
                if countFiles > 1:
                    if fileToGo >0:
                        #print ("removing %s" % fileB)
                        time.sleep(60)
                        os.remove(fileB)
                    else:
                        #fileD =fileB
                        print('One file left to remove: %s' % fileB)


            else:
                print ("FileC ( %s ) does not exist" % FileC)
        else:
            print ("%s does not exist" % fileB)
    #print"---------------------------------------------------\n\n"
    #print("---------------------------------------------------\n\n")
    #print("---------------------------------------------------\n\n")

print('Done copying the files. Please see them. One file left to delete %s ' % fileB)


#FileB=StringIO.StringIO()

#fileStatus=os.stat(fileB)
#print ('Below is the file status information')
#print (fileStatus)
#print ('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')


print ('opening the file to close it')
df=open(fileB,'w')
#with open('test', 'wb') as file:
#with open (fileB,'r') as file:
#    pickle.dump(fileB, file)

#pickle.dump(df,fileB,'w',fix_imports=True)
print ('closing the file')
df.close()
time.sleep(420)
os.chdir('/')
if os.path.exists(fileB):
   print("Removing %s" % fileB)
   if countFiles > 1:
       Print("one file needs to be removed")
     #  os.remove(fileB)



print ("%s files have been modified" % countFiles)
