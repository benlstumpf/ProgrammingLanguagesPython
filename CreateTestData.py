#Test Data Creation program
#MSP airlines are Aer Lingus, Air Canada, Air Choice One, Air France, Alaska Airlines, American Airlines, Boutique Air, Delta Air Lines, Frontier Airlines, KLM Royal Dutch Airlines, Spirit Airlines, United Airlines

#format is ID, Submission Time, Requested Start, Requested Duration

import random

def main():
    passedArgument = sys.argv[0]
    while i in range passedArgument:
        if i%

def createPlane():
    id = getID

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
    }.get(random.randrange( 12)


if __name__ == "__main__"
    main()
