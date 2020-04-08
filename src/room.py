# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.w_to = None
        self.e_to = None
        self.s_to = None
        self.n_to = None
        self.items = []
        self.name = name
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def see_items(self):
        for i in self.items:
            return i.name
