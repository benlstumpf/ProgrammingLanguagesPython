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
    timeVariable = 6
    for i in range(numberOfRecords):
        id, submissionTime, requestedStart, requestedDuration = createPlane(submissionLastTime, timeVariable)
        print(id, " ",randrange(1000), ", ",
              submissionTime, ", ",
              requestedStart, ", ",
              requestedDuration,
              sep="")
        submissionLastTime = submissionTime

def createPlane( lastTimeSubmition, timeVariable):
    id = getID(randrange(0, 11))
    submissionTime = lastTimeSubmition + randrange(timeVariable)
    requestedStart = submissionTime + randrange(timeVariable)
    requestedDuration = randrange(1,timeVariable)
    return id, submissionTime, requestedStart, requestedDuration

def getID(airLineNumber):
     # 12 is the number of airlines listed at start of file
     # started counting at 1 and realized it at the end so united is at the top
    return {
        0: "United Airlines" ,
        1: "Aer Lingus" ,
        2: "Air Canada" ,
        3: "Air Choice One" ,
        4: "Air France" ,
        5: "Alaska Airlines" ,
        6: "American Airlines" ,
        7: "Boutique Air" ,
        8: "Delta Air Lines" ,
        9: "Frontier Airlines" ,
        10: "KLM Royal Dutch Airlines" ,
        11: "Spirit Airlines"
    }.get(airLineNumber)

if __name__ == "__main__" :
    numberOfRecords = int(sys.argv[1])
    main(numberOfRecords)
