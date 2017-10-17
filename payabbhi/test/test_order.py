import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_list_of_orders, assert_order, assert_list_of_payments


class TestOrder(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.order_id = 'dummy_order_id'
        self.order_url = payabbhi.api_base + '/api/v1/orders'

    @responses.activate
    def test_order_all(self):
        result = mock_file('dummy_order_collection')
        responses.add(responses.GET, self.order_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.order.all()
        resp = json.loads(result)
        assert_list_of_orders(self, response, resp)

    @responses.activate
    def test_order_with_options(self):
        result = mock_file('dummy_order_collection_filters')
        count = 3
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.order_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.order.all(data={'count': count, 'skip':skip})
        resp = json.loads(result)
        assert_list_of_orders(self, response, resp)

    @responses.activate
    def test_order_retrieve(self):
        result = mock_file('dummy_order')
        url = '{0}/{1}'.format(self.order_url, self.order_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.order.retrieve(self.order_id)
        resp = json.loads(result)
        assert_order(self, response, resp)

    @responses.activate
    def test_order_create(self):
        result = mock_file('dummy_order')
        url = self.order_url
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.order.create(data={'amount':100, 'merchant_order_id':'M123', 'currency':'INR', 'payment_auto_capture':False, 'notes':{"merchant_order_id":"M123"}})
        resp = json.loads(result)
        assert_order(self, response, resp)

    @responses.activate
    def test_order_retrieve_payments(self):
        result = mock_file('dummy_order_payments')
        url = '{0}/{1}/payments'.format(self.order_url, self.order_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        self.client.order.id = self.order_id
        response = self.client.order.payments()
        resp = json.loads(result)
        assert_list_of_payments(self, response, resp)

    @responses.activate
    def test_empty_order_retrieve_payments(self):
        if sys.version_info[0] <= 2:
            with self.assertRaises(payabbhi.error.InvalidRequestError) as error:
                self.client.order.payments()
            self.assertTrue('message: Object Id not set' in str(error.exception))
            self.assertTrue('Object Id not set' in error.exception.description)
            self.assertIsNone(error.exception.http_status)
            self.assertIsNone(error.exception.field)
