def first(word):
    	return word[0]

def last(word):
    	return word[-1]

def middle(word):
    	return word[1:-1]
def palindrome(word):
   	if ( first(word) ==  last(word)):
		 palindrome( middle(word)) 
		 print 1


palindrome("noon")
    
