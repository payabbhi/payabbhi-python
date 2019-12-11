from ..error import InvalidRequestError
from .api_resource import APIResource


class BeneficiaryAccount(APIResource):

    def __init__(self, client=None):
        super(BeneficiaryAccount, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Beneficiary Accounts
        Args:
            data : Dictionary having keys using which beneficiary account list will be filtered
                count:              Count of beneficiary accounts to be retrieved
                skip:               Number of beneficiary accounts to be skipped
                to:                 Beneficiary accounts list till this timestamp will be retrieved
                from:               Beneficiary accounts list from this timestamp will be retrieved
        Returns:
            List of BeneficiaryAccount objects
        """
        if data is None:
            data = {}
        return super(BeneficiaryAccount, self)._all(data, **kwargs)

    def create(self, data, **kwargs):
        """"
        Create BeneficiaryAccount from given data
        Args:
            data : Dictionary having keys using which BeneficiaryAccount has to be created
                name:  Name of the beneficiary account owner
                beneficiary_name: Name of the beneficiary of the bank account
                ifsc: IFSC code of the bank branch of the bank account
                bank_account_number: Bank Account Number of the beneficiary account owner
                account_type: Type of Bank Accoun
        Returns:
            BeneficiaryAccount object containing data for created beneficiary account
        """
        return self._post(self.class_url(), data, **kwargs)

    def retrieve(self, beneficiary_id, **kwargs):
        """"
        Retrieve BeneficiaryAccount for given Id
        Args:
            beneficiary_id : Id for which BeneficiaryAccount object has to be retrieved
        Returns:
            BeneficiaryAccount object for given beneficiary Id
        """
        return self._retrieve(beneficiary_id, **kwargs)
