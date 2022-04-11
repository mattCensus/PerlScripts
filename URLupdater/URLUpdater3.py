import os
import fnmatch
import shutil
import re
import datetime

path="U:/2016TigerFiles/2017Files/Linearwater"
#path="U:/2016TigerFiles/2017Files/addr"
#path ="W:/2016TigerFiles/2018Files/addrfn/test"
#path="C:/Users/mattp/Desktop/WorkFiles/XML Files/ISO Files/2017Files/2017addrfeat"
#path="C:/Users/mattp/Desktop/WorkFiles/XML Files/ISO Files/2017Files/elsd"

#create a list  or an array. This array uses the os.path modules, part of the os modules
#os.path.join joins or merges one or more path components
#os.walk

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
Tiger2017URL="https://www2.census.gov/geo/tiger/TIGER2017/"

#the new Tiger Url
baseTigerUrl="                          <gmd:URL>https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html </gmd:URL>\n"
#datecheck
DatesUpdated=0

#The proper values for the spatialRepresentationType
spatRepType1="<gmd:spatialRepresentationType>\n"
spatRepType2="<gmd:MD_SpatialRepresentationTypeCode codeList=\"http://www.isotc211.org/2005/resources/Codelist/gmxCodelists.xml#MD_SpatialRepresentationTypeCode\"\n"
spatRepType3="                                      codeListValue=\"textTable\"> textTable</gmd:MD_SpatialRepresentationTypeCode>\n"
spatRepType4=" </gmd:spatialRepresentationType>\n"


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
def metadataDateUpdater(DatesUpdatedB):
    #print("Date Found")
    #print("the new date is" + PresentDate2)
    #nf.write("      <gco:Date>%s</gco:Date>\n" % PresentDate2)
    nf.write("      <gco:Date>%s</gco:Date>\n" % TodaysDate())
    DatesUpdatedB+=1
    print ("Updating the date counter: " + str(DatesUpdated))
    return DatesUpdated



docuCompCounter=0
for fileA in configfiles:
    #print ("fileA= " + fileA)
    countFiles += 1
    linNum=0
    # opening the original file (fileA) for reading
    f = open(fileA, "r")

    if re.search('.shp',fileA,flags=0):
        # get the location of .shp using the find string property
        locShp = fileA.find('.shp')
        # get the base string using replace and substring functions
        fileA.replace("\\", "/")
        newStringBase = fileA[0:locShp]
        newString = newStringBase + "_newfile.shp.iso.xml"
    else:
        # get the location of .shp using the find string property
        locDBF = fileA.find('.dbf')
        # get the base string using replace and substring functions
        fileA.replace("\\", "/")
        newStringBase = fileA[0:locDBF]
        newString = newStringBase + "_newfile.dbf.iso.xml"
    #print ("newstring = " +newString)
    # open the file, represented by newString, for writing
    nf = open(newString, "w")
    # read through each line in the original file
    # using the re module to find the desired string using a Regular Expression
    DatesUpdated = 0
    for x in f:
        linNum+=1

        if re.search('2017-12-12', x, flags=0):
            # inserting the new date
            DatesUpdated=metadataDateUpdater(DatesUpdated)
        elif re.search('2019-02-06',x,flags=0):
            DatesUpdated =metadataDateUpdater(DatesUpdated)
        elif re.search('2019-03-04',x,flags=0):
            DatesUpdated =metadataDateUpdater(DatesUpdated)
            #print ("date20190304")
        elif re.search('2019-07-02',x,flags=0):
            DatesUpdated = metadataDateUpdater(DatesUpdated)
        elif re.search('2019-06-27',x,flags=0):
            DatesUpdated =metadataDateUpdater(DatesUpdated)
        elif re.search('2017-06-01',x,flags=0):
            DatesUpdated =metadataDateUpdater(DatesUpdated)
            print ("DatesUpdated" + str(DatesUpdated))
        elif re.search('2018-03-13',x,flags=0):
            #print ("Found the date!!!!!!")
            DatesUpdated =metadataDateUpdater(DatesUpdated)
        elif re.search('2019-07-02',x,flags=0):
            DatesUpdated =metadataDateUpdater(DatesUpdated)
        elif re.search('2019-07-12',x,flags=0):
            DatesUpdated=metadataDateUpdater(DatesUpdated)
        elif re.search('TIGER2017', x, flags=0):
            tagLoc = x.find('>') + 1
            begTag = x[0:tagLoc]
            #print("begTag = " + begTag)
            locUrl = x.find('2017') + 5
            BaseFilename = x[0:locUrl]
            #print("ZipFileName=" + BaseFilename)
            zipFileName = x[locUrl:]
            #print("zipFileName = " + zipFileName)
            newURL = begTag + Tiger2017URL + zipFileName
            #print("newURL = " + newURL)
            #print("-----------------------------\n\n")
            nf.write(newURL)
        elif re.search('https://www.census.gov/geo/maps-data/data/tiger-line.html', x, flags=0):
            nf.write(baseTigerUrl)
        elif re.search('http://www.census.gov/geo/maps-data/data/tiger-line.html', x, flags=0):
            nf.write(baseTigerUrl)
        elif re.search(' <gmd:spatialRepresentationType/>', x, flags=0):
            # inserting the updated spatialRepresentationType
            nf.write(spatRepType1)
            nf.write(spatRepType2)
            nf.write(spatRepType3)
            nf.write(spatRepType4)
        elif re.search ('<gco:CharacterString>TIGER/Line®',x,flags=0):
            nf.write(' <gco:CharacterString>TIGER/Line&#174;Shapefiles</gco:CharacterString>')
        elif re.search('gml:BaseUnit gml:id',x,flags=0):
            print("\n\nAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            locOfSpace=x.find(' ')
            print ('locOfSpace= ' + str(locOfSpace))
            print("Line" + x)
            print('The value of isspace=' + str(x.isspace()))
            numOfSpaces=x.count(' ')
            print ('numOfSpaces= ' + str(numOfFiles))

            #for a in x:
             #
              #  print("Line" + x)
               # if x.isspace()==True:
                #    emptySpaceCounter+=1
                #print ("emptySpaceCounter= " + str(emptySpaceCounter))
                #emptySpaceCounter=0
            nf.write(x)


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
print ("numOfFiles= " + str(numOfFiles))

print ("\n\n copying the new files into the new files-----------------------------")
for fileB in newFilesList:
    filesDone+=1
    tenCounter+=1
    if tenCounter == 30:
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
                os.remove(fileB)
                #print("---------------------------------else1-------------------\n\n")

            else:
                print("FileC ( %s ) does not exist!!!!!!!!!!" % FileC)
                print("\n\n")
                #print("-----------------------------------else2-----------------\n\n")
        else:
            print ("newfile  does not exist")
            print("%s does not exist" % fileB)
            #print("-----------------------------------else3-----------------\n\n")



print ("The number of files are: " + str(countFiles))
print ("The number of files with updated dates: " + str(DatesUpdated))
needNewDates=countFiles - DatesUpdated

if needNewDates>0:
    print (str(needNewDates) + " files have not had their dates updated")
exit(0)
