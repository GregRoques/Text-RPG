# class Hero():
#     def __init__(self, name):
#         self.name = name
#         self.health - 10
#         self.power = 5

# theHero = Hero("Link")
# print theHero.power

# ______PROVIDING A VARIABLE IF IT IS NOT PROVIDED BY USER____________

# class Hero():
#     def __init__(self, name, power = 5):
#         self.name = name
#         self.health = 10 # this an still be changed too. See below vv
#         self.power = power

# theHero = Hero("Link") ### You can set power here, but if you don't it will default to 5
# theHero.health = 15
# print theHero.name
# print theHero.power
# print theHero.health
# ________________________________________________________________________

class Monster():
    def __init__ (self, name, health, power):
        self.name = name
        self.health = health
        self.power = power

goblin = Monster("goblin", 10, 3)
dragon = Monster("dragon", 20, 5)


class Hero():
    def __init__(self, name):
        self.name = name
        self.health = 10 
        self.power = 5
        self.power_up = 2