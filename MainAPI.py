import requests
import json
import config

URL = "https://api.worldoftanks.ru/"


class MainAPI:
    def __init__(self, application_id):
        self.__application_id = application_id
        with open('access_token', 'r') as f:
            self._access_token = json.load(f)

    def _format(self, par):
        if type(par) is list:
            return ','.join(par)
        else:
            return par

    def _get_json(self, ending: str, **kwargs):
        parameters = kwargs
        parameters['application_id'] = self.__application_id
        r = requests.get(URL + ending, params=parameters, headers=config.HEADERS)
        return r.json()

    def _dump(self, js):
        return json.dumps(js, indent=2)
