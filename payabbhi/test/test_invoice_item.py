import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_list_of_invoice_items, assert_invoice_item


class TestInvoiceItem(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.invoice_item_id = 'dummy_invoice_item_id'
        self.invoice_item_url = payabbhi.api_base + '/api/v1/invoiceitems'

    @responses.activate
    def test_invoice_item_all(self):
        result = mock_file('dummy_invoice_item_collection')
        responses.add(responses.GET, self.invoice_item_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.invoice_item.all()
        resp = json.loads(result)
        assert_list_of_invoice_items(self, response, resp)

    @responses.activate
    def test_invoice_item_with_options(self):
        result = mock_file('dummy_invoice_item_collection_filters')
        count = 3
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.invoice_item_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.invoice_item.all(data={'count': count, 'skip':skip})
        resp = json.loads(result)
        assert_list_of_invoice_items(self, response, resp)

    @responses.activate
    def test_invoice_item_retrieve(self):
        result = mock_file('dummy_invoice_item')
        url = '{0}/{1}'.format(self.invoice_item_url, self.invoice_item_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.invoice_item.retrieve(self.invoice_item_id)
        resp = json.loads(result)
        assert_invoice_item(self, response, resp)

    @responses.activate
    def test_invoice_item_create(self):
        result = mock_file('dummy_invoice_item')
        url = self.invoice_item_url
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.invoice_item.create(data={'customer_id':'cust_2WmsQoSRZMWWkcZg', 'name':'Line Item', 'currency':'INR', 'amount':200})
        resp = json.loads(result)
        assert_invoice_item(self, response, resp)

    @responses.activate
    def test_invoice_item_delete(self):
        result = mock_file('dummy_invoice_item_delete')
        url = '{0}/{1}'.format(self.invoice_item_url, self.invoice_item_id)
        responses.add(responses.DELETE, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.invoice_item.delete(self.invoice_item_id)
        resp = json.loads(result)
        assert_invoice_item(self, response, resp)
