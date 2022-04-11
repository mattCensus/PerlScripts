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

initial_count=0

path="C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger"
OutPath="C:/Users/mattp/Desktop/WorkFiles/FileCount"

baseName=str(os.path.basename(path))

#C:\Users\mattp\Desktop\WorkFiles\FileCount

ReportFile ="ListCount_" +baseName+ "A.txt"
ReportFileB ="ListCount_" +baseName+ "B.txt"
ReportFileFull = OutPath + "/" + ReportFile

URLReport=open(ReportFileFull,"w")
URLReport.write("dir:Num\n")


# Opening a file
file1 = open(ReportFileB, 'w')
L = ["This is Delhi \n", "This is Paris \n", "This is London \n"]
s = "Hello\n"

# Writing a string to file
file1.write(s)

# Writing multiple strings
# at a time
file1.writelines(L)

# Closing file
file1.close()

# Checking if the data is
# written to file or not


sys.exit(1)