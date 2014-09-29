def histogram(a):
        d = dict()
        for i in a:
                if i not in d:
                        d[i] = 1
        else:
                        d[i] += 1
        return d

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


