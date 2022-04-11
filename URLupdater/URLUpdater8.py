import os
import fnmatch
import shutil
import re
import datetime
import unicodedata


#work directories
#file:/U:/2016TigerFiles/TIGER2016/addr/tl_2016_01007_addr.dbf.iso.xml
#path="U:/2016TigerFiles/TIGER2016/necta"
#file:/U:/2016TigerFiles/TIGER2016/aitsn/tl_2016_us_aitsn.shp.iso.xml
# path="U:/2016TigerFiles/2017Files/zcta510"
#path="U:/2016TigerFiles/2017Files/addr"
#path ="W:/2016TigerFiles/2018Files/addrfn/test"

#home directories
#path="C:/Users/mattp/Desktop/WorkFiles/XML Files/ISO Files/2017Files/2017addrfeat"
#path="C:/Users/mattp/Desktop/WorkFiles/XML Files/ISO Files/2017Files/elsd"
#path="C:/Users/mattp/Desktop/WorkFiles/XML Files/ISO Files/2017Files/featnames"
path='C:/Users/mattp/Desktop/WorkFiles/XML Files/ISO Files/2017Files/Parent files/ParentFiles'

#create a list  or an array. This array uses the os.path modules, part of the os modules
#os.path.join joins or merges one or more path components
#os.walk

if os.path.exists(path):
    print ("The " + path + " directory exists")
else:
    print ("Could not find " + path + ". Please make sure the path is correct")
    exit(1)


configfiles =[os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.endswith('.xml')]

#print configfiles

#initialize the counter variables
countFiles=0
numOfFiles=0
tenCounter=0
filesDone=0
perDone=0
numOfSpaces=0
emptySpaceCounter = 0

#the url for vintage shapefiles
BaseZip=" https://www2.census.gov/geo/tiger"
#2016
Tiger2016URL="https://www2.census.gov/geo/tiger/TIGER2016/"
Tiger2016EAURL="https://meta.geo.census.gov/data/existing/decennial/GEO/GPMB/TIGERline/TIGER2016/"
WMS2016="https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_ACS2016/MapServer"
#2017
Tiger2017URL="https://www2.census.gov/geo/tiger/TIGER2017/"
Tiger2017EAURL='https://meta.geo.census.gov/data/existing/decennial/GEO/GPMB/TIGERline/TIGER2017/'
#2018
Tiger2018URL='https://meta.geo.census.gov/data/existing/decennial/GEO/GPMB/TIGERline/TIGER2018'
Tiger2018EAURL='https://meta.geo.census.gov/data/existing/decennial/GEO/GPMB/TIGERline/TIGER2018/'
baseUnitString=""
dateStampCounter=0;
EaURLIndin = 'False'

#the new Tiger Url
baseTigerUrl="                          <gmd:URL>https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html </gmd:URL>\n"
#datecheck
DatesUpdated=0
DatesUpdatedA=0
#The proper values for the spatialRepresentationType
spatRepType1="<gmd:spatialRepresentationType>\n"
spatRepType2="<gmd:MD_SpatialRepresentationTypeCode codeList=\"http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_SpatialRepresentationTypeCode\"\n"
spatRepType3="                                      codeListValue=\"textTable\"> textTable</gmd:MD_SpatialRepresentationTypeCode>\n"
spatRepType4=" </gmd:spatialRepresentationType>\n"

#status
StatusOne= " </gmd:status>\n"
StatusTwo= "<gmd:pointOfContact"
StatusThree =" xlink:href = \"https:\/\/www.ngdc.noaa.gov/docucomp/c5ceb003-1ed6-4126-8a16-bc08ce8fc267\"\n"
StatusFour ="xlink:title = \"U.S. Department of Commerce, U.S. Census Bureau, Geography Division, Spatial Data Collection and Products Branch\" />"


#the datesupdated array
datesupdated=[]

#getting today's date using the datetime module
PresentDate=datetime.datetime.now()

if PresentDate.month<10:
    if PresentDate.day <10:
        PresentDate2 = str(PresentDate.year) + "-" + "0" + str(PresentDate.month) + "-0" + str(PresentDate.day)
    else:
        PresentDate2 = str(PresentDate.year) + "-" + "0"+ str(PresentDate.month) + "-" + str(PresentDate.day)
