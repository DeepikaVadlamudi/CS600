def bubblesort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                swapped = True
                arr[j], arr[j+1] = arr[j+1], arr[j];
        if swapped == False:
            break
arr = [16,45,16,19,24,50]
bubblesort(arr)
print("Sorted array is : ")
for i in range(len(arr)):
    print("%d" %arr[i])
