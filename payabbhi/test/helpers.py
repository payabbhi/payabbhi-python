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
    self.assertEqual(actual.order_id, expected.get('order_id'))
    self.assertEqual(actual.invoice_id, expected.get('invoice_id'))
    self.assertEqual(actual.international, expected.get('international'))
    self.assertEqual(actual.method, expected.get('method'))
    self.assertEqual(actual.description, expected.get('description'))
    self.assertEqual(actual.card, expected.get('card'))
    self.assertEqual(actual.bank, expected.get('bank'))
    self.assertEqual(actual.wallet, expected.get('wallet'))
    self.assertEqual(actual.vpa, expected.get('vpa'))
    self.assertEqual(actual.customer_id, expected.get('customer_id'))
    self.assertEqual(actual.email, expected.get('email'))
    self.assertEqual(actual.contact, expected.get('contact'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.fee, expected.get('fee'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.service_tax, expected.get('service_tax'))
    self.assertEqual(actual.payout_amount, expected.get('payout_amount'))
    self.assertEqual(actual.payout_type, expected.get('payout_type'))
    self.assertEqual(actual.settled, expected.get('settled'))
    self.assertEqual(actual.settlement_id, expected.get('settlement_id'))
    self.assertEqual(actual.refunded_amount, expected.get('refunded_amount'))
    self.assertEqual(actual.refund_status, expected.get('refund_status'))
    assert_list_of_refunds(self, actual.refunds, expected.get('refunds'))
    self.assertEqual(actual.error_code, expected.get('error_code'))
    self.assertEqual(actual.error_description, expected.get('error_description'))
    self.assertEqual(actual.created_at, expected.get('created_at'))
    self.assertEqual(actual.virtual_account_id, expected.get('virtual_account_id'))
    self.assertEqual(actual.payment_page_id, expected.get('payment_page_id'))


def assert_refund(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Refund), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.amount, expected.get('amount'))
    self.assertEqual(actual.currency, expected.get('currency'))
    self.assertEqual(actual.created_at, expected.get('created_at'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.payment_id, expected.get('payment_id'))

def assert_product(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Product), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.name, expected.get('name'))
    self.assertEqual(actual.type, expected.get('type'))
    self.assertEqual(actual.unit_label, expected.get('unit_label'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.created_at, expected.get('created_at'))

def assert_plan(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Plan), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.name, expected.get('name'))
    self.assertEqual(actual.amount, expected.get('amount'))
    self.assertEqual(actual.currency, expected.get('currency'))
    self.assertEqual(actual.frequency, expected.get('frequency'))
    self.assertEqual(actual.interval, expected.get('interval'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.created_at, expected.get('created_at'))

def assert_customer(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Customer), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.name, expected.get('name'))
    self.assertEqual(actual.email, expected.get('email'))
    self.assertEqual(actual.contact_no, expected.get('contact_no'))
    self.assertEqual(actual.billing_address, expected.get('billing_address'))
    self.assertEqual(actual.shipping_address, expected.get('shipping_address'))
    self.assertEqual(actual.gstin, expected.get('gstin'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.created_at, expected.get('created_at'))
    assert_list_of_subscriptions(self, actual.subscriptions, expected.get('subscriptions'))

def assert_mandate(self, actual, expected):
    if actual != None and expected != None:
        self.assertEqual(actual.id, expected.get('id'))
        self.assertEqual(actual.object, expected.get('object'))
        self.assertEqual(actual.method, expected.get('method'))
        self.assertEqual(actual.instrument, expected.get('instrument'))
        self.assertEqual(actual.bank, expected.get('bank'))
        self.assertEqual(actual.error_description, expected.get('error_description'))
        self.assertEqual(actual.url, expected.get('url'))
        self.assertEqual(actual.status, expected.get('status'))
        self.assertEqual(actual.subscription_id, expected.get('subscription_id'))
        self.assertEqual(actual.customer_id, expected.get('customer_id'))
        self.assertEqual(actual.created_at, expected.get('created_at'))

def assert_subscription(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Subscription), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.plan_id, expected.get('plan_id'))
    self.assertEqual(actual.customer_id, expected.get('customer_id'))
    self.assertEqual(actual.billing_method, expected.get('billing_method'))
    self.assertEqual(actual.quantity, expected.get('quantity'))
    self.assertEqual(actual.customer_notification_by, expected.get('customer_notification_by'))
    self.assertEqual(actual.billing_cycle_count, expected.get('billing_cycle_count'))
    self.assertEqual(actual.paid_count, expected.get('paid_count'))
    self.assertEqual(actual.cancel_at_period_end, expected.get('cancel_at_period_end'))
    self.assertEqual(actual.due_at, expected.get('due_at'))
    self.assertEqual(actual.trial_end_at, expected.get('trial_end_at'))
    self.assertEqual(actual.trial_duration, expected.get('trial_duration'))
    self.assertEqual(actual.status, expected.get('status'))
    assert_mandate(self, actual.mandate, expected.get('mandate'))
    self.assertEqual(actual.current_start_at, expected.get('current_start_at'))
    self.assertEqual(actual.current_end_at, expected.get('current_end_at'))
    self.assertEqual(actual.ended_at, expected.get('ended_at'))
    self.assertEqual(actual.cancelled_at, expected.get('cancelled_at'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.created_at, expected.get('created_at'))

def assert_invoice_item(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.InvoiceItem), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.description, expected.get('description'))
    self.assertEqual(actual.amount, expected.get('amount'))
    self.assertEqual(actual.currency, expected.get('currency'))
    self.assertEqual(actual.customer_id, expected.get('customer_id'))
    self.assertEqual(actual.quantity, expected.get('quantity'))
    self.assertEqual(actual.created_at, expected.get('created_at'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.deleted_at, expected.get('deleted_at'))
    self.assertEqual(actual.unit, expected.get('unit'))
    self.assertEqual(actual.hsn_code, expected.get('hsn_code'))
    self.assertEqual(actual.sac_code, expected.get('sac_code'))
    self.assertEqual(actual.tax_rate, expected.get('tax_rate'))
    self.assertEqual(actual.cess, expected.get('cess'))
    self.assertEqual(actual.tax_inclusive, expected.get('tax_inclusive'))
    self.assertEqual(actual.discount, expected.get('discount'))
    self.assertEqual(actual.tax_amount, expected.get('tax_amount'))
    self.assertEqual(actual.net_amount, expected.get('net_amount'))
    self.assertEqual(actual.taxable_amount, expected.get('taxable_amount'))
    self.assertEqual(actual.gross_amount, expected.get('gross_amount'))

def assert_invoice(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Invoice), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.amount, expected.get('amount'))
    self.assertEqual(actual.billing_method, expected.get('billing_method'))
    self.assertEqual(actual.customer_id, expected.get('customer_id'))
    self.assertEqual(actual.currency, expected.get('currency'))
    self.assertEqual(actual.created_at, expected.get('created_at'))
    self.assertEqual(actual.description, expected.get('description'))
    self.assertEqual(actual.due_date, expected.get('due_date'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.notify_by, expected.get('notify_by'))
    self.assertEqual(actual.payment_attempt, expected.get('payment_attempt'))
    self.assertEqual(actual.invoice_no, expected.get('invoice_no'))
    self.assertEqual(actual.status, expected.get('status'))
    self.assertEqual(actual.subscription_id, expected.get('subscription_id'))
    self.assertEqual(actual.url, expected.get('url'))
    assert_list_of_invoice_items(self, actual.line_items, expected.get('line_items'))

def assert_event(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Event), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.type, expected.get('type'))
    self.assertEqual(actual.created_at, expected.get('created_at'))
    self.assertEqual(actual.environment, expected.get('environment'))
    self.assertEqual(actual.data, expected.get('data'))

def assert_transfer(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Transfer), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.description, expected.get('description'))
    self.assertEqual(actual.source_id, expected.get('source_id'))
    self.assertEqual(actual.recipient_id, expected.get('recipient_id'))
    self.assertEqual(actual.amount, expected.get('amount'))
    self.assertEqual(actual.currency, expected.get('currency'))
    self.assertEqual(actual.fees, expected.get('fees'))
    self.assertEqual(actual.gst, expected.get('gst'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.created_at, expected.get('created_at'))

def assert_settlement(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Settlement), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.amount, expected.get('amount'))
    self.assertEqual(actual.status, expected.get('status'))
    self.assertEqual(actual.currency, expected.get('currency'))
    self.assertEqual(actual.fees, expected.get('fees'))
    self.assertEqual(actual.gst, expected.get('gst'))
    self.assertEqual(actual.utr, expected.get('utr'))
    self.assertEqual(actual.settled_at, expected.get('settled_at'))

