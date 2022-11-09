#Buuble Sort

def BubbleSort(arr):
    n = len(arr)

    for i in range(n-1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp


A = [5,2,7,3,1,9,22,4]
print("Array Befor Sorting: ", A)
BubbleSort(A)
print("Array After Sorting: ", A)
