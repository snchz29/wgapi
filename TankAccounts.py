import MainAPI


class Players(MainAPI.MainAPI):
    def get_players(self, search, fields=None, language='ru', limit=100, type_='startswith'):
        url = 'wot/account/list/'
        req = self._get_json(url, search=search, fields=self._format(fields), language=language, limit=limit,
                             type=type_)
        return self._dump(req)

    def get_player_id(self, search: str):
        url = 'wot/account/list/'
        return self._get_json(url, search=search)['data'][0]['account_id']

    def get_personal_data(self, account_id, extra=None, fields=None, language='ru'):
        url = 'wot/account/info/'
        req = self._get_json(url, account_id=account_id, extra=self._format(extra), fields=self._format(fields),
                             language=language, access_token=self._access_token)
        return self._dump(req)

    def get_vehicles(self, account_id, fields=None, language='ru', tank_id=None):
        url = 'wot/account/tanks/'
        req = self._get_json(url, account_id=account_id, fields=self._format(fields), language=language,
                             tank_id=tank_id, access_token=self._access_token)
        return self._dump(req)

    def get_achievements(self, account_id, fields=None, language='ru'):
        url = 'wot/account/achievements/'
        req = self._get_json(url, account_id=account_id, fields=self._format(fields), language=language)
        return self._dump(req)
