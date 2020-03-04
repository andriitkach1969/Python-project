import requests
import json


url = "http://imag-sqa02-2-api.xggameplan.com/accesstokens"

payload = "{\n  \"email\": \"chris@smith.com\",\n  \"password\": \"123123\"\n}"
headers = {
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
if response.status_code == requests.codes.ok:
    print(response.status_code)
    print(response.text.encode('utf8'))
    print(response.content)
    resJson = json.loads(response.content)
    print(resJson)
    print(resJson['token'])
    print(resJson.get('token'))
    print(response.json().get('token'))
