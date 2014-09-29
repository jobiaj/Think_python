def has_duplicate(a):
	b = sorted(a)     
	c = list( set(a))
        if (c == b):
           print "The given string doesn't have  duplicates!!"
        else:
           print "The given string has duplicates.."

has_duplicate([1,2,3,3])
