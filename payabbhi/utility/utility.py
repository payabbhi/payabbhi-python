import hashlib
import hmac
import sys
import time

from ..error import SignatureVerificationError


class Utility(object):
    def __init__(self, client=None):
        self.client = client

    def verify_payment_signature(self, parameters):
        order_id = str(parameters['order_id'])
        payment_id = str(parameters['payment_id'])
        payment_signature = str(parameters['payment_signature'])

        msg = "{0}&{1}".format(payment_id, order_id)

        return self.verify_signature(payment_signature, msg, str(self.client.secret_key))


    def verify_webhook_signature(self, parameters, actual_signature, secret, replay_interval=300):
        entities = actual_signature.split(",")
        payload_map = {}
        for entity in entities:
            key_value = entity.split("=")
            payload_map[key_value[0].strip()] = key_value[1]

        if payload_map.get("t") == None or payload_map.get("v1") == None or int(time.time()) - int(payload_map["t"]) > replay_interval:
            raise SignatureVerificationError('Invalid signature passed')

        canonical_string  = "{0}&{1}".format(parameters, payload_map["t"])
        return self.verify_signature(payload_map["v1"],canonical_string, str(secret))


    def verify_signature(self, signature, body, key):

        if sys.version_info[0] == 3:  # pragma: no cover
            key = bytes(key, 'utf-8')
            body = bytes(body, 'utf-8')

        dig = hmac.new(key=key,
                       msg=body,
                       digestmod=hashlib.sha256)

        generated_signature = dig.hexdigest()

        if not generated_signature == signature:
            raise SignatureVerificationError('Invalid signature passed')

        return True
