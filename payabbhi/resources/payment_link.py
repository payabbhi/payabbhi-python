from ..error import InvalidRequestError
from .api_resource import APIResource


class PaymentLink(APIResource):

    def __init__(self, client=None):
        super(PaymentLink, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all PaymentLinks
        Args:
            data : Dictionary having keys using which PaymentLink list will be filtered
                count: A limit on the number of payment link objects to be returned. This can range between 1 and 100.
                skip: Represents number of payment link objects to be skipped
                from: A filter criterion based on the created_at field of the payment link object. Value can be a timestamp. Returns Payment links created on or after this timestamp.
                to: A filter criterion based on the created_at field of the payment link object. Value can be a timestamp. Returns Payment links created on or before this timestamp.
                due_date_from: A filter criterion based on the due_date field of the payment link object. Value can be a timestamp. Returns Payment links having due date on or after this timestamp.
                due_date_to: A filter criterion based on the due_date field of the payment link object. Value can be a timestamp. Returns Payment links due date on or before this timestamp.
                email: A filter on the payment link list based on the customer's email field.
                contact_no: A filter on the payment link list based on the customer's contact_no field.
                receipt_no: A filter on the payment link list based on the receipt_no field of the payment link object.

        Returns:
            List of PaymentLink objects
        """
        if data is None:
            data = {}
        return self._all(data, **kwargs)

    def create(self, data, **kwargs):
        """"
        Create PaymentLink from given data
        Args:
            data : Dictionary having keys using which PaymentLink has to be created
                customer_id: The unique identifier of the customer who will pay this
                             payment link. Either customer_id or at least one of name,
                             email, contact_no is required.
                name: Name of the customer who will pay this payment link.
                email: Email ID of the customer who will pay this payment link.
                contact_no: Contact Number of the customer who will pay this payment link.
                currency: Three-letter ISO currency code. Currently only INR is supported.
                amount: Amount for the payment link. A positive integer in the smallest
                        currency unit (e.g., 5000 paisa denotes Rs 50.00).
                due_date: Latest Timestamp by which the payment should be paid by the
                          customer. Measured in seconds since the Unix epoch.
                receipt_no: The receipt_id or reference_no. etc at Merchant end which
                            corresponds to this payment link. This should be maximum of 16 characters.
                description: Description of the Payment link.
                notify_by: Describes how the customer would be notified about the payment link.
                           The value is one of email, phone, both, none. The default value is email.
                customer_notification_by: Indicates who is responsible for sharing the payment link
                                          and sending notifications to the customers for important
                                          life cycle events. The value can be either merchant or
                                          platform. The default value is platform.
                notes: Notes is a key-value store used for storing additional data relating to
                       the payment link object in structured format.

        Returns:
            Returns the payment link object if the payment link is created successfully.
            Else it returns an error response.
        """
        return self._post(self.class_url(), data, **kwargs)

    def cancel(self, payment_link_id, data=None, **kwargs):
       """"
       Cancels existing payment link
       Args:
            payment_link_id: The unique identifier of the payment link which needs to be cancelled.
       Returns:
           Returns the payment link object if the payment link is cancelled successfully.
           Else it returns an error response
       """
       if data is None:
           data = {}

       url = "{0}/cancel".format(self.instance_url(payment_link_id))
       return self._post(url, data, **kwargs)

    def retrieve(self, payment_link_id, **kwargs):
        """"
        Retrieve payment link for given Id
        Args:
            payment_link_id: The identifier of the payment link to be retrieved.
        Returns:
            Returns a payment link object, given a valid payment link identifier
            was provided, and returns an error otherwise.
        """
        return self._retrieve(payment_link_id, **kwargs)

    def payments(self, payment_link_id, data=None, **kwargs):
        """"
        Retrieve Payments for the payment link
        Args:
            payment_link_id: The identifier of the payment link whose payments are to be retrieved..
        Returns:
            An object with total_count attribute containing the total count of payments
            corresponding to the given Payment link, object attribute containing list
            and a data attribute containing an array of payment objects.
        """
        if data is None:
            data = {}

        url = "{0}/payments".format(self.instance_url(payment_link_id))
        return self._get(url, data, **kwargs)
