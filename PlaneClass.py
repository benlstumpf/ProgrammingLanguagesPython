#class for planes
#held data will be ID, Submission Time, Requested Start, Requested Duration

#given airlines at

# Frontier Airlines 323, 5, 9, 2

class Plane:
    """
    docstring for Plane.
    """
    id = ""
    submissionTime = 0
    requestedStart = 0
    requestedDuration = 0
    realTimeStart = -1

    """
    docstring stub
    """
    def __init__(self, id, submissionTime, requestedStart, requestedDuration):
        super(Plane, self).__init__()
        self.id = id
        self.submissionTime = submissionTime
        self.requestedStart = requestedStart
        self.requestedDuration = requestedDuration


    """
    docstring stub
    """
    def __init__(self, array):
        super(Plane, self).__init__()
        self.id = array[0]
        self.submissionTime = array[1]
        self.requestedStart = array[2]
        self.requestedDuration = array[3]


    """
    docstring stub
    """
    def setRealTimeStart(self, time):
        self.realTimeStart = time


    """
    docstring stub
    """
    def setScheduledTime(self, time):
        self.scheduledTime = time