def assert_beneficiary_account(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.BeneficiaryAccount), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.name, expected.get('name'))
    self.assertEqual(actual.contact_no, expected.get('contact_no'))
    self.assertEqual(actual.email_id, expected.get('email_id'))
    self.assertEqual(actual.business_name, expected.get('business_name'))
    self.assertEqual(actual.business_entity_type, expected.get('business_entity_type'))
    self.assertEqual(actual.beneficiary_name, expected.get('beneficiary_name'))
    self.assertEqual(actual.ifsc, expected.get('ifsc'))
    self.assertEqual(actual.bank_account_number, expected.get('bank_account_number'))
    self.assertEqual(actual.account_type, expected.get('account_type'))
    self.assertEqual(actual.status, expected.get('status'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.created_at, expected.get('created_at'))

def assert_payment_link(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.PaymentLink), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.amount, expected.get('amount'))
    self.assertEqual(actual.customer_id, expected.get('customer_id'))
    self.assertEqual(actual.currency, expected.get('currency'))
    self.assertEqual(actual.description, expected.get('description'))
    self.assertEqual(actual.due_date, expected.get('due_date'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.notify_by, expected.get('notify_by'))
    self.assertEqual(actual.customer_notification_by, expected.get('customer_notification_by'))
    self.assertEqual(actual.payment_attempt, expected.get('payment_attempt'))
    self.assertEqual(actual.receipt_no, expected.get('receipt_no'))
    self.assertEqual(actual.status, expected.get('status'))
    self.assertEqual(actual.url, expected.get('url'))
    self.assertEqual(actual.created_at, expected.get('created_at'))

def assert_collection_method(self, actual, expected):
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.name, expected.get('name'))
    self.assertEqual(actual.account_no, expected.get('account_no'))
    self.assertEqual(actual.ifsc, expected.get('ifsc'))
    self.assertEqual(actual.created_at, expected.get('created_at'))

