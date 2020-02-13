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

heuristic = {}
path = []
visited = []

straightLine = False
temp = input("Do you want to travel by straight line distance? Default is by fewest cities (y/n)\n")
if(temp == "Y" or temp == "y"):
      straightLine = True
      
if(straightLine == True):
      startingX = int(filehandler.Locations[start][0])
      startingY = int(filehandler.Locations[start][1])
      for i in filehandler.Locations:
            if(i != "END"):
                  endingX = int(filehandler.Locations[i][0])
                  endingY = int(filehandler.Locations[i][[1])
                  distance = math.sqrt((startingX-endingX)**2+(startingY-endingY)**2)
                  heuristic[i] = distance
      path = [start]
      visited = [start]

      while(path[-1] != end):
            change = 0  # flag to indicate whether any unvisited neighbors were found
      # iterate over neighbors of current node
            for x in filehandler.Connections[path[-1]]:
    # if neighbor has not been visited yet, add neighbor to the path
                  if x not in visited:
                        curr = x
                        visited.append(x)
                        path.append(x)
                        change = 1
                        break 
  # if no unvisited neighbors were found, pop current node from the stack
            if change == 0:
                  path.pop()