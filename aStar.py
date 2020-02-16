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
curr = start

heuristic = {}
path = []
visited = []

for x in temp[2]:
    del filehandler.Locations[x] # remove that city from Locations dict
    del filehandler.Connections[x] # remove that city from Connections dict

for y in filehandler.Connections: # to remove any connections in other keys
    for z in filehandler.Connections[y]:
        if z in temp[2]:
            filehandler.Connections[y].remove(z)

if end not in filehandler.Locations:
      print("Destination does not exist in possible locations, you may have removed the destination from search list (intentionally, no doubt).")
      exit(0)

stepByStep = False
strinput = input("Would you like to search Step-by-Step? Y/N\n") 
if (strinput == 'Y' or strinput == 'y'):
    stepByStep = True


straightLine = False
temp = input("Do you want to travel by straight line distance? Default is by fewest cities (y/n)\n")
if(temp == "Y" or temp == "y"):
      straightLine = True
      
if(straightLine == True):
      if(stepByStep == True):
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

            print("Total Distance Travelled: ", totalDistance) 
            print("Visited Path: ", visited)
            print("Total Path: ",path)

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

else: # Default is fewest cities, to find path with fewest cities a dictionary based implementation of a shortest path algorithm
      if stepByStep == True:
            heuristic[end] = 0
            curr = end
            visitedDict = {}
            for x in filehandler.Locations:
                  visitedDict[x] = 999999

            while (visitedDict): # While not empty
                  visitedDict.pop(curr)
                  for z in filehandler.Connections[curr]:
                        currDist = heuristic[curr] + 1
                        if z not in heuristic or currDist < heuristic[z]:
                              heuristic[z] = currDist
                              visitedDict[z] = currDist
                  curr = helpers.getNext(visitedDict)
            
      

                                  
      else:
            print("at non step-bystep")
            # don't output step by step, only final path and distance