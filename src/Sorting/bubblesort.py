def bubblsesort(alist):
    for i in range(len(alist)):
        for j in range(1,len(alist) - i):
            if alist[j-1] > alist[j]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
#                temp = alist[j]
#                alist[j]=alist[j-1]
#                alist[j-1]=temp
    return alist

alist = [8,7,6,5,4,3,2,1]
print(bubblsesort(alist))

