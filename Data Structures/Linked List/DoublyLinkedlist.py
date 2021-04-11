class Node:
    def __init__(self,data):
        self.prev = None
        self.value = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_in_empty_list(self,data):
        if self.head is None:
            new = Node(data)
            self.head = new
        else:
            print("List is not empty")
    
    def display(self):
        if self.head is None:
            print(List is empty)
        else:
            n = self.head
            while n is not None:
                print(f"{n.value}")
                n = n.next
    
    def insert_at_start(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        
        new.next = self.head
        self.head.prev = new
        self.head = new
    
    def insert_at_end(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        n = self.head
        while n.next is not None:
            n = n.next
        
        new.prev = n
        n.next = new
    
    def insert_after_element(self, x, data):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        while n is not None:
            if n.value == x :
                break
            n = n.next
        if n is None:
            print("Element not found")
            return
        else:
            new = Node(data)
            new.prev = n
            new.next = n.next
            if n.next is not None:
                new.next.prev = new
            n.next = new
    
    def insert_before_element(self, x, data):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        flag = 1
        while n is not None:
            if x == self.head.value:
                flag = 0
            if x == n.value:
                break
            n = n.next
        if n is None:
            print("Element not Found")
        else:
            new = Node(data)
            new.next = n    
            new.prev = n.prev
            if n.prev is not None:
                n.prev.next = new
            n.prev = new
            if flag == 0:
                self.head = new
    
    def delete_from_start(self):
        if self.head is None:
            print("List is empty Node cannot be deleted")
            return
        if self.head.next is None:
            self.head =  None
            return
        self.head = self.head.next
        self.head.prev = None
            
    def delete_from_end(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        n = self.head
        while n.next is not None:
            n = n.next
        n.prev.next = None
    
    def delete_at_element(self, x):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            if x == self.head.value:
                self.head = None
            else:
                print("Value not Found")
            return
        if self.head.value == x:
            self.head.next.prev = None
            self.head = self.head.next
            return
        n = self.head
        while n.next is not None:
            if x == n.value:
                break
            n = n.next
        
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.value == x:
                n.prev.next = None
            else:
                print("Element not found")       
    
    def reverse_list(self):
        if self.head is None:
            print("List is empty")
            return
        p = self.head
        q = p.next
        p.next = None
        p.prev = q
        while q is not None:
            q.prev = q.next
            q.next = p
            p = q
            q = q.prev
        self.head = p
    
            
dbl = DoublyLinkedList()
dbl.insert_in_empty_list(0)
dbl.insert_at_end(1)
dbl.insert_at_end(2)
dbl.insert_at_end(3)
dbl.insert_after_element(3,4)
dbl.insert_before_element(0,-1)
dbl.delete_from_start()
dbl.delete_at_element(0)
dbl.display()
print("After reverse")
dbl.reverse_list()
dbl.display()