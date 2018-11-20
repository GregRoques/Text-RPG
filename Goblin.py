from random import randint #if the only function in random you want to use is RANDINT

class Goblin(object);
    def __init__(self):
        randomPower = randint(2,5)
        self.name = "Goblin"
        self.health = 6
        self.power = randomPower

    def takeDamage(self,ammountOfDamage):
        self.health -= ammountOfDamage
