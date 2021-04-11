class Node:
    def __init__(self, data):
        self.value = data
        self.ref = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
    
    def display(self):
        if self.head is None:
            print("List is empty")
        else:
            n = self.head
            while n is not None:
                print(f"{n.value} -> ",end="")
                n = n.ref
            print()
    
    def insert_at_head(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
    
    def insert_at_end(self,data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return

        n = self.head

        while n.ref is not None:
            n = n.ref
        
        n.ref = new

    def insert_after_node(self,x,data):
        n = self.head
        while n is not None:
            if n.value == x:
                break
            n = n.ref

        if n is None:
            print("Value not found")
        else:
            new  = Node(data)
            new.ref = n.ref
            n.ref = new

    def insert_before_node(self,x,data):
        if x == self.head.value:
            new = Node(data)
            new.ref = self.head
            self.head = new
            return
        n = self.head
        while n.ref is not None:
            if n.ref.value == x:
                new = Node(data)
                new.ref = n.ref
                n.ref = new
            else:
                print("Vlaue not found")
            n = n.ref
    
    def insert_at_index(self,index,data):
 
        if index == 1:
            new = Node(data)
            new.ref = self.head
            self.head = new
            return
        
        i = 1
        n = self.head
        while i < index-1 and n is not None:
            if i == index:
                break
            n = n.ref
            i += 1
        
        if n is None:
            print("Index out of bound")
        else:
            new = Node(data)
            new.ref = n.ref
            n.ref = new
    
    def count_list(self):
        if self.head is None:
            print("List is empty")
            return
        else:
            n = self.head
            count = 0
            while n is not None:
                count +=1
                n = n.ref
            print(f"Total elements in list are: {count}")
    
    def search_element(self,x):
        n = self.head
        if self.head is None:
            print("List is empty")
        else:
            while n is not None:
                if x == n.value:
                    print(f"Value found : {x}")
                    return
                n = n.ref
            print("Value not found")
    
    def add_n_elements(self):
        no = int(input("Enter number of elements you want to enter in list"))
        
        for i in range(no):
            z = int(input("Enter element:"))
            self.insert_at_end(z)
    
    def delete_head(self):
        if self.head is None:
            print("List is empty")
            return
        self.head = self.head.ref
    
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return
        n = self.head
        if self.head.ref is None:
            self.delete_head()
            return
        while n.ref.ref is not None:
            n = n.ref
        n.ref = None
    
    def delete_element_node(self,x):
        if self.head is None:
            print("List is empty")
            return
        
        if self.head.value == x:
            self.head = self.ref
            return
        
        n = self.head
        while n.ref is not None:
            if x == n.ref.value:
                break
            n = n.ref
            
        if n.ref is None:
            print("Item not found")
        else:
            n.ref = n.ref.ref
        
    def reverse_a_list(self):
        if self.head is None:
            print("List is Empty")
            return
        n = self.head
        prev = None
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.head = prev
            
    
l = SinglyLinkedList()
l.insert_at_head(3)
# l.insert_at_end(12)
# l.insert_after_node(3,7)
# l.insert_after_node(7,2)
# l.insert_before_node(3,9)
# l.insert_at_index(1,11)
# l.delete_element_node(7)
# l.delete_head()
l.delete_at_end()
# l.add_n_elements()
l.display()
# l.count_list()
# l.search_element(10)
# l.reverse_a_list()
# print("Reversed list")
# l.display()