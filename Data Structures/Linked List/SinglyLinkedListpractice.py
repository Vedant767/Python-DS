class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class singly:
    def __init__(self):
        self.head = None
    
    def add(self, data):
        new = Node(data)
        
        if self.head is None:
            self.head = new
            return
        
        n = self.head
        while n.next is None:
            n = n.next
        
        n.next = new
    
    def add_at_head(self, data):
        new = Node(data)
        
        new.next = self.head
        self.head = new
    
    def insert_after_node(self, x, data):
        n = self.head
        while n:
            if n.data == x:
                break
            n = n.next
        
        if n is None:
            print("Element not presend ")
        else:
            new = Node(data)
            new.next = n.next
            n.next = new
    
    def insert_before_node(self, data):
        if x == self.head.data:
            self.add_at_head(data)
            return
        n = self.head
        
        while n.next is not None:
            if x == n.next.data:
                new = Node(data)
                new.next = n.next
                n.next = new
            n = n.next