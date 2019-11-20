import textwrap

from room import Room
from player import Player

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

# Spawn Player
# Make a new player object that is currently in the 'outside' room.
player.current_room = room["outside"]

#
# Main
#

# loop control
playing = True
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

wrapper = textwrap.TextWrapper(width=70, break_long_words=False)

while playing:
    print( '\n' + wrapper.fill( f"{player.name}\'s current location is {player.current_room.name}. " + player.current_room.description ) )

    # Get User Command
    command = input( "\nSelect Action\n------> " )
    command.lower()

    if command == 'q' or command == "quit":
        print("\n------> Game Over <------")
        break

    elif command == "c" or command == "commands":
        print("\n \'q\' or \'quit\' to end game")
        print(" \'w\' or \'forward\' to move north\n \'s\' or \'back\' to move south")
        print(" \'a\' or \'left\' to move west\n \'d\' or \'right\' to move east")

        input( "\n hit any key to continue..." )

    elif command == "w" or command == "forward":
        if player.current_room.n_to == "Solid Wall":
            print( "\nYou find a solid wall, there might be another way..." )
        else:
            player.current_room = player.current_room.n_to

    elif command == "s" or command == "back":
        if player.current_room.s_to == "Solid Wall":
            print( "\nYou find a solid wall, there might be another way..." )
        else:
            player.current_room = player.current_room.s_to

    elif command == "d" or command == "right":
        if player.current_room.s_to == "Solid Wall":
            print( "\nYou find a solid wall, there might be another way..." )
        else:
            player.current_room = player.current_room.e_to

    elif command == "a" or command == "left":
        if player.current_room.w_to == "Solid Wall":
            print( "\nYou find a solid wall, there might be another way..." )
        else:
            player.current_room = player.current_room.w_to
    else:
        print( "\n-----> Enter a valid command; use \'c\' or \'commands\' for full list" )
