# Basic Author Class

class Author(object):
    """
    Base class for author of an Idea. An Author has following minimal attributes:

    attributes:
        unique_researcher_id: Unique author identifier hash. Should be unique within OSO. Can be provided by external service. E.g. URI id
        first_name: A string representing the first name of the author.
        middle_name: A string representing the middle name of the author.
        last_name: A string representing the last name of the author.
        name_suffix: A string representing the name suffix of the author.
        title_name: A string representing the title name of the author.
    """

    def __init__(self, unique_researcher_id, **kwargs):
        self.unique_researcher_id = unique_researcher_id
        self.first_name = kwargs.get("first_name", None)
        self.middle_name = kwargs.get("middle_name", None)
        self.last_name = kwargs.get("last_name", None)
        self.name_suffix = kwargs.get("name_suffix", None)
        self.title_name = kwargs.get("title_name", None)
