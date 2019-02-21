import json

inFile = open('1.json', 'r')
inData = inFile.read()

jsonData = json.loads(inData)
for key in jsonData:
    print(key)
item = jsonData['item']
print(item)
print(type(item))
