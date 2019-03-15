from .api_resource import APIResource


class Customer(APIResource):

    def __init__(self, client=None):
        super(Customer, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Customers
        Args:
            data : Dictionary having keys using which customer list will be filtered
                count:              Count of customers to be retrieved
                skip:               Number of customers to be skipped
                to:                 Customer list till this timestamp will be retrieved
                from:               Customer list from this timestamp will be retrieved
        Returns:
            List of Customer objects
        """
        if data is None:
            data = {}
        return self._all(data, **kwargs)

    def create(self, data, **kwargs):
        """"
        Create Customer from given data
        Args:
            data : Dictionary having keys using which customer has to be created
                email: Email ID of the Customer.
                contact_no: Contact Number of the Customer.
                name: Name of the Customer.
                gstin: GSTIN of the Customer.
                billing_address: Billing Address is a key-value pair denoting the billing address of the customer. Valid keys are address_line1, address_line2, city, state, pin.
                shipping_address: Shipping Address is a key-value pair denoting the shipping address of the customer. Valid keys are address_line1, address_line2, city, state, pin.
                notes: key value pair as notes
        Returns:
            Customer object containing data for created customer
        """
        return self._post(self.class_url(), data, **kwargs)

    def edit(self, customer_id, data, **kwargs):
        """"
        Updates existing Customer from given data
        Args:
             customer_id: The identifier of the customer which needs to be updated.
             data : Dictionary having keys using which customer has to be created
                 email: Email ID of the Customer.
                 contact_no: Contact Number of the Customer.
                 name: Name of the Customer.
                 gstin: GSTIN of the Customer.
                 billing_address: Billing Address is a key-value pair denoting the billing address of the customer. Valid keys are address_line1, address_line2, city, state, pin.
                 shipping_address: Shipping Address is a key-value pair denoting the shipping address of the customer. Valid keys are address_line1, address_line2, city, state, pin.
                 notes: key value pair as notes
        Returns:
            Customer object containing data for updated customer
        """
        return self._put(self.instance_url(customer_id), data, **kwargs)

    def retrieve(self, customer_id, **kwargs):
        """"
        Retrieve Customer for given Id
        Args:
            customer_id : Id for which Customer object has to be retrieved
        Returns:
            Customer object for given customer Id
        """
        return self._retrieve(customer_id, **kwargs)
