from module import *

x=""
y=""

x  = input ("Enter a city ")
y = input ("Enter a contry ")
    
new_adress = cities(x, y)
print (new_adress)

user1 = create_record ("andrej", "131313131", "Kiev")
print (user1)


give_award(" for education", "vasya", "petya", "andrej")
print (give_award)


for i in range (1,10):
    print (str(i) + "!\t = " + str(factorial(i)))
