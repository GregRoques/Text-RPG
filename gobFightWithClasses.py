import os
from hero import Hero

# ======The Hero=====

theHero = ("hero_name", 8)

hero_name = raw_input("What is your name brave one: ")
theHero = ("hero_name", 8)
theHero.cheerHero()



while (theHero.health > 0 and goblin_health > 0):
        print""
        
        print """
    You have %d health and %d power. 
    The goblin has %d health and %d power. 
    What do you want to do?
    1. fight goblin
    2. dance
    3. flee
    4. power up
    > """ % (theHero.health, theHero.power, goblin_health, goblin_power)

        userInput = raw_input()

        if (userInput == "1"):
            # The hero has decided to attack
            # subtract goblins health by hero power
            goblin_health -= theHero.power
            print""
     
            if (goblin_health < 1):
                print "Thou hath killithed the goblin."
                break

            else:
                    print "You have done %d damage to the goblin." % theHero.power

        elif (userInput == "2"):
            randomDance = random.randint(0,1)
            if (randomDance == 0):
                theHero.health -=5

                if(hero_health < 1):
                    print "SMH... %s, you are pathetic!!!" % theHero.name
                    break

                else:
                    print "You got served! Health reduces to %d." % hero_health

            else:
                goblin_health -=1

                if (goblin_health < 1):
                    print "The goblin can't keep up...he admits defeat."
                    break
                else:
                    print "The goblin got served. Goblin health reduces to %d." % goblin_health

        elif (userInput == "3"):
            print ""
            print "Goodbye cowardly, %s." % theHero.name
            # break statement will end the loop immediately
            break

        elif (userInput == "4"):
            if (power_up > 0):
                power_up -= 1
                theHero.health +=4
                print ""
                print "Your health increases to %d" % theHero.health
            else:
                print "You have no power ups left."


        else: 
            # User entered something we didn't offer
            theHero.health -=1
            print "Thou fool. Your health goes down %d for your stupidity. (invalid input)." % hero_health
            
        # Now it's the goblin's turn (as long as he is alive.)
        if (goblin_health > 0):
            theHero.health -= goblin_power
        
            print "The goblin hits you for %d damage." % goblin_power
            if (theHero.health == 0):
                print "Thou hast been vanquished. Thou suckith."
                os.system("say Thou hast been vanquished. Thou suckith.")
                break
        raw_input("Hit enter to continue.")
        os.system("clear")

fight()    