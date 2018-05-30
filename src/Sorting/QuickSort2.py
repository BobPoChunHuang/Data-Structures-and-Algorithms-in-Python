def qsort2(alist,low,up):
    if low > up:
        return
    mid = low
    for i in range(low+1,up+1):
        if alist[i]<alist[low]:
            mid = mid + 1
            alist[mid], alist[i] = alist[i], alist[mid]
            print(alist)
        
    alist[mid], alist[low] = alist[low], alist[mid]
    qsort2(alist, low, mid-1)
    qsort2(alist, mid+1, up)
    print(alist)
    
alist = [8,7,6,5,4,3,2,1]
print(qsort2(alist,0,len(alist) - 1))
        
        
    
    
        
    