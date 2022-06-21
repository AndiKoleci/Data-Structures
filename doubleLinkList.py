class ListNode:
    def __init__(self, data):
        self.data=data
        self.next=None
        self.prev=None

class List:
    def __init__(self):
        self.first = None
        self.last = None
        
    def insertFirst(self, data):
        node = ListNode(data)
        if self.first==None:
            self.first = node
            self.last = node
        else:
            self.first.prev = node
            node.next = self.first
            self.first = node
        
    def insertLast(self, data):
        node = ListNode(data)
        if self.first==None:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            node.prev = self.last
            self.last = node
            
    def contains(self, data):
        aux = self.first
        while(aux!=None):
            if aux.data==data:
                return 1
            aux = aux.next
        return 0
    
    def length(self):
        i = 0
        aux = self.first
        while(aux!=None):
            i = i + 1
            aux = aux.next
        return i
    
    def delete(self, data):
        aux = self.first
        i = 0
        
        while(aux!=None):
            if(aux.data==data):
                break
            i=i+1
            aux = aux.next
            
        if(aux==0): 
            return
        
        if(self.length()==1):
            self.first=None
            self.last=None
            
        elif(i==0):
            self.first = self.first.next
            self.first.prev = None
            
        elif(i==self.length()-1):
            self.last = self.last.prev
            self.last.next = None
            
        else:
            aux = aux.prev
            ptr = aux.next
            aux.next = ptr.next
            ptr.next.prev = aux
            
    def print(self):
        i = 0
        listPrint = ""
        aux = self.first
        while(aux!=None):
            if(i!=self.length()-1):
                auxString = "%d - " % aux.data
                listPrint += auxString
            else:
                auxString = "%d" % aux.data
                listPrint += auxString
            aux=aux.next
            i=i+1
        print(listPrint)
