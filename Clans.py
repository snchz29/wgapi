import MainAPI
import URLBuilder


class Clans(MainAPI.MainAPI):
    def get_clans(self, fields=None, game=None, language='ru', limit=None, page_no=None, search=None):
        builder = URLBuilder.URLBuilder('wgn')
        builder.set_request_target('clans/list')\
            .set_application_id(self.__application_id)\
            .add_parameter('fields', fields)\
            .add_parameter('game', game)\
            .add_parameter('language', language)\
            .add_parameter('limit', limit)\
            .add_parameter('page_no', page_no)\
            .add_parameter('search', search)
        return self.get_json(builder.url).json()

    def get_details(self, clan_id, access_token=None, extra=None, fields=None, game=None, language='ru', members_key=None):
        builder = URLBuilder.URLBuilder('wgn')
        builder.set_request_target('clans/info') \
            .set_application_id(self.__application_id) \
            .add_parameter('clan_id', clan_id) \
            .add_parameter('__access_token', access_token) \
            .add_parameter('extra', extra) \
            .add_parameter('fields', fields) \
            .add_parameter('game', game) \
            .add_parameter('language', language)\
            .add_parameter('members_key', members_key)
        return self.get_json(builder.url).json()

    def get_member_details(self, account_id, fields=None, game=None, language='ru'):
        builder = URLBuilder.URLBuilder('wgn')
        builder.set_request_target('clans/membersinfo') \
            .set_application_id(self.__application_id) \
            .add_parameter('account_id', account_id) \
            .add_parameter('fields', fields) \
            .add_parameter('game', game) \
            .add_parameter('language', language)
        return self.get_json(builder.url).json()

    def get_glossary(self, fields=None, game=None, language='ru'):
        builder = URLBuilder.URLBuilder('wgn')
        builder.set_request_target('clans/glossary') \
            .set_application_id(self.__application_id) \
            .add_parameter('fields', fields) \
            .add_parameter('game', game) \
            .add_parameter('language', language)
        return self.get_json(builder.url).json()

    def get_message_board(self, access_token=None, fields=None, game=None):
        builder = URLBuilder.URLBuilder('wgn')
        builder.set_request_target('clans/messageboard') \
            .set_application_id(self.__application_id) \
            .add_parameter('__access_token', access_token) \
            .add_parameter('fields', fields)\
            .add_parameter('game', game)
        return self.get_json(builder.url).json()

    def get_history(self, account_id, fields=None, game=None, language=None):
        builder = URLBuilder.URLBuilder('wgn')
        builder.set_request_target('clans/memberhistory') \
            .set_application_id(self.__application_id) \
            .add_parameter('account_id', account_id) \
            .add_parameter('fields', fields) \
            .add_parameter('game', game)\
        .add_parameter('language', language)
        return self.get_json(builder.url).json()

