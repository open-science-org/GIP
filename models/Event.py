# Event Class

class Event(object):
    """
    Event class for any kind of event related to an Idea. An Event has following minimal attributes:

    attributes:
        date: A UTC date object representing the date of the event.
        type: A string short name for the event. E.g. published, reviewed, etc
        description: A comprehensive text description of the event.
    """

    def __init__(self, date, type, **kwargs):
        self.date = date
        self.type = type
        self.description = kwargs.get("description", None)
