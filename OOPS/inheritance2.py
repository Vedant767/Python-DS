class mother:
    def print_color(self):
        print("Color is white")

class father:
    def print_color(self):
        print("Color is black")

class child(father, mother):
    def print_color(self):
        super().print_color()
        

children = child()
children.print_color()