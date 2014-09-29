def histogram(a):
        d = dict()
        for i in a:
                if i not in d:
                        d[i] = 1
        else:
                        d[i] += 1
        return d

h = histogram('parrot')
def print_hist(h):
	for c in h:
		print c, h[c]

	
print print_hist(h)

