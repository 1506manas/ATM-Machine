#Merge Sort

def mergesort(arr,left,right):
    if left < right:
        mid = (left+right)//2
        mergesort(arr,left,mid)
        mergesort(arr,mid+1,right)
        merge(arr,left,mid,right)

def merge(arr,left,mid,right):
    i = left
    j = mid+1
    k = left
    brr = [0]*(right+1)

    while i <= mid and j <= right:
        if arr[i] < arr[j]:
            brr[k] = arr[i]
            i = i+1
            k = k+1

        else:
            brr[k] = arr[j]
            j = j+1
            k = k+1

    while i <= mid:
        brr[k] = arr[i]
        i = i+1
        k = k+1

    while j <= right:
        brr[k] = arr[j]
        j = j+1
        k = k+1

    for x in range(left, right+1):
        arr[x] = brr[x]


#__main__

A = [7,6,2,5,1,0]
n = len(A)
left = 0
right = n-1
print("Array Before sortint: ", A)
mergesort(A,left,right)
print("Array After sortint: ", A)
