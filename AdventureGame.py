#inventory = ("tibbers")

#gameOver = False

#while not gameOver:

    ##print (inventory)
    #userinput = input("?").lower()

    #if userinput in ["yes", "ye", "yaaasss", "sure", "ok", "well why the fakiti not then les fuckin do it lmao360 "]:
        #print (inventory)
        #f = input("Well Yippe! who's fighting today then? ")
        #if f in inverntory:
            #print ("%s is ready to go" % f)
        #else:
            #print("You don't have that weapon")


inventory = []
chest = ["gold", "rubies", "diamonds", "skull", "chalice"]

gameOver = False

while not gameOver:

    userinput = input("After a long expedition you reached the secret Temple of Dratini, do you wish to enter?: ").lower()
    if userinput in ["yes", "ye", "yaaasss", "sure", "ok", "lesdoit"]:
        choice1 = input("You enter the huge doorway of the temple. You walk through a long corridor that enters a large empty room with a chest in the centre. You approach the chest, do you open it?: ").lower()

        if choice1 in ["yes", "open it", "i open it", "open"]:

                print ("You lift the lid off the chest and start to hear gears turning, you look behind to see the door slowing closing. You look into the chest and have to make a decision.")
                while True
                    print (chest)
                    choice1a = input("QUICK you can only choose 3 items: ").lower()

                    ch = choice1a.split(" ")
                    for word in ch:
                        if word in chest:
                            inventory.append(word)
                        else:
                            print("This is not in the chest")

                #if choice1a in chest:
                    #print(" %s, Good choice" % choice1a)

                    #choice1b = input("What else?: ").lower()
                    #if choice1b in chest:
                #         print (" %s , I dont know about that one" % choice1b)
                #         choice1c = input("One more time come on!: ").lower()
                #         if choice1c in chest:
                #             print (" %s ? Good enough lets go"% choice1c)
                #
                # else:
                #     print("This is not in the chest, make sure to type 1")




        else:
            if choice1 in ["no", "nah im going home", "bye", "nope"]:
                print ("You turn around to exit the temple and trip on a twig and break your neck")
                gameOver = True




    else:
        if userinput in ["no", "nah im going home", "bye", "nope"]:
            print ("You turn around to exit the temple and trip on a twig and break your neck")
            gameOver = True
