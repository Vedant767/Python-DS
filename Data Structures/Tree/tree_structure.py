class treeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        
        while p:
            level += 1
            p = p.parent
        return level
    
    def print_tree(self):
        spaces = " " * self.get_level() * 2
        prefix = spaces + "|__" if self.parent else ""
        
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def tree():
    root = treeNode("Electronics")
    
    laptop = treeNode("Laptop")
    laptop.add(treeNode("Mac"))
    laptop.add(treeNode("Surface"))
    laptop.add(treeNode("Windows"))
    
    
    phones = treeNode("Phones")
    phones.add(treeNode("Iphone"))
    phones.add(treeNode("Android"))
    phones.add(treeNode("nokia"))
    
    root.add(laptop)
    root.add(phones)
    return root

root = tree()
root.print_tree()