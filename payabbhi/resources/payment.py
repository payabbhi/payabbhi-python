from ..error import InvalidRequestError
from .api_resource import APIResource


class Payment(APIResource):

    def __init__(self, client=None):
        super(Payment, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Payments
        Args:
            data : Dictionary having keys using which payment list will be filtered
                count:           Count of payments to be retrieved
                skip:            Number of payments to be skipped
                to:              Payment list till this timestamp will be retrieved
                from:            Payment list from this timestamp will be retrieved
        Returns:
            List of Payment objects
        """
        if data is None:
            data = {}

        return super(Payment, self)._all(data, **kwargs)

    def retrieve(self, payment_id, data=None, **kwargs):
        """"
        Retrieve payment for given Id
        Args:
            payment_id : Id for which Payment object has to be retrieved
        Returns:
            Payment object with given payment Id
        """
        if data is None:
            data = {}

        return super(Payment, self)._retrieve(payment_id, data, **kwargs)

    def refunds(self, payment_id, data=None, **kwargs):
        """"
        Retrieve Refunds for given payment Id
        Args:
            payment_id:
            data : Dictionary having keys using which refund list will be filtered
                count:           Count of refunds to be retrieved
                skip:            Number of refunds to be skipped
                to:              Refund list till this timestamp will be retrieved
                from:            Refund list from this timestamp will be retrieved
        Returns:
            Refund list for a payment object
        """
        if data is None:
            data = {}

        url = "{0}/refunds".format(self.instance_url(payment_id))
        return self._get(url, data, **kwargs)

    def capture(self, data=None, **kwargs):
        """"
        Captures the Payment object
        Returns:
            Updated Payment object after getting captured
        """
        if data is None:
            data = {}

        if not hasattr(self, 'id'):
            raise InvalidRequestError('Object Id not set')

        url = self.instance_url(self.id) + '/capture'
        captured_payment = self._post(url, data, **kwargs)
        self.__dict__.update(captured_payment.__dict__)

        return self

    def refund(self, data=None, **kwargs):
        """"
        Refunds Payment object with given data
        Args:
            data : Dictionary having keys using which payment has to be refunded
                amount : Amount for which the payment has to be refunded
                notes: Key value pair as notes
        Returns:
            Refund object that is created
        """
        if data is None:
            data = {}

        if not hasattr(self, 'id'):
            raise InvalidRequestError('Object Id not set')

        url = self.instance_url(self.id) +'/refunds'
        refund = self._post(url, data, **kwargs)

        refunded_payment = super(Payment, self)._retrieve(self.id, {})
        self.__dict__.update(refunded_payment.__dict__)

        return refund
