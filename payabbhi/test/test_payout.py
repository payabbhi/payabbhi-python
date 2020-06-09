import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_list_of_payouts, assert_payout


class TestPayout(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.payout_id = 'dummy_payout_id'
        self.payout_url = payabbhi.api_base + '/api/v1/payouts'

    @responses.activate
    def test_payout_all(self):
        result = mock_file('dummy_payout_collection')
        responses.add(responses.GET, self.payout_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payout.all()
        resp = json.loads(result)
        assert_list_of_payouts(self, response, resp)

    @responses.activate
    def test_payout_with_options(self):
        result = mock_file('dummy_payout_collection_filters')
        count = 2
        url = '{0}?count={1}'.format(self.payout_url, count)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payout.all(data={'count': count})
        resp = json.loads(result)
        assert_list_of_payouts(self, response, resp)

    @responses.activate
    def test_payout_retrieve(self):
        result = mock_file('dummy_payout')
        url = '{0}/{1}'.format(self.payout_url, self.payout_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payout.retrieve(self.payout_id)
        resp = json.loads(result)
        assert_payout(self, response, resp)

    @responses.activate
    def test_payout_create(self):
        result = mock_file('dummy_payout')
        url = self.payout_url
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payout.create(data={
            	'amount':1000,
            	'currency' : 'INR',
            	'merchant_reference_id' : 'ref_00001',
            	'remittance_account_no' :'1234567890',
            	'beneficiary_account_no':'01234567890',
            	'beneficiary_ifsc':'ABCD1234567',
            	'beneficiary_name':'BenTest',
            	'method':'bank_transfer',
            	'purpose':'cashback',
            	'narration':'info',
            	'instrument':'NEFT'
            })
        resp = json.loads(result)
        assert_payout(self, response, resp)
