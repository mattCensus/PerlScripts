import datetime
def TodaysDate():
    print('IN the TodaysDate module')
    PresentDate = datetime.datetime.now()
    if PresentDate.month < 10:
        print ("module month less than 10")
        if PresentDate.day < 10:
            presentDate2a = str(PresentDate.year) + "-" + "0" + str(PresentDate.month) + "-0" + str(PresentDate.day)
            return presentDate2a
        else:
             presentDate2a = str(PresentDate.year) + "-" + "0" + str(PresentDate.month) + "-" + str(PresentDate.day)
             return presentDate2a
    else:
        print("module month greater than 10")
        if PresentDate.day < 10:
             presentDate2 = str(PresentDate.year) + "-" + str(PresentDate.month) + "-0" + str(PresentDate.day)
             return presentDate2
        else:
             presentDate2 = str(PresentDate.year) + "-" + str(PresentDate.month) + "-" + str(PresentDate.day)
             return presentDate2


def metadataDateUpdater(DatesUpdatedB,fileName, updatedInputFileName, datesupdated=[], ):
    # with open(fileA, "r") as f:
    print ('IN the metadataDateUpdater module')
    print ("DatesUpdatedB= " + str(DatesUpdatedB))
    print ("fileName= " + fileName)
    print ("updatedInputFileName= " + updatedInputFileName)
    DatesUpdated = DatesUpdatedB
    #nf = open(updatedInputFileNameFileName, "w")
    #print("Date Found")
    #print("the new date is" + PresentDate2)
    #nf.write("      <gco:Date>%s</gco:Date>\n" % PresentDate2)
    with open(updatedInputFileName,'w') as nf:
        nf.write("      <gco:Date>%s</gco:Date>\n" % TodaysDate())
    DatesUpdatedB= DatesUpdated + 1
    print ("Updating the date counter: " + str(DatesUpdatedB))
    datesupdated.append(fileName)
    return DatesUpdatedB