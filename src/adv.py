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
room['common_room'].w_to = room['foyer']
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

player_name = "Luna Lovegood"
starting_room = room['outside']
player = Player(player_name, starting_room)

while True:
    current_room = player.current_room

    print(f"You are now at the {current_room.name}\n, {current_room_description}, \n Which direction would you like to move?")

    cmd = input("Enter 'n', 's', 'e', or 'w' to move or 'q' to quit:")

    if cmd == 'q':
        print('\n See you again next time \n')
        break

    elif cmd == 'n':
        if hasattr(current_room, 'n_to'):
            print('**********\n Moving North \n**********')
            player.current_room = current_room.n_to
        else:
            print("Uh oh! There isn't an exit to the south! \n \n Try a different direction")

    elif cmd == 'e':
        if hasattr(current_room, 'e_to'):
            print('**********\n Moving East \n***********')
            player.current_room = current_room.e_to
        else:
            print("Blocked! \n \n Try a different way.")

    elif cmd == 's':
        if hasattr(current_room, 's_to'):
            print ('********** \n Moving South \n *********')
            player.current_room = current_room.s_to
        else:
            print("Do you need glasses? There isn't a door this way! Pick another direction!")

    elif cmd == 'w':
        if hasattr(current_room, 'w_to'):
            print ('********** \n Moving West \n *********')
            player.current_room = current_room.w_to
        else: print("*sigh* You're really bad at this aren't you? There is no way out this way!")

    if cmd !== 'q' or 'n' or 'e' or 's' or 'w':
        print("Can you read? I said enter 'n', 's', 'e', 'w', or 'q' \n this wasn't any of those!")
