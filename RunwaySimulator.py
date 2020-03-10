#This will contain the logic for the runway simulation

import PlaneClass
import ReportingFunctions

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
def takingOff(currentQueue, finishedList, time):
    #if there is a plane in the queue
    if len(currentQueue) > 0:
        takenOffTime = currentQueue[0].getsubmissionTime() + currentQueue[0].getDuration()
        if takenOffTime <= time:
            finishedList.append(currentQueue[0])
            currentQueue.pop(0)
"""
docstring stub
"""
def isNotFinished (submissionList, CurrentQueue):
    if len(submissionList) == 0:
        print("CurrentQueue", len(CurrentQueue))
        if len(CurrentQueue) == 0:
            return False
    return True
"""
docstring stub
"""
def addNextPlane(submissionList, CurrentQueue, currentTime):
    if len(submissionList) > 0:
        if submissionList[0].getsubmissionTime() == currentTime:
            #if the CurrentQueue is not empty
            if len(CurrentQueue) > 0:
                CurrentQueue.insert(1, submissionList[0])
                submissionList.pop(0)
                schedulePlane(CurrentQueue[1], CurrentQueue[0])
                #if the queue has more than 2 elements
                if len(CurrentQueue) > 2:
                    sortPlanes(CurrentQueue)
                    scheduleQueue(CurrentQueue)
                    #if the queue is empty
                else:
                    CurrentQueue.insert(0, submissionList[0])
                    submissionList.pop(0)
                    CurrentQueue[0].setRealTimeStart(currentTime)
                    addNextPlane(submissionList, CurrentQueue, currentTime)
"""
docstring stub
"""
def sortPlanes(CurrentQueue):
    for i in range( 2, len(CurrentQueue)):
        if CurrentQueue[i].getsubmissionTime() < CurrentQueue[i-1].getsubmissionTime():
            CurrentQueue[i], CurrentQueue[i-1] = CurrentQueue[i-1], CurrentQueue[i]

def schedulePlane(plane, previousPlane):
    plane.setRealTimeStart(previousPlane.getDuration() + previousPlane.getRealTimeStart())

def scheduleQueue(CurrentQueue):
    for i in range( 2, len(CurrentQueue)):
        previousScheduleTime = CurrentQueue[i-1].getRealTimeStart()
        previousDuration = CurrentQueue[i-1].getDuration()
