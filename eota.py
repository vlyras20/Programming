print ("You have woken up in a jungle, wounded and with no memory of coming here.")
print ("...Guuhh.. uuhH.. wha.. what the... Who did this?")
print ("I gotta get out of here... uugh.. Ah.")
print ("Fast")
print ("There's a clearing down the mountain I can see.")
print ("I also hear a river closeby.")
print ("Should I go for the clearing[1], follow the river[2] or maybe try climb a tree and scout my surroundings[3]")

number = int(input("Where do I go?([1][2][3]) "))

if number == 1:
    print ("Alright, I'm almost at the clearing. There's monkeys roaming above in the trees. I should be careful")
    print ("This is a small clearing and doesn't lead anywhere, I should keep moving.")
    print ("I could maybe cut through the jungle and go as far as I can see where it leads me.")
    print ("The other option is heading back where I could hear the river and follow that.")
    print ("Cut through the jungle[1] or follow the river[2]?")
    route = int(input("Where do I go?"))
    if route == 1:
        print ("Ok, im just going to keep moving through the jungle and see where it leads me.")
        print ("AHH! I think a snake just took a bite out of my leg. I'm running back to the clearing")
        print ("I'm.. getting.. really dizzy.. I think I'm going to just take a.. nap.. for a minute")
        print ("Player death: VENOMOUS SNAKE BITE")
    elif route == 2:
        print ("Alright, hopefully this leads me to some sort of civilization.")
        print ("Hey, I think I see some old shacks at the bottom of the mountain.")
        print ("Yeah! I think I see people!")
        print ("... wh. wait a minute... .. Thats not people. what the f.. they look alien.")
        print ("omg, I think they see me. WHERE THE HELL DID I WAKE UP INTO?")
        print ("OHHHHH THEY SEE ME!. OMG THEY'RE FAST. nooo nononooo no DOnt NOOO!!")
        print ("You are captured and have to escape. DEMO OVER")
elif number == 2:
    print ("Alright, hopefully this leads me to some sort of civilization.")
    print ("Hey, I think I see some old shacks at the bottom of the mountain.")
    print ("Yeah! I think I see people!")
    print ("... wh. wait a minute... .. Thats not people. what the f.. they look alien.")
    print ("omg, I think they see me. WHERE THE HELL DID I WAKE UP INTO?")
    print ("OHHHHH THEY SEE ME!. OMG THEY'RE FAST. nooo nononooo no DOnt NOOO!!")
    print ("You are captured and have to escape. DEMO OVER")
elif number == 3:
    print ("Alright, up we go, I have to figure out where I am so I get out of here")
    print ("Ohhh noo! ... Uhh.. uhgh. Damn. Ok gotta remind myself not to slip again.")
    print ("Is it even a good idea to still climb this tree or should I head elsewhere?")
    option = int(input("Keep climbing[1] or head down[2]?"))
    if option == 1:
        print ("I can do this. I have to see where I am or I don't know where to go.")
        print ("..... Almost... there..")
        print ("ohh no! uhghh ahhh! Ahhhhhh!")
        print ("Player death: FELL OF JUNGLE TREE TOP")
    elif option == 2:
        print ("Yeah.. Lets head down, this was a terrible idea.")
        print ("Alright. Now do I go for the clearing[1] or the river[2]")
        path = int(input("Where do I go?"))
        if path == 1:
            print ("Alright, I'm almost at the clearing. There's monkeys roaming above in the trees. I should be careful")
            print ("This is a small clearing and doesn't lead anywhere, I should keep moving.")
            print ("I could maybe cut through the jungle and go as far as I can see where it leads me.")
            print ("The other option is heading back where I could hear the river and follow that.")
            print ("Cut through the jungle[1] or follow the river[2]?")
            route = int(input("Where do I go?"))
            if route == 1:
                print ("Ok, im just going to keep moving through the jungle and see where it leads me.")
                print ("AHH! I think a snake just took a bite out of my leg. I'm running back to the clearing")
                print ("I'm.. getting.. really dizzy.. I think I'm going to just take a.. nap.. for a minute")
                print ("Player death: VENOMOUS SNAKE BITE")
            elif route == 2:
                print ("Alright, hopefully this leads me to some sort of civilization.")
                print ("Hey, I think I see some old shacks at the bottom of the mountain.")
                print ("Yeah! I think I see people!")
                print ("... wh. wait a minute... .. Thats not people. what the f.. they look alien.")
                print ("omg, I think they see me. WHERE THE HELL DID I WAKE UP INTO?")
                print ("OHHHHH THEY SEE ME!. OMG THEY'RE FAST. nooo nononooo no DOnt NOOO!!")
                print ("You are captured and have to escape. DEMO OVER")
        elif path == 2:
            print ("Alright, hopefully this leads me to some sort of civilization.")
            print ("Hey, I think I see some old shacks at the bottom of the mountain.")
            print ("Yeah! I think I see people!")
            print ("... wh. wait a minute... .. Thats not people. what the f.. they look alien.")
            print ("omg, I think they see me. WHERE THE HELL DID I WAKE UP INTO?")
            print ("OHHHHH THEY SEE ME!. OMG THEY'RE FAST. nooo nononooo no DOnt NOOO!!")
            print ("You are captured and have to escape. DEMO OVER")
