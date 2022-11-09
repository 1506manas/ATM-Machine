#Linear search

def LinearSearch(key, n, length):
    for i in range(0,length):
        
        if key == n[i]:
            return 1
    return -1

#__Main__
list1 = [12,34,12,76,13,97,45,18]
length = len(list1)
key = int(input("enter the number"))
search = LinearSearch(key, list1, length)

print(search)

if search == 1:
    print("the number is in list")
else:
    print("not found")
