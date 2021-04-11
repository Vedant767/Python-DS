class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

class Circular:
    def __init__(self):
        self.head = None
    
    def display(self):
        n = self.head
        if self.head is None:
            print("List is empty")
            return
        
        while n:
            print(f"{n.value}")
            n = n.next
            if n is self.head:
                break
        print()

    def insert_at_head(self, data):
        new = Node(data)
        n = self.head
        new.next = self.head
        if self.head is not None:
            while n.next != self.head:
                n = n.next
            n.next = new
        else:
            new.next = new
        self.head = new
    
    def insert_at_end(self, data):
        new = Node(data)
        n = self.head
        
        new.next = self.head
        
        if self.head is not None:
            while(n.next != self.head):
                n = n.next
            n.next = new
        # else:
        #     new.next = new
        
    def insert_after_node(self, index, data):
        if self.head is None:
            print("List is empty")
            return
        new = Node(data)
        n = self.head
        counter = 0
        while n:
            print(counter)
            if counter == index:
                break
            n = n.next
            counter += 1
        if n is self.head:
            print("Index not found")
        else:

            new.next = n.next
            n.next = new


cir = Circular()
cir.insert_at_head(2)
cir.insert_at_head(3)
# cir.insert_at_head(5)
cir.insert_at_end(7)
# cir.insert_after_node(0,4)
cir.display()