from ..error import InvalidRequestError
from .api_resource import APIResource


class VirtualAccount(APIResource):

    def __init__(self, client=None):
        super(VirtualAccount, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Virtual Accounts.
        Args:
            data : Dictionary having keys using which virtual Account list will be filtered
                count : A limit on the number of virtual account objects to be returned. This can range between 1 and 100.
                skip : Represents number of virtual account objects to be skipped
                from : A filter criterion based on the created_at field of the virtual account object. Value can be a timestamp. Returns Virtual accounts created on or after this timestamp.
                to : A filter criterion based on the created_at field of the virtual account object. Value can be a timestamp. Returns Virtual accounts created on or before this timestamp.
        Returns:
            List of Virtual Account objects
        """
        if data is None:
            data = {}
        return self._all(data, **kwargs)

    def create(self, data, **kwargs):
        """"
        Create V from virtual Account given data
        Args:
            data : Dictionary having keys using which virtual Account has to be created
                customer_id :Unique identifier of the customer who will pay to this virtual account.
                email : Email ID of the customer who will pay to this virtual account.
                contact_no : Contact Number of the customer who will pay to this virtual account.
                order_id : Unique identifier of an Order object created using Payabbhi API.
                invoice_id : Unique identifier of an Invoice object created using Payabbhi API.
                description : Description of the virtual account.
                collection_methods : A list of collection methods that should be used to collect
                                     payments for the virtual account. The values can be bank_account.
                notification_method : Describes how the customer would be notified
                                      about the virtual account. The value is one of email, sms,
                                      both, none. The default value is email.
                customer_notification_by : Indicates who is responsible for sharing the virtual
                                           account details and sending notifications to the customers
                                           for important life cycle events. The value can be either
                                           merchant or platform. The default value is platform.
                notes : Set of key/value pairs that you can attach to a virtual account object.
                        It can be useful for storing additional information about the virtual account
                        object in a structured format.
        Returns:
            Returns the virtual account object if the virtual account is created successfully.
            Else it returns an error response.
        """
        return self._post(self.class_url(), data, **kwargs)

    def retrieve(self, virtual_account_id, **kwargs):
        """"
        Retrieve virtual account for given virtual account id
        Args:
            virtual_account_id: The identifier of the virtual account to be retrieved.
        Returns:
            Returns a virtual account object, given a valid virtual account identifier
            was provided, and returns an error otherwise.
        """
        return self._retrieve(virtual_account_id, **kwargs)

    def close(self, virtual_account_id,**kwargs):
        """"
        Close virtual account for given virtual account id
        Args:
            virtual_account_id : Id for which virtual account is to be closed
        Returns:
            Returns the virtual account object if the virtual account is closed successfully.
            Else it returns an error response.
        """
        return self._patch(virtual_account_id, **kwargs)

    def payments(self, virtual_account_id, data=None, **kwargs):
        """"
        Retrieve all payments for given virtual account Id
        Args:
            virtual_account_id: The identifier of the virtual account whose payments
                                are to be retrieved.
        Returns:
            An object with total_count attribute containing the total count of payments
            corresponding to the given Virtual account, object attribute containing list
            and a data attribute containing an array of payment objects.
        """
        if data is None:
            data = {}

        url = "{0}/payments".format(self.instance_url(virtual_account_id))
        return self._get(url, data, **kwargs)
