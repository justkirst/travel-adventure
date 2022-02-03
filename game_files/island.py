from time import sleep

# Setup
yes_no = ["yes", "no"]
directions = ["left", "right", "straight ahead"]
accommodation = ["beach hut", "beach hotel", "on the beach under the stars"]

#game start

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

response = ""
while response not in accommodation:
    response = input("Where would you like to stay?")
    if response == "Beach Hut":
        print("I hope you will be safe there... The taxi driver outside the airport will take you straight there")
    elif response == "Beach Hotel":
        print("I think you will have a lovely, relaxing time there... or will you? The taxi driver outside the airport will take you straight there")
    elif response == "on the beach under the stars":
        print("An adventurer! I like that. Please take the local bus to the spot on the beach where you want to sleep")
    else:
        print("I don't understand that")    
