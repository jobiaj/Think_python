import math
def distance(x1,y1,x2,y2):
	dx = x1 - x2
	dy = y1 - y2
	z = dx**2 + dy**2
	return math.sqrt(z)
print distance(1,2,3,4)
 
