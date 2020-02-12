import filehandler as filehandler
import helpers as helpers
import math

# for each node in locations, add a third element to the pair for estimate score
Open = []
Closed = []


filehandler.init()
temp = helpers.getInput()

start = temp[0]
end = temp[1]

for x in temp[2]:
    del filehandler.Locations[x] # remove that city from Locations dict
    del filehandler.Connections[x] # remove that city from Connections dict

for y in filehandler.Connections: # to remove any connections in other keys
    for z in filehandler.Connections[y]:
        if z in temp[2]:
            filehandler.Connections[y].remove(z)

strinput = input("Would you like to search Step-by-Step? Y/N") 
if strinput == 'Y':
    helpers.step_by_step()