else:
    if PresentDate.day < 10:
        PresentDate2 = str(PresentDate.year) + "-" + "0" + str(PresentDate.month) + "-0" + str(PresentDate.day)
    else:
        PresentDate2=str(PresentDate.year) + "-" + str(PresentDate.month) + "-" + str(PresentDate.day)

#modules

#TodaysDate Formats the correct ISO Date
print ('Creating the new files.........................................................................\n')
def TodaysDate():
    PresentDate = datetime.datetime.now()
    if PresentDate.month < 10:
        if PresentDate.day < 10:
            presentDate2a = str(PresentDate.year) + "-" + "0" + str(PresentDate.month) + "-0" + str(PresentDate.day)
            return presentDate2a
        else:
             presentDate2a = str(PresentDate.year) + "-" + "0" + str(PresentDate.month) + "-" + str(PresentDate.day)
             return presentDate2a
    else:
        if PresentDate.day < 10:
             presentDate2 = str(PresentDate.year) + "-" + "0" + str(PresentDate.month) + "-0" + str(PresentDate.day)
             return presentDate2
        else:
             presentDate2 = str(PresentDate.year) + "-" + str(PresentDate.month) + "-" + str(PresentDate.day)
             return presentDate2




#Supplies the correct date
def metadataDateUpdater(DatesUpdatedB,fileName):
    #print("Date Found")
    #print("the new date is" + PresentDate2)
    #nf.write("      <gco:Date>%s</gco:Date>\n" % PresentDate2)
    nf.write("      <gco:Date>%s</gco:Date>\n" % TodaysDate())
    DatesUpdatedB= DatesUpdated + 1
    print ("Updating the date counter: " + str(DatesUpdatedB))
    datesupdated.append(fileName)
    return DatesUpdatedB




