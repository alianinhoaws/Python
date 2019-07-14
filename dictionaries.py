enemy ={
    'loc_x':16,
    'loc_y':30,
    'color': 'green',
    'health': 100,
    'name':'enemy',
}
print (enemy)
print ("location_X = " + str(enemy['loc_x']))
print ("location_Y = "+ str(enemy['loc_y']))
print ("His name =" + str(enemy['name']))
enemy['rank'] = 'Superman'
print (enemy)
enemy['loc_x'] = enemy ['loc_x'] + 40
enemy ['health'] = enemy ['health'] - 30
if enemy ['health'] < 80:
    enemy ['color'] = 'yellow'
print (enemy)
print (enemy.keys())
print (enemy.values())

all_enemies = []
for x in range (0,10):
    all_enemies.append(enemy.copy())

all_enemies[5]['health'] = 30
all_enemies[2]['name'] = "Vasya"


for ene in all_enemies:
    print (ene)
