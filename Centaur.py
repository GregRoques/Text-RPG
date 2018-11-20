from random import randint

class Centaur(object):
    def __init__(self):
        randomStrength = randint(8,12)
        self.name = "Centaur"
        self.health = 30
        self.strength = randomStrength
        self.speed = 100

    def takeDamage(self,ammountOfDamage):
        self.health -= ammountOfDamage

    def isAlive(self):
        return self.health > 0