def area(a, h):
    """
    Returns the area of the triangle with specified side and height
    
        Parameters:
            a (int or float): length of the triangle`s side
            h (int or float): height passed to the side a
        
        Return value:
            area (float): area of the triangle calculated by formula a * h / 2
    """
    if (not(isinstance(a, int) or isinstance(a, float)) or \
            not(isinstance(h, int) or isinstance(h, float))):
        raise ValueError("Side and height of the triangle must be numbers")
    if (a < 0 or h < 0):
        raise ValueError("Side and height of the triangle must have positive length")
    
    return a * h / 2 

def perimeter(a, b, c):
    """
    Returns the perimeter of the triangle with specified sides
    
        Parameters:
            a, b, c (int or float): lengths of the triangle`s sides
        
        Return value:
            perimeter (int or float): perimeter of the triangle calculated by formula a + b + c
    """
    if (not(isinstance(a, int) or isinstance(a, float)) or \
            not(isinstance(b, int) or isinstance(b, float)) or \
            not(isinstance(c, int) or isinstance(c, float))):
        raise ValueError("Sides of the triangle must be numbers")
    if (a < 0 or b < 0 or c < 0):
        raise ValueError("Sides of the triangle must have positive length")
    
    return a + b + c 
