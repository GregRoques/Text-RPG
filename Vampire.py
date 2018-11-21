from random import randint

class Vampire(object):
    def __init__(self):
        randomStrength = randint(6,8)
        randomSpeed = randint(3,8)
        self.name = "Vampire"
        self.health = 10
        self.strength = randomStrength
        self.speed = randomSpeed

    def takeDamage(self,ammountOfDamage):
        self.health -= ammountOfDamage

    def isAlive(self):
        return self.health > 0

    def makeGirlsSwoon(self):
        print "The skin of the Cullins shines bright like a diamond."