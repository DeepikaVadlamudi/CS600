def partition(a,low,q):
    print("low,q",low,q)
    v = a[low]
    i = low
    j = q +1
    while(i<j):
        i+=1
        j-=1
        while(a[i] < v):
            i+=1
        while(a[j] > v):
            j-=1
        if i < j:
            t = a[j]
            a[j] = a[i]
            a[i] = t

    a[low] = a[j]
    a[j] = v
    return j;

def quicksort(a,low,high):
    if low < high:
        j = partition(a,low,high)
        quicksort(a,low,j-1)
        quicksort(a,j+1,high)

a = [12, 5, 3, 6, 13, 19, 9, 5, 10,1000000]
low = 0
high = 8
quicksort(a,low,high)
for i in range(len(a)):
    print(a[i],end='|')
