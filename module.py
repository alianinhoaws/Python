
def give_award (medal, *persons):
    """give medals for undefined persons"""
    for person in persons:
        print ("Friend " + person.title() + " awarded " + medal)

def create_record (name, telephone, address):
    """craeate record"""
    record = {
        'name': name,
        'phone': telephone,
        'address': address
    }
    return record

def factorial (x):
    "Calculate factorial of nubmer X"
    otvet = 1
    for i in range (1, x+1):
        otvet = otvet * i
    return otvet

def cities (x,y):
    city = ("City " + str (x) + " Country " + str (y))
    return city

def dicrionary (first_name, last_name):
    name = {'First': first_name, 'Last': last_name}
    return name