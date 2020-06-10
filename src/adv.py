from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [Item('Stick')]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                     [Item('Knife'), Item('CandleStick')]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                     [Item('Rock')]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                     [Item('Gun')]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                     [Item('Empty Chest')]),
}
# room['outside'].item = Item('Stick')
# room['foyer'].item = Item('Knife')
# room['overlook'].item = Item('Rock')
# room['narrow'].item = Item('Gun')
# room['treasure'].item = Item('Empty')


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
newPlayer = Player('Chris', room['outside'], [Item('FlashLight')])
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


def getItem(a):
    newItem = newPlayer.current_room.items[int(a)]
    newPlayer.items.append(newItem)
    newPlayer.current_room.items.pop(int(a))


def dropItem(a):
    newPlayer.current_room.items.append(newPlayer.items[int(a)])
    newPlayer.items.pop(int(a))


def start():
    print(
        f"Player {newPlayer.name}, you are in room {newPlayer.current_room.name}")


start()


def run():
    begin = True
    while begin == True:
        print('What next?')
        command = input(
            f'n = north, s = south, e = east, w = west, get {[i.name for i in newPlayer.current_room.items]}, drop {[i.name for i in newPlayer.items]}, q = quit \n')
        if command == 'q':
            begin = False
        elif command == 'n':
            if hasattr(newPlayer.current_room, 'n_to'):
                newPlayer.current_room = newPlayer.current_room.n_to
                print(f"You are now in the {newPlayer.current_room.name}")
                print(f"Description: {newPlayer.current_room.description}")
            else:
                print('You cannot move that way')
        elif command == 's':
            if hasattr(newPlayer.current_room, 's_to'):
                newPlayer.current_room = newPlayer.current_room.s_to
                print(f"You are now in the {newPlayer.current_room.name}")
                print(f"Description: {newPlayer.current_room.description}")
            else:
                print('You cannot move that way')
        elif command == 'e':
            if hasattr(newPlayer.current_room, 'e_to'):
                newPlayer.current_room = newPlayer.current_room.e_to
                print(f"You are now in the {newPlayer.current_room.name}")
                print(f"Description: {newPlayer.current_room.description}")
            else:
                print('You cannot move that way')
        elif command == 'w':
            if hasattr(newPlayer.current_room, 'w_to'):
                newPlayer.current_room = newPlayer.current_room.w_to
                print(f"You are now in the {newPlayer.current_room.name}")
                print(f"Description: {newPlayer.current_room.description}")
            else:
                print('You cannot move that way')
        elif command == 'get':
            if len(newPlayer.current_room.items) > 0:
                print('Select which item you would like to pick up.')
                for idx, item in enumerate(newPlayer.current_room.items):
                    print(f'{idx}: {item.name}')
                selectItem = input('Enter the number for your selection: ')
                getItem(selectItem)
                print(f"Player now has: {[i.name for i in newPlayer.items]}")
            else:
                print('No available items')
        elif command == 'drop':
            if len(newPlayer.items) > 0:
                print('Select which item you would like to drop.')
                for idx, item in enumerate(newPlayer.items):
                    print(f"{idx}: {item.name}")
                selectItem = input('Enter the number of your selection: ')
                droppedItem = newPlayer.items[int(selectItem)]
                dropItem(selectItem)
                print(
                    f"Player has dropped {droppedItem.name} in {newPlayer.current_room.name} ")
            else:
                print('No available items to drop.')


run()
