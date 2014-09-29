import math
def distance_between(x1,y1,x2,y2):
	a = x1 - x2
    	b = y1 - y2
	c = (a**2) + (b**2)
        d = math.sqrt(c)
        return d

print distance_between(2,3,4,5)
