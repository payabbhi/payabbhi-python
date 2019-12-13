from ..error import InvalidRequestError
from .api_resource import APIResource


class Settlement(APIResource):

    def __init__(self, client=None):
        super(Settlement, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Settlements
        Args:
            data : Dictionary having keys using which settlement list will be filtered
                count:              Count of Settlements to be retrieved
                skip:               Number of Settlements to be skipped
        Returns:
            List of Settlement objects
        """
        if data is None:
            data = {}
        return self._all(data, **kwargs)

    def retrieve(self, settlement_id, **kwargs):
        """"
        Retrieve Settlement for given settlement_id
        Args:
            settlement_id : Id for which Settlement object has to be retrieved
        Returns:
            Settlement object for given settlement_id
        """
        return self._retrieve(settlement_id, **kwargs)
