import responses
import payabbhi
import unittest2
from .helpers import mock_file


class TestAPIResource(unittest2.TestCase):

    def setUp(self):
        payabbhi.api_base = 'https://payabbhi.com'
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        self.client.set_app_info('TestApplication', 'beta', 'http://www.test.com')

    @responses.activate
    def test_class_url(self):
        self.assertEqual('/api/v1/testapiresources', payabbhi.resources.APIResource().class_url())

    @responses.activate
    def test_pretty_print(self):
        payment_url = payabbhi.api_base + '/api/v1/payments'
        result = mock_file('dummy_payment_collection')
        responses.add(responses.GET, payment_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment.all()
        response.pretty_print()
