class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.head = None
        self.back = None
        self.size = 0
        
    def enqueue(self, elem):
        node = QueueNode(elem)
        if(self==None or self.head==None):
            self.head = node
            self.back = node
            node.next = None
            self.size = self.size+1
        else:
            self.back.next = node
            self.back = node
            self.size = self.size+1
        
    def front(self):
        return self.head.data    
    
    def dequeue(self):
        self.head=self.head.next
        if(self.size==1):
            self.back = None
        self.size = self.size-1
