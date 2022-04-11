import os
import fnmatch
import shutil
import re
import datetime
import time
#import StringIO
import pickle
import sys
from ThemeDir import ThemeDir

#This module strips the basename (all the stuff before the "\") from the filename, leaving only the filename. It has only one module:  FileNameCorrector

def FileNameCorrector (FileName,OutFile):
    NewFile = OutFile
    FinalFile =''
    print ("In the FileNameCorrector ")
    File=str(FileName)
    print ("Writing to: " + NewFile)

    SlashLoc=File.rfind('\\')+1
    #print ('SlashLoc' +   str(SlashLoc))
    RealFileName=File[SlashLoc:]
    print ('RealFileName' + str(RealFileName))
    FinalFile ='     <gco:CharacterString>' + RealFileName+ '</gco:CharacterString>'
    #NewFile.write(FinalFile)
    return FinalFile

def RealfileName (FileName,OutFile):
    NewFile = OutFile
    FinalFile =''
    print ("In the FileNameCorrector ")
    File=str(FileName)
    print ("Writing to: " + NewFile)

    SlashLoc=File.rfind('/')
    SlashLoc2=File.rfind('\\')
    print ('Slash =' + str(SlashLoc))
    print ('Slash =' + str(SlashLoc2))

    if SlashLoc >0 and SlashLoc2>0:
        print('SlashLoc' + str(SlashLoc))
        RealFileName = File[SlashLoc2 + 1:]
        return RealFileName
    elif SlashLoc2>0:
        print('SlashLoc' + str(SlashLoc))
        RealFileName = File[SlashLoc2+1:]
        return RealFileName
    elif SlashLoc >0:
        print ('SlashLoc' +   str(SlashLoc))
        RealFileName=File[SlashLoc+1:]
        return RealFileName
