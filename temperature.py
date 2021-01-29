# temperature.py
# Very small example of a class representing a temperature.
# 

class Temperature:
    """Represents a single temperature"""
    
    def __init__(self) :
        self.f = 0
    
    def __init__(self, temp, kind) :
        if kind == 'f' :
            self.f = temp
        else :
            self.f = self.convertToF( temp)
    
    def getTempInC( self) :
        return self.convertToF( self.f)
    
    def getTempInF( self) :
        return self.f
    
    def convertToF( self, tc) :
        tempf = tc * 9.0 / 5.0 + 32
        return tempf
    

today = Temperature( 0, 'f' )
print( "Today is ", today.getTempInC())
print( "Today is ", today.getTempInF())
