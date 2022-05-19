import requests
from requests.exceptions import HTTPError
import json


class Requests:
    def __init__(self):
        self.baseURL = f'https://covid19-api-philippines.herokuapp.com/api/'
        self.result = ''

    def getResource(self, endpoint):

        try:
            self.result = requests.get(self.baseURL+endpoint)
            self.result.encoding = 'utf-8'
        except HTTPError as http_error:
            print(f'There is an HTTP Error : {http_error}')
        except Exception as error:
            print(f'Some other error : {error}')
        else:
            print('Request is Successful!')
        return json.loads(self.result.text)


req = Requests()
data = req.getResource('timeline')
dumps = json.dumps(data, indent=4)
print(dumps)

total = 0
for data in data['data']:
    total += data['cases']

print(total)
