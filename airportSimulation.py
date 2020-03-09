#will call funtions to intake file, run simulation, and print final report

import FileIntake
import RunwaySimulator
import sys
import ReportingFunctions

def main(list):
    startingList = FileIntake.fileToList(list)
    finalList = RunwaySimulator.runway(startingList)
    ReportingFunctions.printFinalPrint(finalList)

if __name__ == "__main__" :
   main(sys.argv[1])
