import responses
import time
import hmac
import hashlib
import payabbhi

import unittest2
from ..error import SignatureVerificationError

class TestClientValidator(unittest2.TestCase):

    def setUp(self):
        self.client = payabbhi.Client(access_id='access_id', secret_key='secret_key')

    @responses.activate
    def test_verify_payment_signature(self):
        sig = 'e70360e32919311d31cbc9b558ea9024715b816ce64293ffc992459a94daac42'
        parameters = {}
        parameters['order_id'] = 'dummy_order_id'
        parameters['payment_id'] = 'dummy_payment_id'
        parameters['payment_signature'] = sig

        self.assertEqual(self.client.utility.verify_payment_signature(parameters), True)

    @responses.activate
    def test_verify_payment_signature_with_exception(self):
        parameters = {}
        parameters['order_id'] = 'dummy_order_id'
        parameters['payment_id'] = 'dummy_payment_id'
        parameters['payment_signature'] = 'wrong_signature'

        self.assertRaises(SignatureVerificationError, self.client.utility.verify_payment_signature, parameters)

    @responses.activate
    def test_verify_webhook_signature(self):
        payload = '{"event":"payment.captured"}'
        t = int(time.time())
        secret="skw_live_jHNxKsDqJusco5hA"
        message = payload + '&' + str(t)
        v1 = hmac.new(secret, message, hashlib.sha256).hexdigest()
        actual_signature = "t=" + str(t) + ", v1=" + v1
        self.assertEqual(self.client.utility.verify_webhook_signature(payload,actual_signature,secret), True)

    @responses.activate
    def test_verify_webhook_signature_with_replay(self):
        payload = '{"event":"payment.captured"}'
        t = int(time.time())
        secret="skw_live_jHNxKsDqJusco5hA"
        message = payload + '&' + str(t)
        v1 = hmac.new(secret, message, hashlib.sha256).hexdigest()
        actual_signature = "t=" + str(t) + ", v1=" + v1
        self.assertEqual(self.client.utility.verify_webhook_signature(payload,actual_signature,secret,30), True)

    @responses.activate
    def test_verify_webhook_signature_with_error(self):
        payload = '{"event":"payment.captured"}'
        t = int(time.time()) - 40
        secret="skw_live_jHNxKsDqJusco5hA"
        message = payload + '&' + str(t)
        v1 = hmac.new(secret, message, hashlib.sha256).hexdigest()
        actual_signature = "t=" + str(t) + ", v1=" + v1
        self.assertRaises(SignatureVerificationError, self.client.utility.verify_webhook_signature, payload,actual_signature,secret,30)
