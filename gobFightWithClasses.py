# =========IMPORTS===========

from Hero import Hero
from Goblin import Goblin
from Vampire import Vampire
from Wolf import Wolf
from Centaur import Centaur
from random import randint
import os

# =======Input Hero============

print ""
hero_name = raw_input("What is your name, brave one? ")
# There is only one Frodo
theHero = Hero(hero_name)
print""
theHero.cheerHero()

gameOn = True
while(theHero.isAlive() and gameOn == True):
    # There are many, many monsters.
    # get random Monster
    fightCount = 0
    if (fightCount < 5):
        randMonster = randint(1,3)
        if randMonster == 1:
            monster = Goblin()
        if randMonster == 2:
            monster = Wolf()
        else:
            monster = Vampire()
    else:
        monster = Centaur()
    print ""
    print "You have encounterd the terrifying %s" % monster.name
    print""
    while(theHero.isAlive() and monster.isAlive()):

        print """
        You have %d health and %d strength.
        The %s has %d health and %d strength.
        You have %d power ups left.

        What do you want to do?
        1. Fight %s
        2. Twerk Off
        3. Flee
        4. Power Up
        """ % (theHero.health,theHero.strength, monster.name, monster.health, monster.strength, theHero.powerUp, monster.name)
        # Get the user's choice
        userInput = raw_input("> ")

        if userInput == "1":
            # The hero has decided to attack!
            # subtract monsters health by hero strength
            monster.takeDamage(theHero.strength)
            print "You have done %d damage to the %s!" % (theHero.strength, monster.name)
        
        elif userInput == "2":
            randomDance = randint(0,1)
            if (randomDance == 0):
                theHero.takeDamage(5)
                if(theHero.isDead()):
                    print "SMH... %s, you are pathetic." % theHero.name
                    break
                else:
                    print "You got served! Health reduces to %d." % theHero.health

            else:
                monster.takeDamage(5)
                if (monster.isAlive()):
                    print "The %s got served. Its health reduces to %d." % (monster.name, monster.health)
                    
                else:
                    print "The %s has no moves. He humbly admits defeat." % monster.name
                    break
                    


        elif userInput == "3":
            if theHero.speed > monster.speed:
                theHero.runAway()
                break

            elif theHero.speed == monster.speed:
                coinFlip = randint(0,1)
                if coinFlip == 0:
                    theHero.runAway()
                    break
                else:
                    theHero.takeDamage(monster.strength)
                    print """Thou arst slow and cowardly. 
                    The %s blocks you and inflicts %d damage.
                    """ % (monster.name, monster.strength)
            
            else:
                theHero.takeDamage(monster.strength)
                print """Thou arst slow and cowardly. 
                The %s blocks you and inflicts %d damage.
                """ % (monster.name, monster.strength)

        elif userInput == "4":
            if theHero.powerUp > 0:
                theHero.health += 10
                theHero.powerUp -= 1
                print """Your health increases to %d.
                You have %d power ups left.""" % (theHero.health, theHero.powerUp)    
            else:
                print """Thou arst out of power ups.
                Forfeit turn."""           
        
        else:
            # user entered something that we didnt offer
            thehero.takeDamage(1)
            print """Thou need learneth to count. 
            Your health reduces to %d because of your stupidity.""" % theHero.health

# ====================THE MONSTER'S TURN==============================

        if monster.isAlive():
            theHero.takeDamage(monster.strength)
            print "The monster hits you for %d damage" % monster.strength
            if theHero.isAlive() == False:
                print "Thou arst dead."
                os.system("say Thou arst dead.")
        else:
            os.system("say Hooray. Thou hast killed the monster!")
            print "Thou hast killed the monster!"
            theHero.levelup(monster.health, monster.strength)
            fightCount +=1
       
        raw_input("Hit enter to continue")
        os.system("clear")
    
    
    if (fightCount == 3):
        print "You slayedeth the Centaur. You are the king of the world."
        gameOn = False
    else:
        if theHero.isAlive():
            fightAgain = raw_input("Fight another fiend? Y or N? ") 
            if fightAgain == "Y" or "y":
                continue
            else: 
                gameOn = False
                break
        else:
            gameOn = False    
            
            
  
    
