import MainAPI
import URLBuilder


class Accounts(MainAPI.MainAPI):
    def get_accounts(self, search, fields=None, game=None, language='ru', limit=None, _type=None):
        builder = URLBuilder.URLBuilder('wgn')
        builder.set_request_target('list') \
            .set_application_id(self.application_id) \
            .add_parameter('search', search) \
            .add_parameter('fields', fields) \
            .add_parameter('game', game) \
            .add_parameter('language', language) \
            .add_parameter('limit', limit) \
            .add_parameter('type', _type)
        return self.get_json(builder.url).json()

    def get_account_information(self, account_id, access_token=None, fields=None, language='ru'):
        builder = URLBuilder.URLBuilder('wgn')
        builder.set_request_target('info') \
            .set_application_id(self.application_id) \
            .add_parameter('account_id', account_id) \
            .add_parameter('access_token', access_token) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language)
        return self.get_json(builder.url).json()