docuCompCounter=0
for fileA in configfiles:
    #print ("fileA= " + fileA)
    countFiles += 1
    linNum=0
    DatesUpdatedA = DatesUpdated
    # opening the original file (fileA) for reading
    #f = open(fileA, "r")
    with open(fileA, "r") as f:
        if re.search('.shp',fileA,flags=0):
            #get the location of .shp using the find string property
            locShp = fileA.find('.shp')
            # get the base string using replace and substring functions
            fileA.replace("\\", "/")
            newStringBase = fileA[0:locShp]
            newString = newStringBase + "_newfile.shp.iso.xml"
        elif re.search('.dbf',fileA,flags=0):
            # get the location of .shp using the find string property
            print ("Dealing with a dbf file")
            locDBF = fileA.find('.dbf')
            # get the base string using replace and substring functions
            fileA.replace("\\", "/")
            newStringBase = fileA[0:locDBF]
            newString = newStringBase + "_newfile.dbf.iso.xml"
        # print ("newstring = " +newString)
        # open the file, represented by newString, for writing
        elif re.search('.ea',fileA,flags=0):
            print('Found an ea file!!!!!!!')
            continue
        else:
            #get the location of .shp using the find string property
            locDBF = fileA.find('.dbf')
            #get the base string using replace and substring functions
            fileA.replace("\\", "/")
            newStringBase = fileA[0:locDBF]
            newString = newStringBase + "_newfile.dbf.iso.xml"
        #print ("newstring = " +newString)
        # open the file, represented by newString, for writing
    #nf = open(newString, "w")
    # read through each line in the original file
    # using the re module to find the desired string using a Regular Expression
    #DatesUpdated = 0
        with open(newString, "w") as nf:
            for x in f:
                linNum+=1
                if re.search('<gmd:dateStamp>',x,flags=0):
                    print ('Found the datestamp')
                    nf.write('   <gmd:dateStamp>\n')
                    DatesUpdated = metadataDateUpdater(DatesUpdatedA, fileA)
                    nf.write('</gmd:dateStamp>\n')
                    #nf.write('   <gmd:metadataStandardName>')
                    dateStampCounter=1
                    #print("dateStampCounter:" + str(dateStampCounter))
                    #nf.write("<!-- The  dateStampCounter is: " + str(dateStampCounter) + "A-->\n")
                elif (dateStampCounter==1):
                     dateStampCounter+=1
                     print (x)
                     print ("dateStampCounter:" + str(dateStampCounter))
                     #nf.write("<!-- The  dateStampCounter is: " + str(dateStampCounter) + "B-->\n")
                elif (dateStampCounter==2):
                    #print(x)
                    nf.write ("<!-- The  dateStampCounter is: " + str(dateStampCounter) + "C-->\n")
                    if re.search('</gmd:dateStamp>',x,flags=0):
                        dateStampCounter = 0
                        continue
                    else:
                        dateStampCounter += 1
                    #print("dateStampCounter:" + str(dateStampCounter))
                    nf.write("<!-- End of the 2's  -->\n")
                    nf.write("<!-- Line: " + x + "-->\n")
                elif (dateStampCounter==3):
                    #nf.write("<!-- The  dateStampCounter is: " + str(dateStampCounter) + "D-->\n")
                    dateStampCounter=0
                    #print("dateStampCounter:" + str(dateStampCounter))
                    #nf.write("<!-- End of the 3's  -->\n")
                    continue
               # elif re.search('</gmd:dateStamp>',x,flags=0):
                #    nf.write("<!-- The  dateStampCounter is: " + str(dateStampCounter) + "D-->\n")
                elif re.search('.zip',x,flags=0):
                    if re.search('TIGER2018', x, flags=0):
                        loc2018=x.find('TIGER2018')
                        zipPart=x[loc2018:]
                        if re.search('gco:CharacterString',x,flags=0):
                            newZip = "       <gco:CharacterString>" + BaseZip + "/" + zipPart
                            nf.write(newZip)
                        elif re.search('gmd:URL',x, flags=0):
                            newZip= "                         <gmd:URL>" + BaseZip + "/" + zipPart
                            nf.write(newZip)
                    elif re.search('WMS',x,flags=0):
                        if re.search('2016',x,flags=0):
                            nf.write(WMS2016)
                    elif re.search('TIGER2016',x,flags=0):
                        loc2016=x.find('TIGER2016')
                        zipPart=x[loc2016:]
                        if re.search('gco:CharacterString',x,flags=0):
                            newZip = "       <gco:CharacterString>" + BaseZip + "/" + zipPart
                            nf.write(newZip)
                        elif re.search('gmd:URL',x, flags=0):
                            newZip= "                         <gmd:URL>" + BaseZip + "/" + zipPart
                            nf.write(newZip)
                    else:
                        nf.write(x)
                elif re.search('TIGER2016', x, flags=0):
                    if re.search('ea',x,flags=0):
                        Tiger2016Loc=x.find('TIGER2016')+10
                        EaName=x[Tiger2016Loc:]
                        print('EaName: ' + EaName + '\n')
                        if re.search('gmd:URL',x,flags=0):
                            if re.search('</gmd:URL>',x,flags=0):
                                newEAURL = "<gmd:URL>" + Tiger2016EAURL + "/" + EaName
                                print('newEAURL: ' + newEAURL)
                                nf.write(newEAURL)
                                #nf.write("<!-- gmd:URL(newEAURL): " + newEAURL + "-->\n")
                                EaURLIndin = 'True'
                            else:
                                newEAURL ="<gmd:URL>" + Tiger2016EAURL + "/" + EaName + "</gmd:URL>"
                                print('newEAURL: ' + newEAURL)
                                nf.write(newEAURL)
                                #nf.write("<!-- gmd:URL(newEAURL): " +newEAURL  + "-->\n")
                                EaURLIndin = 'True'
                        elif re.search('<gco:CharacterString>',x,flags=0):
                            #nf.write("<!-- In the EA 2016 Character String -->")
                            if re.search('</gco:CharacterString>',x,flags=0):
                                #nf.write("<!-- In the EA 2016 characterstring end tag -->")
                                print ("line with ea " + x + "\n")
                                #nf.write("<!-- Tiger2016EAURL"  + Tiger2016EAURL + "-->\n")
                                newEAURL = "<gco:CharacterString>" + Tiger2016EAURL  + EaName
                                #nf.write("<!-- newAEURL" + newEAURL + "-->\n")
                                #nf.write(newEAURL)
                                print('newEAURL: ' + newEAURL)
                                nf.write(newEAURL)
                                EaURLIndin='True'
                            else:
                                #nf.write("<!-- In the EA 2016 Character String else structure -->")
                                #nf.write("<!-- newAEURL" + newEAURL + "-->\n")
                                newEAURL = "<gco:CharacterString>" + Tiger2016EAURL  + EaName + "</gco:CharacterString>"
                                print('newEAURL: ' + newEAURL)
                                nf.write(newEAURL)
                                EaURLIndin = 'True'
                                #nf.write(newEAURL)
                        else:
                            newEAURL = Tiger2016EAURL + "/" + EaName
                            nf.write(newEAURL)
                    else:
                        #nf.write("<!-- In the else else -->")
                        tagLoc = x.find('>') + 1
                        begTag = x[0:tagLoc]
                        #print("begTag = " + begTag)
                        locUrl = x.find('2016') + 5
                        BaseFilename = x[0:locUrl]
                        print("ZipFileName=" + BaseFilename)
                        zipFileName = x[locUrl:]
                        #print("zipFileName = " + zipFileName)
                        newURL = begTag + Tiger2016URL + zipFileName
                        #print("newURL = " + newURL)
                        #print("-----------------------------\n\n")
                        nf.write(newURL +"\n")
                        EaURLIndin = 'True'
                elif re.search('TIGER2017', x, flags=0):
                    if re.search('ea',x,flags=0):
                        Tiger2017Loc=x.find('TIGER2017')+10
                        EaName=x[Tiger2017Loc:]
                        print('EaName: ' + EaName + '\n')
                        if re.search('gmd:URL',x,flags=0):
                            newEAURL ="<gmd:URL>" + Tiger2017EAURL + "/" + EaName + "<gmd:URL>"
                            print('newEAURL: ' + newEAURL)
                            nf.write(newEAURL)
                        elif re.search('<gco:CharacterString>',x,flags=0):
                            #nf.write("<!-- In the EA 2016 Character String -->")
                            if re.search('</gco:CharacterString>',x,flags=0):
                                newEAURL = "<gco:CharacterString>" + Tiger2017EAURL  + EaName
                                nf.write(newEAURL)
                                print('newEAURL: ' + newEAURL)
                                EaURLIndin='True'
                            else:
                                newEAURL = "<gco:CharacterString>" + Tiger2017EAURL  + EaName + "</gco:CharacterString>"
                                nf.write(newEAURL)
                                EaURLIndin = 'False'
                        else:
                            newEAURL = Tiger2017EAURL + "/" + EaName
                            nf.write(newEAURL)
                            EaURLIndin = 'False'
                    else:
                        tagLoc = x.find('>') + 1
                        begTag = x[0:tagLoc]
                        #print("begTag = " + begTag)
                        locUrl = x.find('2017') + 5
                        BaseFilename = x[0:locUrl]
                        print("ZipFileName=" + BaseFilename)
                        zipFileName = x[locUrl:]
                        #print("zipFileName = " + zipFileName)
                        newURL = begTag + Tiger2017URL + zipFileName
                        #print("newURL = " + newURL)
                        #print("-----------------------------\n\n")
                        nf.write(newURL)
                elif re.search('TIGER2018', x, flags=0):
                    print ("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                    print ("In the 2018 \n")
                    print ("string" + x)
                    lengthofUrl = len(x)
                    lengthofUrl =x.__len__()
                    print("lengthofUrl: " + str(lengthofUrl) + "\n")
                    #nf.write("<!-- lengthofUrl: " + str(lengthofUrl) + "-->\n")
                    print("BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB")
                    if re.search('ea',x,flags=0):
                        Tiger2018Loc=x.find('TIGER2018')+10
                        EaName=x[Tiger2018Loc:]
                        print('EaName: ' + EaName + '\n')
                        #nf.write("<!-- in the EA -->\n")
                        if re.search('gmd:URL',x,flags=0):
                            if re.search('</gmd:URL>',EaName,flags=0):
                                newEAURL = "<gmd:URL>" + Tiger2018EAURL + "/" + EaName
                                print('newEAURL: ' + newEAURL + "\n")
                                #nf.write("<!-- in the EA: gmd:URL </gmd:URL> -->\n")
                                nf.write(newEAURL)
                            else:
                                newEAURL ="<gmd:URL>" + Tiger2018EAURL + "/" + EaName + "</gmd:URL>"
                                print('newEAURL: ' + newEAURL + "\n")
                                #nf.write("<!-- in the EA: gmd:URL else-->\n")
                                nf.write(newEAURL)
                        elif re.search('<gco:CharacterString>',x,flags=0):
                            #nf.write("<!-- in the EA: <gco:CharacterString>  -->\n")
                            if re.search('</gco:CharacterString>',x,flags=0):
                                #nf.write("<!-- in the end characterstring -->\n")
                                newEAURL = "<gco:CharacterString>" + Tiger2018EAURL  + EaName
                                nf.write(newEAURL)
                                print('newEAURL: ' + newEAURL)
                                EaURLIndin='True'
                            else:
                                #nf.write("<!-- in the EA: <gco:CharacterString> else  -->\n")
                                newEAURL = "<gco:CharacterString>" + Tiger2018EAURL  + EaName + "</gco:CharacterString>"
                                nf.write(newEAURL)
                        elif re.search('<gmd:URL', x, flags=0):
                            #nf.write("<!-- in the URL -->\n")
                            if re.search('</gmd:URL', x, flags=0):
                                nf.write(x)
                                #nf.write("<!-- in the END URL -->")
                            else:
                                #nf.write("<!-- In the else!!!!!!!!!!!!!!!!!!!!! -->\n")
                                tagLoc = x.find('>') + 1
                                begTag = x[0:tagLoc]
                                #print("begTag = " + begTag)
                                locUrl = x.find('2017') + 5
                                BaseFilename = x[0:locUrl]
                                #print("ZipFileName=" + BaseFilename)
                                zipFileName = x[locUrl:]
                                #print("zipFileName = " + zipFileName)
                                newURL = begTag + Tiger2018URL + zipFileName
                                #print("newURL = " + newURL)
                                #print("-----------------------------\n\n")
                                nf.write(newURL)
                        else:
                            #nf.write("<!-- In the EA Else!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! -->")
                            newEAURL = Tiger2018EAURL + "/" + EaName
                            nf.write(newEAURL)
                    elif re.search('<gco:CharacterString>',x,flags=0):
                        if re.search('</gco:CharacterString>', x, flags=0):
                            nf.write(x)
                        else:
                            tagLoc = x.find('>') + 1
                            begTag = x[0:tagLoc]
                            #print("begTag = " + begTag)
                            locUrl = x.find('2017') + 5
                            BaseFilename = x[0:locUrl]
                            #print("ZipFileName=" + BaseFilename)
                            zipFileName = x[locUrl:]
                            #print("zipFileName = " + zipFileName)
                            newURL = begTag + Tiger2018URL + zipFileName
                            #print("newURL = " + newURL)
                            #print("-----------------------------\n\n")
                            nf.write(newURL)
                    elif re.search('<gmd:URL',x,flags=0):
                        #nf.write("<!-- in the URL partA -->\n")
                        if re.search('</gmd:URL',x,flags=0):
                            nf.write(x)
                            #nf.write("<!-- in the END URL ParB -->")
                        else:
                            #nf.write("<!-- In the else PartC -->")
                            tagLoc = x.find('>') + 1
                            begTag = x[0:tagLoc]
                            print("begTag = " + begTag)
                            locUrl = x.find('2017') + 5
                            BaseFilename = x[0:locUrl]
                            print("ZipFileName=" + BaseFilename)
                            zipFileName = x[locUrl:]
                            print("zipFileName = " + zipFileName)
                            newURL = begTag + Tiger2018URL + zipFileName
                            #print("newURL = " + newURL)
                            #print("-----------------------------\n\n")
                            nf.write(newURL)
                    else:
                        #nf.write("<!-- In all Else partD -->\n")
                        tagLoc = x.find('>') + 1
                        begTag = x[0:tagLoc]
                        #print("begTag = " + begTag)
                        locUrl = x.find('2017') + 5
                        BaseFilename = x[0:locUrl]
                        #print("ZipFileName=" + BaseFilename)
                        zipFileName = x[locUrl:]
                        #print("zipFileName = " + zipFileName)
                        newURL = begTag + Tiger2018URL + zipFileName
                        #print("newURL = " + newURL)
                        #print("-----------------------------\n\n")
                        nf.write(newURL)
                #elif re.search('xmlns:xsi',x,flags=0):
                 #   print ("skipping the xsi")
                elif re.search(' </gmd:linkage>',x,flags=0):
                    #print ("In the linkage")
                    #nf.write("\n <!-- In the linkage partE -->\n")
                    print ("troublesome LIne----------------" + x + "\n")
                    if re.search('gmd:name',x,flags=0):
                        #nf.write("<!-- In the linkage: gmb:name partF -->\n")
                        nf.write(' </gmd:linkage>\n')
                        nf.write('<gmd:name>\n')
                    elif EaURLIndin == 'True':
                        nf.write('                      </gmd:linkage>\n')
                        EaURLIndin='False'
                        #nf.write("<!-- In the linkage: gmb:name partG -->\n")
                        #print("In the linkage  EaURLIndin='False'")
                        #nf.write ('<!-- In the linkage  EaURLIndin=False -->')
                    elif re.search('gco:CharacterString',x,flags=0):
                        nf.write(' </gmd:linkage>\n')
                        nf.write(' <gmd:name>\n')
                        nf.write('<gco:CharacterString>Shapefile Zip File</gco:CharacterString>')
                        #nf.write("<!-- In the linkage: gco:CharacterString partH -->\n")
                        #print("In the linkage  gco:CharacterString'")
                    elif re.search('<gmd:URL> ',x,flags=0):
                        nf.write(' </gmd:linkage>\n')
                        #nf.write("<!-- In the linkage: gco:CharacterString partI -->\n")
                    elif re.search('</gmd:URL> ', x, flags=0):
                        nf.write(' </gmd:linkage>\n')
                        #nf.write("<!-- In the linkage: gco:CharacterString partJ -->\n")
                    else:
                        nf.write(x + "\n")
                        #nf.write("<!-- \n In the linkage: else partK -->\n")
                elif re.search('https://www.census.gov/geo/maps-data/data/tiger-line.html', x, flags=0):
                    nf.write(baseTigerUrl)
                elif re.search('http://www.census.gov/geo/maps-data/data/tiger-line.html', x, flags=0):
                    nf.write(baseTigerUrl)
                elif re.search('//www.census.gov/geo/maps-data/data/tiger-line.html',x,flags=0):
                    nf.write(baseTigerUrl)
                elif re.search('//www.census.gov/geo/maps-data/data/tiger-line.html',x,flags=0):
                    nf.write(baseTigerUrl)
                #elif re.search ('')
                elif re.search(' <gmd:spatialRepresentationType/>', x, flags=0):
                    # inserting the updated spatialRepresentationType
                    nf.write(spatRepType1)
                    nf.write(spatRepType2)
                    nf.write(spatRepType3)
                    nf.write(spatRepType4)
                elif re.search ('<gco:CharacterString>TIGER/Line\u00AE',x,flags=0):
                    print('dealing with the trademark')
                    nf.write(' <gco:CharacterString>TIGER/Line &#174;Shapefiles</gco:CharacterString>')
                #elif re.search('')
                elif re.search('gml:BaseUnit gml:id',x,flags=0):
                    baseUnitString=""
                    print("\n\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
                    locOfSpace=x.find(' ')
                    print ('locOfSpace= ' + str(locOfSpace))
                    print("Line" + x)
                    print('The value of isspace=' + str(x.isspace()))
                    numOfSpaces=x.count(' ')
                    print ('numOfSpaces= ' + str(numOfFiles))
                    if re.search(r"\s",x,flags=0):
                        print("whitespace found!!")
                        wordArray=x.split()
                        for a in wordArray:
                            baseUnitString = baseUnitString + a
                        print ("baseUnitString" + baseUnitString)
                        locOfGml=baseUnitString.find('gml:id')
                        baseUnitFirstHalf=baseUnitString[0:locOfGml]
                        baseUnitSecondHalf=baseUnitString[locOfGml:]
                        secondBaseUnitString= baseUnitFirstHalf + " " + baseUnitSecondHalf
                        nf.write("                       " + secondBaseUnitString + "\n")
                    else:
                        nf.write(x)
                #elif re.search( '</gmd:status>',x,flags=0):
                 #   nf.write(StatusOne)
                  #  nf.write(StatusTwo)
                   # nf.write(StatusThree)
                 #   #nf.write(StatusFour)
                else:
                    #print ("Writing to file for line: " + str(linNum))
                    #print(x)
                    nf.write(x)
                    #print ("printed to file!!!!!!!!")
        #print("Closing the file")
        nf.close()


    #x.close
    #https://www2.census.gov/geo/tiger/TIGER2017/



newFilesList=[os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.endswith('.xml')]

numOfFiles=len(newFilesList)


print ("\n\n copying the new files into the new files-----------------------------")
for fileB in newFilesList:
    filesDone+=1
    tenCounter+=1
    if tenCounter == 30:
        if numOfFiles >0:
            perDone=round((filesDone/numOfFiles)*100,3)
        tenCounter=0
        print(str(perDone) + " % done!!")
    #print ("FileB: %s" % fileB)

    if re.search('newfile',fileB,flags=0):
        #print ("\n\n We have a match !!!!!!!!!!!!! A file has newfile in it")
        os.chdir(path)
        LocPreNewfile=fileB.find('newfile')
        FileBBase=fileB[0:LocPreNewfile-1]#was -1
        if re.search('shp',fileB,flags=0):
            FileC = FileBBase + ".shp.iso.xml"
        else:
            #print ("the file has dbf in it")
            FileC= FileBBase + ".dbf.iso.xml"

        #print("AAAAAAAAAAAAAAAAAAAAAAAAAA")
        #print("FileB: " + fileB)
        #print(" LocPreNewfile: " + str(LocPreNewfile) + " \n\n")
        #print("FileBBase %s" % FileBBase)
        #print("FileC: %s " % FileC)
        #print("BBBBBBBBBBBBBBBBBBBBBBB")

        os.chdir(path)
        #print ('pre decision!!!!!!!!!!!!!!!!')
        if os.path.exists(fileB):
            #print ("fileB %s exists!!!!!!!!!!!!!!!!!!!!!" % fileB)
            #print('pre decision222222!!!!!!!!!!!!!!!!')

            if os.path.exists(FileC):
                #print("%s exists!!!!!!!!!!!!!!!!!!!!!" % FileC)
                #print("now copying" + fileB  + " to " + FileC)

                shutil.copyfile(fileB, FileC)
                #print ("Now removing " + fileB)
                #fileB.close()
                os.remove(fileB)
                #FileC.close()
                #print("---------------------------------else1-------------------\n\n")

            else:
                print("FileC ( %s ) does not exist!!!!!!!!!!" % FileC)
                print("\n\n")
                #print("-----------------------------------else2-----------------\n\n")
        else:
            print ("newfile  does not exist")
            print("%s does not exist" % fileB)
            #print("-----------------------------------else3-----------------\n\n")
    #FileC.close()


newFilesListFinal=[os.path.join(dirpath, f)
    for dirpath, dirnames, files in os.walk(path)
    for f in files if f.endswith('.xml')]

print ("numOfFiles (newfile List)= " + str(numOfFiles))
print ("The number of files are: " + str(countFiles))
print ("The number of files with updated dates: " + str(DatesUpdated))

for susFile in newFilesListFinal:
    if re.search('newfile',susFile, flags=0):
        print ("Found a file to be removed:" + susFile + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n")
        os.remove(susFile)


needNewDates=countFiles - DatesUpdated
lengthOfDatesUpdated=len(datesupdated)
print ('lengthOfDatesUpdated: ' + str(lengthOfDatesUpdated))
datesupdated.sort()
newFilesList.sort()


if needNewDates>0:
    print (str(needNewDates) + " files have not had their dates updated")
    for origFile in configfiles:
        #print ("update" + update)
        for update in datesupdated:
            if origFile == update:
                break
        else:
            print ("NeedNewDates: " + origFile)


exit(0)
