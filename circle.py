import math


def area(r):
    """
    Returns the area of the circle with specified radius
    
        Parameters:
            r (float): circle`s radius
        
        Return value:
            area (float): area of the circus calculated by formula Pi * r * r
    """
    return math.pi * r * r


def perimeter(r):
    """
    Returns the length of the circle with specified radius

        Parameters:
            r (float): circle`s radius
        
        Return value:
            circumference (float): length of the circus calculated by formula 2 * Pi * r
    """
    return 2 * math.pi * r
