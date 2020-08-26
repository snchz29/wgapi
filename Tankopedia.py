import MainAPI
import URLBuilder


class Tankopedia(MainAPI.MainAPI):
    def get_list_vehicles(self, fields=None, language='ru', limit=None, nation=None, page_no=None, tank_id=None,
                          tier=None, type_=None):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('encyclopedia/vehicles') \
            .set_application_id(self.__application_id) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language) \
            .add_parameter('limit', limit) \
            .add_parameter('nation', nation) \
            .add_parameter('page_no', page_no) \
            .add_parameter('tank_id', tank_id) \
            .add_parameter('tier', tier) \
            .add_parameter('type', type_)
        return self.get_json(builder.url)

    def get_vehicle_characteristics(self, tank_id, engine_id=None, fields=None, gun_id=None, language='ru',
                                    profile_id=None, radio_id=None, suspension_id=None, turret_id=None):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('encyclopedia/vehicleprofile') \
            .set_application_id(self.__application_id) \
            .add_parameter('tank_id', tank_id) \
            .add_parameter('engine_id', engine_id) \
            .add_parameter('fields', fields) \
            .add_parameter('gun_id', gun_id) \
            .add_parameter('language', language) \
            .add_parameter('profile_id', profile_id) \
            .add_parameter('radio_id', radio_id) \
            .add_parameter('suspension_id', suspension_id) \
            .add_parameter('turret_id', turret_id)
        return self.get_json(builder.url)

    def get_achievements(self, fields=None, language='ru'):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('encyclopedia/achievements') \
            .set_application_id(self.__application_id) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language)
        return self.get_json(builder.url)

    def get_info(self, fields=None, language='ru'):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('encyclopedia/info') \
            .set_application_id(self.__application_id) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language)
        return self.get_json(builder.url)

    def get_maps(self, fields=None, language='ru'):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('encyclopedia/arenas') \
            .set_application_id(self.__application_id) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language)
        return self.get_json(builder.url)

    def get_equipments_n_consumables(self, fields=None, language='ru', limit=None, page_no=None, provision_id=None,
                                     type_=None):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('encyclopedia/provisions') \
            .set_application_id(self.__application_id) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language) \
            .add_parameter('limit', limit) \
            .add_parameter('page_no', page_no) \
            .add_parameter('provision_id', provision_id) \
            .add_parameter('type', type_)
        return self.get_json(builder.url)

    def get_personal_missions(self, campaign_id=None, fields=None, language=None, operation_id=None, set_id=None,
                              tag=None):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('encyclopedia/personalmissions') \
            .set_application_id(self.__application_id) \
            .add_parameter('campaign_id', campaign_id) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language) \
            .add_parameter('operation_id', operation_id) \
            .add_parameter('set_id', set_id) \
            .add_parameter('tag', tag)
        return self.get_json(builder.url)

    def get_boosters(self, fields=None, language='ru'):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('encyclopedia/boosters') \
            .set_application_id(self.__application_id) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language)
        return self.get_json(builder.url)

    def get_vehicle_configurations(self, tank_id=None, fields=None, language=None, order_by=None):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('encyclopedia/vehicleprofiles') \
            .set_application_id(self.__application_id) \
            .add_parameter('tank_id', tank_id) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language) \
            .add_parameter('order_by', order_by)
        return self.get_json(builder.url)

    def get_modules(self, extra=None, fields=None, language=None, limit=None, module_id=None, nation=None, page_no=None,
                    type_=None):
        builder = URLBuilder.URLBuilder('wot')
        builder.set_request_target('encyclopedia/modules') \
            .set_application_id(self.__application_id) \
            .add_parameter('fields', fields) \
            .add_parameter('language', language) \
            .add_parameter('limit', limit)\
            .add_parameter('module_id',module_id)\
            .add_parameter('nation', nation)\
            .add_parameter('page_no',page_no)\
            .add_parameter('type', type_)
        return self.get_json(builder.url)

