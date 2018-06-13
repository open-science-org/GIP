# Idea Type Class

class IdeaType(object):
    """
    Base class for subnetwork or subgroup or category of an Idea. An IdeaType has following minimal attributes:

    attributes:
        id: Unique type identifier hash.
        name: A string representing the name of the type.
        description: Text description or abstract of the idea.
    """

    def __init__(self, name, **kwargs):
        self.id = self.get_new_id()
        self.name = name
        self.description = kwargs.get("description", None)
