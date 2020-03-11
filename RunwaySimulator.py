#This will contain the logic for the runway simulation

import PlaneClass
import ReportingFunctions
import time

"""
docstring stub
"""
def runway(submissionList):
    currentQueue = []
    finishedList = []
    currentTime = 0
    while isNotFinished(submissionList, currentQueue):
        addNextPlane(submissionList, currentQueue, currentTime)
        takingOff(currentQueue, finishedList, currentTime)
        ReportingFunctions.printCurrentQueue(currentQueue, currentTime)
        currentTime = currentTime + 1
    return finishedList
"""
docstring stub
"""
def takingOff(currentQueue, finishedList, timeCounter):
    #if there is a plane in the queue
    if len(currentQueue) > 0:
        takenOffTime = currentQueue[0].getsubmissionTime() + currentQueue[0].getDuration()
        if takenOffTime <= timeCounter:
            finishedList.append(currentQueue[0])
            currentQueue.pop(0)
"""
docstring stub
"""
def isNotFinished (submissionList, currentQueue):
    if len(currentQueue) == 0:
        if len(submissionList) == 0:
            return False
    return True
"""
docstring stub
"""
def addNextPlane(submissionList, currentQueue, currentTime):
    if len(submissionList) > 0:
        if submissionList[0].getsubmissionTime() == currentTime:
            #if the currentQueue is not empty
            if len(currentQueue) > 0:
                currentQueue.insert(1, submissionList[0])
                schedulePlane(currentQueue[1], currentQueue[0])
                #if the queue has more than 2 elements
                if len(currentQueue) > 2:
                    sortPlanes(currentQueue)
                    scheduleQueue(currentQueue)
                    #if the queue is empty
            else:
                currentQueue.insert(0, submissionList[0])
                currentQueue[0].setRealTimeStart(currentTime)
            submissionList.pop(0)
            addNextPlane(submissionList, currentQueue, currentTime)

"""
docstring stub
"""
def sortPlanes(currentQueue):
    for i in range( 2, len(currentQueue)):
        if currentQueue[i].getsubmissionTime() < currentQueue[i-1].getsubmissionTime():
            currentQueue[i], currentQueue[i-1] = currentQueue[i-1], currentQueue[i]

def schedulePlane(plane, previousPlane):
    plane.setRealTimeStart(previousPlane.getDuration() + previousPlane.getRealTimeStart())

def scheduleQueue(currentQueue):
    for i in range( 2, len(currentQueue)):
        previousScheduleTime = currentQueue[i-1].getRealTimeStart()
        previousDuration = currentQueue[i-1].getDuration()
