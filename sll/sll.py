class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insertEnd(self, val):
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def remove(self,val):
        dummy = Node(0)
        prev, current = dummy, self.head

        while current:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
            current = current.next
        return dummy.next
    
    def print(self):
        current = self.head
        while current:
            print(current.val, end = " -> ")
            current = current.next


Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)

LinkedList1 = LinkedList()
LinkedList1.insertEnd(1)
LinkedList1.insertEnd(2)
LinkedList1.insertEnd(3)

#LinkedList1.print()

LinkedList1.remove(2)

LinkedList1.remove(3)
LinkedList1.print()