 
#ready to play
import time
import random
def looking(prechoice):
    explore="You take a look around."
    print("")
    print(explore)
    time.sleep(2)
    print("What would you like to look at?")
    print("")
    print("Look at your bed (Bed)")
    print("Look at desk (Desk)")
    print("Look at your wardrobe (Wardrobe)")
    print("Stop looking around (Stop)")
    pre2=input("")
    exploreroom=pre2.lower()
    return exploreroom
    
def begin():
    print("What would you like to do?")
    print("")
    print("Check inventory (Inventory)")
    print("Leave your room (Leave)")
    print("Look around the room (Explore)")
    pre1=input("")
    prechoice=pre1.lower()
    return prechoice

game="running"
while game=="running":
#    print("___________________________________________________________________________________________________________________________________________________________________________________")
#   print("")
#    print("")
#    print("Thank you for playing ______________.")
#    time.sleep(2)
#    print("This game is currently in devolopement so expect bugs and random stops in the game.")
#    time.sleep(4)
#    print("Until this game has been finished, please enjoy the early Alpha of ______________!")
#    time.sleep(4)
#    print("")
#    print("")
#    print("")

#    print("Welcome to Narvalia.")
#    time.sleep(2)
#    print("")
#    print("The story of this great place is one that has been lost through the ages.")
#    time.sleep(3)
#    print("")
#    print("Forgotten by all but my family.")
#    time.sleep(2)
#    print("")
#    print("My family is a line of powerful mages that evaded the king's soldiers at almost every turn.")
#    time.sleep(4)
#    print("")
#    print("So let me tell you the story of an ancient time, one of magic, poverty, racism, and an all around awful situation.")
#    time.sleep(6)
#    print("")
#    print("Ahem")
#    time.sleep(1)
#    print("")
#    print("Once apon a time, Narvalia was a beautiful place.")
#    time.sleep(3)
#    print("")
#    print("Until that is a mystical event took place that would change the world.")
#    time.sleep(3)
#    print("")
#    print("An event that would cause the greatest advances and the worst conflicts.")
#    time.sleep(4)
#    print("")
#    print("After a long night of rest you wake up")
#    time.sleep(3)
#    print("")

    ###Game begins here###

    print("Are you a man or woman?")
    gen=input("")
    gender=gen.lower()

    if gender=="man":
        spouse="Set"
        print("Your gender is now male.")

    if gender=="woman":
        spouse="Forish"
        print("Your gender is now male")
        
    name=input("Enter your name or enter random: ")
    namel=name.lower()
    if namel=="random":
        if gender=="man":
            names=["Winerah", "Arcake", "Anjeff", "Savid", "Brito", "Gormamen", "Lin", "Gakim", "Thasevermark", "Riwyn", "Ingchar", "Ordlett", "Markdino", "Thaechet", "Garlas", "Winemax", "Nidic", "Donni",]
            AIchoice=random.randint(0,17)
            name=names[AIchoice]

        if gender=="woman":
            names=["Inesmih", "Ceihnol", "Jhiznizno", "Mune", "Ralne", "Mos", "Zigofni", "Hafnay", "Zushutheth", "Vazhu", "Sirsendru", "Zue", "Mai", "Fonc", "Bonnv", "Asmoreih", "Yeismoh", "Uzodra",]
            AIchoice=random.randint(0,17)
            name=names[AIchoice]

        print("So "+name+", you are a normal person who lives in a normal house with a normal family, I think that you should go and see them.  After all, it is breakfast time.")
        #time.sleep(4)
    else:
        print("So "+name+", you are a normal person who lives in a normal house with a normal family, I think that you should go and see them.  After all, it is breakfast time.")
        #time.sleep(4)
    

    start="running"
    while start=="running":    
        prechoice=begin()
    

        if prechoice=="inventory":
            inventory="You have "
            pen1=" your trusty pen"
            clothing1=" normal clothing "
            print(inventory+clothing1+"and"+pen1+".")
            time.sleep(3)
            print("")
            #prechoice=begin()
        
        if prechoice=="explore":
            exploreroom=looking(prechoice) 
        
            
            if exploreroom =="bed":
                print("A normal bed, brought to us by Lopino's.")
                time.sleep(2)
                print("")
                exploreroom=looking(prechoice)
              
            if exploreroom =="desk":
                print("A normal desk, "+spouse+" got this from Lopino's if I'm not mistaken.")
                time.sleep(2)
                print("")
                exploreroom=looking(prechoice)
              
            if exploreroom =="wardrobe":
                print("I really need to clean this old thing out.  Many of these clothes I don't even use anymore.")
                time.sleep(2)
                print("")
                exploreroom=looking(prechoice)

            if exploreroom =="stop":
                print("")
                #exploreroom=prechoice=begin()
                a=1

        if prechoice=="leave":
            start="stop"
            print("As you open the door to your room, the smell of fresh eggs from the farm hits your nose")
