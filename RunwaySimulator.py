#This will contain the logic for the runway simulation


def runway(submissionList):
    currentQueue = []
    finishedList = []
    currentTime = 0
    while isFinished(submissionList, currentQueue):
        addNextPlane(submissionList, CurrentQueue, currentTime)
    return finishedList

def isFinished (submissionList, CurrentQueue):
    if not submissionList and not CurrentQueue:
        return True
    else:
        return False

def addNextPlane(submissionList, CurrentQueue, currentTime):
    while submissionList[0].submissionTime == currentTime:
        CurrentQueue.insert(1, submissionList[0])
        sortPlanes(CurrentQueue)

def sortPlanes(CurrentQueue):
    for i in range( 2, len(CurrentQueue+1)):
        if CurrentQueue[i].submissionTime < CurrentQueue[i-1].submissionTime:
            CurrentQueue[i], CurrentQueue[i-1] = CurrentQueue[i-1] < CurrentQueue[i]
