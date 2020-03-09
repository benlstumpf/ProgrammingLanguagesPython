#functins in this file are to take a file of comma dillimited plane values and biuld a list from that file using each line as a singular plane
#
#

# Frontier Airlines 323, 5, 9, 2

from PlaneClass import Plane
"""
docstring stub
"""
def fileToList (fileName):
    planeList = []
    file = open(fileName, 'r')
    for line in file:
        plane = stringToPlane(line)
        planeList.append(plane)
    return planeList
"""
docstring stub
"""
def stringToPlane(string):
    string = string.rstrip()
    arrayFromString = string.split(", ")
    arrayFromString[1] = int(arrayFromString[1])
    arrayFromString[2] = int(arrayFromString[2])
    arrayFromString[3] = int(arrayFromString[3])
    return Plane(arrayFromString)
