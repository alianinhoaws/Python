import json

filename = "user_settingx.txt"
"""open file for write"""
myfile = open (filename, mode='w', encoding = 'Latin_1')
"""put it to *myfile"""

player1 = {
    'playername': "Donald Trump",
    'Score': 300,
    'deserved': ["OR","NY","TX"]
}

player2 = {
    'playername': "Hillary Cl",
    'Score': 286,
    'deserved': ["WT","CA","MI"]
}
"""players to save informations in dictionary"""
myPlayers = []
"""create array of players"""
myPlayers.append(player1)
myPlayers.append(player2)
"""appending players to array"""

json.dump(myPlayers, myfile)
myfile.close()
"""save array to myfile by json"""


myfile=open(filename, mode='r',encoding='Latin_1')
json_data=json.load(myfile)
"""open myfile by json and put it to json_data"""


for user in json_data:
    print ("Player name is: " + str(user['playername']))
    print ("Player score is: " + str(user['Score']))

"""print json data"""
