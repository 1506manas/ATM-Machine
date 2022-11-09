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
            

        def Search(self, key):
            temp = self.head
            index = 0
            while(temp):
                if temp.data == key:
                    print(" element is at: ", index)
                    return 0
                temp = temp.next
                index += 1

            print(" element is not found ")

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

llist.Search(1687)
