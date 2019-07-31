from classauto import *
from classHero import *
myhero = Hero ("Warlock", 5, "Undead")
myhero.show_hero ()
myhero.level_up()
myhero.move()
myhero.show_hero()
myhero.set_health(60)
myhero.show_hero()

mysuperherro = SuperHerro ("Mage", 5 , "Night elf", 100)
mysuperherro.show_hero ()
mysuperherro.makemagic ()
mysuperherro.show_hero ()

newcar = Car ('A4', 'Audi', 1997)
newcar.describe_name()
newcar.change_odometer(222)
newcar.change_odometer(33)
newcar.read_odometer()
newcar.incremant_odometer (100)
newcar.read_odometer()

newElectroCar = Electrocar ('X', 'Tesla', 2018)
newElectroCar.describe_name()
newElectroCar.describe_battery()