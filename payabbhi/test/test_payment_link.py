import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_list_of_payment_links, assert_list_of_payments, assert_payment_link


class TestPaymentLink(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.payment_link_id = 'dummy_payment_link_id'
        self.payment_link_url = payabbhi.api_base + '/api/v1/payment_links'

    @responses.activate
    def test_payment_link_all(self):
        result = mock_file('dummy_payment_link_collection')
        responses.add(responses.GET, self.payment_link_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment_link.all()
        resp = json.loads(result)
        assert_list_of_payment_links(self, response, resp)

    @responses.activate
    def test_payment_link_with_options(self):
        result = mock_file('dummy_payment_link_collection_filters')
        count = 3
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.payment_link_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment_link.all(data={'count': count, 'skip':skip})
        resp = json.loads(result)
        assert_list_of_payment_links(self, response, resp)

    @responses.activate
    def test_payment_link_retrieve(self):
        result = mock_file('dummy_payment_link')
        url = '{0}/{1}'.format(self.payment_link_url, self.payment_link_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment_link.retrieve(self.payment_link_id)
        resp = json.loads(result)
        assert_payment_link(self, response, resp)

    @responses.activate
    def test_payment_link_create(self):
        result = mock_file('dummy_payment_link')
        url = self.payment_link_url
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment_link.create(data={'name':'Bruce', 'amount':100, 'currency':'INR', 'email': 'a@b.com', 'contact_no': '9999999999', 'receipt_no': 'Test_R123'})
        resp = json.loads(result)
        assert_payment_link(self, response, resp)

    @responses.activate
    def test_payment_link_cancel(self):
        result = mock_file('dummy_payment_link_cancel')
        url = '{0}/{1}/cancel'.format(self.payment_link_url, self.payment_link_id)
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment_link.cancel(self.payment_link_id)
        resp = json.loads(result)
        assert_payment_link(self, response, resp)

    @responses.activate
    def test_payment_link_retrieve_payments(self):
        result = mock_file('dummy_payment_link_payments')
        url = '{0}/{1}/payments'.format(self.payment_link_url, self.payment_link_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment_link.payments(self.payment_link_id)
        resp = json.loads(result)
        assert_list_of_payments(self, response, resp)