#            time.sleep(3)
            print(""" "So you've finally woken up!  Just in time, I just finished you eggs." """)
#            time.sleep(3)
            print(""" "A letter came by while you were asleep.  I've put it on the table." """)
#            time.sleep(3)
            print("")

    dinningroom="running"
    while dinningroom=="running":
        print("What do you want to do?")
        print("")
        print("Check inventory (Inventory)")
        print("Look around the area (Explore)")
        print("Talk to "+spouse+" (Spouse)")
        print("Eat and look at your letter (Letter)")
        pre3=input("")
        eggsandletter=pre3.lower()

        if eggsandletter=="inventory":
            inventory="You have "
            pen1=" your trusty pen"
            clothing1=" normal clothing "
            print(inventory+clothing1+"and"+pen1+".")
            time.sleep(3)
        
        if eggsandletter=="explore":
            #print("This section of the game is experiencing bugs.  It will be unavalible at this time please enjoy another option.")
            #time.sleep(3)
            #print("")
            eal="going"
            print("You take a look around.")
            time.sleep(2)
            while eal=="going":
                print("")
                print("What do you want to look at?")
                print("")
                print("Look at the dinning room table (Table)")
                print("Look at the children (Children)")
                print("Look at "+spouse+" (Spouse)")
                print("Stop looking around (Stop)")
                pre4=input()
                lookingeal=pre4.lower()


                if lookingeal=="table":
                    print("It's the table I made for our anniversary.  I can't believe I kept it hidden from her.")
                    time.sleep(4)

                if lookingeal=="children":
                    print("It's our children, Tarrel (the eldest) and Raffi.  It's Tarrel's birthday in a few weeks.")
                    time.sleep(4)

                if lookingeal=="spouse":
                    if spouse=="Set":
                        print("It's my lovely wife, Set.  I can't wait to show her the desk I've been working on.")
                        time.sleep(3)
                    if spouse=="Forish":
                        print("It's my husband, Forish.  I can't wait until Lopino's finishes the couch that I've bought for him.  Our current one is to small for him.")
                        time.sleep(5)

                if lookingeal=="stop":
                    eal="ending"

        if eggsandletter=="spouse":
    #       wife="active"
    #       while wife=="active":
            print("This portion of the game is currently experiencing bugs.  Please feel free to look at other features and check back later for a fixed version.")
    #            print("You walk over to Set.")
    #            time.sleep(2)
    #            print("What do you want to say?")
    #            print("")
    #            print("Why aren't the children at school? (Children)")
    #            print("""What's the letter about? (Letter)""")
    #            print("I though that we were all out of eggs. (Eggs)")
    #            print("Say nothing (Stop)")
    #            pre5=input("")
    #            lovely=pre5.lower()

#            if pre5=="children":
#                print("They're teacher needed to go out of town for a few days so the children don't have any school.")
#                time.sleep(3)

#            if pre5=="letter":
#                print("I haven't openned it but on the back it says it's from Polino's.")
#                time.sleep(3)

