#Extract the zip files
from zipfile import ZipFile
import os

zip_file = 'my_files.zip'

#open the directory and get a list of zip files
cwd = os.getcwd()
path = "C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip"
print ("The current Working directory is " + cwd)

configfiles = [os.path.join(dirpath, f)
               for dirpath, dirnames, files in os.walk(path)
               for f in files if f.endswith('.zip')]


for file in configfiles:
    print ("Now working on: " + file)
    with ZipFile(file, 'r') as zf:
        # display the files inside the zip
        zf.printdir()
        # Extracting the files from zip file
        zf.extractall()
        print('Zip Extraction Completed')



'''
with ZipFile(zip_file, 'r') as zf:
   #display the files inside the zip
   zf.printdir()
   #Extracting the files from zip file
   zf.extractall()
   print('Zip Extraction Completed')

'''
