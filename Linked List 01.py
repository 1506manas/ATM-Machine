class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
        def __init__(self):
            self.head = None
            self.tail = None
            self._size = 0

        def __len__(self):
            return self._size

        def Display(self):
            temp = self.head
            while(temp):
                print(temp.data, end='-->')
                temp = temp.next

            print()

        def isempty(self):
            return self._size == 0

        def Addlast(self,element):
            new = Node(element)
            if self.isempty():
                self.head = new

            else:
                self.tail.next = new

            self.tail = new
            self._size += 1 


#__main__

llist = LinkedList()
llist.Addlast(10)
llist.Addlast(21)
llist.Addlast(12)
llist.Addlast(16)
llist.Addlast(111)

llist.Display()

print("Size of llist is: ", len(llist))
