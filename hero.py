
class Hero(object):
    def __init__(self, name, power = 5):
        self.name = name
        self.health = 10 
        self.power = power
        
    def cheerHero(self):
        print "Welcome, brave %s" % (self.name)    

    def takeDamage(self, ammountOfDamage):
        self.health -= ammountOfDamage