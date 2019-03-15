from .api_resource import APIResource


class Subscription(APIResource):

    def __init__(self, client=None):
        super(Subscription, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Subscriptions
        Args:
            data : Dictionary having keys using which subscription list will be filtered
                count:              Count of subscriptions to be retrieved
                skip:               Number of subscriptions to be skipped
                to:                 Subscription list till this timestamp will be retrieved
                from:               Subscription list from this timestamp will be retrieved
                plan_id:            A filter on the subscription list based on the plan_id field
                status:             A filter on the subscription list based on the status field
                billing_method:     A filter on the subscription list based on the billing_method field
                customer_id:        A filter on the subscription list based on the customer_id field
        Returns:
            List of Subscription objects
        """
        if data is None:
            data = {}
        return self._all(data, **kwargs)

    def create(self, data, **kwargs):
        """"
        Create Subscription from given data
        Args:
            data : Dictionary having keys using which subscription has to be created
                plan_id: The unique identifier of the Plan against which this subscription is to be created.
                billing_cycle_count: Total no. of billing cycles. This represents how long the subscription will run.
                customer_id: The unique identifier of the Customer who is subscribing to the plan.
                customer_notification_by: Indicates who is responsible for notification to the customers for important subscription life cycle events.
                trial_duration: Duration of the trial period in days
                quantity: The quantity of the plan, which the customer is subscribing to. Ex : 5 users are subscribing to the plan.
                billing_method: Billing mode of the Subscription. the value can be either recurring or manual.
                due_by_days: No. of days by which the invoices associated with the subscription should be paid starting from the Invoice Issue date. This is applicable only when billing_method is manual.
                notes: key value pair as notes
                upfront_items: List of item objects to be included as upfront charges or set up fees of the subscription.
        Returns:
            Subscription object containing data for created subscription
        """

        return self._post(self.class_url(), data, **kwargs)

    def cancel(self, subscription_id, data=None, **kwargs):
        """"
        Cancels existing Subscription
        Args:
             subscription_id: The identifier of the subscription which needs to be cancelled.
             data : Dictionary having keys using which subscription has to be cancelled
                 at_billing_cycle_end: The flag which determines if the Subscription to be cancelled immediately or at the end of the current billing cycle.
        Returns:
            Subscription object containing data for cancelled subscription
        """
        if data is None:
            data = {}

        url = "{0}/cancel".format(self.instance_url(subscription_id))
        return self._post(url, data, **kwargs)

    def retrieve(self, subscription_id, **kwargs):
        """"
        Retrieve Subscription for given Id
        Args:
            subscription_id : Id for which Subscription object has to be retrieved
        Returns:
            Subscription object for given subscription Id
        """

        return self._retrieve(subscription_id, **kwargs)
