# This is a procedural approach to a text based rpg game
# The hero is fighting a goblin
# The hero has the option to:
# 1. Fight
# 2. Dance
# 3. Flee

# Go get the os module from python
import os
import random
# os.system() will take any Linux command and if python can run it, it will

# Get the hero name from the player
print """ 
                   (    )
                  ((((()))
                  |o\ /o)|
                  ( (  _')
                   (._.  /\__
                  ,\___,/ '  ')
    '.,_,,       (  .- .   .    )
     \   \\     ( '        )(    )
      \   \\    \.  _.__ ____( .  |
       \  /\\   .(   .'  /\  '.  )
        \(  \\.-' ( /    \/    \)
         '  ()) _'.-|/\/\/\/\/\|
             '\\ .( |\/\/\/\/\/|
               '((  \    /\    /
               ((((  '.__\/__.')
                ((,) /   ((()   )
                 "..-,  (()("   /
            pils  _//.   ((() ."
          _____ //,/" ___ ((( ', ___
                           ((  )
                            / /
                          _/,/'
                        /,/,"

------------------------------------------------
==================Goblin Game=================== """
print ""
hero_name= raw_input("What is your name brave adventurer? ")
print ""
print "Welcome, %s! Thou art brave!" % hero_name

def fight():
    #declare some variables
    # These variables are within the function scope...meaning only assesible inside the fight function
    hero_health = 10
    hero_power = 5
    power_up = 2

    enemyName1 = "Goblin"
    goblin_health= 6
    goblin_power = 2

    enemyName2 = "Dragon"
    dragon_health = 20
    dragon_power = 5

    #Select an Enemy at Random
    randomDance = random.randint(0,1)
            if (randomDance == 0):
                enemy = enemyName1
            else:
                enemy = enemyName2    

    #run the game as long as both characters have health > 0
    while (hero_health > 0 and goblin_health > 0):
        print""
        print """
                        _______
            ..-'`       ````---.
        .'          ___ .'````.'SS'.
        /        ..-SS####'.  /SSHH##'.
        |       .'SSSHHHH##|/#/#HH#H####'.
        /      .'SSHHHHH####/||#/: \SHH#####\
    /      /SSHHHHH#####/!||;`___|SSHH###\
    -..__    /SSSHHH######.         \SSSHH###\
    `.'-.''--._SHHH#####.'           '.SH####/
    '. ``'-  '/SH####`/_             `|H##/
    | '.     /SSHH###|`'==.       .=='/\H|
    |   `'-.|SHHHH##/\__\/        /\//|~|/
    |    |S#|/HHH##/             |``  |
    |    \H' |H#.'`              \    |
    |        ''`|               -     /
    |          /H\          .----    /
    |         |H#/'.           `    /
    |          \| | '..            /
    |    ^~DLF   /|    ''..______.'
    \          //\__    _..-. | 
        \         ||   ````     \ |_
        \    _.-|               \| |_
        _\_.-'   `'''''-.        |   `--.
    ''``    \            `''-;    \ /
            \      .-'|     ````.' -
            |    .'  `--'''''-.. |/
            |  .'               \|
            |.'"""
        print""
        print """
    You have %d health and %d power. 
    The goblin has %d health and %d power. 
    What do you want to do?
    1. fight goblin
    2. dance
    3. flee
    4. power up
    > """ % (hero_health, hero_power, goblin_health, goblin_power)

        userInput = raw_input()

        if (userInput == "1"):
            # The hero has decided to attack
            # subtract goblins health by hero power
            goblin_health -= hero_power
            print""
            print """
        ==
        ||_________________________
    OOOOO||_________________________>
        ||
        == """
            if (goblin_health < 1):
                print "Thou hath killithed the goblin."
                break

            else:
                    print "You have done %d damage to the goblin." % hero_power 

        elif (userInput == "2"):
            randomDance = random.randint(0,1)
            if (randomDance == 0):
                hero_health -=5

                if(hero_health < 1):
                    print "SMH... %s, you are pathetic!!!" % hero_name
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
            print "Goodbye cowardly, %s." % hero_name
            # break statement will end the loop immediately
            break

        elif (userInput == "4"):
            if (power_up > 0):
                power_up -= 1
                hero_health +=4
                print ""
                print "Your health increases to %d" %hero_health
            else:
                print "You have no power ups left."


        else: 
            # User entered something we didn't offer
            hero_health -=1
            print "Thou fool. Your health goes down %d for your stupidity. (invalid input)." % hero_health
            
        # Now it's the goblin's turn (as long as he is alive.)
        if (goblin_health > 0):
            hero_health -= goblin_power
            print """
                    ____  
                `/(#)#(#) `-
            `     (#)#(#)  \ ___
        __(     \ ,,,/    `.  ``.
        /   \     \,-/      |     \
        |     `--   ( (      /__   (
        `   (   `---\ `---._` (    }
        |   |    \   `----._`.`.  .'
        .  ( `-)  \     `.  )) )  |
        /    \ /   /       )    / {
        /      \   /       (    |  (
    /    ,\ /\\\        (    |_  \
    /  /\(  )            /     .`\\\
    \\/  \             .-' | |  -_
            \           .'___( )  \ `-.
                        -'   \/\___\\__\  """

            print""
            print "The goblin hits you for %d damage." % goblin_power
            if (hero_health == 0):
                print "Thou hast been vanquished. Thou suckith."
                os.system("say Thou hast been vanquished. Thou suckith.")
                break
        raw_input("Hit enter to continue.")
        os.system("clear")

fight()