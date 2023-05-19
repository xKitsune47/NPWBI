import os
import yaml
import xmltodict
import json
from yaml import SafeLoader

print("The file will be located in the same place as the executable file!")
filePath = input("Paste in the path to the file:\n")

if not os.path.isfile(filePath):
    quit()

if ''.join(list(filePath)[-4:]) in ['yaml', 'json']:
    pConvFormat = ''.join(list(filePath)[-4:])
elif ''.join(list(filePath)[-3:]) in ['xml', 'yml']:
    pConvFormat = ''.join(list(filePath)[-3:])
else:
    quit()

newFileName = input("Specify the name of the new file:\n")
convType = int(input("Conversion type (1-xml, 2-json, 3-yml)\n"))

if pConvFormat == 'xml':
    sourceFile = open(filePath, 'r')
    xmlObj = xmltodict.parse(sourceFile.read())
elif pConvFormat == 'json':
    sourceFile = open(filePath, 'r')
    jsonObj = json.load(sourceFile)
elif pConvFormat == ('yml' or 'yaml'):
    sourceFile = open(filePath, 'r')
    ymlObj = yaml.load(sourceFile, Loader=SafeLoader)

if convType == 1:
    outputFile = open('{}.xml'.format(newFileName), 'w')
    if pConvFormat == 'xml':
        xmltodict.unparse(xmlObj, outputFile)
    elif pConvFormat == 'json':
        xmltodict.unparse(jsonObj, outputFile)
    elif pConvFormat == ('yml' or 'yaml'):
        xmltodict.unparse(ymlObj, outputFile, full_document=False)
elif convType == 2:
    outputFile = open('{}.json'.format(newFileName), 'w')
    if pConvFormat == 'xml':
        json.dump(xmlObj, outputFile)
    elif pConvFormat == 'json':
        json.dump(jsonObj, outputFile)
    elif pConvFormat == ('yml' or 'yaml'):
        json.dump(ymlObj, outputFile)
elif convType == 3:
    outputFile = open('{}.yml'.format(newFileName), 'w')
    if pConvFormat == 'xml':
        yaml.dump(xmlObj, outputFile)
    elif pConvFormat == 'json':
        yaml.dump(jsonObj, outputFile)
    elif pConvFormat == ('yml' or 'yaml'):
        yaml.dump(ymlObj, outputFile)

sourceFile.close()
outputFile.close()
