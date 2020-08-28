import MainAPI


class Tankopedia(MainAPI.MainAPI):
    def get_list_vehicles(self, fields=None, language='ru', limit=None, nation=None, page_no=None, tank_id=None,
                          tier=None, type_=None):
        url = 'wot/encyclopedia/vehicles/'
        req = self._get_json(url, fields=fields, language=language, limit=limit, nation=nation, page_no=page_no,
                             tank_id=tank_id, tier=tier, type=type_)
        return self._dump(req)

    def get_vehicle_characteristics(self, tank_id, engine_id=None, fields=None, gun_id=None, language='ru',
                                    profile_id=None, radio_id=None, suspension_id=None, turret_id=None):
        url = 'wot/encyclopedia/vehicleprofile/'
        req = self._get_json(url, tank_id=tank_id, engine_id=engine_id, fields=fields, gun_id=gun_id, language=language,
                             profile_id=profile_id, radio_id=radio_id, suspension_id=suspension_id, turret_id=turret_id)
        return self._dump(req)

    def get_achievements(self, fields=None, language='ru'):
        url = 'wot/encyclopedia/achievements/'
        req = self._get_json(url, fields=fields, language=language)
        return self._dump(req)

    def get_info(self, fields=None, language='ru'):
        url = 'wot/encyclopedia/info/'
        req = self._get_json(url, fields=fields, language=language)
        return self._dump(req)

    def get_maps(self, fields=None, language='ru'):
        url = 'wot/encyclopedia/arenas/'
        req = self._get_json(url, fields=fields, language=language)
        return self._dump(req)

    def get_equipments_n_consumables(self, fields=None, language='ru', limit=None, page_no=None, provision_id=None,
                                     type_=None):
        url = 'wot/encyclopedia/provisions/'
        req = self._get_json(url, fields=fields, language=language, limit=limit, page_no=page_no,
                             provision_id=provision_id)
        return self._dump(req)

    def get_personal_missions(self, campaign_id=None, fields=None, language=None, operation_id=None, set_id=None,
                              tag=None):
        url = 'wot/encyclopedia/personalmissions/'
        req = self._get_json(url, campaign_id=campaign_id, fields=fields, language=language, operation_id=operation_id,
                             set_id=set_id, tag=tag)
        return self._dump(req)

    def get_boosters(self, fields=None, language='ru'):
        url = 'wot/encyclopedia/boosters/'
        req = self._get_json(url, fields=fields, language=language)
        return self._dump(req)

    def get_vehicle_configurations(self, tank_id=None, fields=None, language=None, order_by=None):
        url = 'wot/encyclopedia/vehicleprofiles/'
        req = self._get_json(url, tank_id=tank_id, fields=fields, language=language, order_by=order_by)
        return self._dump(req)

    def get_modules(self, extra=None, fields=None, language=None, limit=None, module_id=None, nation=None, page_no=None,
                    type_=None):
        url = 'wot/encyclopedia/modules/'
        req = self._get_json(url, extra=extra, fields=fields, language=language, limit=limit, module_id=module_id,
                             nation=nation, page_no=page_no, type=type_)
        return self._dump(req)
