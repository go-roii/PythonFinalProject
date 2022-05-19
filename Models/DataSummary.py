from Models.Requests import Requests
import datetime


class DataSummary:

    def __init__(self):
        self.request = Requests()
        self.data = self.request.getResource('summary')
        self.last_update = self.data['last_update']
        self.total = self.data['data']['total']
        self.recoveries = self.data['data']['recoveries']
        self.deaths = self.data['data']['deaths']
        self.active_cases = self.data['data']['active_cases']
        self.fatality_rate = self.data['data']['fatality_rate']
        self.recovery_rate = self.data['data']['recovery_rate']


data = DataSummary()
print('last_update  : ', data.last_update)
print('total        : ', data.total)
print('recoveries   : ', data.recoveries)
print('deaths       : ', data.deaths)
print('active_cases : ', data.active_cases)
print('fatality_rate: ', data.fatality_rate)
print('recovery_rate: ', data.recovery_rate)

