def area(a, h):
    """
    Returns the area of the triangle with specified side and height
    
        Parameters:
            a (int or float): length of the triangle`s side
            h (int or float): height passed to the side a
        
        Return value:
            area (float): area of the triangle calculated by formula a * h / 2
    """
    return a * h / 2 

def perimeter(a, b, c):
    """
    Returns the perimeter of the triangle with specified sides
    
        Parameters:
            a, b, c (int or float): lengths of the triangle`s sides
        
        Return value:
            perimeter (int or float): perimeter of the triangle calculated by formula a + b + c
    """
    return a + b + c 
