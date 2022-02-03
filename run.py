from time import sleep
import game_files

# Setup
yes_no = ["yes", "no"]
response = ""
destination = ["Tropical Island", "Dark Rainforest"]
directions = ["left", "right", "straight ahead"]
response = ""
plane_island = game_files.island()
rainforest = game_files.rainforest()

# Game Introduction
"""
Introduction part of the game for the player to start their adventure
"""
name = input("What is your name?\n")
print("Hi " + name + "!")

while response not in yes_no:
    response = input("Would you like to start a new game?\n Yes or No?\n")
    if response == "yes":
        print("Great! Let's get started!")
    elif response == "no":
            print("You are not ready for the adventure of a lifetime… Goodbye!")
            quit()
    else:
                print("I didn't understand that.\n")

sleep(1)
print("You have just won the lottery and decided to go on an adventure and run straight to the airport for the next available flight.")
sleep(1.5)
print("You have two choices when you arrive at the airport.")

while response not in destination:
    response = input("Do you want to go to a Tropical Island or a Dark Rainforest?\n")
    if response == "Tropical Island":
        print("Great choice " + name + "! I hope you've brought your beach gear")
    elif response == "Dark Rainforrest":
            print("Great choice " + name + "! I hope you've brought your raincoat and wellies.")
    else:
        print("This destination is not available today. You've now left the airport. Goodbye!\n")
        quit() 

#Start of the Game
"""
This is the section where the game will break off either for the Tropical Island portion or the Dark Rainforest portion.
"""