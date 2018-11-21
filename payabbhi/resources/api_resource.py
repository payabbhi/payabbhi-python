import inspect
import json
import sys

from payabbhi import http_client

try:
    import urlparse
    import urllib
except ImportError:
    import urllib.parse as urlparse


class APIResource(http_client.HTTPClient):

    def __init__(self, client=None):
        self.client = client

    def pretty_print(self):
        new_dict = {}
        for key, value in self.__dict__.items():
            if key != 'client':
                if isinstance(value, list):
                    new_dict[key] = [json.loads(i.pretty_print()) for i in value]
                elif isinstance(value, APIResource):
                    new_dict[key] = json.loads(value.pretty_print())
                else:
                    new_dict[key] = value
        return json.dumps(new_dict, indent=4)

    def __str__(self):
        return self.pretty_print()

    def __repr__(self):
        return self.pretty_print()

    def class_url(self):
        stack = inspect.stack()
        called_class = stack[1][0].f_locals["self"].__class__
        called_class = str(called_class)
        class_name = called_class[8:len(called_class)-2]
        splitted_class_name = str(class_name).split(".")
        cls_name = splitted_class_name[len(splitted_class_name)-1].lower()
        return "/api/v1/%ss" % (cls_name,)

    def instance_url(self, instance_id):
        class_url = self.class_url()
        if sys.version_info[0] >= 3:
            return class_url + '/' + urlparse.quote(instance_id.encode('utf8'))

        return class_url + '/' + urllib.quote(instance_id.encode('utf8'))

    def _all(self, data, **kwargs):
        return self._get(self.class_url(), data, **kwargs)

    def _retrieve(self, _id, **kwargs):
        return self._get(self.instance_url(_id), {}, **kwargs)

    def _get(self, path, params, **kwargs):
        return self.request('GET', path, self.client, params=params, **kwargs)

    def _post(self, path, data, **kwargs):
        return self.request('POST', path, self.client, data=data, **kwargs)

    def _put(self, path, data, **kwargs):
        return self.request('PUT', path, self.client, data=data, **kwargs)

    def _delete(self, _id, **kwargs):
        return self.request('DELETE', self.instance_url(_id), self.client, data=None, **kwargs)
