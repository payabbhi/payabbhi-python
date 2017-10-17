from .api_resource import APIResource


class List(APIResource):
    def __init__(self, client=None):
        super(List, self).__init__(client)
