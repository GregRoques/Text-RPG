from random import randint 

class Wolf(object):
    def __init__(self):
        randomStrength = randint(6,8)
        randomSpeed = randint(3,8)
        self.name = "Wolf"
        self.health = 15
        self.strength = randomStrength
        self.speed = randomSpeed

    def takeDamage(self,ammountOfDamage):
        self.health -= ammountOfDamage

    def isAlive(self):
        return self.health > 0

    def giveHeroFleas(self):
        print """The wolf brushes against %s.
        It's nasty fleas migrate to %'s nice fleece sweater
        that his gam-gam bought him on sale at Old Navy.
        """ % (theHero.name, theHero.name)