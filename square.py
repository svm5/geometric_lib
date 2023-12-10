def area(a):
    """
    Returns the area of the square with specified side
    
        Parameters:
            a (int or float): length of the square`s side 
        
        Return value:
            area (int or float): area of the square calculated by formula a * a
    """
    if (not(isinstance(a, int) or isinstance(a, float))):
        raise ValueError("Side of the square must be a number")
    if (a < 0):
        raise ValueError("Side of the square must have positive length")
    
    return a * a


def perimeter(a):
    """
    Returns the perimeter of the square with specified side
    
        Parameters:
            a (int or float): length of the square`s side 
        
        Return value:
            perimeter (int or float): perimeter of the square calculated by formula 4 * a
    """
    if (not(isinstance(a, int) or isinstance(a, float))):
        raise ValueError("Side of the square must be a number")
    if (a < 0):
        raise ValueError("Side of the square must have positive length")
    
    return 4 * a
