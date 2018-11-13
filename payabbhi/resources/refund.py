from .api_resource import APIResource


class Refund(APIResource):

    def __init__(self, client=None):
        super(Refund, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Refunds
        Args:
            data : Dictionary having keys using which order list will be filtered
                count:           Count of refunds to be retrieved
                skip:            Number of refunds to be skipped
                to:              Refund list till this timestamp will be retrieved
                from:            Refund list from this timestamp will be retrieved
        Returns:
            List of Refund objects
        """
        if data is None:
            data = {}

        return super(Refund, self)._all(data, **kwargs)

    def retrieve(self, refund_id, **kwargs):
        """"
        Retrieve Refund for given Id
        Args:
            refund_id : Id for which refund object has to be retrieved
        Returns:
            Refund object with given refund Id
        """
        return super(Refund, self)._retrieve(refund_id, **kwargs)

    def create(self, payment_id, data=None, **kwargs):
        """"
        Create Refund from given data and payment Id
        Args:
            payment_id : Id for which Refund has to be created
            data : Dictionary having keys using which order have to be created
                'amount' :  Amount to be refunded
                'notes' : key value pair as notes
        Returns:
            Refund object containing data for created refund
        """
        if data is None:
            data = {}

        url = '/api/v1/payments/' + payment_id + '/refunds'
        return self._post(url, data, **kwargs)
