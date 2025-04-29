class Node:
    # node will have val and a next pointer to the next node
    def __init__(self, val):
        self.val = val
        self.next = None

class Queue:

    def __init__(self):
        self.head = self.tail = None
    
    def enqueue(self, val):
        new_node = Node(val)

        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def dequeue(self):
        if not self.head:
            return
        val = self.head.val
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return val
    
