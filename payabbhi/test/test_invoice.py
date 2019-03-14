import json
import sys

import payabbhi
import responses
import unittest2

from .helpers import (assert_invoice, assert_list_of_invoice_items,
                      assert_list_of_invoices, assert_list_of_payments,
                      mock_file)


class TestInvoice(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(
            access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.invoice_id = 'dummy_invoice_id'
        self.invoice_url = payabbhi.api_base + '/api/v1/invoices'

    @responses.activate
    def test_invoice_all(self):
        result = mock_file('dummy_invoice_collection')
        responses.add(responses.GET, self.invoice_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.invoice.all()
        resp = json.loads(result)
        assert_list_of_invoices(self, response, resp)

    @responses.activate
    def test_invoice_with_options(self):
        result = mock_file('dummy_invoice_collection_filters')
        count = 3
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.invoice_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.invoice.all(data={'count': count, 'skip': skip})
        resp = json.loads(result)
        assert_list_of_invoices(self, response, resp)

    @responses.activate
    def test_invoice_retrieve(self):
        result = mock_file('dummy_invoice')
        url = '{0}/{1}'.format(self.invoice_url, self.invoice_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.invoice.retrieve(self.invoice_id)
        resp = json.loads(result)
        assert_invoice(self, response, resp)

    @responses.activate
    def test_invoice_create(self):
        result = mock_file('dummy_invoice')
        url = self.invoice_url
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.invoice.create(data={'customer_id': 'dummy_customer_id', 'invoice_no': '123123123123', 'due_date': 1549176945,
                                                    'currency': 'INR', 'description': 'TestInvoice', 'notes': {"mode": "test"}, 'line_items': [{"id": "dummy_item_id"}]})
        resp = json.loads(result)
        assert_invoice(self, response, resp)

    @responses.activate
    def test_invoice_void(self):
        result = mock_file('dummy_invoice_void')
        url = '{0}/{1}/void'.format(self.invoice_url, self.invoice_id)
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.invoice.void(self.invoice_id)
        resp = json.loads(result)
        assert_invoice(self, response, resp)

    @responses.activate
    def test_invoice_retrieve_lineitems(self):
        result = mock_file('dummy_invoice_lineitems')
        url = '{0}/{1}/line_items'.format(self.invoice_url, self.invoice_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.invoice.line_items(self.invoice_id)
        resp = json.loads(result)
        assert_list_of_invoice_items(self, response, resp)

    @responses.activate
    def test_invoice_retrieve_payments(self):
        result = mock_file('dummy_invoice_payments')
        url = '{0}/{1}/payments'.format(self.invoice_url, self.invoice_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.invoice.payments(self.invoice_id)
        resp = json.loads(result)
        assert_list_of_payments(self, response, resp)
