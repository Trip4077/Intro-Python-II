import textwrap

from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


# Generate Items

item_list = {
    'sword': Item("Sword", "A swift double bladed weapon"),
    'mace': Item("Mace", "A powerful blunt force weapon"),
    "wand": Item("Wand", "A magical weapon"),
    "bow": Item("Bow", "A ranged weapon"),
    "potion": Item("Potion", "Recover Health"),
    "gold": Item("Gold", "It's gold")
}

# Add Items to rooms
room['outside'].items.append(item_list['sword'])
room['outside'].items.append(item_list['potion'])

room['foyer'].items.append(item_list['mace'])
room['foyer'].items.append(item_list['potion'])

room['overlook'].items.append(item_list['bow'])

room['narrow'].items.append(item_list['gold'])
room['narrow'].items.append(item_list['wand'])

category = ''

# Ensure User Selects Valide Category
while( len( category ) < 1 ):

    category = input( "\nEnter Character Category:\n>>Warrior\n>>Mage\n>>Theif\n------>  " ).lower()

    if category != "warrior" and category != "mage" and category != "theif":
        print('\n****************\nInvalid Category\n****************')
        category = ''

# Create Player
player = Player(
    input( "\nEnter Chacter Name\n------> " ),
    category
)

# Spawn Player/
# Make a new player object that is currently in the 'outside' room.
player.current_room = room["outside"]

#
# Main
#

# loop control
playing = True

wrapper = textwrap.TextWrapper(width=70, break_long_words=False)

while playing:
    # Format and Display Turn Infomation
    print( '\n' + wrapper.fill( f"{player.name}\'s current location is {player.current_room.name}. " + player.current_room.description ) )

    # Get User Command
    command = input( "\nSelect Action\n------> " )

    # Determine if single or multiple arguments
    if (" " in command) == True:

        # Split arguments into command and item
        commands = command.split(" ")
        command[0].lower()
        
        if commands[0] == 'g' or commands[0] == 'grab':
            player.grab_specific( commands[1] )

        elif commands[0] == 'd' or commands[0] == 'drop':
            player.drop_specific( commands[1] )

    else:
        
        command.lower()

        if command == 'q' or command == "quit":
            print("\n------> Game Over <------")
            break

        elif command == "c" or command == "commands":
            print("\n \'q\' or \'quit\' to end game")
            print(" \'n\' or \'north\' to move north\n \'s\' or \'south\' to move south")
            print(" \'w\' or \'west\' to move west\n \'e\' or \'east\' to move east")
            print(" \'l\' or \'look\' to look for items in a room")

            input( "\n hit any key to continue..." )

        elif command == "i" or command == "inventory":
            player.show_inventory()

        elif command == "l" or command == "look":
            player.look()
        
        elif command == "g" or command == "grab":
            player.grab()

        elif command == "d" or command == "drop":
            player.drop()

        elif command == "n" or command == "north" or command == "s" or command == "south":
            player.move_rooms( command[0] )

        elif command == "e" or command == "right" or command == "w" or command == "left":
            player.move_rooms( command[0] )

        else:
            print( "\n-----> Enter a valid command; use \'c\' or \'commands\' for full list" )
