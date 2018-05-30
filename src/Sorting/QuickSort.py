def qsort(alist):
    print(alist)
    if len(alist) <=1:
        return alist
    else:
        pivot = alist[0]
        return qsort([x for x in alist[1:] if x < pivot]) + \
                     [pivot] + \
                     qsort([x for x in alist[1:] if x>= pivot])
    alist = [8,7,6,5,4,3,2,1]
    print(qsort(alist))
    