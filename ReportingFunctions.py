#this file will have reporting functions


#At time 2 the queue would look like: Delta 160 (started at 0), Delta 6 (scheduled for 4), UAL 120 (scheduled for 10)

#Delta 160 (0-3), Delta 6 (4-9), UAL 120 (10-13)

import PlaneClass

"""
docstring stub
"""
def printCurrentQueue(planeQueue, time):
    print("At time", time, "the queue would look like:", end=" ")
    for index in planeQueue:
        if index.getRealTimeStart() <= time:
            print(index.id, "(started at", index.realTimeStart, ")", end=" ")
        else:
            print(index.id, "(scheduled for", index.getRealTimeStart(), ")", end=" ")
    print(len(planeQueue))
"""
docstring stub
"""
def printFinalPrint(planeQueue):
    for index in planeQueue:
        print(index.id, "(", index.getRealTimeStart(), "-", index.getRealTimeStart()+index.getDuration()-1, "),", end=" ")
