class dog:
    def print1(self):
        print("Hello")
        

class cat(dog):
    def print1(self):
        super().print1()
        


c = cat()
c.print1()