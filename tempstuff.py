# tempstuff.py
# Some functions to deal with time and temperature
#

import random

def displayTimeTemp( time, temp) :
   """ Displays the given time and temperature in a nice format. """
   day = time // 24
   hour = time % 24
   print( "Day ", day, " at ", hour,":00 o'clock it is ", temp, " degrees.", sep="")

def adjustTemperature( time, temp) :
   """ Calculates a new temperature given the time of day.

       If it is daytime, the temperature might go up, otherwise it
       might go down.
   """
   variance = random.randrange( 5)
   if isDaylight( time) :
      temp = temp + variance
   else :
      temp = temp - variance
   return temp

def isDaylight( time) :
   """ Determines whether or not the given time is daytime. """
   hour = time % 24
   if hour < 6 or hour > 18 :
      return False
   else :
      return True