#            if pre5=="eggs":
#                print("I asked the neighbors if they had any eggs and they gave us some of their extras.")

#            if pre5=="stop":
#                wife="dormant"

        if eggsandletter=="letter":
            dinningroom="stopped"
            if gender=="man":
                print(name+" sits down at the table and opens the letter.")
#               #time.sleep(2)
                print(""" "Mr. Narui, we regret to inform you that due to the recent blaze at the Polino's Furniture and Carvings in your area your slot and items within have been destroyed by the flames." """)
#               #time.sleep(7)
                print(""" "Because of this we have given to you the 40 pieces that you used to buy the slot and the items within.  We hope we haven't lost you as a loyal customer.  Sincerely, Polino's Furniture and Carvings" """)
#               #time.sleep(7)
                print("Holding the letter in his hand "+name+" was furious.  He had spent so much time and money creating the desk that was in his slot.")
#               #time.sleep(6)
                print("But his anger was interupted by the screams coming from outside.")
#               #time.sleep(3)
                print("Openning his front door "+name+" saw monsterous beasts chasing down and killing the neighbors and and workers in his community.")
#               #time.sleep(5)
                print("He instructed his children and wife to head for the cellar.")
#               #time.sleep(3)
                print("But before he could join them his neighbor was pushed to the ground and was being attacked by a beast.")
#               #time.sleep(5)
                print("")
                print("Deside carefully as this choice could effect the game and future events.")
                print("")
#               #time.sleep(4)
            if gender=="woman":
                print(name+" sits down at the table and opens the letter.")
#               #time.sleep(2)
                print(""" "Mrs. Narui, we regret to inform you that due to the recent blaze at the Polino's Furniture and Carvings in your area your slot and items within have been destroyed by the flames." """)
#               #time.sleep(7)
                print(""" "Because of this we have given to you the 40 pieces that you used to buy the slot and the items within.  We hope we haven't lost you as a loyal customer.  Sincerely, Polino's Furniture and Carvings" """)
#               #time.sleep(7)
                print("40 pieces have been added to your inventory")
                time.sleep(3)
                print("Holding the letter in her hand "+name+" was furious.  She had spent so much money on that slot and wood for her and her husband that it could make her rip the letter to shreds.")
#               #time.sleep(7)
                print("But her anger was interupted by the screams coming from outside.")
#               #time.sleep(3)
                print("Openning her front door "+name+" saw monsterous beasts chasing down and killing the neighbors and and workers in her community.")
#                #time.sleep(5)
                print("She instructed her children and husband to head for the cellar and meet her there.")
#                #time.sleep(3)
                print("But before she could join them her neighbor was pushed to the ground and was being attacked by a beast.")
#                #time.sleep(5)
                print("")
                print("Deside carefully as this choice could effect the game and future events.")
                print("")
#                time.sleep(4)

            firstchoice="deside_time"
            while firstchoice=="deside_time":
                print("Grab a knife from the kitchen and save your neighbor (Neighbor)")
                print("")
#man                time.sleep(4)
                print("or")
                print("")
                print("Run with your family to the cellar and help protect them (Family)")
                print("")
                (4)
                choosecarefully=input("")
                dontmessup=choosecarefully.lower()

                if dontmessup=="neighbor":
                    firstchoice="wasthatright"
                    print("You entered the kitchen, grabbed a knife, and have saved your neighbor but your family had a harder time entering the cellar.")
#                    time.sleep(4)
                    choice1="neighbor"
                    print("Your neighbor looks at you and thanks you before running away.")
#                    time.sleep(3)
                    print("You run to your family, get them into the cellar, and close the door and block it with an old bookshelf inside.")
#                    time.sleep(5)
                    print(""" "What took you so long?!  We almost were killed on the way here!" """)
