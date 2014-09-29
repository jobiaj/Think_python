def is_sorted(a):
    b = sorted(a)
    if (b==a):
       return True
    else:
       return False

print "Checking list [1,2,3] is sorted or not"
print is_sorted([1,2,3])
print "Checking whether the list ['athul','jobi','fasal','reshmi','najeeb']"
print is_sorted(['athul','jobi','fasal','reshmi','najeeb'])
