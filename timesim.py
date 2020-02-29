# timesim.py
#
# Runs a time simulator of MN temperatures.
# Each time step represents one hour.
#

import sys  # lets us use sys.argv
from tempstuff import displayTimeTemp, adjustTemperature

def simulation():
   """ Runs a temperature simulation for 240 hours. """
   currentTime = 0
   currentTemperature = 0
   while currentTime < 240 :
      displayTimeTemp( currentTime, currentTemperature)
      currentTime = currentTime + 1
      currentTemperature = adjustTemperature( currentTime, currentTemperature)

if __name__ == "__main__" :
   argnum = len(sys.argv)
   print("There are ", argnum, " arguments")
   simulation()
