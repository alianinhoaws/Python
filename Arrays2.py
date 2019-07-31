
cars = ['Bwm','WV', 'Volvo', 'Fiat','Mercedes']
for x in cars:
    print (x.lower())

for x in range (1,6):
    print(x)
    if x==2:
        break

newArray=list(range (0,10)) #create array from range values
print (newArray)

for x in newArray:
    x=x*2
    print (x)

newArray.sort(reverse=True) 
print (newArray)

print ("MaxNuberofList " + str(max(newArray))) #max
print ("MinNumberofList "+ str(min(newArray))) #min
print ("SumOfList "+ str(sum(newArray))) #sum

mycars=cars[1:3] #cut elements 
print(mycars)
mycars=cars[:4]
print(mycars)
mycars=cars[:-2]
print(mycars)

mycars=cars [:] #copy array
print(mycars)

#tuple
dimension = (200,50)
for dimension in dimension:
    print (dimension)
dimension = (400,50)
for dimension in dimension:
    print (dimension)

