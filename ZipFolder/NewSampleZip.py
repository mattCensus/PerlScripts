# importing necessary modules
import requests, zipfile
from io import BytesIO
print('Downloading started')

#Defining the zip file URL
url = 'https://www.learningcontainer.com/wp-content/uploads/2020/05/sample-zip-file.zip'

# Split URL to get the file name
filename = url.split('/')[-1]

# Downloading the file by sending the request to the URL
req = requests.get(url)
print('Downloading Completed')

# extracting the zip file contents
zipfile= zipfile.ZipFile(BytesIO(req.content))
zipfile.extractall('C:/Users/mattp/Desktop/WorkFiles/XMLFiles/2021Tiger/Zip')