def is_palindrome(word):
     reverse = word[::-1]
     if (word == reverse):
        print "Given string is a palindrome"
     else:
        print "Given string is not a palindrome"

is_palindrome("noon")
