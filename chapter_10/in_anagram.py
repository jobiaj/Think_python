def in_anagram(a,b):
     c = list(a)
     d = list(b)
     x = sorted(c)
     y = sorted(d)
     if (x==y):
		print "The given strings are anagrams"
     else:
		print "The given strings are not anagrams "


in_anagram("athul","jobzz")
