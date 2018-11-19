# class Hero():
#     def __init__(self, name):
#         self.name = name
#         self.health - 10
#         self.power = 5

# theHero = Hero("Link")
# print theHero.power

# ______PROVIDING A VARIABLE IF IT IS NOT PROVIDED BY USER____________

class Hero():
    def __init__(self, name, power = 5):
        self.name = name
        self.health = 10
        self.power = power

theHero = Hero("Link") ### You can set power here, but if you don't it will default to 5
theHero.health = 15
print theHero.power
print theHero.health
# ________________________________________________________________________