#                    time.sleep(3)
                    while choice1=="neighbor":
                        if spouse=="Set":
                            print("What would you like to say to your wife?")
                            print("")
                            print("")
                            print("Tell her that took you so long (Truth)")
                            print("")
                            print("Quickly make up a lie (Lie)")
                            evn1=input("")
                            incellar=evn1.lower()
                        if spouse=="Forish":
                            print("What would you like to say to your husband?")
                            print("")
                            print("")
                            print("Tell him that took you so long (Truth)")
                            print("")
                            print("Quickly make up a lie (Lie)")
                            evn1=input("")
                            incellar=evn1.lower()

                        if incellar=="truth":
                            print("You tell "+spouse+" the truth")
                            print(""" "Thank you for being honest but you really should've been here and helped move the cart." """)
                            choice1="happened"
                            cellar1="inside"

                        if incellar=="lie":
                            print("You tell "+spouse+" that your foot was caught on.")
                            print(""" "That's why you were late?  You could've yelled for help." """)
                            choice1="happened"
                            cellar1="inside"





                if dontmessup=="family":
                    firstchoice="wasthatright"
                    print("You stayed with your family all the way to the cellar and helped them quickly get out of harms way but your neighbor has died.")
                    choice1="cellar"
                    while choice1=="cellar":
                        print("You see your neighbor is killed in front of you, looking with pleading eyes but you run away as quick as you can.")
#                        time.sleep(4)
                        print("You reach the cellar and helped push a cart that had been pushed over in front of the door away.")
#                        time.sleep(5)
                        print(""" "Thank you for helping.  I wouldn't have been able to push that cart on my own." """)
#                        time.sleep(3)
                        print("You and your family enter the cellar and block the door with an old bookshelf.")
#                        time.sleep(3)
                        cellar1="inside"


                    while cellar1=="inside":
                        cellar1="ininside"
                        print(""" "Well I'm just thankful that we made it out of there safe.  What do you think those things were?" """)
#                        time.sleep(4)
                        print("You tell your wife that you've never seen anything like what that was.")
#                        time.sleep(3)
                        print(""" "They just came out of no where.  I could feel what I think was an earthquake and then they just appeared." """)
#                        time.sleep(5)
                        if dontmessup=="neighbor":
                            print("Thinking about what you just saw out there your second child, Raffi, begins to scream out in pain.")
#                            time.sleep(4)
                            print("You look him over and see that he has been bitten on his arm and poisoned him.")
#                            time.sleep(3)
                            print("You tell him it will all be fine as you cut open the bite and start sucking out the poison.")
#                            time.sleep(4)
                            print("The sounds attracted the beasts outside and they began to break down the door to the cellar.")
#                            time.sleep(4)
                            quick=ly
                        if dontmessup=="family":
                            print("Suddenly you hear footsteps outside the cellar door followed by beasts attempting to break the door down.")
#                            time.sleep(5)
                            print("You realized that they followed you in here after you ran for your family.")
#                            time.sleep(3)
                            
                        quick="ly"
                        while quick=="ly":
                            print("What do you want to do?")
                            print("")
                            print("Fight the beasts (Fight)")
                            print("Find a way to flee (Flee)")
                            print("Hide from the beasts (Hide)")
                            evn2=input("")
                            breakingin=evn2
                            time.sleep(6)
                            quick="er"
                            print("You were to slow and were thrown against the wall by the beast, knocking you out.")
                            aftermath="seeing"


                        if breakingin==("fight"):
                            quick=er
                            if gender=="man":
                                if dontmessup=="neighbor":
                                    print("You grab the kitchen kife you grabbed and do your best to kill the beast but it throws you against the wall, knocking you out.")
#                                    time.sleep(6)
                                    quick="er"
                                    aftermath="seeing"
                            if gender=="man":
                                if dontmessup=="family":
                                    print("You grab a large stick that fell in the cellar do your best to kill the beast but it throws you against the wall, knocking you out.")
