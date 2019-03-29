import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_list_of_products, assert_product


class TestProduct(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.product_id = 'dummy_product_id'
        self.product_url = payabbhi.api_base + '/api/v1/products'

    @responses.activate
    def test_product_all(self):
        result = mock_file('dummy_product_collection')
        responses.add(responses.GET, self.product_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.product.all()
        resp = json.loads(result)
        assert_list_of_products(self, response, resp)

    @responses.activate
    def test_product_with_options(self):
        result = mock_file('dummy_product_collection_filters')
        count = 3
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.product_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.product.all(data={'count': count, 'skip':skip})
        resp = json.loads(result)
        assert_list_of_products(self, response, resp)

    @responses.activate
    def test_product_retrieve(self):
        result = mock_file('dummy_product')
        url = '{0}/{1}'.format(self.product_url, self.product_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.product.retrieve(self.product_id)
        resp = json.loads(result)
        assert_product(self, response, resp)

    @responses.activate
    def test_product_create(self):
        result = mock_file('dummy_product')
        url = self.product_url
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.product.create(data={'name':'Books', 'unit_label':'MB', 'notes':{"genre":"comedy"}})
        resp = json.loads(result)
        assert_product(self, response, resp)
