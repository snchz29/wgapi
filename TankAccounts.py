import MainAPI
import URLBuilder

class Players(MainAPI.MainAPI):
    def get_players(self, search, fields=None, language='ru', limit=100, _type='startswith'):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('account/list') \
            .set_application_id(self.application_id) \
            .add_parameter('search', search) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language) \
            .add_parameter('limit', str(limit)) \
            .add_parameter('type', _type)
        return self.get_json(builder.url)

    def get_player_id(self, search: str):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('account/list') \
            .set_application_id(self.application_id) \
            .add_parameter('search', search)
        return self.get_json(builder.url)['data'][0]['account_id']

    def get_personal_data(self, account_id, extra=None, fields=None, language='ru'):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('account/info') \
            .set_application_id(self.application_id) \
            .add_parameter('account_id', account_id) \
            .add_parameter('access_token', self.access_token) \
            .add_parameter('extra', extra) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language)
        return self.get_json(builder.url)

    def get_vehicles(self, account_id, fields=None, language='ru', tank_id=None):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('account/tanks') \
            .set_application_id(self.application_id) \
            .add_parameter('account_id', account_id) \
            .add_parameter('access_token', self.access_token) \
            .add_parameter('field', fields) \
            .add_parameter('language', language) \
            .add_parameter('tank_id', tank_id)
        return self.get_json(builder.url)

    def get_achievements(self, account_id, fields=None, language='ru'):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('account/achievements') \
            .set_application_id(self.application_id) \
            .add_parameter('account_id', account_id) \
            .add_parameter('access_token', self.access_token) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language)
        return self.get_json(builder.url)
