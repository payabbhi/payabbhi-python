import json
import platform

import payabbhi
import requests

from .error import (APIConnectionError, APIError, AuthenticationError,
                    GatewayError, InvalidRequestError)


class HTTPClient(object):

    def build_get_query(self, path, **options):
        try:
            import urlparse
            from urllib import urlencode
        except ImportError:
            import urllib.parse as urlparse
            from urllib.parse import urlencode

        url = payabbhi.api_base + path

        url_parts = list(urlparse.urlparse(url))
        query = dict(urlparse.parse_qsl(url_parts[4]))

        if 'params' in options:
            query.update(options['params'])

        url_parts[4] = urlencode(query)
        encoded_url = urlparse.urlunparse(url_parts)
        if url_parts[4]:
            path = path+'?'+url_parts[4]
        return encoded_url, path

    def build_post_query(self, path, **options):
        url = payabbhi.api_base + path
        try:
            val = ''
            if 'data' in options:
                val = json.dumps(options['data'])

        except Exception:
            raise InvalidRequestError("Error in request payload formation")
        return url, val

    def _format_app_info(self, client):
        app_info_ua = ""

        app_info = client.get_app_info()

        if app_info:
            if 'name' in app_info:
                app_info_ua += app_info['name']
                if 'version' in app_info:
                    app_info_ua += ('/' + app_info['version'])
                if 'url' in app_info:
                    app_info_ua += (' (' + app_info['url'] + ')')
        return app_info_ua

    def set_headers(self, client):

        app_info = client.get_app_info()

        ua_string = 'Payabbhi/v1 PythonBindings/' + client.VERSION

        user_agent = {
            'bindings_version': client.VERSION,
            'lang': 'python',
            'publisher': 'payabbhi',
            'httplib': requests.__name__
        }

        for attr, func in [['lang_version', platform.python_version],
                           ['platform', platform.platform],
                           ['uname', lambda: ' '.join(platform.uname())]]:
            try:
                val = func()
            except Exception as exception:
                raise APIError(str(exception))
            user_agent[attr] = val

        if app_info:
            user_agent['application'] = app_info
            ua_string += ' ' + self._format_app_info(client)

        headers = {
            'Content-Type': 'application/json',
            'X-Payabbhi-Client-User-Agent':  json.dumps(user_agent),
            'User-Agent': ua_string
        }
        return headers

    def handle_http_method(self, method, path, client, **options):
        if method == 'GET':
            url, path = self.build_get_query(path, **options)
            headers = self.set_headers(client)
            return url, headers, None
        if method == 'POST':
            url, body = self.build_post_query(path, **options)
            headers = self.set_headers(client)
            return url, headers, body
        else:
            msg = 'Unexpected Method: ' + method
            raise APIError(msg, None, "method")

    def handle_http_code(self, response):
        if response.status_code == 200:
            return
        else:
            error_response = response.json()
            msg = ''
            field = ''
            if 'error' in error_response:
                msg = error_response['error']['message']
                field = error_response['error']['field']
            if response.status_code == 400 or response.status_code == 404:
                raise InvalidRequestError(msg, response.status_code, field)
            if response.status_code == 401:
                raise AuthenticationError(msg, response.status_code, field)
            elif response.status_code == 500:
                raise APIError(msg, response.status_code)
            elif response.status_code == 502:
                if msg:
                    raise GatewayError(msg, response.status_code)
                else:
                    raise APIError("Something did not work as expected on our side",
                                   response.status_code)
            else:
                msg = "Unexpected HTTP code: " + str(response.status_code)
                raise APIError(msg, response.status_code)

    def request(self, method, path, client, **options):
        url, headers, body = self.handle_http_method(method, path, client, **options)
        try:
            response = getattr(requests.Session(), method.lower())(url,
                                                                   auth=(client.access_id, client.secret_key),
                                                                   headers=headers,
                                                                   data=body)
        except Exception as exception:
            raise APIConnectionError(str(exception))
        try:
            json_resp = response.json()
        except Exception:
            raise APIError("Something did not work as expected on our side", 500)
        self.handle_http_code(response)
        return self.convert_to_object(json_resp, client)

    def convert_to_object(self, resp, client):
        types = {
            'order': payabbhi.resources.Order,
            'payment': payabbhi.resources.Payment,
            'refund': payabbhi.resources.Refund,
            'list': payabbhi.resources.List,
        }
        klass_name = resp.get('object')
        if not klass_name:
            return resp
        klass = types.get(klass_name)
        new_object = klass(client=client)
        for key, value in resp.items():
            if isinstance(value, list):
                arr = [self.convert_to_object(i, client) for i in value]
                setattr(new_object, key, arr)
            elif isinstance(value, dict):
                setattr(new_object, key, self.convert_to_object(value, client))
            else:
                setattr(new_object, key, value)
        return new_object
