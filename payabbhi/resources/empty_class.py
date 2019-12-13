from ..error import InvalidRequestError
from .api_resource import APIResource

# this EmptyClass is needed so that http_client.py/convert_to_object function 
# never fails during recursive search
class EmptyClass(APIResource):

    def __init__(self, client=None):
        super(EmptyClass, self).__init__(client)
