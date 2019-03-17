from .api_resource import APIResource


class InvoiceItem(APIResource):

    def __init__(self, client=None):
        super(InvoiceItem, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Invoice Items
        Args:
            data : Dictionary having keys using which invoice item list will be filtered
                count:              Count of invoice items to be retrieved
                skip:               Number of invoice items to be skipped
                to:                 Invoice Item list till this timestamp will be retrieved
                from:               Invoice Item list from this timestamp will be retrieved
        Returns:
            List of Invoice Item objects
        """
        if data is None:
            data = {}
        return self._all(data, **kwargs)

    def create(self, data, **kwargs):
        """"
        Create Invoice Item from given data
        Args:
            data : Dictionary having keys using which invoice item has to be created
                customer_id:  The unique identifier of the Customer who will pay this invoice
                name: Name of the invoice item
                amount: Amount of the invoice item
                currency: Currency of the invoice item amoount
                invoice_id: The unique identifier of the invoice to which this invoice item to be added
                subscription_id: The unique identifier of the subscription to which this invoice item is to be added as an addon
                description: Description of the invoice item
                quantity: Quantity of the invoice item
                notes: key value pair as notes
        Returns:
            Invoice Item object containing data for created invoice item
        """
        return self._post(self.class_url(), data, **kwargs)

    def retrieve(self, invoice_item_id, **kwargs):
        """"
        Retrieve Invoice Item for given Id
        Args:
            invoice_item_id : Id for which Invoice Item object is to be retrieved
        Returns:
            Invoice Item object for given invoice item Id
        """
        return self._retrieve(invoice_item_id, **kwargs)

    def invoices(self, invoice_item_id, data=None, **kwargs):
        """"
        Retrieve Invoices where the invoice item with invoice_item_id is attached
        Returns:
            List of Invoice objects
        """
        if data is None:
            data = {}

        url = "{0}/invoices".format(self.instance_url(invoice_item_id))
        return self._get(url, data, **kwargs)

    def delete(self, invoice_item_id, **kwargs):
        """"
        Delete Invoice Item for given Id
        Args:
            invoice_item_id : Id for which Invoice Item object is to be deleted
        Returns:
            Invoice Item object corresponding to the invoice item Id after successful deletion
        """
        return self._delete(invoice_item_id, **kwargs)
