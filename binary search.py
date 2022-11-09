#Binary Search

def BinarySearch(list1, length, key):
    l = int(length/2)
    if key == list1[l]:
        return 1

    elif key < list1[l]:
        for i in range(0, l):
            if key == list1[i]:
               return 1
        return -1
    
    else:
        for i in range(l+1, length):
            if key == list1[i]:
                return 1
        return -1
    
#__main__
list1 = [10,23,5,33,65,4,34,56,32,86,22]
list1.sort()

print(list1)

length = len(list1)
key = int(input("enter the number: "))

search = BinarySearch(list1, length, key)

if search == 1:
    print("the number is in list")

else:
    print("not found")

