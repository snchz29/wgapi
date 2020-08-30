import MainAPI


class Accounts(MainAPI.MainAPI):
    def get_accounts(self, search, fields=None, game=None, language='ru', limit=None, type_=None):
        url = 'wgn/account/list/'
        return self._get_json(url, search=search, fields=fields, game=game, language=language, limit=limit, type=type_)

    def get_account_id(self, search):
        url = 'wgn/account/list/'
        return self._get_json(url, search=search)['data'][0]['account_id']

    def get_account_information(self, account_id, fields=None, language='ru'):
        url = 'wgn/account/info/'
        return self._get_json(url, account_id=account_id, access_token=self._access_token, fields=fields,
                             language=language)
