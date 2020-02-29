#class for planes
#held data will be ID, Submission Time, Requested Start, Requested Duration

#given airlines at


class Plane(object):
    """docstring for Plane."""
    id = ""
    submissionTime =
    requestedStart =
    requestedDuration =
    timeFinished = requestedStart + requestedDuration

    def __init__(self, id, submissionTime, requestedStart, requestedDuration):
        super(Plane, self).__init__()
        self.id = id
        self.submissionTime = submissionTime
        self.requestedStart = requestedStart
        self.requestedDuration = requestedDuration

    def setTimeFinished(self, time)
        self.timeFinished = time
