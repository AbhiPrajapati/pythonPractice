person = {}

person['abhishek'] = {
    "name":"abhishek",
    "mother_name":"surekha",
    "father_name": "Deepak",
    "mobile_no":93224011534,
}

person['deepak'] = {
    "name":"deepak",
    "mother_name":"aunty",
    "father_name": "kamlesh",
    "mobile_no":8600473951,
}

person['ananya'] = {
    "name":"ananya",
    "mother_name":"aunty",
    "father_name": "uncle",
    "mobile_no":1234567890,
}

import json
jsonFile = json.dumps(person)
with open("/home/abhishek/Desktop/pythonPractice/fileInPython/jsonfile.txt","w") as jFile:
    jFile.write(jsonFile)

