# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.w_to = None                    # These didn't exist in the constructor
        self.e_to = None                    # So I added them
        self.s_to = None                    # So my IDE would stop throwing errors
        self.n_to = None
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description
