import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_list_of_settlements, assert_settlement


class TestSettlement(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.settlement_id = 'dummy_settlement_id'
        self.settlement_url = payabbhi.api_base + '/api/v1/settlements'

    @responses.activate
    def test_settlement_all(self):
        result = mock_file('dummy_settlement_collection')
        responses.add(responses.GET, self.settlement_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.settlement.all()
        resp = json.loads(result)
        assert_list_of_settlements(self, response, resp)

    @responses.activate
    def test_settlement_with_options(self):
        result = mock_file('dummy_settlement_collection_filters')
        count = 2
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.settlement_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.settlement.all(data={'count': count, 'skip': skip})
        resp = json.loads(result)
        assert_list_of_settlements(self, response, resp)

    @responses.activate
    def test_settlement_retrieve(self):
        result = mock_file('dummy_settlement')
        url = '{0}/{1}'.format(self.settlement_url, self.settlement_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.settlement.retrieve(self.settlement_id)
        resp = json.loads(result)
        assert_settlement(self, response, resp)
