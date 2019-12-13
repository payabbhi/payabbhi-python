import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_list_of_transfers, assert_transfer


class TestTransfer(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.transfer_id = 'dummy_transfer_id'
        self.transfer_url = payabbhi.api_base + '/api/v1/transfers'
        self.source_id = 'dummy_source_id'

    @responses.activate
    def test_transfer_all(self):
        result = mock_file('dummy_transfer_collection')
        responses.add(responses.GET, self.transfer_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.transfer.all()
        resp = json.loads(result)
        assert_list_of_transfers(self, response, resp)

    @responses.activate
    def test_transfer_with_options(self):
        result = mock_file('dummy_transfer_collection')
        count = 3
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.transfer_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.transfer.all(data={'count': count, 'skip':skip})
        resp = json.loads(result)
        assert_list_of_transfers(self, response, resp)

    @responses.activate
    def test_transfer_retrieve(self):
        result = mock_file('dummy_transfer')
        url = '{0}/{1}'.format(self.transfer_url, self.transfer_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.transfer.retrieve(self.transfer_id)
        resp = json.loads(result)
        assert_transfer(self, response, resp)

    @responses.activate
    def test_transfer_create(self):
        result = mock_file('dummy_transfer_collection')
        url = self.transfer_url
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.transfer.create(data={'transfers':[{'source_id':self.source_id, 'amount':20,'currency':'INR','recipient_id':'recp_Za30i2k3p6blq3i1'},
                                                                                  {'source_id':self.source_id, 'amount':30,'currency':'INR','recipient_id':'recp_Y2ojRlJVqRMhB0Ay'}]})
        resp = json.loads(result)
        assert_list_of_transfers(self, response, resp)
