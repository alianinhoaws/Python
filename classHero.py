class Hero ():
    """Class to create hero for our game"""
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero (self):
        description = ("Name " + self.name + "Level " + str(self.level) + "Race " + self.race + "Health " + str(self.health)).title()
        print(description)

    def level_up (self):
        self.level += 1

    def move (self):
        print ("Hero" + self.name + "Are moving")

    def set_health (self, new_health):
        self.health = new_health