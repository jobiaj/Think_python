def check_fermat(a,b,c,n):
	if(n>2):
		if((a**n + b**n) == c**n):
			return "Holy smokes, Fermat was wrong!"
		else:
                	return "No, that doesn\'t work."
	else:

		print " n is less than 2 "

print check_fermat(1,2,3,3)
