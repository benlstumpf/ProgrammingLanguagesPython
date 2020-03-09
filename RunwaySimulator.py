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
    takenOffTime = currentQueue[0].submissionTime + currentQueue[0].requestedDuration
    if takenOffTime >= time:
        finishedList.append(currentQueue[0])
        currentQueue.pop(0)
"""
docstring stub
"""
def isNotFinished (submissionList, CurrentQueue):
    if len(submissionList) == 0 and len(CurrentQueue) == 0:
        return False
    else:
        return True
"""
docstring stub
"""
def addNextPlane(submissionList, CurrentQueue, currentTime):
    while submissionList[0].getsubmissionTime() == currentTime:
        CurrentQueue.insert(1, submissionList[0])
        sortPlanes(CurrentQueue)
"""
docstring stub
"""
def sortPlanes(CurrentQueue):
    for i in range( 2, len(CurrentQueue+1)):
        if CurrentQueue[i].submissionTime < CurrentQueue[i-1].submissionTime:
            CurrentQueue[i], CurrentQueue[i-1] = CurrentQueue[i-1] < CurrentQueue[i]
