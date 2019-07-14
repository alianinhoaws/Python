
#password autentification while insert "secret" 
massage = ""
while True:
    massage=input("enter a pass ")
    if massage == 'secret':
        break
    print (massage + "Password is incorrect")
print ("pass success")

#append to list/array by insert before 'STOP' + msg STOP deleted

array=[]
msg=""
while msg !='stop'.upper():
    msg = input ("Enter new item, and STOP if finished ")
    array.append(msg)
array.remove("STOP")
print (array)
