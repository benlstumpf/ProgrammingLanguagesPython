#Test Data Creation program

#to enterData into a file in linux use the > or >> operators

#MSP airlines are Aer Lingus, Air Canada, Air Choice One, Air France, Alaska Airlines, American Airlines, Boutique Air, Delta Air Lines, Frontier Airlines, KLM Royal Dutch Airlines, Spirit Airlines, United Airlines

#format is ID, Submission Time, Requested Start, Requested Duration
#e.g. Delta 160, 0, 0, 4

#using randrange a lot so importing it as a function
from random import randrange
import sys

def main(numberOfRecords):
    submissionLastTime = 0
    for i in range(numberOfRecords):
        id, submissionTime, requestedStart, requestedDuration = createPlane(submissionLastTime)
        print(id,
              submissionTime, ", ",
              requestedStart, ", ",
              requestedDuration, ", ",
              sep="")
        submissionLastTime = submissionTime

def createPlane( lastTimeSubmition):
    id = getID
    submissionTime = lastTimeSubmition + randrange(6)
    requestedStart = submissionTime + randrange(6)
    requestedDuration = randrange(6)
    return id, submissionTime, requestedStart, requestedDuration

def getID():
     # 12 is the number of airlines listed at start of file
     # started counting at 1 and realized it at the end so united is at the top
    return {
        "United Airlines" : 0,
        "Aer Lingus" : 1,
        "Air Canada" : 2,
        "Air Choice One" : 3,
        "Air France" : 4,
        "Alaska Airlines" : 5,
        "American Airlines" : 6,
        "Boutique Air" : 7,
        "Delta Air Lines" : 8,
        "Frontier Airlines" : 9,
        "KLM Royal Dutch Airlines" : 10,
        "Spirit Airlines" : 11
    }[randrange( 12)]

if __name__ == "__main__" :
    numberOfRecords = int(sys.argv[1])
    main(numberOfRecords)
