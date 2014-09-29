import math
def area(radius):
     	area = math.pi * (r**2)
	return area
def radius(x1,y1,x2,y2):
	dx = x1 - x2
	dy = y1 - y2
	z = dx**2 + dy**2
	radius = math.sqrt(z)
        return radius
def circle_area(x1, y1, x2, y2):
    	radius = radius(x1, y1, x2, y2)
    	result = area(radius)
    	return result

print circle_area(1,2,3,4)
 

