from ..error import InvalidRequestError
from .api_resource import APIResource


class Payout(APIResource):

    def __init__(self, client=None):
        super(Payout, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Payouts
        Args:
            data : Dictionary having keys using which payout list will be filtered
                count:              Count of payouts to be retrieved
                skip:               Number of payouts to be skipped
                to:                 Payout list till this timestamp will be retrieved
                from:               Payout list from this timestamp will be retrieved.
        Returns:
            List of Payout objects
        """
        if data is None:
            data = {}
        return self._all(data, **kwargs)

    def create(self, data, **kwargs):
        """"
        Create Payout from given data
        Args:

            data : Dictionary having keys using which payout has to be created
                remittance_account_no: Bank account of corporate or business from which the payout should be remitted.
                beneficiary_id: ID of beneficiary whose bank account would be credited for this payout.
                beneficiary_ifsc: IFSC of beneficiary whose bank account would be credited for this payout.
                beneficiary_account_no: Account No of beneficiary whose bank account would be credited for this payout.
                beneficiary_name:Name of beneficiary whose bank account would be credited for this payout.
                amount: A positive integer in the smallest currency unit (e.g., 5000 paisa denotes Rs 50.00). Minimum amount is 100 paise.
                currency: Three-letter ISO currency code. Currently only INR is supported.
                method: The value can be one of bank_transfer, card, upi, wallet. Currently only bank_transfer is supported.
                instrument:The value can be one of IMPS, NEFT or RTGS.
                purpose:The value can be one of vendor_payout,cashback or instant_refund.
                merchant_reference_id: Unique identifier of the Merchant Account who has initiated this payout
                narration: Narration to be mentioned in beneficiary's bank account statement.
                
                notes: key value pair as notes
        Returns:
            Payout object containing data for created plan
        """
        return self._post(self.class_url(), data, **kwargs)

    def retrieve(self, payout_id, **kwargs):
        """"
        Retrieve Payout for given Id
        Args:
            payout_id : Id for which Payout object has to be retrieved
        Returns:
            Payout object for given payout Id
        """
        return self._retrieve(payout_id, **kwargs)
