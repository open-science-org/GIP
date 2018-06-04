# Generalized Idea Class

class Idea(object):
    """
    A unique idea. An idea has following attributes:

    attributes:
        id: Unique idea identifier hash.
        name: A string representing the name of the idea - easy to understand.
        types: List of subnetwork or subgroups 
        parents: List of <parent idea id, strength of relationship>
        source:: Optional id of previous version of the same idea
        supporting_files: List of urls to files/objects related with the idea such as publication, data.
        authors: List of authors
        events: List of relevant events
        description: Text description or abstract of the idea.
        keywords: List of keywords or tags or subjects
    """

    def __init__(self, name, **kwargs):
        """
        """ 
        self.id = self.get_new_id()
        self.name = name
        self.types = kwargs.get("types", None)
        self.parents = kwargs.get("parents", None)
        self.source = kwargs.get("source", None)
        self.supporting_files = kwargs.get("supporting_files", None)
        self.authors = kwargs.get("authors", None)
        self.events = kwargs.get("events", None)
        self.description = kwargs.get("description", None)
        self.keywords: kwargs.get("keywords", None)
