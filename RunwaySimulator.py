#This will contain the logic for the runway simulation


def runway(submissionList):
    currentQueue = []
    finishedList = []


def isFinished (submissionList, CurrentQueue):
    if not submissionList && not CurrentQueue:
        return True
    else:
        return False

def addNextPlane(submissionList, CurrentQueue, currentTime):
    while submissionList[0].submissionTime == currentTime:
        CurrentQueue.insert(1, submissionList[0])
        sortPlanes(CurrentQueue)

def sortPlanes(CurrentQueue):
