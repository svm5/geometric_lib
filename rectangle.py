def area(a, b): 
    """
    Returns the area of the rectangle with specified sides
    
        Parameters:
            a (int or float): length of the rectangle`s side
            b (int or float): length of the other rectangle`s side
        
        Return value:
            area (int or float): area of the rectangle calculated by formula a * b
    """
    if (not(isinstance(a, int) or isinstance(a, float)) or \
            not(isinstance(b, int) or isinstance(b, float))):
        raise ValueError("Sides of the rectangle must numbers")
    if (a < 0 or b < 0):
        raise ValueError("Sides of the rectangle must have positive length")
    
    return a * b

def perimeter(a, b):
    """
    Returns the perimeter of the rectangle with specified sides
    
        Parameters:
            a (int or float): length of the rectangle`s side
            b (int or float): length of the other rectangle`s side
        
        Return value:
            perimeter (int or float): perimeter of the rectangle calculated by formula 2 * (a + b)
    """
    if (not(isinstance(a, int) or isinstance(a, float)) or \
            not(isinstance(b, int) or isinstance(b, float))):
        raise ValueError("Sides of the rectangle must be numbers")
    if (a < 0 or b < 0):
        raise ValueError("Sides of the rectangle must have positive length")
    
    return 2 * (a + b)
