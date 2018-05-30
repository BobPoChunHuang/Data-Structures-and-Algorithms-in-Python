def qsort3(alist,low,up):
    print(alist)
    if low >= up:
        return
        
    pivot = alist[low]
    left, right = low + 1, up
    while left <= right:
        while left <= right and alist[left] < pivot:
            left += 1
        while left <= right and alist[left] > pivot:
            right -= 1
        
        if left > right:
            break
        alist[left], alist[right] = alist[right], alist[left]
    alist[low], alist[right] = alist[right], alist[low]
    
    qsort3(alist, low, right - 1)
    qsort3(alist, right + 1, up)
    
alist= [8,7,6,5,4,3,2,1]
print(qsort3(alist,0,len(alist)-1))
    
    
