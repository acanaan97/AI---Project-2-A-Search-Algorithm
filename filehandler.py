# Create our empty dictionaries
Locations = {}
Connections = {}

def init():
    #Open and parse the location/connection files
    file = open("locations.txt").read().split("\n")
    for x in file:
        temp1 = x.split(" ")
        if temp1[0] == "END":
             break # If at the last line in the file
        Locations[temp1[0]] = (temp1[1], temp1[2]) # add to dictionary for location by key-val pair. Key is location, and value is coordinate pair

    file = open("connections.txt").read().split("\n")
    for y in file:
        temp2 = y.split(" ")
        if temp2[0] == "END":
             break # If at the last line in the file
        connects = temp2[2:] # Store each entry from index 2 onward (but not including index 1, which is the number of connections per node)
        Connections[temp2[0]] = connects # Store the connections to the associated node dictionary