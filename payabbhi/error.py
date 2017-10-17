class PayabbhiError(Exception):

    def __init__(self, description=None, http_status=None,
                 field=None):
        self.description = description
        self.http_status = http_status
        self.field = field
        self._message = self.error_message()
        super(PayabbhiError, self).__init__(self._message)

    def error_message(self):
        msg = "message: " + self.description
        msg = (msg + ", http_code: " + str(self.http_status)) if self.http_status else msg
        msg = (msg + ", field: " + self.field) if self.field else msg
        return msg + "\n"


class APIError(PayabbhiError):
    pass


class APIConnectionError(PayabbhiError):
    pass


class AuthenticationError(PayabbhiError):
    pass


class InvalidRequestError(PayabbhiError):
    pass


class GatewayError(PayabbhiError):
    pass


class SignatureVerificationError(PayabbhiError):
    pass
