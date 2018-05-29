def SelectionSort(alist):
    for i in range(len(alist)):
        min_index = i
        for j in range(i+1,len(alist)):
            if alist[j] < alist[min_index]:
                min_index= j
        alist[i],alist[min_index] = alist[min_index],alist[i]
    return alist

alist = [8,7,6,5,4,3,2,1]

print(SelectionSort(alist))