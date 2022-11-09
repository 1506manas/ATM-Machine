# selection sort

def SelectionSort(arr):
    n = len(arr)

    for i in range(n-1):
        pos = i
        for j in range(i+1,n):
            if arr[j] < arr[pos]:
                pos = j

        temp = arr[i]
        arr[i] = arr[pos]
        arr[pos] = temp

#__main__
a = [1,6,3,9,2,7]
print("Original Array: ", a)

SelectionSort(a)
print("After sorting: ", a)

    
        
