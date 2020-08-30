import MainAPI


class Players(MainAPI.MainAPI):
    def get_players(self, search, fields=None, language='ru', limit=None, type_='startswith'):
        url = 'wot/account/list/'
        return self._get_json(url, search=search, fields=fields, language=language, limit=limit, type=type_)

    def get_player_id(self, search: str):
        url = 'wot/account/list/'
        return self._get_json(url, search=search)['data'][0]['account_id']

    def get_personal_data(self, account_id, extra=None, fields=None, language='ru'):
        url = 'wot/account/info/'
        return self._get_json(url, account_id=account_id, extra=extra, fields=fields, language=language,
                              access_token=self._access_token)

    def get_vehicles(self, account_id, fields=None, language='ru', tank_id=None):
        url = 'wot/account/tanks/'
        return self._get_json(url, account_id=account_id, fields=fields, language=language, tank_id=tank_id,
                              access_token=self._access_token)

    def get_achievements(self, account_id, fields=None, language='ru'):
        url = 'wot/account/achievements/'
        return self._get_json(url, account_id=account_id, fields=fields, language=language)