def assert_virtual_account(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.VirtualAccount), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.status, expected.get('status'))
    self.assertEqual(actual.paid_amount, expected.get('paid_amount'))
    self.assertEqual(actual.customer_id, expected.get('customer_id'))
    self.assertEqual(actual.email, expected.get('email'))
    self.assertEqual(actual.contact_no, expected.get('contact_no'))
    self.assertEqual(actual.order_id, expected.get('order_id'))
    self.assertEqual(actual.invoice_id, expected.get('invoice_id'))
    self.assertEqual(actual.description, expected.get('description'))
    for (collection_method_actual, collection_method_expected) in zip(actual.collection_methods, expected.get('collection_methods')):
        assert_collection_method(self, collection_method_actual, collection_method_expected)
    self.assertEqual(actual.notification_method, expected.get('notification_method'))
    self.assertEqual(actual.customer_notification_by, expected.get('customer_notification_by'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.created_at, expected.get('created_at'))

def assert_payer_bank_account(self, actual, expected):
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.object, expected.get('object'))
    self.assertEqual(actual.type, expected.get('type'))
    self.assertEqual(actual.name, expected.get('name'))
    self.assertEqual(actual.address, expected.get('address'))
    self.assertEqual(actual.account_no, expected.get('account_no'))
    self.assertEqual(actual.account_type, expected.get('account_type'))
    self.assertEqual(actual.ifsc, expected.get('ifsc'))
    self.assertEqual(actual.note_to_beneficiary, expected.get('note_to_beneficiary'))
    self.assertEqual(actual.created_at, expected.get('created_at'))

