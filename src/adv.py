from room import Room
from player import Player 

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north, east, and west."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'chamber': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),

    'common_room': Room("Common Room", """Welcome to the Ravenclaw Common Room!
This room bends from west to north. 
Don't forget to say hello to Luna 
on your way to get the gold!"""),

    'passage': Room('Wide Passage', """A wide passage is laid out before you. 
There is a mysterious mist and you cannot 
see the end of it. You think you seem a 
dim light in the east.""")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']
room['common_room'].n_to = room['chamber']
room['chamber'].s_to = room['common_room']
room['foyer'].e_to = room['common_room']
room['common_room'].w.to = room['foyer']
room['passage'].e_to = room['foyer']
room['foyer'].w_to = room['passage']



#
# Main
#

# Make a new player object that is currently in the 'outside' room.

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
