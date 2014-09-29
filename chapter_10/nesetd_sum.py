def nested_sum(a):
    index = 0
    sum1 = 0
    index1 = 0
    b = []
    c = []
    for i in a:
        if (index<len(a)):
             for j in i:
                if (index1<len(i)):
                     sum1 = sum1+i[index1]
                     index1 +1
                     b.appened(sum1)
                return b
                index = index+1
    return c + b
  
print nested_sum([[1,2,3],[12,1],[1,2,3]])
