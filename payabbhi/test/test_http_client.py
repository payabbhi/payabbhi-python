import sys
import responses
import payabbhi

import unittest2
from .helpers import mock_file

class TestHTTPClient(unittest2.TestCase):

    def setUp(self):
        payabbhi.api_base = 'https://payabbhi.com'
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        self.client.set_app_info('TestApplication', 'beta', 'http://www.test.com')

    def test_build_get_query(self):
        self.assertEqual(("https://payabbhi.com/hello/world", "/hello/world"), payabbhi.HTTPClient().build_get_query('/hello/world'))
        self.assertEqual(("https://payabbhi.com/hello/world?test=check%23%23", "/hello/world?test=check%23%23"), payabbhi.HTTPClient().build_get_query('/hello/world', params={'test': 'check##'}))
        self.assertEqual(("https://payabbhi.com/hello/world%$?test=check%23%23", "/hello/world%$?&?test=check%23%23"), payabbhi.HTTPClient().build_get_query('/hello/world%$?&', params={'test': 'check##'}))

    def test_build_post_query(self):
        self.assertEqual(('https://payabbhi.com/hello/world', ''), payabbhi.HTTPClient().build_post_query('/hello/world'))
        if sys.version_info[0] <= 2:
            with self.assertRaises(payabbhi.error.InvalidRequestError) as error:
                payabbhi.HTTPClient().build_post_query('/hello/world', data='\xe1')
            self.assertTrue('message: Error in request payload formation' in str(error.exception))
            self.assertTrue('Error in request payload formation' in error.exception.description)
            self.assertIsNone(error.exception.field)

    def test_set_headers(self):
        header = payabbhi.HTTPClient().set_headers(self.client)
        self.assertEqual('application/json', header['Content-Type'])
        header = payabbhi.HTTPClient().set_headers(self.client)
        self.assertEqual('application/json', header['Content-Type'])
        header = payabbhi.HTTPClient().set_headers(self.client)
        self.assertEqual('application/json', header['Content-Type'])

        self.assertTrue('User-Agent' in header)
        self.assertTrue('X-Payabbhi-Client-User-Agent' in header)


    def test_handle_http_method(self):
        with self.assertRaises(payabbhi.error.APIError) as error:
            payabbhi.HTTPClient().handle_http_method('GETTT', '/hello/world', self.client)
        self.assertTrue('message: Unexpected Method: GETTT, field: method' in str(error.exception))
        self.assertIsNone(error.exception.http_status)
        self.assertTrue('Unexpected Method: GETTT' in error.exception.description)
        self.assertTrue('method' in error.exception.field)

    @responses.activate
    def test_handle_http_code_402(self):
        payment_url = payabbhi.api_base + '/api/v1/payments'
        result = mock_file('dummy_payment_collection')
        responses.add(responses.GET, payment_url, status=402,
                      body=result, match_querystring=True)
        with self.assertRaises(payabbhi.error.APIError) as error:
            payabbhi.HTTPClient().request('GET', '/api/v1/payments', self.client)
        self.assertTrue('message: Unexpected HTTP code: 402, http_code: 402' in str(error.exception))
        self.assertEqual(402, error.exception.http_status)
        self.assertTrue('Unexpected HTTP code: 402' in error.exception.description)
        self.assertIsNone(error.exception.field)

        responses.add(responses.POST, payment_url, status=402,
                      body=result, match_querystring=True)
        with self.assertRaises(payabbhi.error.APIError) as error:
            payabbhi.HTTPClient().request('POST', '/api/v1/payments', self.client)
        self.assertTrue('message: Unexpected HTTP code: 402, http_code: 402' in str(error.exception))
        self.assertEqual(402, error.exception.http_status)
        self.assertTrue('Unexpected HTTP code: 402' in error.exception.description)
        self.assertIsNone(error.exception.field)

    @responses.activate
    def test_handle_http_code_400(self):
        payment_url = payabbhi.api_base + '/api/v1/payments'
        result = mock_file('dummy_invalid_request')
        count = 'a'
        url = '{0}?count={1}'.format(payment_url, count)
        responses.add(responses.GET, url, status=400,
                      body=result, match_querystring=True)
        with self.assertRaises(payabbhi.error.InvalidRequestError) as error:
            self.client.payment.all(data={'count':'a'})
        self.assertTrue('message: An invalid value was specified for one of the request parameters in the URL, http_code: 400, field: count' in str(error.exception))
        self.assertEqual(400, error.exception.http_status)
        self.assertTrue('An invalid value was specified for one of the request parameters in the URL' in error.exception.description)
        self.assertTrue('count' in error.exception.field)

    @responses.activate
    def test_handle_http_code_404(self):
        result = mock_file('dummy_status_not_found')
        url = payabbhi.api_base + '/api/v1/payments123'
        responses.add(responses.GET, url, status=404,
                      body=result, match_querystring=True)
        with self.assertRaises(payabbhi.error.InvalidRequestError) as error:
            payabbhi.HTTPClient().request('GET', '/api/v1/payments123', self.client)
        self.assertTrue('message: Request URL /api/v1/payments123 does not exist. Please check documentation, http_code: 404' in str(error.exception))
        self.assertEqual(404, error.exception.http_status)
        self.assertTrue('Request URL /api/v1/payments123 does not exist. Please check documentation' in error.exception.description)

    @responses.activate
    def test_handle_http_code_401(self):
        payment_url = payabbhi.api_base + '/api/v1/payments'
        result = mock_file('dummy_authentication')
        responses.add(responses.GET, payment_url, status=401,
                      body=result, match_querystring=True)
        with self.assertRaises(payabbhi.error.AuthenticationError) as error:
            self.client.payment.all()
        self.assertTrue('message: Incorrect access_id or secret_key provided., http_code: 401' in str(error.exception))
        self.assertEqual(401, error.exception.http_status)
        self.assertTrue('Incorrect access_id or secret_key provided.' in error.exception.description)

    @responses.activate
    def test_handle_http_code_500(self):
        payment_url = payabbhi.api_base + '/api/v1/payments'
        result = mock_file('dummy_server_error')
        responses.add(responses.GET, payment_url, status=500,
                      body=result, match_querystring=True)
        with self.assertRaises(payabbhi.error.APIError) as error:
            payabbhi.HTTPClient().request('GET', '/api/v1/payments', self.client)
        self.assertTrue('message: There is some problem with the server, http_code: 500' in str(error.exception))
        self.assertEqual(500, error.exception.http_status)
        self.assertTrue('There is some problem with the server' in error.exception.description)

    @responses.activate
    def test_handle_http_code_502(self):
        result = mock_file('dummy_gateway_error')
        url = '/{0}/{1}/refunds'.format('/api/v1/payments', 'payment_id')
        responses.add(responses.POST, payabbhi.api_base + url, status=502,
                      body=result, match_querystring=True)
        with self.assertRaises(payabbhi.error.GatewayError) as error:
            payabbhi.HTTPClient().request('POST', url, self.client)
        self.assertTrue('message: Unable to create refund. Please try again., http_code: 502' in str(error.exception))
        self.assertEqual(502, error.exception.http_status)
        self.assertTrue('Unable to create refund. Please try again.' in error.exception.description)

    @responses.activate
    def test_handle_http_code_502_with_empty_message(self):
        result = mock_file('dummy_http_code_502_with_empty_message')
        url = '/{0}/{1}/refunds'.format('/api/v1/payments', 'payment_id')
        responses.add(responses.POST, payabbhi.api_base + url, status=502,
                      body=result, match_querystring=True)
        with self.assertRaises(payabbhi.error.APIError) as error:
            payabbhi.HTTPClient().request('POST', url, self.client)
        self.assertTrue('message: Something did not work as expected on our side, http_code: 502' in str(error.exception))
        self.assertEqual(502, error.exception.http_status)
        self.assertTrue('Something did not work as expected on our side' in error.exception.description)

    @responses.activate
    def test_handle_api_connection(self):
        payabbhi.api_base = 'http://payabbhi.com'
        with self.assertRaises(payabbhi.error.APIConnectionError) as error:
            self.client.payment.all()
        self.assertIsNone(error.exception.field)
        self.assertIsNone(error.exception.http_status)


    @responses.activate
    def test_handle_http_code_500_due_to_json_response(self):
        payment_url = payabbhi.api_base + '/api/v1/payments'
        result = mock_file('dummy_payment_collection')
        result += '}'
        responses.add(responses.GET, payment_url, status=500,
                      body=result, match_querystring=True)
        with self.assertRaises(payabbhi.error.APIError) as error:
            payabbhi.HTTPClient().request('GET', '/api/v1/payments', self.client)
        self.assertTrue('message: Something did not work as expected on our side, http_code: 500' in str(error.exception))
        self.assertEqual(500, error.exception.http_status)
        self.assertTrue('Something did not work as expected on our side' in error.exception.description)
