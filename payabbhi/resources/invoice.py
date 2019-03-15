from .api_resource import APIResource


class Invoice(APIResource):

    def __init__(self, client=None):
        super(Invoice, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Invoices
        Args:
            data : Dictionary having keys using which invoice item list will be filtered
                count:              Count of invoices to be retrieved
                skip:               Number of invoices to be skipped
                to:                 Invoice list till this timestamp will be retrieved
                from:               Invoice list from this timestamp will be retrieved
                billing_method:     A filter on the invoice list based on the billing_method field
                due_date_from:      A filter criterion based on the due_date field of the invoice object
                due_date_to:        A filter criterion based on the due_date field of the invoice object
                email:              A filter on the invoice list based on the customer's email field
                subscription_id:    A filter on the invoice list based on the subscription_id field
        Returns:
            List of Invoice objects
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
                due_date: Latest Timestamp by which the invoice should be paid by the customer
                currency: Currency of the invoice
                invoice_no: Invoice no. at Merchant end which corresponds to this invoice
                line_items: List of invoice item objects to be included in the invoice
                billing_method: Billing method of the invoice
                description: Description of the Invoice
                notify_by: Describes how the customer would be notified about the invoice
                notes: key value pair as notes
                subscription_id: Unique identifier of the subscription for which this invoice will be generated
        Returns:
            Invoice object containing data for created invoice
        """
        return self._post(self.class_url(), data, **kwargs)

    def retrieve(self, invoice_id, **kwargs):
        """"
        Retrieve Invoice for given Id
        Args:
            invoice_id : Id for which Invoice object is to be retrieved
        Returns:
            Invoice object for given invoice id
        """
        return self._retrieve(invoice_id, **kwargs)

    def void(self, invoice_id, data=None, **kwargs):
        """"
        Mark Invoice as Void for a given Id
        Args:
            invoice_id : The unique identifier of the invoice which needs to be voided
        Returns:
            Returns the invoice object if the invoice is voided successfully
        """
        if data is None:
            data = {}

        url = "{0}/void".format(self.instance_url(invoice_id))
        return self._post(url, data, **kwargs)

    def line_items(self, invoice_id, data=None, **kwargs):
        """"
        Retrieve Invoice Items for the Invoice object
        Returns:
            List of Invoice Item objects
        """
        if data is None:
            data = {}

        url = "{0}/line_items".format(self.instance_url(invoice_id))
        return self._get(url, data, **kwargs)

    def payments(self, invoice_id, data=None, **kwargs):
        """"
        Retrieve Payments for the Invoice object
        Returns:
            List of Payment objects
        """
        if data is None:
            data = {}

        url = "{0}/payments".format(self.instance_url(invoice_id))
        return self._get(url, data, **kwargs)
