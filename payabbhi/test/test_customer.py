import json
import sys

import payabbhi
import responses
import unittest2

from .helpers import assert_customer, assert_list_of_customers, mock_file


class TestCustomer(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(
            access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.customer_id = 'dummy_customer_id'
        self.customer_url = payabbhi.api_base + '/api/v1/customers'

    @responses.activate
    def test_customer_all(self):
        result = mock_file('dummy_customer_collection')
        responses.add(responses.GET, self.customer_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.customer.all()
        resp = json.loads(result)
        assert_list_of_customers(self, response, resp)

    @responses.activate
    def test_customer_with_options(self):
        result = mock_file('dummy_customer_collection_filters')
        count = 3
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.customer_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.customer.all(
            data={'count': count, 'skip': skip})
        resp = json.loads(result)
        assert_list_of_customers(self, response, resp)

    @responses.activate
    def test_customer_retrieve(self):
        result = mock_file('dummy_customer')
        url = '{0}/{1}'.format(self.customer_url, self.customer_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.customer.retrieve(self.customer_id)
        resp = json.loads(result)
        assert_customer(self, response, resp)

    @responses.activate
    def test_customer_create(self):
        result = mock_file('dummy_customer')
        url = self.customer_url
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.customer.create(
            data={'email': 'a@b.com', 'contact_no': '9999999999'})
        resp = json.loads(result)
        assert_customer(self, response, resp)

    @responses.activate
    def test_customer_edit(self):
        result = mock_file('dummy_customer_edit')
        url = '{0}/{1}'.format(self.customer_url, self.customer_id)
        responses.add(responses.PUT, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.customer.edit(
            self.customer_id, data={'email': 'b@c.com', 'contact_no': '1234567890'})
        resp = json.loads(result)
        assert_customer(self, response, resp)
