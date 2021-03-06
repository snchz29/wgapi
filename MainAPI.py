import requests
import json
import config

URL = "https://api.worldoftanks.ru/"


class MainAPI:
    def __init__(self, application_id):
        self.__application_id = application_id
        with open('access_token', 'r') as f:
            self._access_token = json.load(f)

    @staticmethod
    def __format(par):
        if type(par) is list:
            return ','.join(map(str, par))
        elif type(par) is str:
            return par.replace(', ', ',').replace(' ', ',')
        else:
            return par

    def _get_json(self, ending: str, **kwargs):
        parameters = kwargs
        parameters['application_id'] = self.__application_id
        for key, val in parameters.items():
            parameters[key] = self.__format(val)
        r = requests.get(URL + ending, params=parameters, headers=config.HEADERS)
        return r.json()
