# This is a procedural approach to a text based rpg game
# The hero is fighting a goblin
# The hero has the option to:
# 1. Fight
# 2. Dance
# 3. Flee

# Get the hero name from the player
hero_name= raw_input("What is your name brave adventurer? ")

def fight():
    #declare some variables
    # These variables are within the function scope...meaning only assesible inside the fight function
    hero_health = 10
    hero_power = 5
    goblin_health= 6
    goblin_power = 2

    #run the game as long as both characters have health > 0

    while (hero_health > 0 and goblin_health > 0):
        



    print "Fight the goblin"