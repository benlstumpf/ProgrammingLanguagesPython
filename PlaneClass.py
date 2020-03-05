#class for planes
#held data will be ID, Submission Time, Requested Start, Requested Duration

#given airlines at


class Plane(object):
    """docstring for Plane."""
    id = ""
    submissionTime = 0
    requestedStart = 0
    requestedDuration = 0

    def __init__(self, id, submissionTime, requestedStart, requestedDuration):
        super(Plane, self).__init__()
        self.id = id
        self.submissionTime = submissionTime
        self.requestedStart = requestedStart
        self.requestedDuration = requestedDuration

    def setRealTimeStart(self, time)
        self.realTimeStart = time

    def setScheduledTime(self, time)
        self.scheduledTime = time
