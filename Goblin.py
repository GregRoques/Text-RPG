from random import randint #if the only function in random you want to use is RANDINT

class Goblin(object):
    def __init__(self):
        randomStrength = randint(4,6)
        randomSpeed = randint(3,5)
        self.name = "Goblin"
        self.health = 6
        self.strength = randomStrength
        self.speed = randomSpeed

    def takeDamage(self,ammountOfDamage):
        self.health -= ammountOfDamage

    def isAlive(self):
        return self.health > 0

