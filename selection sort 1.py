def SelectionSort(arr):
    n = len(arr)
    for i in range(n):
        m = i
        for j in range(i+1,n):
            if arr[j]<arr[m]:
                arr[j],arr[m]=arr[m],arr[j]
arr = [13,4,9,5,3,16,12]
SelectionSort(arr)
print(arr)



