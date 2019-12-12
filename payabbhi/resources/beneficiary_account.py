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
                name: Name of the Beneficiary Account owner
                beneficiary_name: Name of the beneficiary of the bank account.
                ifsc: IFSC code of the bank branch of the bank account.
                bank_account_number: Bank Account Number of the beneficiary account owner.
                account_type: Type of Bank Account. The value can be one of Current, Savings or Others.
                contact_no: Contact number of the beneficiary account owner.
                email: Email ID of the beneficiary account owner.
                business_name: Legal name of Beneficiary's business to appear in any official communication.
                business_entity_type: Type of Beneficiary's Business Entity.
                notes: Set of key/value pairs that you can attach to an object. It can be useful for storing additional information about the beneficiary account object in a structured format.
                Returns: Returns the beneficiary account object if the beneficiary account is created successfully. Else it returns an error response.
        """
        return self._post(self.class_url(), data, **kwargs)

    def retrieve(self, beneficiary_id, **kwargs):
        """"
        Retrieve BeneficiaryAccount for given Id
        Args:
            beneficiary_id : Id for which BeneficiaryAccount object has to be retrieved
        Returns:
            BeneficiaryAccount object for given beneficiary_id
        """
        return self._retrieve(beneficiary_id, **kwargs)
