import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_list_of_events, assert_event


class TestEvent(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.event_id = 'dummy_event_id'
        self.event_url = payabbhi.api_base + '/api/v1/events'

    @responses.activate
    def test_event_all(self):
        result = mock_file('dummy_event_collection')
        responses.add(responses.GET, self.event_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.event.all()
        resp = json.loads(result)
        assert_list_of_events(self, response, resp)

    @responses.activate
    def test_event_with_options(self):
        result = mock_file('dummy_event_collection')
        count = 3
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.event_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.event.all(data={'count': count, 'skip':skip})
        resp = json.loads(result)
        assert_list_of_events(self, response, resp)

    @responses.activate
    def test_event_retrieve(self):
        result = mock_file('dummy_event')
        url = '{0}/{1}'.format(self.event_url, self.event_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.event.retrieve(self.event_id)
        resp = json.loads(result)
        assert_event(self, response, resp)
