def area(a, b): 
    """
    Returns the area of the rectangle with specified sides
    
        Parameters:
            a (int or float): length of the rectangle`s side
            b (int or float): length of the other rectangle`s side
        
        Return value:
            area (int or float): area of the rectangle calculated by formula a * b
    """
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
    return 2 * (a + b)
