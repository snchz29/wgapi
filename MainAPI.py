import requests
import config


class MainAPI:
    def __init__(self, application_id, access_token=None):
        self.__application_id = application_id
        self.__access_token = access_token

    def get_json(self, url: str):
        return requests.get(url, headers=config.HEADERS).json()
