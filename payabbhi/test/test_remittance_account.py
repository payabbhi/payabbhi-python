import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_remittance_account


class TestRemittanceAccount(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.remittance_account_id = 'dummy_remittance_account_id'
        self.remittance_account_url = payabbhi.api_base + '/api/v1/remittance_accounts'

    @responses.activate
    def test_remittance_account_retrieve(self):
        result = mock_file('dummy_remittance_account')
        url = '{0}/{1}'.format(self.remittance_account_url, self.remittance_account_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.remittance_account.retrieve(self.remittance_account_id)
        resp = json.loads(result)
        assert_remittance_account(self, response, resp)
