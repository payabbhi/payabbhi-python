from .api_resource import APIResource


class Product(APIResource):

    def __init__(self, client=None):
        super(Product, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Products
        Args:
            data : Dictionary having keys using which product list will be filtered
                count:              Count of products to be retrieved
                skip:               Number of products to be skipped
                to:                 Product list till this timestamp will be retrieved
                from:               Product list from this timestamp will be retrieved
        Returns:
            List of Product objects
        """
        if data is None:
            data = {}
        return self._all(data, **kwargs)

    def create(self, data, **kwargs):
        """"
        Create Product from given data
        Args:
            data : Dictionary having keys using which product has to be created
                name: Name of the Product, which should be displayed to the customer in receipt and invoice.
                type: Type of the Product. This can be good or service
                unit_label: Unit label describing the unit of the product being charged for metered billing - MB, text messages etc
                notes: key value pair as notes
        Returns:
            Product object containing data for created product
        """
        return self._post(self.class_url(), data, **kwargs)

    def retrieve(self, product_id, **kwargs):
        """"
        Retrieve Product for given Id
        Args:
            product_id : Id for which Product object has to be retrieved
        Returns:
            Product object for given product Id
        """
        return self._retrieve(product_id, **kwargs)
