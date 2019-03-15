from .api_resource import APIResource


class Event(APIResource):

    def __init__(self, client=None):
        super(Event, self).__init__(client)

    def all(self, data=None, **kwargs):
        """"
        Get all Events
        Args:
            data : Dictionary having keys using which event list will be filtered
                count:              Count of events to be retrieved
                skip:               Number of events to be skipped
                to:                 Event list till this timestamp will be retrieved
                from:               Event list from this timestamp will be retrieved
                type:               Types of events to be listed
        Returns:
            List of Event objects
        """
        if data is None:
            data = {}
        return super(Event, self)._all(data, **kwargs)

    def retrieve(self, event_id, **kwargs):
        """"
        Retrieve Event for given Id
        Args:
            event_id : Id for which Event object has to be retrieved
        Returns:
            Event object for given event Id
        """
        return self._retrieve(event_id, **kwargs)