def assert_payment_virtual_account(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.Payment), True)
    self.assertEqual(actual.id, expected.get('id'))
    self.assertEqual(actual.amount, expected.get('amount'))
    self.assertEqual(actual.currency, expected.get('currency'))
    self.assertEqual(actual.status, expected.get('status'))
    self.assertEqual(actual.order_id, expected.get('order_id'))
    self.assertEqual(actual.invoice_id, expected.get('invoice_id'))
    self.assertEqual(actual.international, expected.get('international'))
    self.assertEqual(actual.method, expected.get('method'))
    self.assertEqual(actual.description, expected.get('description'))
    self.assertEqual(actual.card, expected.get('card'))
    self.assertEqual(actual.bank, expected.get('bank'))
    self.assertEqual(actual.wallet, expected.get('wallet'))
    self.assertEqual(actual.vpa, expected.get('vpa'))
    self.assertEqual(actual.email, expected.get('email'))
    self.assertEqual(actual.contact_no, expected.get('contact_no'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.fee, expected.get('fee'))
    self.assertEqual(actual.notes, expected.get('notes'))
    self.assertEqual(actual.service_tax, expected.get('service_tax'))
    self.assertEqual(actual.payout_amount, expected.get('payout_amount'))
    self.assertEqual(actual.payout_type, expected.get('payout_type'))
    self.assertEqual(actual.settlement_id, expected.get('settlement_id'))
    self.assertEqual(actual.refunded_amount, expected.get('refunded_amount'))
    self.assertEqual(actual.refund_status, expected.get('refund_status'))
    assert_list_of_refunds(self, actual.refunds, expected.get('refunds'))
    assert_payer_bank_account(self, actual.payer_bank_account, expected.get('payer_bank_account'))
    assert_virtual_account(self, actual.virtual_account, expected.get('virtual_account'))
    self.assertEqual(actual.error_code, expected.get('error_code'))
    self.assertEqual(actual.error_description, expected.get('error_description'))
    self.assertEqual(actual.created_at, expected.get('created_at'))
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

def assert_list_of_products(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (product_actual, product_expected) in zip(actual.data, expected.get('data')):
        assert_product(self, product_actual, product_expected)

def assert_list_of_plans(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (plan_actual, plan_expected) in zip(actual.data, expected.get('data')):
        assert_plan(self, plan_actual, plan_expected)

def assert_list_of_customers(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (customer_actual, customer_expected) in zip(actual.data, expected.get('data')):
        assert_customer(self, customer_actual, customer_expected)

def assert_list_of_subscriptions(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (subscription_actual, subscription_expected) in zip(actual.data, expected.get('data')):
        assert_subscription(self, subscription_actual, subscription_expected)

def assert_list_of_invoice_items(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (invoice_item_actual, invoice_item_expected) in zip(actual.data, expected.get('data')):
        assert_invoice_item(self, invoice_item_actual, invoice_item_expected)

def assert_list_of_invoices(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (invoice_actual, invoice_expected) in zip(actual.data, expected.get('data')):
        assert_invoice(self, invoice_actual, invoice_expected)

def assert_list_of_events(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (event_actual, event_expected) in zip(actual.data, expected.get('data')):
        assert_event(self, event_actual, event_expected)

def assert_list_of_transfers(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (transfer_actual, transfer_expected) in zip(actual.data, expected.get('data')):
        assert_transfer(self, transfer_actual, transfer_expected)

def assert_list_of_settlements(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (settlement_actual, settlement_expected) in zip(actual.data, expected.get('data')):
        assert_settlement(self, settlement_actual, settlement_expected)

def assert_list_of_beneficiary_accounts(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (beneficiary_account_actual, beneficiary_account_expected) in zip(actual.data, expected.get('data')):
        assert_beneficiary_account(self, beneficiary_account_actual, beneficiary_account_expected)

def assert_list_of_payment_links(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (payment_link_actual, payment_link_expected) in zip(actual.data, expected.get('data')):
        assert_payment_link(self, payment_link_actual, payment_link_expected)

def assert_list_of_virtual_accounts(self, actual, expected):
    self.assertEqual(isinstance(actual, payabbhi.resources.List), True)
    self.assertEqual(actual.total_count, expected.get('total_count'))
    self.assertEqual(actual.object, expected.get('object'))
    for (virtual_account_actual, virtual_account_expected) in zip(actual.data, expected.get('data')):
        assert_virtual_account(self, virtual_account_actual, virtual_account_expected)
