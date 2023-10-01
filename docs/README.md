# Geometric Lib

<p>This is the official documentation for Geometric Lib</p>

* [General description of the solution](#general_description) 
* [Description of functions](#functions_description)
    * [Circle](#circle_description)
    * [Rectangle](#rectangle_description)
    * [Square](#square_description)
    * [Triangle](#triangle_description)
* [Project modification history](#modification)

## <a id="general_description">General description of the solution</a>
<p>This library is created to calculate the area and perimeter of geometric shapes. The following formulas are used:</p>

### Area
- Circle: S = πR²
- Rectangle: S = ab
- Square: S = a²
- Triangle: S = ${ah\over 2}$

### Perimeter
- Circle: P = 2πR
- Rectangle: P = 2a + 2b
- Square: P = 4a
- Triangle: P = a + b + c

## <a id="functions_description">Description of functions</a>
<p>Here you can see description of the functionality for each geometric shape</p>

### <a id="circle_description">Circle</a>
**area**(r)  
&nbsp; Returns the area of the circle with specified radius **r**  
**perimeter**(r)  
&nbsp; Returns the length of the circle with specified radius **r**

    >>> circle_area = area(5)
    >>> circle_area
    78.53981633974483
    >>> circle_perimeter = perimeter(5)
    >>> circle_perimeter
    31.41592653589793
    >>> circle_perimeter = perimeter(2.3)
    >>> circle_perimeter
    14.451326206513047

### <a id="rectangle_description">Rectangle</a>
**area**(a, b)  
&nbsp; Returns the area of the rectangle with specified sides **a**  and **b**  
**perimeter**(a, b)  
&nbsp; Returns the perimeter of the rectangle with specified sides **a** and **b**

    >>> rectangle_area = area(5, 8)
    >>> rectangle_area
    40
    >>> rectangle_area = area(3.5, 9.7)
    >>> rectangle_area
    33.949999999999996
    >>> rectangle_perimeter = perimeter(2, 3)
    >>> rectangle_perimeter
    10
    >>> rectangle_perimeter = perimeter(2.3, 6.9)
    >>> rectangle_perimeter
    18.4

### <a id="square_description">Square</a>
**area**(a)  
&nbsp; Returns the area of the square with specified side **a**   
**perimeter**(a)  
&nbsp; Returns the perimeter of the square with specified side **a**

    >>> square_area = area(5)
    >>> square_area
    25
    >>> square_perimeter = perimeter(2.3)
    >>> square_perimeter
    9.2

### <a id="triangle_description">Triangle</a>
**area**(a, h)  
&nbsp; Returns the area of the triangle with specified side **a** and height **h**  
**perimeter**(a, b, c)  
&nbsp; Returns the perimeter of the triangle with specified sides **a**, **b** and **c**

    >>> triangle_area = area(12, 5)
    >>> triangle_area
    30.0
    >>> triangle_perimeter = perimeter(2.5, 3.7, 4)
    >>> triangle_perimeter
    10.2

## <a id="modification">Project modification history</a>
| Commit hash    | Commit message (description)                            |
| -------------- | ------------------------------------------------------- |
| 8ba9aeb        | Circle and square added                                 |
| d078c8d        | Docs added                                              |
| 8eed03e        | Rectangle added                                         |
| e661c97        | Correct calculation of the rectangle perimeter          |
| 477bc4a        | Correct calculation of the rectangle perimeter and area |
| c1c5080        | Triangle added                                          |