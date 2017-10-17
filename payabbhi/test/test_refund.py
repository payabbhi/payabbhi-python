import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_list_of_refunds, assert_refund

class TestRefund(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.refund_id = 'dummy_refund_id'
        self.refund_url = payabbhi.api_base + '/api/v1/refunds'
        self.payment_url = payabbhi.api_base + '/api/v1/payments'
        self.payment_id = 'dummy_payment_id'

    @responses.activate
    def test_refund_all(self):
        result = mock_file('dummy_refund_collection')
        responses.add(responses.GET, self.refund_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.refund.all()
        resp = json.loads(result)
        assert_list_of_refunds(self, response, resp)

    @responses.activate
    def test_refund_with_options(self):
        result = mock_file('dummy_refund_collection_filters')
        count = 5
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.refund_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.refund.all(data={'count': count, 'skip': skip})
        resp = json.loads(result)
        assert_list_of_refunds(self, response, resp)

    @responses.activate
    def test_refund_retrieve(self):
        result = mock_file('dummy_refund')
        url = '{0}/{1}'.format(self.refund_url, self.refund_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.refund.retrieve(self.refund_id)
        resp = json.loads(result)
        assert_refund(self, response, resp)

    @responses.activate
    def test_refund_create(self):
        result = mock_file('dummy_payment_refund')
        url = '{0}/{1}/refunds'.format(self.payment_url, self.payment_id)
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.refund.create(self.payment_id, amount=5000, currency="INR", notes="{\"merchant_order_id\":\"M1234\"}")
        resp = json.loads(result)
        assert_refund(self, response, resp)
