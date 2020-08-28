import MainAPI


class Clans(MainAPI.MainAPI):
    def get_clans(self, fields=None, game=None, language='ru', limit=None, page_no=None, search=None):
        url = 'wgn/clans/list/'
        req = self._get_json(url, fields=fields, game=game, language=language, limit=limit, page_no=page_no,
                             search=search)
        return self._dump(req)

    def get_details(self, clan_id, access_token=None, extra=None, fields=None, game=None, language='ru',
                    members_key=None):
        url = 'wgn/clans/info/'
        req = self._get_json(url, clan_id=clan_id, access_token=access_token, extra=extra, fields=fields, game=game,
                             language=language, members_key=members_key)
        return self._dump(req)

    def get_member_details(self, account_id, fields=None, game=None, language='ru'):
        url = 'wgn/clans/membersinfo/'
        req = self._get_json(url, account_id=account_id, fields=fields, game=game, language=language)
        return self._dump(req)

    def get_glossary(self, fields=None, game=None, language='ru'):
        url = 'wgn/clans/glossary/'
        req = self._get_json(url, fields=fields, game=game, language=language)
        return self._dump(req)

    def get_message_board(self, access_token=None, fields=None, game=None):
        url = 'wgn/clans/messageboard/'
        req = self._get_json(url, access_token=access_token, fields=fields, game=game)
        return self._dump(req)

    def get_history(self, account_id, fields=None, game=None, language=None):
        url = 'wgn/clans/memberhistory/'
        req = self._get_json(url, fields=fields, game=game, language=language)
        return self._dump(req)

