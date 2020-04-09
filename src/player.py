# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, items=None):
        self.name = name
        self.current_room = current_room
        self.items = items if items else []

    def get_name(self):
        return self.name

    def get_current_room(self):
        return self.current_room.name

    def see_items(self):
        print('Current Inventory:')
        inventory = [i.name for i in self.items]
        return inventory

    def set_current_room(self, xcr):  # Need ability to change current room
        self.current_room = xcr  # xcr = change current room

    def drop_item(self, item):
        self.items.remove(item)
        self.current_room.items.append(item)
        print(f'You dropped the {item.name}')
        print(self.see_items())
