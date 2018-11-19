# This is a procedural approach to a text based rpg game
# The hero is fighting a goblin
# The hero has the option to:
# 1. Fight
# 2. Dance
# 3. Flee

# Get the hero name from the player
hero_name= raw_input("What is your name brave adventurer? ")
print "Welcome, %s! Thou art brave!" % hero_name

def fight():
    #declare some variables
    # These variables are within the function scope...meaning only assesible inside the fight function
    hero_health = 10
    hero_power = 5
    goblin_health= 6
    goblin_power = 2

    #run the game as long as both characters have health > 0

    while (hero_health > 0 and goblin_health > 0):
        print""
        print """You have %d health and %d power. 
The goblin has %d health and %d power. 
What do you want to do?
1. fight goblin
2. dance
3. flee
> """ % (hero_health, hero_power, goblin_health, goblin_power)

        userInput = raw_input()

        if (userInput == "1"):
            # The hero has decided to attack
            # subtract goblins health by hero power
            goblin_health -= hero_power
            print""
            print "You have done %d damage to the goblin." % hero_power 
        elif (userInput == "2"):
            hero_health += 10
            print""
            print """The goblin stares at you in disbelief of your stupidity.
Little does he know you just gained 10 health. His jaw drops as your wounds heal."""
            print "Your health is now %d." % hero_health
        elif (userInput == "3"):
            print ""
            print "Goodbye cowardly, %s." % hero_name
            # break statement will end the loop immediately
            break
        else: 
            # User entered something we didn't offer
            print "Thou fool. Thou has stubmledith (invalid input)."

fight()