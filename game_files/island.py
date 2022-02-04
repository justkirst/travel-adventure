from time import sleep
import run

# Setup
yes_no = ["yes", "no"]
response = [""]
directions = ["left", "right", "straight ahead"]
accommodation = ["beach hut", "beach hotel", "on the beach under the stars"]
explore = ["local town", "old castle", "history museum"]

#game start
"""
This is the game section for the Tropical Island portion of the game.
"""

def plane_island():
    print("You jump on the plane to go to the Tropical Island and sitting next to you is a man acting very strangely.")
    sleep(0.5)
    print("He is reading what appears to be a book from the medieval times. He looks dazed but is not bothering you so you ignore him and go to sleep.")
    sleep(0.5)
    print("Before you know it, the plane is starting to land and you realise that you've not booked anywhere to sleep...")
    print("After landing and getting your luggage, you go to the nearest Tourist information desk to enquire about accommodation")
    sleep(0.5)
    print("The assistant advises you of the options and the costs for each")
    print("The first option is the Beach Hut located with the best view over the main beach. There have been stories though of strange goings on but nothing major")
    print("The second option is the Beach Hotel that has a private pool and butler. It is very peaceful and relaxing")
    print("The final option is to not bother with any accommodation and sleep on the beach under the stars. There is bound to be adventure and interesting people to meet with this option")

while response not in accommodation:
    response = input("Where would you like to stay?\n")
    if response == "Beach Hut":
        print("I hope you will be safe there... The taxi driver outside the airport will take you straight there")
    elif response == "Beach Hotel":
        print("I think you will have a lovely, relaxing time there... or will you? The taxi driver outside the airport will take you straight there")
    elif response == "on the beach under the stars":
        print("An adventurer! I like that. Please take the local bus to the spot on the beach where you want to sleep")
    else:
        print("I don't understand that")

    if response == "Beach Hut":
        print("You have reached the Beach Hut and get settled in nicely")
        sleep(0.5)
        print("After unwinding for a while, you decide to go exploring")

    if response == "Beach Hotel":
        print("You have reached the Beach Hotel and get settled in nicely")
        sleep(0.5)
        print("After unwinding for a while, you decide to go exploring")

    if response == "on the beach under the stars":
        print("You have chosen your spot on the beach and found a safe spot for your belongings")
        sleep(0.5)
        print("After unwinding for a while, you decide to go exploring")        

while response not in explore:
    response = input("You've looked through the information booklets. Do you want to go the local town, an old castle or the history museum?\n")
    if response =="local town":
        print("Brilliant choice. Grab your comfy shoes and sunscreen. Let's Go!")
    elif response == "Old Castle":
        print("Good choice. Grab your comfy shoes and camera. Let's Go!")
    elif response == "history museum":
        print("Awesome, let's go and find out more about this island!")
    else:
        print("I don't understand that. Let us try again.")

if response == "local town":
    print("You arrive in the town centre and notice the man from the plane sitting at a nearby cafe")
    sleep(0.5)
    print("You watch him for a while and decide to go to the cafe and have a drink at a table next to him.")
    print("You secretly hope for him to notice you, so you can initiate a conversation.")
    sleep(1)
    print("You arrive at the cafe and order your drink. You sit next to him and watch.")
    sleep(0.5)
    print("You only have to wait a few minutes before he recognises you and asks your name")
    print("You tell him your name and ask what his name is.")
    print("The man tells you his name is Jacob and that he remembers you from the plane. He asks if you'd like to go to a local stone monument that is rich in history.")
    sleep(0.5)

print("Do you want to go and see the monument?\n")
response = input(yes_no)

while response not in yes_no:
    print("I don't understand. Please try again")
    response = input(yes_no)
if response == "yes":
    print("Jacob pays for your drink and you leave for the monument")
elif response == "no":
    print("Well that means it is the end of the adventure for you. Goodbye!")
    quit()

def monument():
    print("You arrive at the monument and start to look around")
    sleep(0.25)
    print("All of a sudden you feel a chill down your spine and notice that Jacob has started to chant")
    print("You are not one to believe in spirits or being possessed but it does seem that this has happened to Jacob")
    sleep(0.5)
    print("You look around to leave but realise that you're lost and don't know where the exit is")
    print("What direction should you go to leave?\n")    



plane_island()
monument()
