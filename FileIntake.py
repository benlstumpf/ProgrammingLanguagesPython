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
    return Plane(arrayFromString)
