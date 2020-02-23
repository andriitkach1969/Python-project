import requests
# import json


API_SERVER = 'http://stage.e-tickets-crm.stag.stfalcon.com/api'

DEFAULT_HEADER = 'application/json'

SUCCESS = 200
INCORRECT_HEADER = 400
ADDED = 201


def getFullEventbyID(id):
    responce = requests.get(API_SERVER + '/events/' + str(id))
    return responce


def parseLastEventPoint(allResp):
    data = allResp.json()
    print(data)
    return data["eventPoints"][len(data)]


def putEventsAddEventPoint(jstr):
    pass


if __name__ == '__main__':
    fullResponce = getFullEventbyID(355)
    print(fullResponce.status_code)
    print(fullResponce.headers)
    print(fullResponce.url)
    print(fullResponce.content)

#    lastStr = parseLastEventPoint(fullStr)
#    print(lastStr)