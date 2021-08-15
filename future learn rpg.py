import json

    
def showInstructions():
    # Print a main menu and the commands
    print("""
RPG Game
========

Get to the Garden with a key and a potion.
Avoid the monsters!

You are getting tired; each time you move you lose one health point.

Commands:
    go [north | south | east | west]
    get [item]
    use [item]
""")

def showStatus():
    print("---------------------------")
    print(name + " is in the " + currentRoom)
    print("Health : " + str(health))
    # Print the current inventory
    print("Inventory : " + str(inventory))
    # Print an item if there is one
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"])
    print("---------------------------")

try:
    print("Retrieving player data")
    with open("gamedata.json","r") as f: #<----
        gamedata = json.load(f)
        name = gamedata["playername"]
        health = gamedata["playerhealth"]
        currentRoom = gamedata["playercurrentRoom"]
        inventory = []
except FileNotFoundError:
    print("No previous game found. Starting new game...")
    name = None
    health= 5
    currentRoom = "Hall"
    inventory = []


    

rooms = {
          "Hall" : { "south" : "Kitchen",
                     "east"  : "Dining Room",
                     "item"  : "key"
                   },

          "Kitchen" : { "north" : "Hall",
                        "item"  : "monster"
                      },

          "Dining Room" : { "west"  : "Hall",
                            "south" : "Garden",
                            "item"  : "potion"
                          },

          "Garden" : { "north" : "Dining Room" }
        }


for room in rooms.keys():
    # is there an item in the room
    if "item" in rooms[room]:
        # is the item in the room in the inventory?
        if rooms[room]["item"] in inventory:
            # if so, delete it
            del rooms[room]["item"]

if name is None:
    name = input("What is your name, Adventurer? >>")
    showInstructions()
while True:
    showStatus()
    move = ""
    while move == "":
        move = input(">")
    move = move.lower().split()

    if move[0] == "go":
        if move[1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
            health -= 1
        else:
            print("You can't go that way!")
    if move[0] == "get":
        if "item" in rooms[currentRoom] and move[1]:
            inventory += [move[1]]
            print("{} got!".format(move[1]))
            del rooms[currentRoom]["item"]
        else:
            print("Can't get" + move[1] + "!")
    if move[0] == "use":
        if move[1] == "potion" and "potion" in inventory:
            health += 1
            print("Potion used, you have {} potions left".format(inventory.count("potion")))
            inventory.remove("potion")
    if "item" in rooms[currentRoom] and "monster" in rooms[currentRoom]["item"]:
        print("You have been spotted by a monster! 3 health taken")
        health -= 3
    if health == 0:
        print("You collapse from exhaustion...")
        break
    if currentRoom == "Garden" and "key" in inventory:
        print("You escaped...YOU WIN!")
        break

    gamedata = {
    "playername": name,
    "playerhealth": health,
        "playercurrentRoom": currentRoom
        }
    with open("gamedata.json","w") as f:
        json.dump(gamedata,f)

