
import os
import fnmatch
import shutil
import re
import datetime
import time
#import StringIO
import pickle
import sys

def BrowseGraphicInserter (Theme,OutFile):
    NewFile = OutFile
    CurrentWMS='https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Current/MapServer/WmsServer?REQUEST=GetMap&amp;SERVICE=WMS&amp;VERSION=1.3.0'
    Census2020='https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_Census2020/MapServer?REQUEST=GetMap&amp;SERVICE=WMS&amp;VERSION=1.3.0'
    PhysicalFeatures='https://tigerweb.geo.census.gov/arcgis/rest/services/TIGERweb/tigerWMS_PhysicalFeatures/MapServer'
    Format2EPSG='&amp;STYLES=default,default&amp;FORMAT=image/svg+xml&amp;BGCOLOR=0xFFFFFF&amp;TRANSPARENT=TRUE&amp;CRS=EPSG:4326'
    WidthHeight ='&amp;WIDTH=891&amp;HEIGHT=751'
    #&    amp;


    NewFile.write('<gmd:graphicOverview>\n')
    NewFile.write('<gmd:MD_BrowseGraphic>\n')
    NewFile.write('<gmd:fileName>\n')

    if re.search('State Legislative District (SLD) Upper Chamber',Theme,flags=0):
        GraphicURL='<gco:CharacterString>'+ CurrentWMS +'&amp;LAYERS= 2018 State Legislative Districts - Upper, 2018 State Legislative Districts - Upper Labels'+Format2EPSG + 'BBOX=42.299053,-71.408142,42.35679,-70.798861'+WidthHeight +'</gco:CharacterString>'
        NewFile.write (GraphicURL)
    elif re.search('State and Equivalent',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS= States, States Labels' + Format2EPSG + 'BBOX=32.860571,-113.5097542,46.389131,-113.509754' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('SubMinor Civil Division',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS= Subbarrios,Subbarrios Labels,Counties,Counties ' + Format2EPSG + 'BBOX=18.4271,-66.0859,18.4618,-66.0430' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('Census  Block',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS= 2020 Census Blocks,2020 Census Blocks Labels' + Format2EPSG + 'BBOX=42.499053,-71.897142,42.52679,-71.889999' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('Census Block', Theme, flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS= 2020 Census Blocks,2020 Census Blocks Labels' + Format2EPSG + 'BBOX=42.499053,-71.897142,42.52679,-71.889999' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('Census Tract',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS=Census Tracts,Census Tracts' + Format2EPSG + 'BBOX=41.187053,-72.508142,42.88679,-69.858861' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('Urban Growth Area (UGA)',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + Census2020 + '&amp;LAYERS=Urban Growth Areas,Urban Growth Areas Labels' + Format2EPSG + 'BBOX=42.006078,-124.520539,49.002494,-116.935343' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('AIANNH',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS=Off-Reservation Trust Lands,Off-Reservation Trust Lands Labels,State American Indian Reservations,State American Indian Reservations Labels,Hawaiian Home Lands,Hawaiian Home Lands Labels,Alaska Native Village Statistical Areas,Alaska Native Village Statistical Areas Labels,Federal American Indian Reservations,Federal American Indian Reservations Labels,Tribal Subdivisions,Tribal Subdivisions Labels,Oklahoma Tribal Statistical Areas,Oklahoma Tribal Statistical Areas Labels' + Format2EPSG + 'BBOX=+31.7134386,-112.0355607,+32.17347503,-111.640779' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('AITS',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS=Off-Reservation Trust Lands,Off-Reservation Trust Lands Labels,State American Indian Reservations,State American Indian Reservations Labels,Hawaiian Home Lands,Hawaiian Home Lands Labels,Alaska Native Village Statistical Areas,Alaska Native Village Statistical Areas Labels,Federal American Indian Reservations,Federal American Indian Reservations Labels,Tribal Subdivisions,Tribal Subdivisions Labels,Oklahoma Tribal Statistical Areas,Oklahoma Tribal Statistical Areas Labels' + Format2EPSG + 'BBOX=+31.7134386,-112.0355607,+32.17347503,-111.640779' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search (' Block Group',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS=Census Block Groups,Census Block Groups Labels' + Format2EPSG + 'BBOX=+42.389053,-71.907142,42.52679,-71.879999' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('116th Congressional District',Theme, flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS=116th Congressional Districts,116th Congressional Districts Labels' + Format2EPSG + 'BBOX=+32.860571,-113.5097542,46.389131,-113.509754' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
        #116th Congressional Districts Consolidated City  Consolidated Cities
    elif re.search('Consolidated City', Theme, flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS=Consolidated Cities,Consolidated Cities Labels' + Format2EPSG + 'BBOX=+41.1581676,-073.1316819,+41.2909526,-072.97466503' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('Census County and Equivalent',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS Counties, Counties Labels' + Format2EPSG + 'BBOX=41.187053,-73.508142,42.88679,-69.858861' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('County Subdivision',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS County Subdivisions,County Subdivisions Labels' + Format2EPSG + 'BBOX=43.628449,-71.934903,43.706635,-71.346863' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search(' Elementary School District',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS Elementary School Districts,Elementary School Districts Labels' + Format2EPSG + 'BBOX=+41.3255598,-073.0942359,+41.4663967,-072.8549872' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('Census Place',Theme, flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS Census Designated Places,Census Designated Places Labels,Incorporated Places,Incorporated Places Labels' + Format2EPSG + 'BBOX=+42.299053,-71.408142,42.35679,-70.798861' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('Current Place',Theme, flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS Census Designated Places,Census Designated Places Labels,Incorporated Places,Incorporated Places Labels' + Format2EPSG + 'BBOX=+42.299053,-71.408142,42.35679,-70.798861' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search ('Census Secondary School District',Theme, flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS Secondary School Districts,Secondary School Districts Labels' + Format2EPSG + 'BBOX=+11679625.942909468,4709198.547476525,-11645573.246808422,4737900.651597611' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('Current Secondary School Districts', Theme, flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS Secondary School Districts,Secondary School Districts Labels' + Format2EPSG + 'BBOX=+11679625.942909468,4709198.547476525,-11645573.246808422,4737900.651597611' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('State Legislative District (SLD) Lower Chamber',Theme, flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS 2018 State Legislative Districts - Lower,2018 State Legislative Districts - Lower Labels' + Format2EPSG + 'BBOX=+11679625.942909468,4709198.547476525,-11645573.246808422,4737900.651597611' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('(SLD)Lower Chamber',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS 2018 State Legislative Districts - Lower,2018 State Legislative Districts - Lower Labels' + Format2EPSG + 'BBOX=+11679625.942909468,4709198.547476525,-11645573.246808422,4737900.651597611' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('UGA',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + Census2020 + '&amp;LAYERS Urban Growth Areas, Urban Growth Areas Labels' + Format2EPSG + 'BBOX=+11679625.942909468,4709198.547476525,-11645573.246808422,4737900.651597611' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('Unified School Districts',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS Unified School Districts,Unified School Districts Labels' + Format2EPSG + 'BBOX=+11679625.942909468,4709198.547476525,-11645573.246808422,4737900.651597611' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('All Roads',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + PhysicalFeatures + '&amp;LAYERS Primary Roads,Primary Roads Labels, Secondary Roads, Secondary Roads Labels, Local Roads, Local Roads Labels' + Format2EPSG + 'BBOX=+11679625.942909468,4709198.547476525,-11645573.246808422,4737900.651597611' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('Places',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS Census Designated Places,Census Designated Places Labels,Incorporated Places,Incorporated Places Labels' + Format2EPSG + 'BBOX=42.299053,-71.408142,42.35679,-70.798861' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
        #Census Designated Places,Census Designated Places Labels,Incorporated Places,Incorporated Places Labels
    elif re.search('PUMA',Theme, flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS 2010 Census Public Use Microdata Areas,2010 Census Public Use Microdata Areas ' + Format2EPSG + 'BBOX=42.1993,-71.4805,42.6317,-70.7939' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)
    elif re.search('(SLD) Upper Chamber State',Theme,flags=0):
        GraphicURL = '<gco:CharacterString>' + CurrentWMS + '&amp;LAYERS 2018 State Legislative Districts - Upper, 2018 State Legislative Districts - Upper Labels' + Format2EPSG + 'BBOX=42.1993,-71.4805,42.6317,-70.7939' + WidthHeight + '</gco:CharacterString>'
        NewFile.write(GraphicURL)

    else:
        NewFile.write('<gco:CharacterString> Unable to determine the Theme' + Theme + 'for the Browse Graphic </gco:CharacterString>')








    NewFile.write('</gmd:fileName>\n')
    NewFile.write('</gmd:MD_BrowseGraphic>\n')
    NewFile.write('</gmd:graphicOverview>\n')