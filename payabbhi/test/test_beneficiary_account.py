import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_list_of_beneficiary_accounts, assert_beneficiary_account


class TestBeneficiaryAccount(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.beneficiary_id = 'dummy_beneficiary_account_id'
        self.beneficiary_url = payabbhi.api_base + '/api/v1/beneficiaryaccounts'

    @responses.activate
    def test_beneficiary_account_all(self):
        result = mock_file('dummy_beneficiary_account_collection')
        responses.add(responses.GET, self.beneficiary_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.beneficiaryaccount.all()
        resp = json.loads(result)
        assert_list_of_beneficiary_accounts(self, response, resp)

    @responses.activate
    def test_beneficiary_account_with_options(self):
        result = mock_file('dummy_beneficiary_account_collection_filters')
        count = 3
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.beneficiary_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.beneficiaryaccount.all(data={'count': count, 'skip':skip})
        resp = json.loads(result)
        assert_list_of_beneficiary_accounts(self, response, resp)

    @responses.activate
    def test_beneficiary_account_retrieve(self):
        result = mock_file('dummy_beneficiary_account')
        url = '{0}/{1}'.format(self.beneficiary_url, self.beneficiary_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.beneficiaryaccount.retrieve(self.beneficiary_id)
        resp = json.loads(result)
        assert_beneficiary_account(self, response, resp)

    @responses.activate
    def test_beneficiary_account_create(self):
        result = mock_file('dummy_beneficiary_account')
        url = self.beneficiary_url
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.beneficiaryaccount.create(data={'name':'Bruce Wayne', 'beneficiary_name':'ben_test', 'ifsc':'IFSC0001890', 'bank_account_number':'50100000219', 'account_type':'Savings'})
        resp = json.loads(result)
        assert_beneficiary_account(self, response, resp)
