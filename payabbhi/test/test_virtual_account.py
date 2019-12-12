import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_list_of_virtual_accounts, assert_list_of_payments, assert_virtual_account


class TestVirtualAccount(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.virtual_account_id = 'dummy_virtual_account_id'
        self.virtual_account_url = payabbhi.api_base + '/api/v1/virtual_accounts'

    @responses.activate
    def test_virtual_account_all(self):
        result = mock_file('dummy_virtual_account_collection')
        responses.add(responses.GET, self.virtual_account_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.virtual_account.all()
        resp = json.loads(result)
        assert_list_of_virtual_accounts(self, response, resp)

    @responses.activate
    def test_virtual_account_with_options(self):
        result = mock_file('dummy_virtual_account_filters')
        count = 2
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.virtual_account_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.virtual_account.all(data={'count': count, 'skip':skip})
        resp = json.loads(result)
        assert_list_of_virtual_accounts(self, response, resp)

    @responses.activate
    def test_virtual_account_retrieve(self):
        result = mock_file('dummy_virtual_account')
        url = '{0}/{1}'.format(self.virtual_account_url, self.virtual_account_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.virtual_account.retrieve(self.virtual_account_id)
        resp = json.loads(result)
        assert_virtual_account(self, response, resp)

    @responses.activate
    def test_virtual_account_create(self):
        result = mock_file('dummy_virtual_account')
        url = self.virtual_account_url
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.virtual_account.create(data={"email":"test@example.com","contact_no":"9999999999","description":"virtual_payment","collection_methods":["bank_account"],"notification_method":"both","customer_notification_by":"platform","notes":{"channel":"virtual_account"}})
        resp = json.loads(result)
        assert_virtual_account(self, response, resp)

    @responses.activate
    def test_virtual_account_close(self):
        result = mock_file('dummy_virtual_account_close')
        url = '{0}/{1}'.format(self.virtual_account_url, self.virtual_account_id)
        responses.add(responses.PATCH, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.virtual_account.close(self.virtual_account_id)
        resp = json.loads(result)
        assert_virtual_account(self, response, resp)

    @responses.activate
    def test_virtual_account_retrieve_payments(self):
        result = mock_file('dummy_payment_collection')
        url = '{0}/{1}/payments'.format(self.virtual_account_url, self.virtual_account_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.virtual_account.payments(self.virtual_account_id)
        resp = json.loads(result)
        assert_list_of_payments(self, response, resp)
