import os
import payabbhi
import unittest2


def mock_file(filename):
    if not filename:
        return ''
    file_dir = os.path.dirname(__file__)
    file_path = "{0}/mocks/{1}.json".format(file_dir, filename)
    with open(file_path, 'r') as f:
        return f.read()

def assert_order(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Order), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.amount, expected.get('amount'))
    self.assertEqual(actual.currency, expected.get('currency'))
    self.assertEqual(actual.status, expected.get('status'))
    self.assertEqual(actual.created_at, expected.get('created_at'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.merchant_order_id, expected.get('merchant_order_id'))
    self.assertEqual(actual.payment_attempts, expected.get('payment_attempts'))


def assert_payment(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Payment), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.amount, expected.get('amount'))
    self.assertEqual(actual.currency, expected.get('currency'))
    self.assertEqual(actual.status, expected.get('status'))
    self.assertEqual(actual.description, expected.get('description'))
    self.assertEqual(actual.created_at, expected.get('created_at'))
    self.assertEqual(actual.bank, expected.get('bank'))
    self.assertEqual(actual.card, expected.get('card'))
    self.assertEqual(actual.contact, expected.get('contact'))
    self.assertEqual(actual.email, expected.get('email'))
    self.assertEqual(actual.error_code, expected.get('error_code'))
    self.assertEqual(actual.error_description, expected.get('error_description'))
    self.assertEqual(actual.fee, expected.get('fee'))
    self.assertEqual(actual.international, expected.get('international'))
    self.assertEqual(actual.method, expected.get('method'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.order_id, expected.get('order_id'))
    self.assertEqual(actual.payout_amount, expected.get('payout_amount'))
    self.assertEqual(actual.payout_type, expected.get('payout_type'))
    self.assertEqual(actual.refund_status, expected.get('refund_status'))
    self.assertEqual(actual.refunded_amount, expected.get('refunded_amount'))
    self.assertEqual(actual.service_tax, expected.get('service_tax'))
    self.assertEqual(actual.wallet, expected.get('wallet'))
    assert_list_of_refunds(self, actual.refunds, expected.get('refunds'))

def assert_refund(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Refund), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.amount, expected.get('amount'))
    self.assertEqual(actual.currency, expected.get('currency'))
    self.assertEqual(actual.created_at, expected.get('created_at'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.payment_id, expected.get('payment_id'))

def assert_list_of_orders(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (order_actual, order_expected) in zip(actual.data, expected.get('data')):
        assert_order(self, order_actual, order_expected)

def assert_list_of_payments(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (payment_actual, payment_expected) in zip(actual.data, expected.get('data')):
        assert_payment(self, payment_actual, payment_expected)

def assert_list_of_refunds(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (refund_actual, refund_expected) in zip(actual.data, expected.get('data')):
        assert_refund(self, refund_actual, refund_expected)
