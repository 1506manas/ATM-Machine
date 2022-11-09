#insertion sort

def InsertionSort(arr):
    n = len(arr)

    for i in range(1,n):
        temp = arr[i]
        pos = i

        while pos > 0 and arr[pos-1] > temp:
            arr[pos] = arr[pos-1]
            pos = pos-1

        arr[pos] = temp


#__main__
A = [4,1,5,8,3,15,2]
print("Befor Sorting: ", A)
InsertionSort(A)
print("After Sorting: ", A)
