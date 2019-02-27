import sys
import json
import responses
import payabbhi

import unittest2
from .helpers import mock_file, assert_payment, assert_list_of_refunds, assert_refund, assert_list_of_payments, assert_list_of_transfers

class TestPayment(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')
        payabbhi.api_base = 'https://payabbhi.com'
        self.payment_id = 'dummy_payment_id'
        self.payment_url = payabbhi.api_base + '/api/v1/payments'

    @responses.activate
    def test_payment_all(self):
        result = mock_file('dummy_payment_collection')
        responses.add(responses.GET, self.payment_url, status=200,
                      body=result, match_querystring=True, content_type="application/json")
        response = self.client.payment.all()
        resp = json.loads(result)
        assert_list_of_payments(self, response, resp)

    @responses.activate
    def test_payment_with_options(self):
        result = mock_file('dummy_payment_collection_filters')
        count = 4
        skip = 2
        url = '{0}?count={1}&skip={2}'.format(self.payment_url, count, skip)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment.all(data={'count': count, 'skip': skip})
        resp = json.loads(result)
        assert_list_of_payments(self, response, resp)

    @responses.activate
    def test_payment_retrieve(self):
        result = mock_file('dummy_payment')
        url = '{0}/{1}'.format(self.payment_url, self.payment_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment.retrieve(self.payment_id)
        resp = json.loads(result)
        assert_payment(self, response, resp)

    @responses.activate
    def test_payment_retrieve_refunds(self):
        result = mock_file('dummy_payment_refunds')
        url = '{0}/{1}/refunds'.format(self.payment_url, self.payment_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment.refunds(self.payment_id)
        resp = json.loads(result)
        assert_list_of_refunds(self, response, resp)

    @responses.activate
    def test_payment_retrieves_refunds_with_options(self):
        result = mock_file('dummy_payment_refunds_collection_filters')
        count = 1
        url = '{0}/{1}/refunds?count={2}'.format(self.payment_url, self.payment_id, count)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment.refunds(self.payment_id, data={'count':1})
        resp = json.loads(result)
        assert_list_of_refunds(self, response, resp)

    @responses.activate
    def test_payment_capture(self):
        result = mock_file('dummy_payment_capture')
        url = '{0}/{1}/capture'.format(self.payment_url, self.payment_id)
        responses.add(responses.POST, url, status=200,
                      body=result, match_querystring=True)
        self.client.payment.id = self.payment_id
        response = self.client.payment.capture()
        resp = json.loads(result)
        assert_payment(self, response, resp)

    @responses.activate
    def test_empty_payment_capture(self):
        if sys.version_info[0] <= 2:
            with self.assertRaises(payabbhi.error.InvalidRequestError) as error:
                self.client.payment.capture()
            self.assertTrue('message: Object Id not set' in str(error.exception))
            self.assertTrue('Object Id not set' in error.exception.description)
            self.assertIsNone(error.exception.http_status)
            self.assertIsNone(error.exception.field)

    @responses.activate
    def test_payment_refund(self):
        refund_result = mock_file('dummy_payment_refund')
        refund_url = '{0}/{1}/refunds'.format(self.payment_url, self.payment_id)
        responses.add(responses.POST, refund_url, status=200,
                      body=refund_result, match_querystring=True)

        payment_result = mock_file('dummy_payment')
        retrieve_payment_url = '{0}/{1}'.format(self.payment_url, self.payment_id)
        responses.add(responses.GET, retrieve_payment_url, status=200, body=payment_result, match_querystring=True)

        self.client.payment.id = self.payment_id

        refund_response = self.client.payment.refund(data={'amount':5000, 'currency':'INR', 'notes':{'reason': 'order cancelled'}})
        resp = json.loads(refund_result)
        assert_refund(self, refund_response, resp)

        payment_response = self.client.payment.retrieve(self.payment_id)
        payment_resp = json.loads(payment_result)
        assert_payment(self, payment_response, payment_resp)

    @responses.activate
    def test_empty_payment_refund(self):
        if sys.version_info[0] <= 2:
            with self.assertRaises(payabbhi.error.InvalidRequestError) as error:
                self.client.payment.refund()
            self.assertTrue('message: Object Id not set' in str(error.exception))
            self.assertTrue('Object Id not set' in error.exception.description)
            self.assertIsNone(error.exception.http_status)
            self.assertIsNone(error.exception.field)

    @responses.activate
    def test_payment_retrieve_transfers(self):
        result = mock_file('dummy_transfer_collection')
        url = '{0}/{1}/transfers'.format(self.payment_url, self.payment_id)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment.transfers(self.payment_id)
        resp = json.loads(result)
        assert_list_of_transfers(self, response, resp)

    @responses.activate
    def test_payment_retrieves_transfers_with_options(self):
        result = mock_file('dummy_transfer_collection')
        count = 1
        url = '{0}/{1}/transfers?count={2}'.format(self.payment_url, self.payment_id, count)
        responses.add(responses.GET, url, status=200,
                      body=result, match_querystring=True)
        response = self.client.payment.transfers(self.payment_id, data={'count':1})
        resp = json.loads(result)
        assert_list_of_transfers(self, response, resp)
