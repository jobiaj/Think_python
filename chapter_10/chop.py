def chop(a):
    a[0]='None'
    a[-1]= 'None'
    return a

print chop([1,2,3,4,5,6,7,8,9])
