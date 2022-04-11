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

baseName=os.path.basename(path)

#C:\Users\mattp\Desktop\WorkFiles\FileCount

ReportFile ="ListCount_" +baseName+ ".txt"
ReportFileFull = OutPath + "/" + ReportFile

URLReport=open(ReportFileFull,"w")
URLReport.write("dir:Num\n")
time.sleep(10)

if os.path.exists(path):
    print ("1: The " + path + " directory exists")
else:
    print ("2: Could not find " + path + ". Please make sure the path is correct")
    #exit(1)

configfiles =[os.path.join(dirpath, f)
              for dirpath, dirnames, files in os.walk(path)
              for f in files if f.endswith('.xml')]
pathName =os.path.dirname(path)

for dir in os.listdir(path):

   if os.path.isdir(os.path.join(path, dir)):
       print ("dir:" +dir+ "\n")
       num_files= len(os.listdir(os.path.join(path, dir)))
       print(str(dir) +" has :" + str(num_files) +" files \n")
       #URLReport.write(str(dir) +" has :" + str(num_files) +" files \n")
       URLReport.write(dir +":"+ str(num_files) +"\n")

URLReport.close()

'''
if os.path.isfile(os.path.join(path, dir)):
        initial_count += 1
    print(str(dir) +': '+ str(initial_count))


'''
sys.exit(1)


