def middle(a):
    a.pop(0)
    a.pop(-1)
    return a


print middle([1,2,3,4,5,6,7,8,9])
