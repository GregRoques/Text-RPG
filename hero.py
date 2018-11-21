
class Hero(object):
    def __init__(self, name):
        self.name = name
        self.health = 25
        self.strength = 5
        self.speed = 5
        self.powerUp = 3
        
    def cheerHero(self):
        print "Welcome, brave %s" % self.name    

    def takeDamage(self, ammountOfDamage):
        self.health -= ammountOfDamage

    def isAlive(self):
        return self.health > 0

    def isDead(self):
        return self.health < 1

    def runAway(self):
        print "%s runnith away in fear. Thou arst a coward." % self.name

    def levelup(self,monsterHealth,monsterStrength):
        self.health += monsterHealth/2
        self.strength += monsterStrength/2

        
