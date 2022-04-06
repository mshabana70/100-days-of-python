# Day 3 Project - Stranded
#
# Create a "choose your own adventure" program
# Must take in user input and result in different endings
# depending on user choices

print('''            ^^                   @@@@@@@@@                 
       ^^       ^^            @@@@@@@@@@@@@@@
                            @@@@@@@@@@@@@@@@@@              ^^
                           @@@@@@@@@@@@@@@@@@@@
 ~~~~ ~~ ~~~~~ ~~~~~~~~ ~~ &&&&&&&&&&&&&&&&&&&& ~~~~~~~ ~~~~~~~~~~~ ~~~
 ~         ~~   ~  ~       ~~~~~~~~~~~~~~~~~~~~ ~       ~~     ~~ ~
   ~      ~~      ~~ ~~ ~~  ~~~~~~~~~~~~~ ~~~~  ~     ~~~    ~ ~~~  ~ ~~
   ~  ~~     ~         ~      ~~~~~~  ~~ ~~~       ~~ ~ ~~  ~~ ~
 ~  ~       ~ ~      ~           ~~ ~~~~~~  ~      ~~  ~             ~~
       ~             ~        ~      ~      ~~   ~             ~ \n\n\n''')

print("Welcome to Treasure Island")
choice1 = input("You wash up to shore after a stormy night at sea. It is dark but you can see something shiny in the distance. Press 1 to go towards the shiny object, press 2 to stay in the dark.")
choice2 = ""
choice3 = ""
choice4 = ""

if (choice1 == '1'):
    choice2 = input("You walk towards the shiny object and see that its a zippo lighter. You let out a sigh of relief. You stumble to find dry wood nearby and manage to start a fire. You hear your stomach growl and remember that you havent eaten in days. You look behind you and see some fruits ready to be picked in the jungle behind you. Press 1 to go into the jungle to pick fruit. Press 2 to stay safe by the fire for the night.")
    if (choice2 == '1'):
        print("You go to the jungle and start climbing the tree to get some fruit. You stumble the first couple of tries but you manage to finally get your footing. You get to near top and finally grab some fruit. The wind picks up and you start to lose your grip. You fall and land awkwardly on your back.")
        print("You lay there for a while and realize you cant move. The wind picks up some more and you start to go numb. The numbness helps ease the pain but you start to get sleepy. You close your eyes. Next thing you know youre back home, on your couch watching ESPN. It was all a bad dream.")
    else:
        choice3 = input("You wait by the fire and start to warm up. Your stomach grows louder with hunger. You start to doze off from exhaustion and the warm fire. You fall asleep. Press 1 to wake up, press 2 to stay asleep")
        if (choice3 == '1'):
            choice4 = input("You force yourself away and you see that the sun is up, you go towards the tree line and see some fruit scattered on the floor. You grab some and start eating. You hear a noice in the jungle. Sounds like someone is crying for help. Press 1 to check it out, press 2 to stay on the beach.")
            if (choice4 == '1'):
                print("You go check out the noise. You start to follow the sound and you get closer and closer to the source. The screeching is so loud that it seems like it only a few 100 feet away. You see some bushes ruffle, you go near to investigate. You step into a trap and fall into a spike pit. As you lay there, bleeding out. You see some shady figures that look like people. But they are painted from head to toe. You realize you were baited into a trap for dinner.")
            else:
                print("You stay on the beach and enjoy the fruit you found. You finally feel some more energy within you so you start to make a signal for help. You light some bonfires and set them up on the beach as a beacon. A ship in the distance comes into view. You start waving your hands like a mad man. The ship starts honking in unison. You are saved.")
        else:
            print("You stay asleep and for a bit longer. You finally wake up but everything is upside down. You look around and realize you are hanging above a fire. You notice some figures dancing around you as you slowy begin to roast. You realize you are the main course for supper.")
else:
    print("You stay in the dark and begin to shiver. The cold sends you to sleep. You wake up and find yourself on a helicopter. There are two paramedics attending to your wounds. 'You're lucky we found you, we were heading to SOS signal near by and say a figure on the beach with our night vision.' You cant believe your luck. You thought you were dead for sure but now youre saved!")