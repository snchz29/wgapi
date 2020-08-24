URL = "https://api.worldoftanks.ru/"


class URLBuilder:
    def __init__(self, prefix):
        self.url = URL + prefix + '/'

    def set_request_target(self, target):
        self.url += '/' + target + '/?'
        return self

    def set_application_id(self, app_id):
        self.url += 'application_id=' + app_id
        return self

    def add_parameter(self, param, value):
        if value is None:
            return self
        elif type(value) is list and len(value) > 0:
            self.url += '&' + param + '=' + ','.join(value)
            return self
        self.url += '&' + param + '=' + str(value)
        return self

    def __str__(self):
        return self.url

