ip = '10.1.1.1'
ip.split('.')
print (ip)

result = []

for octet in ip.split('.'):
    result.append(int(octet))

print (result)

result = [int (octet) for octet in ip.split('.')]

print (result)

vlan = ['vlan {}'.format(num) for num in [1,5,2,6]]
print (vlan)

numbers = []
items = [ 10, 2, 'a' , 'b' ,3]

for num in items:
    if type (num) == int:
        numbers.append(num)
print (numbers)

numbers2 = [num for num in items 
if type(num) == int]
print (numbers2)