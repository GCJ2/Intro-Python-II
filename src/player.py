# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.items = []

    def get_name(self):
        return self.name

    def get_current_room(self):
        return self.current_room.name

    def see_items(self):
        print('Current Inventory:')
        for i in self.items:
            print(i.name)

    def set_current_room(self, xcr):  # Need ability to change current room
        self.current_room = xcr  # xcr = change current room

    def drop_item(self, item):
        self.items.remove(item)
        print(f'You dropped the {item.name}')
        print(self.see_items())
