# Michael Alestock

# declaration
rooms = {
    'Flight Deck': {'South': 'Cafeteria', 'North': "Flight Captain's Office", 'East': "Pvt. Pyle's Quarters",
                    'West': 'Infirmary', 'Item': 'Red Key Card'},
    'Cafeteria': {'North': 'Flight Deck', 'East': "Janitor's Closet", 'Item': 'Blue Key Card'},
    "Janitor's Closet": {'West': 'Cafeteria', 'Item': 'Purple Key Card'},
    'Cargo Holding Area': {'West': 'Infirmary', 'Item': 'Xenomorph Queen'},
    "Pvt. Pyle's Quarters": {'West': 'Flight Deck', 'Item': 'Launch Key'},
    "Flight Captain's Office": {'South': 'Flight Deck', 'Item': 'Flamethrower'},
    'Infirmary': {'East': 'Flight Deck', 'South': 'Cargo Holding Area', 'Item': 'Evacuation Protocol Documents'}

}
state = 'Flight Deck'

# Function
def get_new_state(state, direction):
    new_state = state  # Declaring
    for i in rooms:  # Loop
        if i == state:  # if
            if direction in rooms[i]:  # if
                new_state = rooms[i][direction]  # Assigning new_state

    return new_state  # return


def get_item(state):
    return rooms[state]['Item']  # returning Item value

# Function
def show_instructions():
    # Print a Main Menu and the commands to follow
    print('Welcome to Alien')
    print('Collect all 6 items and escape the ship, or be harvested by the Xenomorph Queen')
    print('Move commands: go North, go South, go East, go West')
    print("Add to Inventory: get 'item_name'")
show_instructions()  # Calling the function

Inventory = []
items = ['Red Key Card', 'Purple Key Card', 'Blue Key Card', 'Evacuation Protocol Documents', 'Flamethrower',
         'Launch Key']

while (1):  # Gameplay Loop
    print('You are in', state)  # Printing the state
    print('Inventory:', Inventory)  # Printing the inventory
    item = get_item(state)  # Calling get_item function
    print('You see a', item)  # print
    print('--------------------')
    if item == 'Xenomorph Queen':  # if
        print('You have been harvested... GAME OVER!')
        exit(0)
    direction = input('Enter your move: ')  # Asking the user
    if direction == 'go East' or direction == 'go West' or direction == 'go North' or direction == 'go South':
        direction = direction[3:]
        new_state = get_new_state(state, direction)  # Calling the function
        if new_state == state:  # if
            print('The room has wall in that direction enter other direction!')  # Print
        else:
            state = new_state  # Changing state value to new_state
    elif direction == str('get ' + item):  # if
        if item in Inventory:  # if Item is already present in inventory
            print('Item already taken go to another room!!')
        else:
            Inventory.append(item)  # appending
    else:
        print('Invalid input or move or item')  # print
    if len(Inventory) == 6:
        print('Congratulations! You have collected all items and escaped the Xenomorph Queen!')  # print
        exit(0)
