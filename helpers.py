import math
import filehandler as filehandler

def Square(x1, x2, y1, y2):
    res = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return res

def getNext(locations):
    minCity = ""
    minDist = 999999
    for z in locations:
        if locations[z] < minDist:
            minDist = locations[z]
            minCity = z
    return minCity


def getInput():
    blacklist = []
    flag = False
    while(flag == False):
        inputstr = input("Name the starting city: ")
        if inputstr in filehandler.Locations.keys():
            flag = True
        else:
            print("Invalid city. Try again below.")

    start = inputstr

    flag = False
    while(flag == False):
        inputstr = input("Name the ending city: ")
        if inputstr in filehandler.Locations.keys():
            flag = True
        else:
            print("Invalid city. Try again below.")

    end = inputstr

    flag = False
    while(flag == False):
        exclusion = input("Name cities to exclude in a comma-separated list (no spaces): ")
        if(exclusion != ""):
            exclusions = exclusion.split(",")
            for x in exclusions:
                if x in filehandler.Locations.keys():
                    blacklist.append(x)
                    flag = True
                else:
                    print("Invalid city: " + x + ". Try again below. If there are no cities, leave blank.")
                    flag = False
                    break
        else:
            flag = True

    return start,end, blacklist