#                                    time.sleep(6)
                                    quick="er"
                                    aftermath="seeing"
                                    
                            if gender=="woman":
                                if dontmessup=="neighbor":
                                    print("You hand "+spouse+" the kitchen knife you grabbed and tell him to kill the beast but it throws you against the wall, knocking you out.")
#                                    time.sleep(7)
                                    quick="er"
                                    aftermath="seeing"
                            if gender=="woman":
                                if dontmessup=="family":
                                    print("You watch as "+spouse+" grabs a branch that fell into the cellar and begins to attack the beast but the beast and the beast throws you against the wall, knocking you out.")
#                                    time.sleep(8)
                                    quick="er"
                                    aftermath="seeing"

                        if breakingin==("flee"):
                            if gender=="man":
                                print("You tell "+spouse+" to take Tarrel and Raffi and run out of the cellar but the beast throws you against the wall, knocking you out.")
                                quick="er"
                                aftermath="seeing"
                            if gender=="woman":
                                print("You grab Tarrel and Raffi and begin to run out of the cellar but the beast throws you against the wall, knocking you out.")
                                quick="er"
                                aftermath="seeing"

                        if breakingin==("hide"):
                            if gender=="man":
                                print("You tell "+spouse+" to hide her and the children but before you can hide the beast throws you against the wall, knocking you out.")
                                quick="er"
                                aftermath="seeing"
                            if gender=="woman":
                                print("You take Tarrel and Raffi and hide but before you can the beast knocks you against the wall, knocking you out.")
                                quick="er"
                                aftermath="seeing"



                        
                    

                if dontmessup=="me":
                    firstchoice="youbetternothavecheated"

                else:
                    print("Naughty, you've got to do something.")
                    print("")
    
                if dontmessup=="me":
                    firstchoice="wasthatright"
                    your="dumb"
                    print("So you desided to choose yourself?")
                    time.sleep(2)
                    print("Your family and neighbor died and who knows what kind of adventure you missed.")
                    time.sleep(3)
                    print("What kind of hero just lets everyone die by quitting?")
                    time.sleep(3)
                    print("Geeze, some people")
                    time.sleep(2)
                    print("Well I hope you're happy, a whole adventure for free and you're giving up.")
                    time.sleep(4)
                    print("You know what?  I'll give you a choice.")
                    time.sleep(2)
                    print("Either you can choose to live on regretting your every choice, or you can die.  Or reset but I will not tell you the super-secret-ultra-elite-password for it.  So pick.")
                    time.sleep(6)
                    print("")
                    print("Regret")
                    print("")
                    print("Die")
                    your=="dumb"
                    really=input()
                    seriously=really.lower()


            

                    if seriously=="die":
                        print("This is what you desirve")
                        your="dead"
                        game="closing"
                            
                    if seriously=="regret":
                        print("You desirve death more but I'll be sure to drop by every once in a while.")
                        your="stilldumb"
                        game="closing"

                    if seriously=="reset":
                        print("You found out my super-secret-ultra-elite-password?!?")
                        time.sleep(2)
                        print("How?!")
                        time.sleep(1)
                        print("Did your friend tell you?!?")
                        time.sleep(2)
                        print("Did you look it up online!?!")
                        time.sleep(2)
                        print("DID YOU SOMEHOW MANAGE TO IMPUT THE RIGHT CODE?!?  YOU'VE MADE A MISTA")
                        time.sleep(2)
                        your="lucky"
                        
                    else:
                        print("Please just pick something, I'm already stressed enough.")
                        time.sleep(3)

                        while aftermath=="seeing":
                            print("Game ending")
                            game="stopping"

            


    
#game="running"

#while game == "running":
    #Answer=input("What would you like to play or quit?")
    #Answer=Answer.lower()
    #if Answer=="play":
        #a=1
    #if Answer=="quit":
        #game="False"
        #print("I've never heard of a story where the hero quits but bye anyway")
    #while Answer=="play":
        #choice=input("Enter choice")
        #if choice=="quit":
            #Answer="quit"
