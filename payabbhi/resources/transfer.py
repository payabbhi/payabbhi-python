from .api_resource import APIResource


class Transfer(APIResource):

    def __init__(self, client=None):
        super(Transfer, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Transfers
        Args:
            data : Dictionary having keys using which transfer list will be filtered
                count:              Count of transfers to be retrieved
                skip:               Number of transfers to be skipped
                to:                 Transfer list till this timestamp will be retrieved
                from:               Transfer list from this timestamp will be retrieved
        Returns:
            List of Transfer objects
        """
        if data is None:
            data = {}
        return super(Transfer, self)._all(data, **kwargs)

    def create(self, source_id, data, **kwargs):
        """"
        Create Transfer from given data
        Args:
            source_id: The identifier of the source for which transfers need to be created.
            data : Dictionary having keys using which transfer has to be created
                transfers: List of transfers to be created with following details
                    recipient_id: The identifier of recipient of this transfer
                    description: Description of the Transfer.
                    amount:  Amount of Transfer
                    currency: Currency used in Transfer
                    notes: key value pair as notes
        Returns:
            Transfer object containing data for created transfers
        """
        url = '/api/v1/payments/' + source_id + '/transfers'
        return self._post(url, data, **kwargs)

    def retrieve(self, transfer_id, **kwargs):
        """"
        Retrieve Transfer for given Id
        Args:
            transfer_id : Id for which Transfer object has to be retrieved
        Returns:
            Transfer object for given transfer Id
        """
        return self._retrieve(transfer_id, **kwargs)
