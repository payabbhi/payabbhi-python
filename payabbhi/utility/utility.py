import hashlib
import hmac
import sys

from ..error import SignatureVerificationError


class Utility(object):
    def __init__(self, client=None):
        self.client = client

    def verify_payment_signature(self, parameters):
        order_id = str(parameters['order_id'])
        payment_id = str(parameters['payment_id'])
        payment_signature = str(parameters['payment_signature'])

        msg = "{0}&{1}".format(payment_id, order_id)

        self.verify_signature(payment_signature, msg)


    def verify_signature(self, signature, body):
        key = str(self.client.secret_key)

        if sys.version_info[0] == 3:  # pragma: no cover
            key = bytes(key, 'utf-8')
            body = bytes(body, 'utf-8')

        dig = hmac.new(key=key,
                       msg=body,
                       digestmod=hashlib.sha256)

        generated_signature = dig.hexdigest()

        if not generated_signature == signature:
            raise SignatureVerificationError('Invalid signature passed')
