import os
import yaml
import xmltodict
import json
from yaml import SafeLoader

filePath = input("Paste in the path to the file:\n")
if not os.path.isfile(filePath):
    print("File does not exist")
if ''.join(list(filePath)[-4:]) == ('yaml' or 'json'):
    pConvFormat = ''.join(list(filePath)[-4:])
elif ''.join(list(filePath)[-3:]) == ('xml' or 'yml'):
    pConvFormat = ''.join(list(filePath)[-3:])
else:
    print("The format of the file is not supported by the program")
newFileName = input("Specify the name of the new file:\n")
convType = int(input("Conversion type (1-xml, 2-json, 3-)\n"))

if pConvFormat == 'xml':
    sourceFile = open(filePath, 'r')
    xmlObj = xmltodict.parse(sourceFile.read())
    pass
elif pConvFormat == 'json':
    sourceFile = open(filePath, 'r')
    jsonObj = json.load(sourceFile)
    pass
elif pConvFormat == ('yml' or 'yaml'):
    sourceFile = open(filePath, 'r')
    ymlObj = yaml.load(sourceFile, Loader=SafeLoader)
    pass

if convType == 1:
    outputFile = open('{}.xml'.format(newFileName), 'w')
    pass
elif convType == 2:
    outputFile = open('{}.json'.format(newFileName), 'w')
    pass
elif convType == 3:
    outputFile = open('{}.yml'.format(newFileName), 'w')
    pass

sourceFile.close()
outputFile.close()
