from time import sleep

# Setup
yes_no = ["yes", "no"]
destination = ["Tropical Island", "Dark Rainforest"]

# Game Introduction
name = input("What is your name?\n")
print("Hi " + name + "!")
# Setup
yes_no = ["yes", "no"]

response = ""
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






#Start of the Game
