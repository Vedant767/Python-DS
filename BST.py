class BinarySearchTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_node(self, data):
        
        # Value already present in Tree
        if self.data == data:
            return 
        
        # Check if data is less than self.data then value is present in left sub tree
        if data < self.data:
            if self.left:
                self.left.add_node(data)
            else:
                self.left = BinarySearchTree(data)
        # Present in right sub tree
        else:
            if self.right:
                self.right.add_node(data)
            else:
                self.right = BinarySearchTree(data)
    
    def inorder_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.inorder_traversal()
        
        elements.append(self.data)
        
        if self.right:
            elements += self.right.inorder_traversal()
            
        return elements
    
    def preorder_traversal(self):
        elements = []
        
        elements.append(self.data)
        
        if self.left:
            elements += self.left.preorder_traversal()
        
        
        if self.right:
            elements += self.right.preorder_traversal()
            
        return elements

    def postorder_traversal(self):
        elements = []
        
        if self.left:
            elements += self.left.postorder_traversal()
                
        if self.right:
            elements += self.right.postorder_traversal()
        
        elements.append(self.data)
            
        return elements
    
    def search_element(self, data):
        
        if self.data == data:
            return True
        
        if data < self.data:
            if self.left:
                return self.left.search_element(data)
            else:
                return False
        else:
            if self.right:
                return self.right.search_element(data)
            else:
                return False
    
    def find_min(self):
        if self.left:
            return self.left.find_min()
        else:
            return self.data
    
    def find_max(self):
        if self.right:
            return self.right.find_max()
        else:
            return self.data
    
    def delete_element(self, data):
        
        if data < self.data:
            if self.left:
                self.left = self.left.delete_element(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.delete_element(data)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            
            #There are two ways two delete parent which consist both left and eight 
            # First we can Find max from left and then replace the max value with the value which we want to delete.
            max = self.left.find_max()
            self.data = max 
            self.left = self.left.delete_element(max)
            
            #Second we can find min from right and then replace the min value with the value which we want to delete.
            # min = self.right.find_min()
            # self.data = min
            # self.right = self.right.delete_element(min)
        
        return self



def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BinarySearchTree(elements[0])

    for i in range(1,len(elements)):
        root.add_node(elements[i])

    return root

# countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
numbers = [17, 4, 1, 20, 9, 23, 18, 34]

root = build_tree(numbers)
# print(root.delete_element(34))
# print(root.delete_element(23))
# print(root.delete_element(20))
print()
print("Inorder:-",(root.inorder_traversal()))
# print()
# print("Preorder:-",(root.preorder_traversal()))
# print()
# print("Postorder:-",(root.postorder_traversal()))
# print()
# print("Element UK Present :-",root.search_element('UK'))
# print()
# print("Min:-",root.find_min())
# print("Max:-",root.find_max())
