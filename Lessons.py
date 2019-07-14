
x1 = 15
x2 = 5
print (x1/x2)
print (10*2/5+100)
for x in range (100,5,-2): #cicle could increase or decrease step by 3 elemtnts
    print ("number x = "+str(x)) #contocination str
    if x == 10: #point of end of cicle
        break
print ("------------------")

while True:  #cicle without end
    print (x)
    x=x+1
    if x == 15:
        break

cities=['Tel Aviv', 'Moscow','Tokyo', 'Milan', 'munuch','Astanta', 'Adelaida']   #array
print (cities)
print (len(cities))
print (cities[1])
print (cities[2].title())
print (cities[0].upper())
cities[3]='Kyiv'
print (cities)
cities.append('Rivne')
print (cities)
cities.insert(3,'Kharkiv') #insert
print (cities)
del cities [-2]
print (cities)
del cities [0]
print ("Unsorted")
print (cities)
print ("reverse sort True")
cities.sort(reverse=True) #alphabet reverse
print (cities)
print ("cities sort") #alphabet
cities.sort()
print (cities)
cities.reverse()
print ("cities.reverse()")
print (cities)



