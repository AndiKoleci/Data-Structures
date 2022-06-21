class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0;
        
    def isEmpty(self):
        if(self==None or self.head==None):
            return 0
        return 1
    
    def push(self, elem):
        node = StackNode(elem)
        if(self==None or self.head==None):
            self.head = node
            node.next=None
            self.size = self.size+1
        else:
            node.next=self.head
            self.head = node
            self.size = self.size+1
            
    def top(self):
        if(self==None or self.head==None):
            return None
        return self.head.data
    
    def pop(self):
        if(self==None or self.head==None):
            return 0
        self.head=self.head.next
        self.size = self.size-1
