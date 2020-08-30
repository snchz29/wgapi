import MainAPI


class Clans(MainAPI.MainAPI):
    def get_clans(self, fields=None, game=None, language='ru', limit=None, page_no=None, search=None):
        url = 'wgn/clans/list/'
        return self._get_json(url, fields=fields, game=game, language=language, limit=limit, page_no=page_no,
                              search=search)

    def get_clan_id(self, search):
        url = 'wgn/clans/list/'
        return self._get_json(url, search=search)['data'][0]['clan_id']

    def get_details(self, clan_id, extra=None, fields=None, game=None, language='ru',
                    members_key=None):
        url = 'wgn/clans/info/'
        return self._get_json(url, clan_id=clan_id, access_token=self._access_token, extra=extra, fields=fields,
                              game=game, language=language, members_key=members_key)

    def get_member_details(self, account_id, fields=None, game=None, language='ru'):
        url = 'wgn/clans/membersinfo/'
        return self._get_json(url, account_id=account_id, fields=fields, game=game, language=language)

    def get_glossary(self, fields=None, game=None, language='ru'):
        url = 'wgn/clans/glossary/'
        return self._get_json(url, fields=fields, game=game, language=language)

    def get_message_board(self, fields=None, game=None):
        url = 'wgn/clans/messageboard/'
        return self._get_json(url, access_token=self._access_token, fields=fields, game=game)

    def get_history(self, account_id, fields=None, game=None, language=None):
        url = 'wgn/clans/memberhistory/'
        return self._get_json(url, account_id=account_id, fields=fields, game=game, language=language)
