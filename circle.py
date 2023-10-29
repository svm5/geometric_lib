import math


def area(r):
    """
    Returns the area of the circle with specified radius
    
        Parameters:
            r (int or float): circle`s radius
        
        Return value:
            area (float): area of the circus calculated by formula Pi * r * r
    """
    if (not(isinstance(r, int) or isinstance(r, float))):
        raise ValueError("Radius of the circle must be a number")
    if (r < 0):
        raise ValueError("Radius of the circle must be a positive number")
    
    return math.pi * r * r


def perimeter(r):
    """
    Returns the length of the circle with specified radius

        Parameters:
            r (int or float): circle`s radius
        
        Return value:
            circumference (float): length of the circus calculated by formula 2 * Pi * r
    """
    if (not(isinstance(r, int) or isinstance(r, float))):
        raise ValueError("Radius of the circle must be a number")
    if (r < 0):
        raise ValueError("Radius of the circle must be a positive number")
    
    return 2 * math.pi * r
