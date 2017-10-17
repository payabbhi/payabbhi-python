import responses

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

        self.assertEqual(self.client.utility.verify_payment_signature(parameters), None)

    @responses.activate
    def test_verify_payment_signature_with_exception(self):
        parameters = {}
        parameters['order_id'] = 'dummy_order_id'
        parameters['payment_id'] = 'dummy_payment_id'
        parameters['payment_signature'] = 'wrong_signature'

        self.assertRaises(SignatureVerificationError, self.client.utility.verify_payment_signature, parameters)
