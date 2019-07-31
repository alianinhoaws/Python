#if else 

print ("age")
age=12

if (age <=4):
    print ("You are ready")
elif (age > 4) and (age < 12):
    print ("You are kid")
elif (age >= 12) and (age < 35):
    print ("You are teen")
else:
    print ("You are old")

cars = ['Bmw','WV', 'Volvo', 'Fiat','Mercedes']
cars2 = ['Lada', 'WV', 'Skoda', 'Fiat']

if "Bmw" in cars:
  print ("BMW exist")
else:
    print ("Bmw does not exist")

for x in cars:
    if x in cars2:  
        print (x + " exist in array2")
    else:
        print (x + " dosent in array2")


if  "Bmw" not in cars2:
    print ("BMW")




