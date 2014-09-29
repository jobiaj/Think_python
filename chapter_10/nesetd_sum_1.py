def nested_sum1(a):
    b = []
    for i in a:
        c = sum(i)
        b.append([c])
    return b

print nested_sum1([[1,2,3],[1,2,3,4],[1,2,3,4,5]])
