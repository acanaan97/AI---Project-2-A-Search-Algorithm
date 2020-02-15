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

stepByStep = False
strinput = input("Would you like to search Step-by-Step? Y/N\n") 
if (strinput == 'Y' or strinput == 'y'):
    stepByStep = True

heuristic = {}
path = []
visited = []

straightLine = False
temp = input("Do you want to travel by straight line distance? Default is by fewest cities (y/n)\n")
if(temp == "Y" or temp == "y"):
      straightLine = True
      
if(straightLine == True):
      if(stepByStep == True):
            totalDistance = 0;
            startingX = int(filehandler.Locations[end][0])
            startingY = int(filehandler.Locations[end][1])
            for i in filehandler.Locations:
                  if(i != "END"):
                        endingX = int(filehandler.Locations[i][0])
                        endingY = int(filehandler.Locations[i][1])
                        distance = math.sqrt((startingX-endingX)**2+(startingY-endingY)**2)
                        heuristic[i] = distance
            path = [start]
            visited = [start]

            while(path[-1] != end): #While the last varaible in the path structure is not the ending city
                  change = 0
                  print("City selected: ", path[-1])
                  temp = filehandler.Connections[path[-1]] #a temp structure that has all the connections of the current city
                  print("Possible cities to where to travel: ", temp)
                  minCity = path[-1]
                  minDistance = 999999 #filler big number
                  #Get the X and Y of the current city
                  startingX = int(filehandler.Locations[path[-1]][0]) 
                  startingY = int(filehandler.Locations[path[-1]][1])
                  #repeat for every connecting city
                  for i in temp:
                        if (i == end):
                              endingX = int(filehandler.Locations[i][0])
                              endingY = int(filehandler.Locations[i][1])
                              distance = math.sqrt((startingX-endingX)**2+(startingY-endingY)**2)
                              distance = distance + heuristic[path[-1]] #add the distance to the city with the straight line distance calculated before
                              print(i, "is this far away: ", distance)
                              minCity = i
                              visited.append(i)
                              path.append(i)
                              change =1
                              break
                        #if you already went to the city, continue with the next city
                        if(i not in visited):
                              #X and Y of the next connecting city
                              endingX = int(filehandler.Locations[i][0])
                              endingY = int(filehandler.Locations[i][1])
                              distance = math.sqrt((startingX-endingX)**2+(startingY-endingY)**2)
                              distance = distance + heuristic[path[-1]] #add the distance to the city with the straight line distance calculated before
                              print(i, "is this far away: ", distance)
                              #compare the distance calculated with the current smallest distance
                              if(distance < minDistance):
                                    minDistance = distance
                                    minCity = i
                  print("Selecting: ", minCity)
                  totalDistance = totalDistance + minDistance
                  if(minCity not in visited):
                        visited.append(minCity)
                        path.append(minCity)
                        change =1
                              #If dead end, pop and renavigate
                  if(change ==0):
                        path.pop()

      else:
            totalDistance = 0
            startingX = int(filehandler.Locations[end][0])
            startingY = int(filehandler.Locations[end][1])
            for i in filehandler.Locations:
                  if(i != "END"):
                        endingX = int(filehandler.Locations[i][0])
                        endingY = int(filehandler.Locations[i][1])
                        distance = math.sqrt((startingX-endingX)**2+(startingY-endingY)**2)
                        heuristic[i] = distance
            path = [start]
            visited = [start]

            while(path[-1] != end): #While the last varaible in the path structure is not the ending city
                  change = 0
                  temp = filehandler.Connections[path[-1]] #a temp structure that has all the connections of the current city
                  minCity = path[-1]
                  minDistance = 999999 #filler big number
                  #Get the X and Y of the current city
                  startingX = int(filehandler.Locations[path[-1]][0]) 
                  startingY = int(filehandler.Locations[path[-1]][1])
                  #repeat for every connecting city
                  for i in temp:
                        if (i == end):
                              minCity = i
                              visited.append(i)
                              path.append(i)
                              change =1
                              break
                        #if you already went to the city, continue with the next city
                        if(i not in visited):
                              #X and Y of the next connecting city
                              endingX = int(filehandler.Locations[i][0])
                              endingY = int(filehandler.Locations[i][1])
                              distance = math.sqrt((startingX-endingX)**2+(startingY-endingY)**2)
                              distance = distance + heuristic[path[-1]] #add the distance to the city with the straight line distance calculated before
                              #compare the distance calculated with the current smallest distance
                              if(distance < minDistance):
                                    minDistance = distance
                                    minCity = i
                  totalDistance = totalDistance + minDistance
                  if(minCity not in visited):
                        visited.append(minCity)
                        path.append(minCity)
                        change =1
                              #If dead end, pop and renavigate
                  if(change ==0):
                        path.pop()
            
print("Total Distance Travelled: ", totalDistance)
print("Visited Path: ", visited)
print("Total Path: ",path)
#       while(path[-1] != end):
#             change = 0  
#       # flag to indicate whether any unvisited neighbors were found
#       # iterate over neighbors of current node
#             for i in filehandler.Connections[path]
#                   print(i)
# #             for x in filehandler.Connections[path[-1]]:
# #     # if neighbor has not been visited yet, add neighbor to the path
# #                   if x not in visited:
# #                         for y in filehandler.Connections[x][0]:
# #                             print("TESTING: " + x + "\n") 
# #                         print("Restart")    
# #                         curr = x
# #                         visited.append(x)
# #                         path.append(x)
# #                         change = 1
# #                         break 
#   # if no unvisited neighbors were found, pop current node from the stack
#             if change == 0:
#                   path.pop()
                  
                  
#                   for i in range(0, len(path)-1):
#           #reinitializes the array each time it loops.
#       points = []
      
#       #gets the first element in the pair
#       for value in util.locations[path[i]]:
#             points.append(value)
#       #gets the second element in the pair
#       for value in util.locations[path[i+1]]:
#             points.append(value)
      
#       #assigns the corresponding variable
#       x1 = int(points[0])
#       x2 = int(points[2])
#       y1 = int(points[1])
#       y2 = int(points[3])
      
#       #calculates distance
#       distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
#       print(path[i] + " to " + path[i+1] + " length " + "%.2f" %distance)
#       sum = sum + distance

# print("Total path length %.2f"  %sum)