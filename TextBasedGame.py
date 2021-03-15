import sys
from time import sleep
from os import system, name

def clearScreen():
    if name == "nt":
        _ = system("cls")

def startgame():
    pass

def gamemanual():
    print('Move commands: go North, go South, go East, go West')
    print("Add to Inventory: get 'item_name'")

def main():
    login()

def login():
    username = "ellen"
    password = "ripley"
    print("Enter username : ")
    answer1 = input()
    print("Enter password : ")
    answer2 = input()
    print("")
    if answer1 == username and answer2 == password:
        introtext = "************ACCESS GRANTED*************\n"
        for char in introtext:
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
    else:
        exittext = "************ACCESS DENIED*************\n"
        for char in exittext:
            sleep(0.2)
            sys.stdout.write(char)
            sys.stdout.flush()
        exit(0)
    menu()

def menu():
    print("Welcome to Alien".center(40))
    print("**************MAIN MENU****************")
    # time.sleep(1)
    print()

    choice = input("""
            A: Start Game
            C: Game Manual
            Q: Quit/Log Out

            """)

    if choice == "A" or choice == "a":
        startgame()

    elif choice == "C" or choice == "c":
        gamemanual()
        sleep(1.5)
        clearScreen()
        menu()
    elif choice == "Q" or choice == "q":
        sys.exit
    else:
        print("You must only select either A or C.")
        print("Please try again")
        menu()
main()

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


default_state = 'Flight Deck'

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

sleep(2)
clearScreen()

# Function
def show_instructions():
    # Print an instruction pane and the commands to play the game
    print('Welcome to Alien')
    print("Created by Michael Alestock")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    print('Collect all 6 items and escape the ship, or be harvested by the Xenomorph Queen')
    print('Move commands: go North, go South, go East, go West')
    print("Add to Inventory: get 'item_name'")
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
show_instructions()  # Calling the function

Inventory = []
items = ['Red Key Card', 'Purple Key Card', 'Blue Key Card', 'Evacuation Protocol Documents', 'Flamethrower',
         'Launch Key']


while (1):  # Gameplay Loop
    print('You are in', default_state)  # Printing the default_state
    print('Inventory:', Inventory)  # Printing the inventory
    item = get_item(default_state)  # Calling get_item function
    print('You see a', item)  # print
    print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    if item == 'Xenomorph Queen':  # if
        print('You have been harvested... GAME OVER!')
        exit(0)
    direction = input('Enter your move: ')  # Asking the user
    if direction == 'go East' or direction == 'go West' or direction == 'go North' or direction == 'go South':
        direction = direction[3:]
        new_state = get_new_state(default_state, direction)  # Calling the function
        if new_state == default_state:  # if
            print('The room has wall in that direction enter other direction!')  # Print
        else:
            default_state = new_state  # Changing default_state value to new_state
    elif direction == str('get ' + item):  # if
        if item in Inventory:  # if Item is already present in inventory
            print('Item already taken go to another room!!')
        else:
            Inventory.append(item)  # appending
    elif direction == str('drop ' + item):
        if item in Inventory:
            Inventory.remove(item) # removing
    else:
        print('Invalid input or move or item')  # print
    if len(Inventory) == 6:
        print('Congratulations! You have collected all items and escaped the Xenomorph Queen!')  # print
        exit(0)
