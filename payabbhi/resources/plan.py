from .api_resource import APIResource


class Plan(APIResource):

    def __init__(self, client=None):
        super(Plan, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Plans
        Args:
            data : Dictionary having keys using which plan list will be filtered
                count:              Count of plans to be retrieved
                skip:               Number of plans to be skipped
                to:                 Plan list till this timestamp will be retrieved
                from:               Plan list from this timestamp will be retrieved
                product_id:         A filter on the plan list based on the product_id field.
        Returns:
            List of Plan objects
        """
        if data is None:
            data = {}
        return self._all(data, **kwargs)

    def create(self, data, **kwargs):
        """"
        Create Plan from given data
        Args:
            data : Dictionary having keys using which plan has to be created
                product_id: The identifier of the Product against which plan was created.
                amount: A positive integer in the smallest currency unit (e.g., 5000 paisa denotes Rs 50.00). Minimum amount is 100 paise.
                currency: Three-letter ISO currency code. Currently only INR is supported.
                frequency: Frequency of billing interval.
                interval: Interval at which the Subscription would be billed. This can be day(s), week(s), month(s) or year(s).
                name: Name of the Plan. Ex: Basic, Standard etc.
                notes: key value pair as notes
        Returns:
            Plan object containing data for created plan
        """
        return self._post(self.class_url(), data, **kwargs)

    def retrieve(self, plan_id, **kwargs):
        """"
        Retrieve Plan for given Id
        Args:
            plan_id : Id for which Plan object has to be retrieved
        Returns:
            Plan object for given plan Id
        """
        return self._retrieve(plan_id, **kwargs)
