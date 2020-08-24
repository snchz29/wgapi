import requests
import config


class MainAPI:
    def __init__(self, application_id, access_token=None):
        self.application_id = application_id
        self.access_token = access_token

    def get_json(self, url: str):
        return requests.get(url, headers=config.HEADERS).json()
