from ..error import InvalidRequestError
from .api_resource import APIResource


class RemittanceAccount(APIResource):

    def __init__(self, client=None):
        super(RemittanceAccount, self).__init__(client)

    def retrieve(self, remittance_account_id, **kwargs):
        """"
        Retrieve remittance account for given remittance account id
        Args:
            remittance_account_id: The identifier of the remittance account to be retrieved.
        Returns:
            Returns a remittance account object, given a valid remittance account identifier
            was provided, and returns an error otherwise.
        """
        return self._retrieve(remittance_account_id, **kwargs)
