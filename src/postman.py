import json

STR_ITEM = 'item'
STR_NAME = 'name'
STR_REQUEST = 'request'
STR_AUTH = 'auth'
STR_METHOD = 'method'
STR_HEADER = 'header'
STR_BODY = 'body'
STR_URL = 'url'
STR_DESCRIPTION = 'description'


def crack(dictdata, listdata, count=0):

    schemadict = {STR_NAME:'', STR_DESCRIPTION:'', STR_METHOD:'', STR_AUTH:'', STR_REQUEST:'', STR_HEADER:'', STR_URL:'', STR_BODY:''}

    for item in dictdata[STR_ITEM]:
        gcheck = item.get(STR_REQUEST)
        if gcheck is None:
            count = crack(item, listdata, count)
        else:
            idict = schemadict;
            idict[STR_NAME] = item[STR_NAME]
            idict[STR_DESCRIPTION] = item[STR_REQUEST][STR_DESCRIPTION]

            listdata.append(idict)
            print(type(item), ' ** ', item)
            count += 1
    return count


if __name__ == "__main__":

    resList = []
    totalRoutes = 0

    inFile = open('../collections/Proton API.postman_collection.json', 'r')
    rawdata = inFile.read()
    inFile.close()
    jsonData = json.loads(rawdata)
    totalRoutes = crack(jsonData, resList)
    if totalRoutes != 0:
        print(resList)
    else:
        print('error in parsing')

    print(totalRoutes)