import requests
import logging
import http.client as http_client


http_client.HTTPConnection.debuglevel = 1
logging.basicConfig(filename='./logs/requests.log', filemode='a')
logging.getLogger().setLevel(logging.DEBUG)
requests_log = logging.getLogger("requests.packages.urllib3")
requests_log.setLevel(logging.DEBUG)
requests_log.propagate = True

ACCESS_TOKEN_URL = 'http://master.proton-backend.stag.stfalcon.com/oauth/v2/token'
API_URL = 'http://master.proton-backend.stag.stfalcon.com/api/v1.0/'

DEFAULT_HEADER = 'application/json'

SUCCESS = 200
INCORRECT_HEADER = 400
ADDED = 201

CLIENT_ID = '1_7e971E3E5F4Fd5990Acc2Ad134C0099B18D6Ef45E78A9017De'
CLIENT_SECRET = 'c989E96F3C8Cd21C940Ac3Ca75De5752F31C48D9D8D5Fc333A'
GRANT_TYPE = 'password'
SCOPE = 'web'
USERNAME = 'admin@test.com'
PASSWORD = 'Qwerty123'

access_token = ''

header = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

data = {
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
    'grant_type': GRANT_TYPE,
    'scope': SCOPE,
    'username': USERNAME,
    'password': PASSWORD
}

resp = requests.post(ACCESS_TOKEN_URL, data=data, headers=header)
print(resp.status_code)
if resp.status_code == SUCCESS:
    print('----------------')
    access_token = resp.json()['access_token']
    print(access_token)

header = {
    'Accept-Language': 'en',
    'Authorization': 'Bearer ' + access_token
}

files = {
    'file': ('2png.jpg', open('./pics/2png.jpg', 'rb'), 'multipart/form-data')
}

resp = requests.post(API_URL+'files', files=files, headers=header)
print(resp.status_code)
if resp.status_code == ADDED:
    print('----------------')
    file_id = resp.json()['id']
    print(file_id)

print(resp.request.headers)
