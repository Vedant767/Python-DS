class TreeNode:
    def __init__(self, name, designation):
        self.name = name 
        self.designation = designation
        self.children = []
        self.parent = None
    
    def add(self, name):
        name.parent = self
        self.children.append(name)
    
    def get_level(self):
        level = 0
        p = self.parent
        
        while p:
            level += 1
            p = p.parent
        return level

    def print_name(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.name)
        
        if self.children:
            for child in self.children:
                child.print_name()

    def print_as_per_level(self, lvl):
        if self.get_level() <= lvl:
            spaces = " " * self.get_level() * 3
            prefix = spaces + "|__" if self.parent else ""
            print(prefix + self.name)
        
            if self.children:
                for child in self.children:
                    child.print_as_per_level(lvl)
    
    def print_designation(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.designation)
        
        if self.children:
            for child in self.children:
                child.print_designation()
    
    def print_both(self):
        spaces = " " * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        
        print(f"{prefix} {self.name} ({self.designation})")
        
        if self.children:
            for child in self.children:
                child.print_both()

def create_tree():
    root = TreeNode("Nilupil", "CEO")
    
    Chinmay = TreeNode("Chinmay", "CTO")
    
    Vishwa = TreeNode("Vishwa", "Infrastructure Head")
    
    Dhaval = TreeNode("Dhaval", "Cloud Manager")
    Abhijit = TreeNode("Abhijit", "App Manager")
    
    Amir = TreeNode("Amir", "Application Head")
    
    Gels = TreeNode("Gels", "HR Head")   
    
    Peter = TreeNode("Peter", "Recuitment Manager")   
    Waqas = TreeNode("Waqas", "Policy Manager")   
    
    
    root.add(Chinmay)
    root.add(Gels)
    
    Chinmay.add(Vishwa)
    Chinmay.add(Amir)
    
    Vishwa.add(Dhaval)
    Vishwa.add(Abhijit)
    
    Gels.add(Peter)
    Gels.add(Waqas)
    
    return root

root = create_tree()
root.print_name()
print()
print(root.get_level())
root.print_as_per_level(2)
# print()
# root.print_designation()
# print()
# root.print_both()