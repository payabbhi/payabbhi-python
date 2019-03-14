import json
import sys

import payabbhi
import responses
import unittest2

from .helpers import (assert_list_of_subscriptions, assert_subscription,
                      mock_file)


class TestSubscription(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(
            access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.subscription_id = 'dummy_subscription_id'
        self.subscription_url = payabbhi.api_base + '/api/v1/subscriptions'

    @responses.activate
    def test_subscription_all(self):
        result = mock_file('dummy_subscription_collection')
        responses.add(responses.GET, self.subscription_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.subscription.all()
        resp = json.loads(result)
        assert_list_of_subscriptions(self, response, resp)

    @responses.activate
    def test_subscription_with_options(self):
        result = mock_file('dummy_subscription_collection_filters')
        count = 3
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(
            self.subscription_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.subscription.all(
            data={'count': count, 'skip': skip})
        resp = json.loads(result)
        assert_list_of_subscriptions(self, response, resp)

    @responses.activate
    def test_subscription_retrieve(self):
        result = mock_file('dummy_subscription')
        url = '{0}/{1}'.format(self.subscription_url, self.subscription_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.subscription.retrieve(self.subscription_id)
        resp = json.loads(result)
        assert_subscription(self, response, resp)

    @responses.activate
    def test_subscription_create(self):
        result = mock_file('dummy_subscription')
        url = self.subscription_url
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.subscription.create(
            data={'plan_id': 'dummy_plan_id', 'customer_id': 'dummy_customer_id', 'billing_cycle_count': 5})
        resp = json.loads(result)
        assert_subscription(self, response, resp)

    @responses.activate
    def test_subscription_cancel(self):
        result = mock_file('dummy_subscription_cancel')
        url = '{0}/{1}/cancel'.format(self.subscription_url,
                                      self.subscription_id)
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.subscription.cancel(self.subscription_id)
        resp = json.loads(result)
        assert_subscription(self, response, resp)
