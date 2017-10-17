from ..error import InvalidRequestError
from .api_resource import APIResource


class Order(APIResource):

    def __init__(self, client=None):
        super(Order, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Orders
        Args:
            data : Dictionary having keys using which order list will be filtered
                count:              Count of orders to be retrieved
                skip:               Number of orders to be skipped
                to:                 Order list till this timestamp will be retrieved
                from:               Order list from this timestamp will be retrieved
                authorized:         True/False if only the orders having an authorized payment will be retrieved
                merchant_order_id:  Orders with this merchant_order_id will be retrieved
        Returns:
            List of Order objects
        """
        if data is None:
            data = {}
        return super(Order, self)._all(data, **kwargs)

    def create(self, data=None, **kwargs):
        """"
        Create Order from given data
        Args:
            data : Dictionary having keys using which order has to be created
                amount:  Amount of Order
                currency: Currency used in Order
                merchant_order_id: Merchant side unique identifier for the order
                notes: key value pair as notes
                payment_auto_capture: True/False if payment should be auto captured or not
        Returns:
            Order object containing data for created order
        """
        if data is None:
            data = {}

        return self._post(self.class_url(), data, **kwargs)

    def retrieve(self, order_id, data=None, **kwargs):
        """"
        Retrieve Order for given Id
        Args:
            order_id : Id for which Order object has to be retrieved
        Returns:
            Order object for given order Id
        """
        if data is None:
            data = {}

        return super(Order, self)._retrieve(order_id, data, **kwargs)

    def payments(self, data=None, **kwargs):
        """"
        Retrieve Payments for the Order object
        Returns:
            List of Payment objects
        """
        if data is None:
            data = {}

        if not hasattr(self, 'id'):
            raise InvalidRequestError('Object Id not set')

        url = "{0}/payments".format(self.instance_url(self.id))
        return self._get(url, data, **kwargs)
