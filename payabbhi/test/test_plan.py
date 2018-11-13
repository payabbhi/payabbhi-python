import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_list_of_plans, assert_plan


class TestPlan(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.plan_id = 'dummy_plan_id'
        self.plan_url = payabbhi.api_base + '/api/v1/plans'

    @responses.activate
    def test_plan_all(self):
        result = mock_file('dummy_plan_collection')
        responses.add(responses.GET, self.plan_url, status=200,
                      body=result, match_querystring=True)
        response = self.client.plan.all()
        resp = json.loads(result)
        assert_list_of_plans(self, response, resp)

    @responses.activate
    def test_plan_with_options(self):
        result = mock_file('dummy_plan_collection_filters')
        count = 3
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.plan_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.plan.all(data={'count': count, 'skip':skip})
        resp = json.loads(result)
        assert_list_of_plans(self, response, resp)

    @responses.activate
    def test_plan_retrieve(self):
        result = mock_file('dummy_plan')
        url = '{0}/{1}'.format(self.plan_url, self.plan_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.plan.retrieve(self.plan_id)
        resp = json.loads(result)
        assert_plan(self, response, resp)

    @responses.activate
    def test_plan_create(self):
        result = mock_file('dummy_plan')
        url = self.plan_url
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.plan.create(data={'product_id':'prod_wJ6DyX5Bgg2LqAqt', 'amount':100,'currency':'INR','frequency':2,'interval':'month(s)'})
        resp = json.loads(result)
        assert_plan(self, response, resp)
