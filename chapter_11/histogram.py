def histogram(a):
	d = dict()
	for i in a:
		if i not in d:
			d[i] = 1
	else:
			d[i] += 1
	return d

print histogram("fasalrahman")     

