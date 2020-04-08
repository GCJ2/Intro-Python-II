from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons."),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

sword = Item('Sword', 'A slashy')
dagger = Item('Dagger', 'Get stabby')
cape = Item('Denim Cape', "It's perfect")
treasure = Item('Treasure', 'A box that says Wrath of the Lich King')

room['outside'].items = [sword]
room['narrow'].items = [dagger, cape]
room['treasure'].items = [treasure]

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
new_player = Player('Greg', room['outside'])


def print_details():
    print()
    print(new_player.current_room.name)
    if len(new_player.current_room.items) > 0:
        print(f'You found a {new_player.current_room.see_items()}')
    print(new_player.current_room.description)
    print()


def chose_again():
    print('You cannot move that way')
    print(new_player.items)


def main():
    print_details()
    direction = ''  # Empty string for taking in user input
    while direction != 'q':  # As long as the direction is not q
        direction = input('Please select a direction: N, S, E, W or press Q to quit. ')
        if direction == 'n':
            if new_player.current_room.n_to is not None:  # Looks at current room respective attribute
                new_player.set_current_room(new_player.current_room.n_to)  # If found, set current room to that room
                print_details()  # Which is equal to the adjacent room
            else:
                chose_again()
        if direction == 'e':
            if new_player.current_room.e_to is not None:
                new_player.set_current_room(new_player.current_room.e_to)
                print_details()
            else:
                chose_again()
        if direction == 's':
            if new_player.current_room.s_to is not None:
                new_player.set_current_room(new_player.current_room.s_to)
                print_details()
            else:
                chose_again()
        if direction == 'w':
            if new_player.current_room.w_to is not None:
                new_player.set_current_room(new_player.current_room.w_to)
                print_details()
            else:
                chose_again()
        elif direction == "q":
            print(f'Thank you for playing!')


main()

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
