from time import sleep
import run

# Setup
yes_no = ["yes", "no"]
response = [""]
directions = ["left", "right", "straight ahead"]
accommodation = ["Treehouse", "Ecolodge", "a tent under the trees"]
explore = ["Gorilla Sanctuary", "abandoned village", "Native Community Tour"]

#game start
"""
This is the game section for the Dark Rainforest portion of the game.
"""

def plane_rainforest():
    print("You jump on the plane to go to the Dark Rainforest and sitting next to you is a man acting very strangely.")
    sleep(0.5)
    print("He is reading what appears to be a guidebook from an early explorer. He looks dazed but is not bothering you so you ignore him and go to sleep.")
    sleep(0.5)
    print("Before you know it, the plane is starting to land and you realise that you've not booked anywhere to sleep...")
    print("After landing and getting your luggage, you go to the nearest Tourist information desk to enquire about accommodation")
    sleep(0.5)
    print("The assistant advises you of the options and the costs for each")
    print("The first option is the Treehouse that has great views over the whole rainforest. There have been stories though of strange rituals being performed on but nothing major")
    print("The second option is the Ecolodge that has daily yoga on the terrace. It is very peaceful and relaxing")
    print("The final option is to not bother with any accommodation and sleep in a tent under the trees. There is bound to be adventure and interesting people or animals to meet with this option")

while response not in accommodation:
    response = input("Where would you like to stay?\n")
    if response == "Treehouse":
        print("I hope you will be safe there... The minibus outside the airport will take you straight there")
    elif response == "Ecolodge":
        print("I think you will have a lovely, relaxing time there... or will you? The minibus outside the airport will take you straight there")
    elif response == "a tent under the trees":
        print("An adventurer! I like that. Please take the minibus to the Ecolodge and walk from there to your chosen spot. You can buy a tent from the stall in arrivals")
    else:
        print("I don't understand that")

if response == "Treehouse":
    print("You have reached the Treehouse and get settled in nicely")
    sleep(0.5)
    print("After unwinding for a while, you decide to go exploring")

if response == "Ecolodge":
    print("You have reached the Ecolodge and get settled in nicely")
    sleep(0.5)
    print("After unwinding for a while, you decide to go exploring")    

if response == "a tent under the trees":
    print("You have reached the rainforest and chose your spot to set up your tent. You get set up and settled in nicely")
    sleep(0.5)
    print("After unwinding for a while, you decide to go exploring")

plane_rainforest()