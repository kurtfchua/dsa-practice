class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def insertEnd(self, val):
        if not self.head:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next
    
    def print(self):
        current = self.head
        while current:
            print(current.val, end = " -> ")
            current = current.next


Node1 = Node(1)
Node2 = Node(2)
Node3 = Node(3)

LinkedList1 = LinkedList()
LinkedList1.insertEnd(Node1)
LinkedList1.insertEnd(Node2)
LinkedList1.insertEnd(Node3)

LinkedList1.print()