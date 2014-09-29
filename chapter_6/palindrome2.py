def is_palindrome(a):
	b = a[::-1]
        if (a == b):
		return True
	else:
		return False
print "checking whether \'noon\' is a palindrome"
print is_palindrome("noon")
print "checking whether \'abcde\' is a palindrome"
print is_palindrome("abcde")
