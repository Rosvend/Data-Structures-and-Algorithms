import math
from point2D import Point2D

class Point2DCartesian(Point2D):
    """Class representing points in the plane
    """

    def __init__(self, x, y):
        """Constructs a Point2D instance from the x,y coordinates
        """
        self._x = x
        self._y = y
        
    def __str__(self):
        """Returns a String representation of the point
        """
        return "("+str(self._x)+","+str(self._y)+")"
    
    def __abs__(self):
        """Returns the distance to the origin (magnitude)
        """
        return math.sqrt( self._x**2 + self._y**2 )
    
    def angle(self):
        """Returns the angle to the x axis
        """
        return math.atan2( self._y, self._x )
    
    def getX(self):
        """Returns the x component
        """
        return self._x;

    def getY(self):
        """Returns the y component
        """
        return self._y;


Point1 = Point2DCartesian(5,10)
Point1.__str__()
Point1.getX()