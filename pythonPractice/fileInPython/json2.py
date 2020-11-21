import json

file = open("/home/abhishek/Desktop/pythonPractice/fileInPython/jsonfile.txt","r")

jsonFile = file.read()

print(type(jsonFile))

dictionary = json.loads(jsonFile)

print(type(dictionary))

