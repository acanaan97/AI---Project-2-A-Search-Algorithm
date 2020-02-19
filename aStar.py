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

#checks to see if there is no connections to a city
for i in filehandler.Connections:
      if(filehandler.Connections[i]):   
            continue
      else:
            print("Can't connect to that a city")
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
            #Calculate the straight line distance of each node from the ending node
            startingX = int(filehandler.Locations[end][0])
            startingY = int(filehandler.Locations[end][1])
            #Calculate for all of the nodes except 'END'
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
      
      #Same as above without steps^
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
            path = [start]
            visited = [start]
            heuristic[end] = 0
            starting = end
            visitedDict = {}
            
            #set all distances to infinity essentially
            for x in filehandler.Locations:
                  visitedDict[x] = 999999

            #Calculate how far away each node is away from the end node in order to find how far away it is
            while (visitedDict): # While not empty
                  visitedDict.pop(starting)
                  #calculate how far away each node is from the ending node 
                  for z in filehandler.Connections[starting]:
                        currDist = heuristic[starting] + 1
                        if z not in heuristic or currDist < heuristic[z]:
                              heuristic[z] = currDist
                              visitedDict[z] = currDist
                              
                  #Traverses the graph by going to the city with the smallest distance (BFS search)
                  minCity = ""
                  minDist = 999999
                  for x in visitedDict:
                        if visitedDict[x] < minDist:
                              minDist = visitedDict[x]
                              minCity = x
                  starting = minCity
            
            #Traverse the map
            while(path[-1] != end):
                  change = 0
                  temp = filehandler.Connections[path[-1]] #get all the connections
                  small = 9999
                  tempSmallCity = ""
                  print("Current City: ", path[-1])
                  for i in temp:
                        #if the city connects to a destination, stop
                        if (i == end):
                              tempSmallCity = i
                              print(tempSmallCity, " is this the destination!")
                              visited.append(i)
                              path.append(i)
                              change =1
                              break
                        #compare the distance
                        tempValue = heuristic[i]
                        print(i, " is ", tempValue," steps from the end")
                        
                        #if there is a smaller distance, replace the variable with the smaller one
                        if(tempValue< small):
                              small = tempValue
                              tempSmallCity = i
                  print("City selected: ", tempSmallCity)
                  
                  #if it is not visited, add it in
                  if(tempSmallCity not in visited):
                        path.append(tempSmallCity)
                        visited.append(tempSmallCity)
                        change = 1
                        
                  #if you reach a deadend, pop off the path
                  if(change == 0):
                        path.pop()
            print("VISITED: ", visited)
            print("PATH: ", path)
      
      #Same as above^ but without the print statements
      else:
            path = [start]
            visited = [start]
            heuristic[end] = 0
            starting = end
            visitedDict = {}
            for x in filehandler.Locations:
                  visitedDict[x] = 999999

            while (visitedDict): # While not empty
                  visitedDict.pop(starting)
                  #calculate how far away each node is from the ending node 
                  for z in filehandler.Connections[starting]:
                        currDist = heuristic[starting] + 1
                        if z not in heuristic or currDist < heuristic[z]:
                              heuristic[z] = currDist
                              visitedDict[z] = currDist
                              
                  #Traverses the graph by going to the city with the smallest distance (BFS search)
                  minCity = ""
                  minDist = 999999
                  for x in visitedDict:
                        if visitedDict[x] < minDist:
                              minDist = visitedDict[x]
                              minCity = x
                  starting = minCity
            # while (visitedDict): # While not empty
            #       visitedDict.pop(curr)
            #       for z in filehandler.Connections[curr]:
            #             currDist = heuristic[curr] + 1
            #             if z not in heuristic or currDist < heuristic[z]:
            #                   heuristic[z] = currDist
            #                   visitedDict[z] = currDist
            #       curr = helpers.getNext(visitedDict)
            
            while(path[-1] != end):
                  change = 0
                  temp = filehandler.Connections[path[-1]]
                  small = 9999
                  tempSmallCity = ""
                  for i in temp:
                        if (i == end):
                              tempSmallCity = i
                              visited.append(i)
                              path.append(i)
                              change =1
                              break
                        tempValue = heuristic[i]
                        if(tempValue< small):
                              small = tempValue
                              tempSmallCity = i
                  if(tempSmallCity not in visited):
                        path.append(tempSmallCity)
                        visited.append(tempSmallCity)
                        change = 1
                  if(change == 0):
                        path.pop()
            print("VISITED: ", visited)
            print("PATH: ", path)
            # don't output step by step, only final path and distance