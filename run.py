# Setup
yes_no = ["yes", "no"]

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

print("You have just won the lottery and decided to go on an adventure and run straight to the airport for the next available flight.")
print("You have two choices when you arrive at the airport.")
destination = input("Do you want to go to a Tropical Island or a Dark Rainforest?\nTropical Island or Dark Rainforest\n")

#Start of the Game
