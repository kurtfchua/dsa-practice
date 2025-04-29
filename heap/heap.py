class Heap:

    def __init__(self):
        self.heap = []
    
    def push(self, val):
        # add val to end of heap
        # if val's parent > val, swap until val >= parent

        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 0 and self.heap[(i-1)//2] > self.heap[i]:
            self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1) // 2 
        
        return self.heap
    
    def push_max(self, val):
        self.heap.append(val)
        i = len(self.heap) - 1

        while i > 0 and self.heap[(i-1)//2] < self.heap[i]:
            self.heap[(i-1)//2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
            i = (i-1)//2
        return self.heap

    def pop(self):
        # if heap is empty or size 1 
        if not self.heap:
            return self.heap
        if len(self.heap) == 1:
            return self.heap.pop()
        
        # get last value of heap
        pop_val = self.heap[0]
        # assign new head to last value in heap
        self.heap[0] = self.heap.pop()
        i = 0

        while 2*i + 1 < len(self.heap):
            # check if right child exists
            # right child < left child
            # new root > right child
            # swap down
            if ((2*i + 2 < len(self.heap)) and 
                self.heap[2*i+2] < self.heap[2*i + 1] 
                and self.heap[2*i+2]< self.heap[i]):
                self.heap[i], self.heap[2*i+2] = self.heap[2*i+2], self.heap[i]
                i = 2*i+2

            # if left child < new root
            elif self.heap[2*i+1] < self.heap[i]:
                self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                i = 2*i+1
            
            # value is in the right place, end swaps
            else:
                break
        
        return pop_val
    
    def heapify(self):
        j = (len(self.heap) // 2) - 1

        while j >=0:
            i = j
            while 2*i+1 < len(self.heap):
                if (2*i+2 < len(self.heap) and
                    self.heap[2*i+2] < self.heap[2*i+1] and
                    self.heap[2*i+2] < self.heap[i]):
                    self.heap[2*i+2], self.heap[i] = self.heap[i], self.heap[2*i+2]
                    i = 2*i+2
                elif self.heap[2*i+1] < self.heap[i]:
                    self.heap[2*i+1], self.heap[i] = self.heap[i], self.heap[2*i+1]
                    i = 2*i+1
                else:
                    break
            j -= 1
    



